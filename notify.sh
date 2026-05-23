#!/usr/bin/env bash
# Send signal notification to macOS + (optional) Telegram channel.
# Called by daily.sh after a successful pipeline run.
# Standalone usage: `./notify.sh` — sends current candidates.json state.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

# Pick up secrets if not already exported (e.g. when run directly, not via daily.sh)
if [ -f "$HOME/.idx-signals.env" ] && [ -z "${TELEGRAM_BOT_TOKEN:-}" ]; then
  set -a; . "$HOME/.idx-signals.env"; set +a
fi

CANDIDATES="$ROOT/candidates.json"
if [ ! -s "$CANDIDATES" ]; then
  echo "No candidates.json — nothing to notify about." >&2
  exit 1
fi

WIB_HM=$(TZ=Asia/Jakarta date +%H%M)
WIB_DATE=$(TZ=Asia/Jakarta date +%Y-%m-%d)

case "${WIB_HM:0:2}" in
  09) SESSION="🌅 Sesi Pagi" ;;
  12) SESSION="☀️ Sesi Siang" ;;
  15) SESSION="🌆 Menjelang Tutup" ;;
  *)  SESSION="📊 Update ${WIB_HM:0:2}:${WIB_HM:2:2} WIB" ;;
esac

# Counts
N_HIGH=$(jq '[.[] | select(.history.tier == "high")] | length' "$CANDIDATES")
N_MED=$(jq  '[.[] | select(.history.tier == "medium")] | length' "$CANDIDATES")
N_TOTAL=$(jq 'length' "$CANDIDATES")

# Top 5 picks (high + medium), formatted as fixed-width table for monospace block
TOP5_TABLE=$(jq -r '
  [.[] | select(.history.tier == "high" or .history.tier == "medium")]
  | sort_by(.history.tier, -(.history.edge_5d // 0))
  | .[0:5]
  | (["TICKER", "STRAT", "EDGE", "WIN", "TIER"] | @tsv),
    (.[] | [
      .ticker,
      (.strategy | sub("vol_breakout_up"; "volBO") | sub("rsi_oversold"; "RSI<30") | sub("ma_golden_cross"; "MA✗")),
      (if .history.edge_5d != null then ((.history.edge_5d * 1000 | round / 10) | (if . >= 0 then "+" else "" end) + tostring + "%") else "—" end),
      (if .history.win_5d != null then ((.history.win_5d * 100) | round | tostring + "%") else "—" end),
      (.history.tier | ascii_upcase)
    ] | @tsv)
' "$CANDIDATES" | awk -F'\t' 'BEGIN{
  fmt="%-7s %-7s %7s %5s %-6s\n"
}{ printf fmt, $1, $2, $3, $4, $5 }')

# --- macOS notification (always) ------------------------------------------
TOP3_NAMES=$(jq -r '
  [.[] | select(.history.tier == "high" or .history.tier == "medium")]
  | sort_by(.history.tier, -(.history.edge_5d // 0))
  | .[0:3] | map(.ticker) | join(", ")' "$CANDIDATES")

MAC_TITLE="IDX Signals — $SESSION"
MAC_BODY="${N_HIGH} HIGH, ${N_MED} MEDIUM. Top: ${TOP3_NAMES:-none}"
osascript -e "display notification \"$MAC_BODY\" with title \"$MAC_TITLE\" sound name \"Glass\"" 2>/dev/null || true

# --- Telegram (only if env vars set) --------------------------------------
if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ -z "${TELEGRAM_CHAT_ID:-}" ]; then
  echo "[telegram] env vars not set — skipping (set TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID in ~/.idx-signals.env)"
  exit 0
fi

# Build hybrid message: short header + monospace top-5 + link
# Cache-bust the URL with first 8 chars of report content hash:
# same content → same URL (browser cache works); content changes → URL changes
# → browser fetches fresh (no more "stale on phone" issue).
HERMES_FILE="$ROOT/signals/${WIB_DATE}-hermes.md"
CACHE_BUST=""
if [ -f "$HERMES_FILE" ]; then
  CACHE_BUST="?v=$(shasum -a 256 "$HERMES_FILE" | cut -c1-8)"
fi
REPORT_URL="https://yazqe.github.io/idx-signals/signals/${WIB_DATE}-hermes.html${CACHE_BUST}"

TG_MSG=$(printf '*%s — %s*\n%d HIGH · %d MEDIUM · %d total signals\n\n```\n%s```\n\n[📄 Full report](%s)' \
  "IDX Signals" "$SESSION" \
  "$N_HIGH" "$N_MED" "$N_TOTAL" \
  "$TOP5_TABLE" \
  "$REPORT_URL")

RESP=$(curl -s -X POST \
  "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  -d "chat_id=${TELEGRAM_CHAT_ID}" \
  -d "parse_mode=Markdown" \
  -d "disable_web_page_preview=true" \
  --data-urlencode "text=${TG_MSG}")

if echo "$RESP" | jq -e '.ok' > /dev/null 2>&1; then
  echo "[telegram] sent to chat ${TELEGRAM_CHAT_ID}"
else
  echo "[telegram] send failed:"
  echo "$RESP" | jq . 2>/dev/null || echo "$RESP"
  exit 1
fi
