# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **AADI:**
  - R/R math: (8450 * 1.10 - 8450) / (8450 - 8450 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned in the analysis.
  - Tier consistency: Negative-but-confluence with a historical edge of -3.22% and a win rate of 21.4% is a weak basis for a 5⭐ conviction.

- **ESSA:**
  - R/R math: (705 * 1.10 - 705) / (705 - 705 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned in the analysis.
  - Tier consistency: Negative-but-confluence with a historical edge of -4.94% for ma_golden_cross and -1.97% for vol_breakout_up is a weak basis for a 5⭐ conviction.

- **GOTO:**
  - R/R math: (60 * 1.10 - 60) / (60 - 60 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned in the analysis.
  - Tier consistency: Low conviction with a historical edge of 0.62% and a win rate of 36.4% is consistent.

- **KRYA:**
 - R/R math: (124 * 1.10 - 124) / (124 - 124 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned in the analysis.
  - Tier consistency: Negative conviction with a historical edge of -6.47% and a win rate of 33.3% is a weak basis for a 5⭐ conviction.

- **SMDR:**
  - R/R math: (386 * 1.10 - 386) / (386 - 386 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned in the analysis.
  - Tier consistency: Low conviction with a historical edge of 0.63% and a win rate of 40.0% is consistent.

## 2. Contradiction Hunter

1. **ESSA:**
   - "Negative-but-confluence" conviction with a historical edge of -4.94% for ma_golden_cross and -1.97% for vol_breakout_up is contradictory. The analysis states a strong volume action and golden cross, but the historical performance is poor.
   - **Location quote:** "Dual confluence with strong volume action and golden cross."
   - **Why contradictory:** The historical performance for both signals is negative, which contradicts the strong conviction.

2. **KRYA:**
   - "Negative" conviction with a historical edge of -6.47% and a win rate of 33.3% is contradictory. The analysis states a moderate win rate and recent volume action, but the historical performance is negative.
   - **Location quote:** "RSI oversold with a moderate win rate and recent volume action."
   - **Why contradictory:** The historical performance is negative, which contradicts the moderate win rate and recent volume action.

3. **GOTO:**
   - "Low" conviction with a historical edge of 0.62% and a win rate of 36.4% is contradictory. The analysis states a positive historical edge and recent volume action, but the conviction is low.
   - **Location quote:** "RSI oversold with a positive historical edge and recent volume action."
   - **Why contradictory:** The positive historical edge and recent volume action suggest a higher conviction.

## 3. Hidden Risks

- **Sector concentration:** The analysis does not specify the sectors of the stocks. If multiple stocks are in the same sector (e.g., mining/coal/metal/bank), it could lead to significant single-sector concentration risk. For example, if 50% of the portfolio is in the mining sector, a single-day VaR could be substantial if the sector reverses.
- **Liquidity risk:** The analysis does not mention the average daily volume (ADV) of the stocks relative to the proposed position size. For instance, if a tier-1 pick has thin ADV, it could lead to liquidity issues and slippage.
- **Correlation:** The analysis does not consider the correlation between the stocks. If multiple stocks are part of the same conglomerate group or have the same commodity exposure, it could lead to over-concentration disguised as diversification.
- **Timing:** The analysis does not account for the fact that some stocks have already moved >15% today. For example, if a stock has already gained 15% today, it increases the chase risk and the vulnerability to a gap-down at the next open.
- **Stale data:** The analysis does not specify the training window for the Markov "long-run mix" indicators. If the training window is stale and the regime has shifted recently, the indicators could be unreliable.
- **Indicator overlap:** The analysis uses multiple indicators (SMC + DA8 + Markov) without considering whether they are truly independent signals. This could lead to false confluence and overconfidence in the signals.

## 4. What the Author Got Right

The author correctly identified the strong volume breakout in AADI and the dual confluence in ESSA. These are valid technical signals that can indicate potential buying interest, especially when combined with recent volume action.

## 5. Critical Recommendations

1. **Reduce ESSA position from 15% to 5% because the historical performance for both ma_golden_cross and vol_breakout_up is negative, and the conviction is weak.**
2. **Re-evaluate the stop loss and take profit levels for all picks to ensure they are based on logical structure levels and resistance levels, not arbitrary percentages.**
3. **Conduct a sector concentration analysis to identify and mitigate single-sector concentration risk, especially if multiple stocks are in the same sector.**
