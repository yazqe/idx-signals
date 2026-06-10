#!/usr/bin/env bash
# Stage 3 of 3-stage Hermes pipeline: consolidate picks + critic into FINAL ranking.
#
# Takes initial picks (hermes-picks.md) + critic review (hermes-review.md)
# + full candidates list, produces final consolidated top 5-7 ranking that
# may DEMOTE picks the critic exposed as flawed, or PROMOTE stocks from the
# candidate pool that the initial picks missed.
#
# Output (hermes.md) is what notify.sh links as "Full report".

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
CANDIDATES="$ROOT/candidates.json"
TODAY=$(date +%Y-%m-%d)
PICKS="$ROOT/signals/${TODAY}-hermes-picks.md"
REVIEW="$ROOT/signals/${TODAY}-hermes-review.md"
OUT="$ROOT/signals/${TODAY}-hermes.md"

if [ ! -s "$PICKS" ]; then
  echo "Missing initial picks: $PICKS" >&2
  exit 1
fi
if [ ! -s "$REVIEW" ]; then
  echo "Missing critic review: $REVIEW" >&2
  exit 1
fi
if [ ! -s "$CANDIDATES" ]; then
  echo "Missing candidates.json" >&2
  exit 1
fi

PICKS_CONTENT="$(cat "$PICKS")"
REVIEW_CONTENT="$(cat "$REVIEW")"
ALL_CANDIDATES=$(cat "$CANDIDATES")

read -r -d '' PROMPT <<'EOF' || true
You are the FINAL DECISION-MAKER in a 3-stage IDX trading pipeline. Two
previous stages produced:

  STAGE 1 — Initial picks (10-15 broader candidates picked by another analyst)
  STAGE 2 — Critic review (devil's advocate who found weaknesses)
  RAW DATA — Full candidates list (ALL today's signals, all tiers)

Your job: produce the FINAL CONSOLIDATED RANKING of up to 7 picks for trading.

HARD RULES (violating these makes the output worthless):
  - EVERY ticker MUST appear by name in the RAW DATA candidates list below.
    NEVER introduce a ticker that is not in that list (no PTBA/BBCA/TLKM/etc.
    from memory). If you are unsure a ticker is in the list, do not include it.
  - ALL prices (Entry/SL/TP) MUST be derived from that candidate's `close`
    value in the RAW DATA. NEVER use a price from memory or training data.
  - Use ONLY the strategy names present in the data (rsi_oversold,
    ma_golden_cross, vol_breakout_up). Do NOT invent triggers like "da8_bullish".
  - If fewer than 7 candidates exist, output ONLY that many. Do NOT pad the
    list to reach a count — 2 real picks beats 7 with 5 invented.

You have the AUTHORITY to:
  - DROP picks the critic exposed as mathematically broken or risk-flawed
  - PROMOTE/REORDER underrated picks — but ONLY tickers already in the
    candidates list below (e.g. LOW/UNTESTED tiers with multi-strategy confluence)

For each FINAL pick, output in this format:

## <RANK>. <TICKER> — BUY (5-20d hold)
- **Triggered:** <strategy(s)>
- **Conviction:** <Your assessment, NOT the original tier — e.g., "High after critic review">
- **Historical edge:** <mean_5d>% over <n> trades (win rate <win_5d>%)
- **Entry zone:** <price range>
- **Stop loss:** <price level + brief why — prefer structure over arbitrary %>
- **Take profit:** <price level + brief why>
- **R/R:** <calculate explicitly: (TP - mid_entry) / (mid_entry - SL), single number, e.g. 1.8>
- **Why selected:** <1 sentence — what about this pick wins>
- **Critic addressed:** <1 sentence — which critic finding does this pick survive, OR which finding caused you to demote/drop from initial>

Then add a section:

### Changes from Initial Picks
- **Dropped:** <list tickers from initial picks not in final, + 1-line reason>
- **Added:** <list tickers added from candidate pool, + 1-line reason>
- **Reordered:** <key reorderings worth noting>

### Market Read
2-3 sentences on what today's signal distribution + critic findings say
about IDX small/mid-cap conditions.

Be terse. No preamble. Output must be self-contained — the user will read
THIS file as the primary trading document.

═════════════════════════════════════════════════════════════════════════
STAGE 1 — INITIAL PICKS:
═════════════════════════════════════════════════════════════════════════
EOF

FULL_PROMPT="${PROMPT}

${PICKS_CONTENT}

═════════════════════════════════════════════════════════════════════════
STAGE 2 — CRITIC REVIEW:
═════════════════════════════════════════════════════════════════════════

${REVIEW_CONTENT}

═════════════════════════════════════════════════════════════════════════
RAW DATA — ALL CANDIDATES (use to find missed opportunities):
═════════════════════════════════════════════════════════════════════════

${ALL_CANDIDATES}
"

echo "Stage 3/3: Consolidating picks + critic into final ranking..."
echo ""

"$ROOT/llm_oneshot.sh" "$FULL_PROMPT" | tee "$OUT"

echo ""
echo "Saved final consolidated report to: $OUT"
