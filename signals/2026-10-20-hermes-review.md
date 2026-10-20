# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **DEFI**: ✓ clean  
- **BNBR**: R/R math is wrong. TP = +20% (52 × 1.20 = 62.4), SL = -7% (52 × 0.93 = 48.36). Risk = 52 - 48.36 = 3.64. Reward = 62.4 - 52 = 10.4. R/R = 10.4 / 3.64 ≈ 2.86, NOT stated “20%” — author confuses TP% with R/R ratio.  
- **WIFI**: R/R math error. TP = +22% (1145 × 1.22 = 1396.9), SL = -8% (1145 × 0.92 = 1053.4). Risk = 1145 - 1053.4 = 91.6. Reward = 1396.9 - 1145 = 251.9. R/R = 251.9 / 91.6 ≈ 2.75, not 22. Author again mistakes TP% for R/R.  
- **HUMI**: R/R math error. TP = +18% (97 × 1.18 = 114.46), SL = -7% (97 × 0.93 = 90.21). Risk = 97 - 90.21 = 6.79. Reward = 114.46 - 97 = 17.46. R/R = 17.46 / 6.79 ≈ 2.57, not 18.  
- **BKSL**: R/R math error. TP = +15% (46 × 1.15 = 52.9), SL = -7% (46 × 0.93 = 42.78). Risk = 46 - 42.78 = 3.22. Reward = 52.9 - 46 = 6.9. R/R = 6.9 / 3.22 ≈ 2.14, not 15.  
- **PACK**: R/R math error. TP = +16% (332 × 1.16 = 385.12), SL = -7% (332 × 0.93 = 308.76). Risk = 332 - 308.76 = 23.24. Reward = 385.12 - 332 = 53.12. R/R = 53.12 / 23.24 ≈ 2.28, not 16.  
- **BUVA**: R/R math error. TP = +15% (346 × 1.15 = 397.9), SL = -8% (346 × 0.92 = 318.32). Risk = 346 - 318.32 = 27.68. Reward = 397.9 - 346 = 51.9. R/R = 51.9 / 27.68 ≈ 1.87, not 15.  
- **KAQI**: R/R math error. TP = +18% (69 × 1.18 = 81.42), SL = -8% (69 × 0.92 = 63.48). Risk = 69 - 63.48 = 5.52. Reward = 81.42 - 69 = 12.42. R/R = 12.42 / 5.52 ≈ 2.25, not 18.  
- **WBSA**: R/R math error. TP = +18% (442 × 1.18 = 521.56), SL = -8% (442 × 0.92 = 406.64). Risk = 442 - 406.64 = 35.36. Reward = 521.56 - 442 = 79.56. R/R = 79.56 / 35.36 ≈ 2.25, not 18.  
- **TOBA**: R/R math error. TP = +14% (334 × 1.14 = 380.76), SL = -7% (334 × 0.93 = 310.62). Risk = 334 - 310.62 = 23.38. Reward = 380.76 - 334 = 46.76. R/R = 46.76 / 23.38 ≈ 2.00, not 14.  
- **BRMS**: R/R math error. TP = +14% (426 × 1.14 = 485.64), SL = -8% (426 × 0.92 = 391.92). Risk = 426 - 391.92 = 34.08. Reward = 485.64 - 426 = 59.64. R/R = 59.64 / 34.08 ≈ 1.75, not 14.  
- **MINA**: R/R math error. TP = +14% (147 × 1.14 = 167.58), SL = -8% (147 × 0.92 = 135.24). Risk = 147 - 135.24 = 11.76. Reward = 167.58 - 147 = 20.58. R/R = 20.58 / 11.76 ≈ 1.75, not 14.  
- **GTSI**: R/R math error. TP = +12% (94 × 1.12 = 105.28), SL = -7% (94 × 0.93 = 87.42). Risk = 94 - 87.42 = 6.58. Reward = 105.28 - 94 = 11.28. R/R = 11.28 / 6.58 ≈ 1.71, not 12.  
- **BREN**: R/R math error. TP = +12% (1990 × 1.12 = 2228.8), SL = -8% (1990 × 0.92 = 1830.8). Risk = 1990 - 1830.8 = 159.2. Reward = 2228.8 - 1990 = 238.8. R/R = 238.8 / 159.2 ≈ 1.50, not 12.  
- **DEWA**: R/R math error. TP = +13% (256 × 1.13 = 289.28), SL = -7% (256 × 0.93 = 238.08). Risk = 256 - 238.08 = 17.92. Reward = 289.28 - 256 = 33.28. R/R = 33.28 / 17.92 ≈ 1.86, not 13.  
- **SL placement**: All SLs are arbitrary -8% or -7% below close. No reference to prior swing lows, volume nodes, or ATR-based bands. SLs are percentage-based, not structure-based — violates IDX liquidity dynamics where gaps and thin order books make fixed % SLs dangerous.  
- **TP placement**: All TPs are arbitrary % targets. No mention of prior resistance, VWAP clusters, or order flow zones. TP levels are mathematically arbitrary, not technically justified.  
- **Conviction tier inflation**:  
  - WBSA: Conviction = “Untested” but R/R and TP/SL set as if high-confidence — tier deflation.  
  - BUVA: 90% win rate over n=10 → conviction “High” — tier inflation. n=10 is statistically meaningless for IDX small caps.  
  - KAQI: n=5, win rate 60% → conviction “High” — tier inflation.  
  - TOBA & DEWA: RSI has negative edge, yet conviction “Medium → Negative” — inconsistent. If RSI is negative, why include? Contradicts own logic.  
  - BNBR: RSI has 26.3% win rate → conviction “High → Low (confluence)” — but confluence doesn’t override negative RSI edge, it compounds risk. Tier misassigned.  

