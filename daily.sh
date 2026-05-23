#!/usr/bin/env bash
# IDX signals pipeline — invoked by launchd every 5 minutes.
#
# Self-gates: exits fast outside IDX hours.
# Self-dedupes: hashes the (ticker, strategy) signal set; skips Hermes +
#   git push if unchanged from previous run.
#
# Cost per run when nothing changed: ~2s (TV fetch + compute + hash).
# Cost when signals changed: ~5 min (Hermes 72B + push).

set -euo pipefail

ROOT="$HOME/idx-signals"
LOG_DIR="$ROOT/logs"
HASH_FILE="$ROOT/.last_signals_hash"
mkdir -p "$LOG_DIR"

# --- 1. Market-hours guard (IDX: Mon-Fri 09:00-15:55 WIB = +07) ------------
# Compute the current WIB hour:minute regardless of local TZ.
WIB_HM=$(TZ=Asia/Jakarta date +%H%M)
WIB_DOW=$(TZ=Asia/Jakarta date +%u)  # 1=Mon ... 7=Sun
if [ "$WIB_DOW" -gt 5 ]; then
  exit 0  # weekend
fi
if [ "$WIB_HM" -lt 0900 ] || [ "$WIB_HM" -gt 1555 ]; then
  exit 0  # outside trading hours
fi

# Indonesian public holiday check (IDX closed)
if ! "$ROOT/.venv/bin/python" -c "
import holidays, datetime, pytz
today = datetime.datetime.now(pytz.timezone('Asia/Jakarta')).date()
import sys
sys.exit(1 if today in holidays.Indonesia() else 0)
"; then
  exit 0  # IDX holiday
fi

LOG="$LOG_DIR/$(date +%Y-%m-%d).log"
exec >> "$LOG" 2>&1

WIB_TS=$(TZ=Asia/Jakarta date "+%Y-%m-%d %H:%M:%S WIB")
echo ""
echo "[$WIB_TS] daily.sh tick (local: $(date +%H:%M))"

# --- 2. MLX server lifecycle ----------------------------------------------
MLX_BIN="$HOME/llm/.venv/bin"
MLX_MODEL="mlx-community/Qwen2.5-72B-Instruct-4bit"
MLX_PORT=8080
MLX_LOG="$LOG_DIR/mlx_server.log"
WE_STARTED_MLX=0

ensure_mlx() {
  if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$MLX_PORT/v1/models" | grep -q 200; then
    return
  fi
  echo "  [mlx] starting (will be killed if we started it)"
  nohup "$MLX_BIN/mlx_lm.server" --model "$MLX_MODEL" --port "$MLX_PORT" \
    >> "$MLX_LOG" 2>&1 &
  WE_STARTED_MLX=1
  for i in $(seq 1 60); do
    if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$MLX_PORT/v1/models" | grep -q 200; then
      echo "  [mlx] ready after ${i}×2s"
      return
    fi
    sleep 2
  done
  echo "  [mlx] failed to come up — Hermes step will be skipped"
}

cleanup() {
  if [ "$WE_STARTED_MLX" = "1" ]; then
    pkill -f "mlx_lm.server.*--port $MLX_PORT" || true
  fi
}
trap cleanup EXIT

# --- 3. Fetch + compute (cheap, always run) --------------------------------
"$ROOT/.venv/bin/python" "$ROOT/fetch_intraday_tv.py" > /dev/null
"$ROOT/.venv/bin/python" "$ROOT/compute_signals_live.py" > /dev/null

# --- 4. Dedupe — hash the (ticker, strategy) set ---------------------------
CURRENT_HASH=$(jq -r '[.[] | .ticker + "/" + .strategy] | sort | join(",")' \
                  "$ROOT/candidates.json" | shasum -a 256 | cut -d' ' -f1)
LAST_HASH=$(cat "$HASH_FILE" 2>/dev/null || echo "")
N_SIGNALS=$(jq length "$ROOT/candidates.json")

if [ "$CURRENT_HASH" = "$LAST_HASH" ]; then
  echo "  [dedupe] signal set unchanged ($N_SIGNALS signals) — skipping Hermes + push"
  exit 0
fi

echo "  [change] signal set changed (was $N_SIGNALS now $(jq length $ROOT/candidates.json)) — running full pipeline"

# --- 5. Expensive path: Hermes + outcomes + git push ----------------------
ensure_mlx

"$ROOT/ask_hermes.sh" > /dev/null 2>&1 || echo "  [warn] Hermes step failed; continuing"
"$ROOT/.venv/bin/python" "$ROOT/track_outcomes.py" > /dev/null

cd "$ROOT"
git add signals/ outcomes.csv ticker_edge.json data/snapshot_*.json 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -q -m "auto: $WIB_TS"
  git push -q origin main && echo "  [git] pushed"
fi

# Update hash AFTER successful run so next tick will dedupe correctly
echo "$CURRENT_HASH" > "$HASH_FILE"

# --- 6. Notify (macOS + optional Telegram) --------------------------------
# Pick session label based on current WIB hour
case "${WIB_HM:0:2}" in
  09) SESSION="🌅 Sesi Pagi" ;;
  12) SESSION="☀️ Sesi Siang" ;;
  15) SESSION="🌆 Menjelang Tutup" ;;
  *)  SESSION="📊 Update $WIB_HM WIB" ;;
esac

# Top 3 picks from candidates.json (high/medium only) → notification body
TOP3=$(jq -r '[.[] | select(.history.tier == "high" or .history.tier == "medium")]
              | sort_by(.history.tier, -(.history.edge_5d // 0))
              | .[0:3]
              | map("\(.ticker) (\(.history.tier))")
              | join(", ")' "$ROOT/candidates.json")

N_HIGH=$(jq '[.[] | select(.history.tier == "high")] | length' "$ROOT/candidates.json")
N_MED=$(jq '[.[] | select(.history.tier == "medium")] | length' "$ROOT/candidates.json")

NOTIF_TITLE="IDX Signals — $SESSION"
NOTIF_BODY="${N_HIGH} HIGH, ${N_MED} MEDIUM. Top: ${TOP3:-none}"

# macOS notification (always — zero config)
osascript -e "display notification \"$NOTIF_BODY\" with title \"$NOTIF_TITLE\" sound name \"Glass\"" 2>/dev/null || true

# Telegram push (only if both env vars set — see README for setup)
if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  TG_MSG=$(printf '*%s*\n%s\n\nFull report: %s' \
    "$NOTIF_TITLE" "$NOTIF_BODY" \
    "https://github.com/yazqe/idx-signals/blob/main/signals/$(date +%Y-%m-%d)-hermes.md")
  curl -s -o /dev/null -X POST \
    "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    -d "chat_id=${TELEGRAM_CHAT_ID}" \
    -d "parse_mode=Markdown" \
    --data-urlencode "text=${TG_MSG}" || echo "  [tg] send failed"
fi

echo "  [done]"
