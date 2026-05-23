#!/usr/bin/env bash
# Daily IDX signals pipeline — runs Mon-Fri at 11:00 local (15:00 WIB,
# 1 hour before IDX close) via launchd.
#
# Lifecycle:
#   1. Start MLX server if not already running (Qwen2.5-72B for Hermes)
#   2. Fetch intraday data via TradingView scanner
#   3. Compute live BUY signals (tier-sorted by historical edge)
#   4. Hermes qualitative review → top 5 picks
#   5. Track outcomes of past signals (1/5/20d realized returns)
#   6. Commit + push to GitHub
#   7. Stop MLX server if we started it (leaves it alone if already running)

set -euo pipefail

ROOT="$HOME/idx-signals"
LOG_DIR="$ROOT/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/$(date +%Y-%m-%d).log"

# Redirect everything to log file + stdout
exec > >(tee -a "$LOG") 2>&1

echo ""
echo "==========================================================="
echo "  $(date)  —  daily.sh starting"
echo "==========================================================="

MLX_BIN="$HOME/llm/.venv/bin"
MLX_MODEL="mlx-community/Qwen2.5-72B-Instruct-4bit"
MLX_PORT=8080
MLX_LOG="$LOG_DIR/mlx_server.log"
WE_STARTED_MLX=0

# --- 1. Ensure MLX server up -----------------------------------------------
if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$MLX_PORT/v1/models" | grep -q 200; then
  echo "[mlx] already running on :$MLX_PORT"
else
  echo "[mlx] not running — starting (model: $MLX_MODEL)"
  nohup "$MLX_BIN/mlx_lm.server" --model "$MLX_MODEL" --port "$MLX_PORT" \
    >> "$MLX_LOG" 2>&1 &
  WE_STARTED_MLX=1
  # Wait up to 120s for server (72B takes ~30-60s to load)
  for i in $(seq 1 60); do
    if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$MLX_PORT/v1/models" | grep -q 200; then
      echo "[mlx] ready after ${i}×2s"
      break
    fi
    sleep 2
  done
fi

cleanup() {
  if [ "$WE_STARTED_MLX" = "1" ]; then
    echo "[mlx] stopping (we started it)"
    pkill -f "mlx_lm.server.*port $MLX_PORT" || true
  fi
}
trap cleanup EXIT

# --- 2. Fetch intraday -----------------------------------------------------
echo ""
echo "[1/5] Fetching intraday data via TradingView scanner..."
"$ROOT/.venv/bin/python" "$ROOT/fetch_intraday_tv.py"

# --- 3. Compute signals ----------------------------------------------------
echo ""
echo "[2/5] Computing live signals..."
"$ROOT/.venv/bin/python" "$ROOT/compute_signals_live.py"

# --- 4. Hermes analysis ----------------------------------------------------
echo ""
echo "[3/5] Hermes qualitative review..."
"$ROOT/ask_hermes.sh" || echo "[warn] Hermes step failed; continuing"

# --- 5. Track outcomes -----------------------------------------------------
echo ""
echo "[4/5] Tracking outcomes of past signals..."
"$ROOT/.venv/bin/python" "$ROOT/track_outcomes.py"

# --- 6. Git commit + push --------------------------------------------------
echo ""
echo "[5/5] Committing & pushing to GitHub..."
cd "$ROOT"
git add signals/ outcomes.csv ticker_edge.json data/snapshot_*.json 2>/dev/null || true
if git diff --cached --quiet; then
  echo "  No changes to commit."
else
  git commit -q -m "daily: $(date +%Y-%m-%d)"
  git push -q origin main && echo "  Pushed to origin/main."
fi

echo ""
echo "==========================================================="
echo "  $(date)  —  daily.sh done"
echo "==========================================================="