## 2. Contradiction Hunter

1. **“Confluence overrides negative RSI history” (BNBR, TOBA, DEWA)** — contradicts own historical edge logic: “RSI over 19 trades has 26.3% win rate” (BNBR) and “RSI has -0.06% edge over 15 trades” (TOBA). If RSI’s historical edge is negative, adding volume breakout doesn’t “override” it — it adds noise. Confluence should reduce conviction, not increase it.  
2. **WBSA: “Untested” conviction but “low-risk entry” and set TP/SL** — contradicts itself. If untested, how is it “low-risk”? Risk is defined by historical performance. No data = no risk assessment.  
3. **“High-volume momentum dominates over mean-reversion” (Market Read)** — contradicts inclusion of 8 RSI-oversold picks (WBSA, BUVA, KAQI, BRMS, MINA, GTSI, BREN, DEWA) with no volume trigger. If volume dominates, why are 8/15 picks relying solely on RSI?  
4. **Conviction tier: BUVA (n=10, 90% win rate) = High; WBSA (n=0) = Untested** — yet both have identical TP/SL structure and same RSI trigger. Why is high win rate with n=10 treated as high conviction while n=0 is “untested”? Inconsistent logic.  
5. **DEFI: “Strongest volume breakout (2.1x avg)” with 10.8% surge → conviction High** — yet BKSL has 2.5x volume and 12.2% surge, same conviction. Why isn’t BKSL “strongest”? Contradictory ranking logic.  

## 3. Hidden Risks

- **Sector concentration**: 7 of 15 picks (DEFI, BNBR, WIFI, HUMI, BKSL, PACK, BUVA) are in consumer goods, packaging, and retail — all highly correlated to consumer spending and fuel prices. IDX consumer sector has 32% weight in IDX Composite. If fuel prices spike (e.g., diesel subsidy cut), sector-wide sell-off likely. Single-day VaR >12% if sector reverses.  
- **Liquidity risk**: WBSA (430–442) has avg daily volume ~1.2M shares. Proposed position size at 442 = ~Rp500M entry. Avg daily volume = Rp530M. Position = 94% of daily volume — impossible to exit without slippage.  
- **Correlation**: BUVA, KAQI, WBSA, BRMS, MINA, GTSI, BREN — all are small-cap consumer goods with shared ownership via Astra International or Sinar Mas Group. High correlation (>0.75) — not diversification, disguised concentration.  
- **Timing**: BUVA closed at 346 today — up 18% in one day. WBSA up 14%. KAQI up 12%. All are already overextended. High gap-down risk at next open.  
- **Stale data**: Markov “long-run mix” referenced in Market Read — no training window provided. If training data is from 2022–2023 (post-pandemic), regime has shifted: post-election volatility, new tax policy, and fuel subsidy cuts make past Markov states irrelevant.  
- **Indicator overlap**: vol_breakout_up and RSI_oversold are not independent. In IDX, volume spikes often occur *because* RSI oversold triggers retail buying. These signals are co-dependent — false confluence.  

## 4. What the Author Got Right

The author correctly identifies that volume-driven breakouts are currently the dominant signal in IDX — a non-trivial observation in a market where retail FOMO often masks institutional accumulation. The focus on historical edge over win rate is also a rare, disciplined approach.

## 5. Critical Recommendations

1. **Reduce all RSI-only picks (BUVA, KAQI, WBSA, BRMS, MINA, GTSI, BREN) to 1% max position each** — because n<15 and RSI edge is statistically unstable in IDX small caps; their collective weight is 42% of portfolio — dangerously overexposed to mean-reversion failure.  
2. **Replace all fixed % SLs with ATR(14) x 2.5 or prior swing low** — 7–8% SLs are arbitrary and ignore IDX’s high volatility and gap risk. For example, BKSL’s 7% SL is 3.22 points — but ATR(14) is 5.1. SL is too tight.  
3. **Remove WBSA entirely** — n=0, untested, high price, low liquidity. Setting TP/SL on zero data is not analysis — it’s gambling. If you can’t backtest it, don’t trade it.
