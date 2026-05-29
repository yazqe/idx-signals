# Hermes Review — Friday, May 29, 2026

## 1. Sanity Check (math + logic)

- PTRO: ✓ clean  
- RAJA: ✓ clean  
- MINA: ✓ clean  
- CUAN: ✓ clean  
- GTSI: ✓ clean  
- CBDK: ✓ clean  
- TPIA: ✓ clean  
- BREN: ✓ clean  
- INDY: ✓ clean  
- CDIA: R/R = (850×1.11 - 850) / (850 - 850×0.93) = 93.5 / 59.5 = 1.57, not 1.4. Math error.  
- MEDC: ✓ clean  
- TOBA: R/R = (432×1.08 - 432) / (432 - 432×0.94) = 34.56 / 25.92 = 1.33, not 1.33? Wait — 1.33 is correct. ✓ clean  
- BKSL: R/R = (75×1.09 - 75) / (75 - 75×0.93) = 6.75 / 5.25 = 1.29, not 1.29? Wait — 1.29 is correct. ✓ clean  
- ANTM: ✓ clean  
- NICL: ✓ clean  

**CDIA: R/R misstated.**  
**All SLs are arbitrary -8%/-7%/-6% — no structural support mentioned.**  
**Conviction inflated:** CUAN (high) has 29 trades, CDIA (low) has 10 — but CDIA’s edge is 0.79% vs CUAN’s 7.00%. Conviction deflated for high-edge picks, inflated for low-edge.  

## 2. Contradiction Hunter

1. “Vol breakout signals dominate the top tier with strong historical edge” — yet CDIA (vol breakout) has 0.79% edge and 30% win rate, yet is labeled “Low” conviction. Contradiction: low edge/low win rate should not be in top tier.  
2. “Negative-tier signals are2. “Negative-tier signals are included only where RSI is deeply oversold and volume supports reversal — TOBA and BKSL are the most compelling.” — Yet ANTM and NICL also have negative edge, deep RSI, and volume context. Contradiction: why are TOBA/BKSL “most compelling” when ANTM/NICL are identical?  
3. “Market is in short-term momentum phase with volume confirming upside” — yet 7 of 14 picks (50%) have negative historical edge. Contradiction: momentum phase should favor positive-edge signals, not half-negative.  
4. “RSI oversold plays are abundant but mostly low-tier” — yet BREN (vol breakout) has 1.23% edge and low conviction, while INDY (RSI) has 1.21% edge and low conviction. Contradiction: why is vol breakout treated as high-tier while RSI with identical edge is low-tier?  

## 3. Hidden Risks

- **Sector concentration:** 11/14 picks (79%) are in mining, metals, or energy (PTRO, RAJA, MINA, CUAN, GTSI, CDIA, BREN, TOBA, BKSL, ANTM, NICL). Single-sector VaR >25% if commodity reverses.  
- **Liquidity risk:** BKSL (75 price) avg daily volume ~1.2M shares. Proposed position size (implied by 7% SL) could be >5% of daily volume — slippage risk.  
- **Correlation:** PTRO, RAJA, MINA, CUAN, CDIA, BREN all in coal/metals. High correlation — diversification illusion.  
- **Timing:** CUAN, BREN, ANTM all surged >15% in past 24h. High chase risk.  
- **Stale data:** “Markov long-run mix” — no training window cited. If regime shifted in last 30 days, model is obsolete.  
- **Indicator overlap:** Vol breakout + RSI oversold — both are momentum indicators. False confluence.  

## 4. What the Author Got Right

BREN’s 6.7x volume surge and 25% move justifies its inclusion despite thin history — this is the only pick where volume magnitude overrides sample size with logical justification.

## 5. Critical Recommendations

1. **Remove CDIA** — R/R math is wrong (1.57 vs 1.4), edge is 0.79%, win rate 30%. No justification for inclusion.  
2. **Reduce sector exposure** — cap metals/mining at 40% of portfolio. Remove 3 picks from PTRO, RAJA, MINA, CUAN, CDIA, BREN.  
3. **Require structural SLs** — SL must be below recent swing low or volume node, not arbitrary %. Add 1-sentence justification per SL.
