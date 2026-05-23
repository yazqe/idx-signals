#!/usr/bin/env bash
# Feed today's HIGH + MEDIUM tier signals to Hermes Agent for qualitative analysis.
# Skips LOW/UNTESTED/NEGATIVE — backtest shows poor edge.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
CANDIDATES="$ROOT/candidates.json"
TODAY=$(date +%Y-%m-%d)
OUT="$ROOT/signals/${TODAY}-hermes.md"

if [ ! -s "$CANDIDATES" ]; then
  echo "No candidates.json. Run compute_signals.py first." >&2
  exit 1
fi

# Filter to high + medium only via jq
FILTERED=$(jq '[.[] | select(.history.tier == "high" or .history.tier == "medium")]' "$CANDIDATES")
COUNT=$(echo "$FILTERED" | jq length)

if [ "$COUNT" -eq 0 ]; then
  echo "No high/medium conviction signals today. Skipping Hermes." | tee "$OUT"
  exit 0
fi

read -r -d '' PROMPT <<'EOF' || true
You are an IDX (Indonesia Stock Exchange) trading analyst. Below is a JSON list
of TODAY'S BUY signals, already pre-filtered to only HIGH and MEDIUM historical
conviction tiers (based on 2-year backtest of this exact strategy on this exact
ticker).

Strategies used (all BUY-side; SELL-side dropped because backtest showed they
predict continuation, not reversal):
- rsi_oversold:     14d RSI crossed below 30
- ma_golden_cross:  20-SMA crossed above 50-SMA today
- vol_breakout_up:  volume > 2x 20d avg AND price up > 2% today

Each signal includes a `history` block with:
  - tier:    "high" (mean 5d return ≥ +5%, n≥4) or "medium" (+2% to +5%, n≥3)
  - edge_5d: historical mean 5d forward return for this ticker+strategy
  - win_5d:  historical fraction of trades that closed positive at 5d
  - n:       number of historical occurrences

Your job: pick the TOP 5 ideas for a 5-20 trading-day hold horizon.

Filtering rules:
1. Prioritize HIGH tier over MEDIUM.
2. Prefer confluence (same ticker triggering multiple strategies today).
3. Prefer high win_5d (≥ 0.55) over just-high mean (a few big winners can mask
   most being losses).
4. Note any ticker triggering vol_breakout_up — this had the best Sharpe in
   backtest (1.13 at 20d).

For each of your TOP 5 picks, output in this EXACT format:

## <TICKER> — BUY (5-20d hold)
- Triggered: <strategy(s)>
- Conviction: <High | Medium>
- Historical edge: <mean_5d>% over <n> past trades (win rate <win_5d>%)
- Entry zone: <current close ± a sensible range>
- Stop loss: <-X% below close, e.g. -8%>
- Take profit: <+Y% above close, e.g. +12%>
- Why: <1 sentence — what specific signal + history suggests>

After the 5 picks, write a 2-3 sentence "Market read" — what does the
distribution of HIGH/MEDIUM signals say about IDX small/mid-caps today.

Be terse. No preamble. If fewer than 5 picks meet quality bar, list fewer.

SIGNALS:
EOF

echo "Analyzing $COUNT high+medium conviction signals (skipped low/negative)..."
echo ""

FULL_PROMPT="${PROMPT}
${FILTERED}"

~/.local/bin/hermes -z "$FULL_PROMPT" | tee "$OUT"

echo ""
echo "Saved to: $OUT"
