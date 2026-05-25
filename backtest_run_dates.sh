#!/usr/bin/env bash
# Run full 3-stage Hermes pipeline on a list of historical dates.
#
# For each date:
#   1. Save real candidates.json
#   2. Replace with reconstructed candidates for that date
#   3. Run ask_hermes.sh → ask_hermes_review.sh → ask_hermes_finalize.sh → fix_rr_math.py
#   4. Move outputs to signals/backtest/{date}-hermes-{picks,review,final}.md
#   5. Restore real candidates.json
#   6. Restart MLX server between dates (avoid OOM)
#
# Usage:
#   ./backtest_run_dates.sh 2026-02-02 2026-02-13 2026-03-02 2026-03-13 2026-04-02

set -uo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
BACKTEST_DIR="$ROOT/signals/backtest"
mkdir -p "$BACKTEST_DIR"

MLX_BIN="$HOME/llm/.venv/bin"
MLX_MODEL="mlx-community/Qwen2.5-72B-Instruct-4bit"
MLX_PORT=8080
MLX_LOG="$ROOT/logs/mlx_server.log"

if [ $# -eq 0 ]; then
  echo "Usage: $0 YYYY-MM-DD [YYYY-MM-DD ...]" >&2
  exit 2
fi

DATES=("$@")
TOTAL=${#DATES[@]}

# ── MLX lifecycle ─────────────────────────────────────────────────────────

mlx_alive() {
  curl -s -o /dev/null -w "%{http_code}" --max-time 3 \
    "http://localhost:$MLX_PORT/v1/models" | grep -q 200
}

mlx_restart() {
  pkill -f "mlx_lm.server" 2>/dev/null
  sleep 3
  echo "  [mlx] starting fresh server..."
  nohup "$MLX_BIN/mlx_lm.server" --model "$MLX_MODEL" --port "$MLX_PORT" \
    >> "$MLX_LOG" 2>&1 &
  for i in $(seq 1 60); do
    if mlx_alive; then
      echo "  [mlx] ready after ${i}×3s"
      return 0
    fi
    sleep 3
  done
  echo "  [mlx] FAILED to come up — aborting"
  return 1
}

# ── Per-date pipeline ────────────────────────────────────────────────────

run_one_date() {
  local DATE="$1"
  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "BACKTEST DATE: $DATE  ($(date '+%H:%M:%S'))"
  echo "═══════════════════════════════════════════════════════════════"

  # 1. Reconstruct candidates
  local TMP_CANDIDATES="$ROOT/.backtest_candidates_${DATE}.json"
  "$ROOT/.venv/bin/python" "$ROOT/backtest_reconstruct.py" "$DATE" > "$TMP_CANDIDATES"
  local N=$(jq length "$TMP_CANDIDATES")
  echo "  [reconstruct] $N candidates"
  if [ "$N" -eq 0 ]; then
    echo "  [skip] no candidates for $DATE"
    return 0
  fi

  # 2. Backup + replace real candidates.json
  cp "$ROOT/candidates.json" "$ROOT/candidates.json.realbak"
  cp "$TMP_CANDIDATES" "$ROOT/candidates.json"

  # 3. Run 3-stage pipeline (using TODAY date naming, will rename after)
  local TODAY=$(date +%Y-%m-%d)
  echo "  [stage 1] ask_hermes.sh (initial picks)"
  "$ROOT/ask_hermes.sh" > /dev/null 2>&1 || echo "    [warn] stage 1 failed"

  if [ -s "$ROOT/signals/${TODAY}-hermes-picks.md" ]; then
    echo "  [stage 2] ask_hermes_review.sh (critic)"
    "$ROOT/ask_hermes_review.sh" \
      "$ROOT/signals/${TODAY}-hermes-picks.md" \
      "$ROOT/signals/${TODAY}-hermes-review.md" > /dev/null 2>&1 \
      || echo "    [warn] stage 2 failed"
  fi

  if [ -s "$ROOT/signals/${TODAY}-hermes-review.md" ]; then
    echo "  [stage 3] ask_hermes_finalize.sh"
    "$ROOT/ask_hermes_finalize.sh" > /dev/null 2>&1 || echo "    [warn] stage 3 failed"
  fi

  if [ -s "$ROOT/signals/${TODAY}-hermes.md" ]; then
    echo "  [post] fix_rr_math.py"
    "$ROOT/.venv/bin/python" "$ROOT/fix_rr_math.py" \
      "$ROOT/signals/${TODAY}-hermes.md" > /dev/null 2>&1 || true
  fi

  # 4. Move outputs to backtest dir, RENAMED with backtest date
  for stage in hermes-picks hermes-review hermes; do
    local SRC="$ROOT/signals/${TODAY}-${stage}.md"
    local DST="$BACKTEST_DIR/${DATE}-${stage}.md"
    if [ -s "$SRC" ]; then
      mv "$SRC" "$DST"
      echo "  [save] $DST ($(wc -l < "$DST") lines)"
    fi
  done

  # 5. Restore real candidates.json
  mv "$ROOT/candidates.json.realbak" "$ROOT/candidates.json"
  rm -f "$TMP_CANDIDATES"

  echo "  [done] $DATE complete at $(date '+%H:%M:%S')"
}

# ── Main loop ─────────────────────────────────────────────────────────────

echo "BACKTEST RUN — $TOTAL dates"
echo "Started: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Ensure MLX up at start
if ! mlx_alive; then
  mlx_restart || exit 1
fi

for i in "${!DATES[@]}"; do
  DATE="${DATES[$i]}"
  echo ""
  echo "▶ Date $((i+1))/$TOTAL: $DATE"

  # Restart MLX every date (3 calls per date — safe before OOM)
  if [ "$i" -gt 0 ]; then
    echo "  [mlx] preventive restart between dates (avoid OOM accumulation)"
    mlx_restart || { echo "MLX restart failed at date $i"; exit 1; }
  fi

  run_one_date "$DATE"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "BACKTEST COMPLETE: $TOTAL dates"
echo "Finished: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Outputs in: $BACKTEST_DIR"
echo "═══════════════════════════════════════════════════════════════"
