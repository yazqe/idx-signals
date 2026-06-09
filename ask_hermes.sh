#!/usr/bin/env bash
# Stage 1 of 3-stage Hermes pipeline: initial broader pick selection.
# Considers ALL tiers (high/medium/low/untested/negative) — lets Hermes
# decide which stocks deserve attention, including surprises from lower tiers.
# Output feeds into ask_hermes_review.sh (critic) → ask_hermes_finalize.sh (final).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
CANDIDATES="$ROOT/candidates.json"
TODAY=$(date +%Y-%m-%d)
OUT="$ROOT/signals/${TODAY}-hermes-picks.md"

if [ ! -s "$CANDIDATES" ]; then
  echo "No candidates.json. Run compute_signals.py first." >&2
  exit 1
fi

COUNT=$(jq length "$CANDIDATES")
ALL_CANDIDATES=$(cat "$CANDIDATES")

if [ "$COUNT" -eq 0 ]; then
  echo "No candidates today. Skipping Hermes." | tee "$OUT"
  exit 0
fi

read -r -d '' PROMPT <<'EOF' || true
You are an IDX (Indonesia Stock Exchange) trading analyst. Below is a JSON list
of TODAY'S BUY signals across ALL conviction tiers (high / medium / low /
untested / negative). DO NOT skip lower tiers automatically — sometimes a
LOW tier with multi-strategy confluence beats a HIGH tier with thin evidence.

Strategies used (all BUY-side; SELL-side dropped because backtest showed they
predict continuation, not reversal):
- rsi_oversold:     14d RSI crossed below 30
- ma_golden_cross:  20-SMA crossed above 50-SMA today
- vol_breakout_up:  volume > 2x 20d avg AND price up > 2% today

Each signal includes a `history` block with:
  - tier:    "high" (mean 5d ≥ +5%, n≥4) / "medium" (+2% to +5%, n≥3) /
             "low" (positive but thin) / "untested" (n<3) / "negative" (lost money historically)
  - edge_5d: historical mean 5d forward return for this ticker+strategy
  - win_5d:  historical fraction of trades that closed positive at 5d
  - n:       number of historical occurrences

Your job: pick the TOP 10-15 ideas for a 5-20 trading-day hold horizon. Cast
a wider net than usual — your output will be reviewed by a critic and a
finalize stage will trim to top 5-7. So be inclusive, not picky.

Selection rules:
1. Strongly prefer multi-strategy confluence (same ticker triggering 2+ strategies today).
2. HIGH/MEDIUM tier get default consideration.
3. LOW tier: include if confluence or strong recent volume action.
4. UNTESTED: include if confluence (no history is not disqualifying).
5. NEGATIVE: include only if today's confluence is EXCEPTIONAL (3+ strategies).
6. vol_breakout_up has best Sharpe (1.13 at 20d) — weight more.

For each pick, output in this EXACT format:

## <TICKER> — BUY (5-20d hold)
- **Triggered:** <strategy(s)>
- **Conviction:** <High | Medium | Low | Untested | Negative-but-confluence>
- **Historical edge:** <mean_5d>% over <n> past trades (win rate <win_5d>%)
- **Entry zone:** <current close ± a sensible range>
- **Stop loss:** <-X% below close>
- **Take profit:** <+Y% above close>
- **Why:** <1 sentence — what specific signal + context justifies inclusion>

After picks, write 2-3 sentence "Market read" under `### Market Read`.
Be terse. No preamble.

SIGNALS:
EOF

echo "Stage 1/3: Asking Hermes for initial broader picks from $COUNT candidates (all tiers)..."
echo ""

FULL_PROMPT="${PROMPT}
${ALL_CANDIDATES}"

"$ROOT/llm_oneshot.sh" "$FULL_PROMPT" | tee "$OUT"

echo ""
echo "Saved initial picks to: $OUT"
