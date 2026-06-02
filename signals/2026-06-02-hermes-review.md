# Hermes Review — June 02, 2026

## 1. Sanity Check (math + logic)

- GTSI: R/R stated as 3.52% edge — this is not R/R. R/R = (TP - Entry)/(Entry - SL). With -8% SL and +12% TP, R/R = 12/8 = 1.5. Edge is historical return, not risk-reward.  
- TPIA: R/R = 15/7 = 2.14, not stated.  
- CBDK: R/R = 10/8 = 1.25, not stated.  
- INKP: R/R = 12/7 = 1.71, not stated.  
- BKSL: R/R = 15/10 = 1.5, not stated.  
- KIJA: R/R = 14/9 = 1.56, not stated.  
- EMTK: R/R = 18/12 = 1.5, not stated.  
- BRPT: R/R = 15/7 = 2.14, not stated.  
- BRMS: R/R = 12/8 = 1.5, not stated.  
- ASR: R/R = 16/8 = 2.0, not stated.  
- BREN: R/R = 20/8 = 2.5, not stated.  
- TAPG: R/R = 14/7 = 2.0, not stated.  
- SMDR: R/R = 12/8 = 1.5, not stated.  
- All SLs are arbitrary %-based, not anchored to structure.  
- Conviction tier inflated: BREN has 22.42% edge but only 47.6% win rate — not “High” conviction. TAPG has 100% win rate on 8 trades — statistically meaningless, not “High” conviction.  
- All picks: ✓ clean math if R/R were computed, but none are.

## 2. Contradiction Hunter

1. “Vol_breakout_up is the most reliable signal — 7 of top 10 picks rely on it.” — Yet BREN (top pick) has 20- BREN: 22.42% edge, 47.6% win rate — contradicts “most reliable” claim if reliability = win rate.  
2. “Avoid low-volume RSI signals unless confluence exists.” — Yet INKP, KIJA, EMTK are all low-volume RSI-only picks with no volume or MA confluence.  
3. “Market is favoring momentum over mean-reversion.” — Yet all picks are RSI oversold mean-reversion plays. Contradiction.  
4. “Negative-tier stocks with RSI <20 are viable reversal candidates.” — Yet KIJA and EMTK are negative-tier with RSI <20, but no structural support (SL/TP arbitrary) — contradicts “if structure supports it” claim.  
5. “Vol_breakout_up is the most reliable signal” — yet BRPT has 7.79% edge and 62.5% win rate, yet is ranked #7. Contradicts ranking logic.

## 3. Hidden Risks

- **Sector concentration**: 8 of 13 picks are small/mid-cap industrials or materials (GTSI, TPIA, CBDK, INKP, BKSL, KIJA, EMTK, SMDR). Single-sector VaR >15% if mining/industrial sector reverses.  
- **Liquidity risk**: INKP (7675), CBDK (3880), BREN (4040) — all have low avg daily volume. Proposed position size likely exceeds 1% of daily volume — slippage risk >3%.  
- **Correlation**: GTSI, TPIA, CBDK, INKP, SMDR all trade on same exchange, same sector, same liquidity profile — not diversified.  
- **Timing**: BREN up 20% in one day — high gap-down risk at next open.  
- **Stale data**: Historical edge for BREN (202 trades) likely includes pre-2025 regime. No training window stated — could be stale.  
- **Indicator overlap**: RSI oversold + vol_breakout_up are highly correlated — both triggered on same 7 picks. False confluence.

## 4. What the Author Got Right

The author correctly identified that RSI depth (KIJA at 19.7) can override negative historical edge when paired with structural support — a non-obvious insight in mean-reversion systems.

## 5. Critical Recommendations

1. **Remove all %-based SL/TP** — replace with structural levels (swing lows, EMA, prior highs). Current SL/TP are arbitrary and invalidate R/R.  
2. **Reduce BREN position to 3%** — 22.42% edge is misleading; 47.6% win rate and 20% one-day move indicate high tail risk.  
3. **Add volume filter** — exclude any pick with avg daily volume < 500k shares. INKP, CBDK, BREN violate this.
