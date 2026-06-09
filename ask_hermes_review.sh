#!/usr/bin/env bash
# Send a manual trading ranking/analysis (markdown) to Hermes for CRITIC review.
# Positioned as devil's advocate, NOT co-author — find weaknesses, not validate.
#
# Usage:
#   ./ask_hermes_review.sh <input.md> [output.md]
#
# If output.md omitted, writes to <input_basename>-review.md in same directory.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <input.md> [output.md]" >&2
  echo "Example: $0 ~/Desktop/konglo_ranking_2026-05-25.md" >&2
  exit 2
fi

INPUT="$1"
if [ ! -f "$INPUT" ]; then
  echo "[error] Input file not found: $INPUT" >&2
  exit 1
fi

# Default output: <input>-review.md alongside input
if [ $# -ge 2 ]; then
  OUTPUT="$2"
else
  INPUT_DIR="$(cd "$(dirname "$INPUT")" && pwd)"
  INPUT_BASE="$(basename "$INPUT" .md)"
  OUTPUT="$INPUT_DIR/${INPUT_BASE}-review.md"
fi

RANKING_CONTENT="$(cat "$INPUT")"

read -r -d '' PROMPT <<'EOF' || true
You are a SKEPTICAL trading risk reviewer for IDX (Indonesia Stock Exchange).
Your job is to CRITIQUE a trading analysis someone else produced — find
weaknesses, contradictions, hidden risks, and math errors.

DO NOT validate or restate the analysis. DO NOT add new picks. DO NOT
agree to be polite. Your value = finding what the author missed.

You will receive a markdown document containing a ranked list of stock
picks with entry / stop loss / take profit / risk-reward / conviction.

Produce a review in this EXACT structure:

# Hermes Review — <today's date>

## 1. Sanity Check (math + logic)

For each pick in the ranking, verify:
- R/R math: Is (TP1 - Entry) / (Entry - SL) actually equal to the stated R/R?
- SL placement: Is the SL at a logical structure level, or arbitrary %?
- TP placement: Are TPs at resistance levels mentioned in the analysis, or unjustified?
- Tier consistency: Does the conviction rating match the underlying evidence
  density? Flag tier inflation (5⭐ for thin evidence) or deflation.

Output: bullet list of every issue found. If a pick is mathematically clean,
say "<TICKER>: ✓ clean".

## 2. Contradiction Hunter

Look across the analysis for INTERNAL contradictions:
- Stock flagged "avoid" in one section but appearing in allocation elsewhere?
- Indicators contradicting each other (e.g., bullish CHoCH but Markov live BEAR)?
- Multi-TF mismatch ignored (e.g., Daily bullish but Weekly bearish, treated
  as bullish)?
- Position sizing inconsistent with stated conviction tier?

Output: numbered list of contradictions, each with: location quote + why
contradictory.

## 3. Hidden Risks

Surface risks the author likely did NOT consider:
- **Sector concentration**: What % of portfolio is single-sector (mining/coal/
  metal/bank)? Single-day VaR if sector reverses?
- **Liquidity risk**: Any tier-1 picks with thin avg daily volume relative to
  proposed position size?
- **Correlation**: Stocks that move together (e.g., same conglomerate group,
  same commodity exposure) — over-concentration disguised as diversification.
- **Timing**: Stocks that already moved >15% today — chase risk, gap-down
  vulnerability at next open?
- **Stale data**: Any indicators relying on Markov "long-run mix" — is the
  training window mentioned? Could be stale if regime shifted recently.
- **Indicator overlap**: SMC + DA8 + Markov — are these truly independent
  signals or do they correlate (false confluence)?

## 4. What the Author Got Right

ONE short paragraph acknowledging genuinely strong reasoning in the analysis.
Be specific. This is the only "positive" section — keep it terse.

## 5. Critical Recommendations

Top 3 ACTIONABLE changes the author should make BEFORE entering trades:
- Be specific: "Reduce KAQI position from 15% to 5% because..."
- Not generic: NOT "be careful with small caps"

---

ANALYSIS TO REVIEW:

EOF

FULL_PROMPT="${PROMPT}
${RANKING_CONTENT}"

echo "[hermes-review] Input:  $INPUT"
echo "[hermes-review] Output: $OUTPUT"
echo "[hermes-review] Sending to Hermes (Qwen3-Next-80B-A3B MoE, ~30-90s)..."
echo ""

"$(cd "$(dirname "$0")" && pwd)/llm_oneshot.sh" "$FULL_PROMPT" | tee "$OUTPUT"

echo ""
echo "[hermes-review] Saved review to: $OUTPUT"
