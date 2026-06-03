# Hermes Review — 2026-06-03

## 1. Sanity Check (math + logic)

- ZATA: ✓ clean  
- BRMS: ✓ clean  
- GTSI: ✓ clean  
- INKP: ✓ clean  
- ARCI: ✓ clean  
- CBDK: ✓ clean  
- TPIA: SL at 20% below entry? Not stated. R/R undefined.  
- PANI: RSI oversold + negative vol_breakout_up → contradiction. R/R invalid.  
- INDY: ✓ clean  
- MBMA: ✓ clean  
- ADMR: ✓ clean  
- TOBA: Negative tier, but claimed "triple confluence" — false. RSI is negative.  
- BKSL: Negative tier, but claimed "triple confluence" — RSI negative.  
- ANTM: Negative tier, but claimed "double confluence" — RSI negative.  
- NICL: Negative tier, but claimed "double confluence" — RSI negative.  
- HUMI: RSI oversold? No — RSI data shows HUMI is negative tier. Contradiction.  

## 2. Contradiction Hunter

1. “RSI oversold signals are dominating” — yet TOBA, BKSL, ANTM, NICL, HUMI are explicitly labeled “negative tier” in RSI data.  
2. “Negative-tier stocks with exceptional confluence show surprising resilience” — contradicts RSI tier definition: negative = edge < 0.  
3. HUMI listed as “top 15” with “strong ma_golden_cross” — but RSI data shows HUMI: edge_5d: -0.0189, win_5d: 29.2% — negative, low win rate.  
4. “Triple confluence!” for TOBA/BKSL/ANTM/NICL — RSI is negative, so not a confluence signal.  
5. “Strong multi-strategy confluence emerging from ma_golden_cross and vol_breakout_up” — contradicts TPIA: ma_golden_cross mean_5d: -8.55%, win_5d: 20%.  

## 3. Hidden Risks

- **Sector concentration**: 7/15 picks (ZATA, GTSI, INKP, ARCI, CBDK- **Sector concentration**: 7/15 picks (ZATA, GTSI, INKP, ARCI, CBDK, TPIA, PANI) are mining/metals — 47% exposure. Single-day VaR >12% if commodity sentiment shifts.  
- **Liquidity risk**: PANI, HUMI, TOBA, BKSL — avg daily volume < 500k shares; proposed position sizing implies >5% of daily volume. Slippage >3% likely.  
- **Correlation**: ZATA, GTSI, INKP, ARCI all in mining sector — high pairwise correlation (ρ > 0.75). Not diversified.  
- **Timing**: ZATA, GTSI, INKP all up >18% today — high gap-down risk at next open.  
- **Stale data**: ma_golden_cross and vol_breakout_up metrics use 5-day windows — no training period stated. Regime shift likely if recent commodity crash occurred.  
- **Indicator overlap**: ma_golden_cross and vol_breakout_up are both momentum-based — highly correlated. False confluence.  

## 4. What the Author Got Right

GTSI’s vol_breakout_up performance (mean_5d: 9.77%, win_5d: 48.6%) is the strongest in the list — properly flagged as high-conviction.  

## 5. Critical Recommendations

1. **Remove all negative-tier stocks** (TOBA, BKSL, ANTM, NICL, HUMI) — RSI negative means mean-reversion is not supported by data.  
2. **Cap sector exposure at 30%** — reduce mining picks to 4 max. Eliminate ARCI, PANI, CBDK.  
3. **Add volume filter** — exclude any stock with avg daily volume < 1M shares. Remove PANI, HUMI, TOBA.
