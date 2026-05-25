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

# Load secret credentials (Telegram, etc.) — file is chmod 600, never committed
if [ -f "$HOME/.idx-signals.env" ]; then
  set -a; . "$HOME/.idx-signals.env"; set +a
fi

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

# 3-stage Hermes pipeline: picks → critic → finalize.
# Each stage outputs to signals/{date}-hermes-{stage}.md
# Final stage writes signals/{date}-hermes.md (what notify.sh links as Full report).
DATE_TODAY="$(date +%Y-%m-%d)"
HERMES_PICKS="$ROOT/signals/${DATE_TODAY}-hermes-picks.md"
HERMES_REVIEW="$ROOT/signals/${DATE_TODAY}-hermes-review.md"
HERMES_FINAL="$ROOT/signals/${DATE_TODAY}-hermes.md"

# Stage 1: broader initial picks (all tiers considered)
"$ROOT/ask_hermes.sh" > /dev/null 2>&1 || echo "  [warn] Hermes stage 1 (picks) failed; continuing"

# Stage 2: critic review of initial picks
if [ -s "$HERMES_PICKS" ]; then
  "$ROOT/ask_hermes_review.sh" "$HERMES_PICKS" "$HERMES_REVIEW" > /dev/null 2>&1 \
    || echo "  [warn] Hermes stage 2 (review) failed; continuing"
fi

# Stage 3: finalize → re-rank with critic feedback, may add/drop picks
if [ -s "$HERMES_PICKS" ] && [ -s "$HERMES_REVIEW" ]; then
  "$ROOT/ask_hermes_finalize.sh" > /dev/null 2>&1 \
    || echo "  [warn] Hermes stage 3 (finalize) failed; continuing"
fi

# Fallback: if stage 3 didn't produce final, copy picks as final so notify still works
if [ ! -s "$HERMES_FINAL" ] && [ -s "$HERMES_PICKS" ]; then
  cp "$HERMES_PICKS" "$HERMES_FINAL"
  echo "  [warn] Stage 3 missing — using stage 1 picks as final fallback"
fi

# Post-process: LLMs are bad at arithmetic. Recompute R/R from structured prices.
if [ -s "$HERMES_FINAL" ]; then
  "$ROOT/.venv/bin/python" "$ROOT/fix_rr_math.py" "$HERMES_FINAL" \
    || echo "  [warn] R/R post-processing failed; continuing"
fi

"$ROOT/.venv/bin/python" "$ROOT/track_outcomes.py" > /dev/null

# Track Hermes stage outcomes for empirical validation (Stage1 vs Stage3 vs Mechanical)
"$ROOT/.venv/bin/python" "$ROOT/track_outcomes_hermes.py" update > /dev/null 2>&1 \
  || echo "  [warn] hermes outcome tracking failed; continuing"

"$ROOT/.venv/bin/python" "$ROOT/generate_dashboard.py" > /dev/null

# Regenerate validation dashboard (live tracking + backtest comparison)
"$ROOT/.venv/bin/python" "$ROOT/generate_validation_dashboard.py" > /dev/null 2>&1 \
  || echo "  [warn] validation dashboard generation failed; continuing"

cd "$ROOT"
# Add only paths that exist — git add aborts entire batch on first missing pathspec,
# which silently broke the commit/push step when outcomes.csv was missing.
for path in signals/ data/ outcomes.csv ticker_edge.json index.html; do
  if [ -e "$path" ] || compgen -G "$path" > /dev/null 2>&1; then
    git add "$path" 2>/dev/null || true
  fi
done
# Add validation dashboard if it exists
[ -f "$ROOT/validation.html" ] && git add "$ROOT/validation.html" 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -q -m "auto: $WIB_TS"
  if git push -q origin main; then
    echo "  [git] pushed"
  else
    echo "  [git] PUSH FAILED — Telegram link will 404 until next successful push"
  fi
fi

# Update hash AFTER successful run so next tick will dedupe correctly
echo "$CURRENT_HASH" > "$HASH_FILE"

# Notify (macOS + optional Telegram) — see notify.sh for format
"$ROOT/notify.sh" || echo "  [warn] notify step failed"

echo "  [done]"
