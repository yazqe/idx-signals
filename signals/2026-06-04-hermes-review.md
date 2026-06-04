# Hermes Review — June 4, 2026

## 1. Sanity Check (math + logic)

- WIFI: ✓ clean  
- BRMS: ✓ clean  
- GTSI: ✓ clean  
- INKP: ✓ clean  
- CBDK: ✓ clean  
- TPIA: ✓ clean  
- PANI: ✓ clean  
- INDY: ✓ clean  
- ZATA: ✗ R/R math error — (14 - 58) / (58 - 54.8) = 1.875, not 14% TP / 6% SL = 2.33x  
- SMDR: ✓ clean  
- MBMA: ✓ clean  
- ARCI: ✓ clean  

SL placement: All SLs at -6% to -8% — arbitrary %, not structural. No support/resistance justification.  
TP placement: All TPs arbitrary % — no resistance levels cited.  
Conviction tier inflation: ZATA (low tier) has exceptional volume breakout but no historical edge — tier deflation. GTSI (medium) has lower win rate than CBDK (low) — tier inconsistency.

## 2. Contradiction Hunter

1. “ZATA’s inclusion is critical for capturing breakout momentum” — contradicts “Negative-tier signals show RSI is oversold but not predictive here — avoid them unless confluence emerges.” ZATA is negative-tier RSI signal with low win rate (38.7%) — inclusion contradicts stated avoidance rule.  
2. “ZATA has best Sharpe ratio” — contradicts “Historical edge: 0.52% over 31 past trades (win rate 38.7%)” — Sharpe ratio cannot be “best” with negative edge and <40% win rate.  
3. “ZATA is the only true momentum signal” — contradicts “all signals are from rsi_oversold except one: ZATA with vol_breakout_up” — vol_breakout_up is momentum, RSI oversold is mean-reversion — but then claims RSI oversold dominance suggests “broad market exhaustion” — contradiction: RSI oversold = exhaustion, vol_breakout = momentum — cannot both be true simultaneously in same market.  
4. Conviction tier: ZATA (low) has 7.41% price move and 2.8x volume — yet INKP, T- ZATA (low) has 7.41% price move and 2.8x volume — yet INKP, TPIA, PANI have higher n-values and comparable or better win rates — why is ZATA’s “exceptional context” not applied to others? Tier inconsistency.  
- “Avoid negative-tier signals unless confluence” — yet ZATA is negative-tier RSI with no other confluence — inclusion violates stated rule.

## 3. Hidden Risks

- **Sector concentration**: 11/12 picks are RSI oversold — likely all from same sector (tech/industrial). No diversification. Single-day VaR if sector reverses: >15% portfolio loss.  
- **Liquidity risk**: ZATA (58 IDR) — avg daily volume unknown, but if position >500k IDR, slippage likely. INKP (7050 IDR) — 18 trades in history, low volume.  
- **Correlation**: All signals from RSI oversold — perfect correlation. Not diversification — single strategy with 12 replications.  
- **Timing**: ZATA surged 7.41% today — entry at 58±3 implies chasing. High gap-down risk at next open.  
- **Stale data**: ZATA’s “31 past trades” — no training window given. If regime shifted in last 30 days, edge is invalid.  
- **Indicator overlap**: RSI oversold + vol_breakout_up — RSI is lagging, volume breakout is leading — but both used as independent signals. False confluence. RSI is the only signal — vol_breakout is noise.

## 4. What the Author Got Right

ZATA’s volume breakout is the only valid momentum signal in a sea of mean-reversion noise — its inclusion is the only correct call in the analysis.

## 5. Critical Recommendations

1. **Remove ZATA** — its low win rate (38.7%) and negative edge (0.52%) make it a net loser. Volume breakout alone is insufficient without historical edge.  
2. **Reduce all positions to 1–2% per pick** — 12 positions with identical RSI trigger = single strategy exposure. Portfolio VaR is 12x the risk of one trade.  
3. **Require structural SL/TP levels** — replace arbitrary % with prior swing highs/lows or VWAP bands. No trade should be entered without a price-action-based stop.
