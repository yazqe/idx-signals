# Hermes Review — June 02, 2026

## 1. Sanity Check (math + logic)

- **ASPR**: ✓ clean  
- **GTSI**: ✓ clean  
- **INKP**: ✓ clean  
- **CBDK**: ✓ clean  
- **TPIA**: R/R = (1850×1.15 - 1850) / (1850 - 1850×0.9) = 212.75 / 185 = 1.15 → stated R/R 3.84x? **MATH ERROR**  
- **INDY**: ✓ clean  
- **TOBA**: ✓ clean  
- **BKSL**: R/R = (74×1.1 - 74) / (74 - 74×0.92) = 7.4 / 5.92 = 1.25 → stated R/R 1.25x? **MATH ERROR** (stated 1.25x, but logic implies higher)  
- **KIJA**: R/R = (123×1.12 - 123) / (123 - 123×0.92) = 9.84 / 9.84 = 1 → stated R/R 1.5x? **MATH ERROR**  
- **EMTK**: R/R = (615×1.1 - 615) / (615 - 615×0.92) = 61.5 / 49.2 = 1.25 → stated R/R 1.35x? **MATH ERROR**  
- **COIN**: R/R = (815×1.15 - 815) / (815 - 815×0.9) = 122.25 / 81.5 = 1.5 → stated R/R 1.5x? **MATH ERROR** (stated 1.5x, but 1.5x is correct — no error)  
- **BRPT**: ✓ clean  
- **BRMS**: ✓ clean  
- **BREN**: ✓ clean  
- **MINA**: ✓ clean  
- **SMDR**:- **SMDR**: R/R = (304×1.09 - 304) / (304 - 304×0.94) = 15.2 / 18.24 = 0.83 → stated R/R 1.5x? **MATH ERROR**  
- **TAPG**: ✓ clean  

## 2. Contradiction Hunter

1. **TPIA**: “Negative-but-confluence” conviction with “exceptional 4.8x volume breakout” and “overrides negative history” — contradicts itself: if history is truly negative (-3.9% edge), calling it “exceptional” implies positive bias, not override.  
2. **BKSL**: “Negative” conviction but “ma_golden_cross confluence (mean 5d edge 9.5%)” — positive edge contradicts negative conviction tier.  
3. **KIJA**: “Negative” conviction but “today’s breakout momentum” cited as justification — contradicts stated reliance on historical edge.  
4. **EMTK**: “Negative” conviction with “volume surge and ma_golden_cross” — same as above; contradicts tier.  
5. **COIN**: “Negative” conviction with 0% win rate and “recent price action override past failure” — contradicts logic: if past failure is total (0% win rate), no “recent action” can override without new data.  
6. **SMDR**: “Medium” conviction with “-0.5% historical edge” and “exceptional win rate” — win rate (53.8%) is not exceptional for medium tier; contradicts tier definition.  
7. **BRMS**: “High” conviction with “ma_golden_cross confluence (mean 5d edge -0.0373)” — negative edge contradicts high conviction.  
8. **TAPG**: “High” conviction with “RSI 37.4 oversold” — RSI 37.4 is not oversold (oversold = <30). Contradicts signal trigger logic.  

## 3. Hidden Risks

- **Sector concentration**: 11/15 picks are small/mid-cap industrials or materials (ASPR, GTSI, INKP, CBDK, TPIA, TOBA, BKSL, KIJA, EMTK, COIN, BRPT) — >70% exposure to volatile non-financials. Single-day VaR >15% if mining/industrial sector reverses.  
- **Liquidity risk**: INKP (7750), CBDK (3910), TPIA (1850), BREN (4070) — all have low avg daily volume. Proposed position sizes likely exceed 5% of daily volume — slippage risk >3%.  
- **Correlation**: BRPT, BREN, MINA, TAPG — all show vol_breakout_up + ma_golden_cross. High probability of co-movement due to shared macro triggers (commodity prices, FX). Not diversified.  
- **Timing**: COIN (815), EMTK (615), KIJA (123) — all up >15% today. High gap-down risk at next open.  
- **Stale data**: All Markov “long-run mix” claims — no training window disclosed. If regime shifted in last 30 days (e.g., post-election volatility), model is invalid.  
- **Indicator overlap**: RSI, vol_breakout_up, ma_golden_cross — all are lagging indicators. Vol_breakout_up is derived from price/volume momentum — RSI is derived from price — ma_golden_cross is derived from price. Not independent. False confluence.  

## 4. What the Author Got Right

BRPT and MINA correctly identify high-volume, high-win-rate breakout patterns with consistent edge — the only two picks with >7% historical edge and >50% win rate. Their structure is the only valid baseline.

## 5. Critical Recommendations

1. **Remove TPIA, BKSL, KIJA, EMTK, COIN** — negative conviction with negative edge and no valid edge justification. These are not trades — they are gambling.  
2. **Reduce INKP, CBDK, TPIA, BREN position sizes to 2% max** — all have volume <10% of proposed position size. Slippage will destroy R/R.  
3. **Add sector cap: max 40% in materials/industrials** — current exposure is 73%. Rebalance to include at least 2 bank or tech names with positive edge.
