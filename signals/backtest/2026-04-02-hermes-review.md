# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **AMMN:**
  - R/R math: (4700 * 1.10 - 4700) / (4700 - 4700 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not tied to a specific support level.
  - TP placement: +10% above close is not tied to a specific resistance level.
  - Tier consistency: Medium conviction with strong historical edge and win rate. ✓ clean

- **ASPR:**
  - R/R math: (264 * 1.15 - 264) / (264 - 264 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not tied to a specific support level.
  - TP placement: +15% above close is not tied to a specific resistance level.
  - Tier consistency: Medium conviction with strong historical edge but lower win rate. ✓ clean

- **CUAN:**
  - R/R math: (1045 * 1.10 - 1045) / (1045 - 1045 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not tied to a specific support level.
  - TP placement: +10% above close is not tied to a specific resistance level.
  - Tier consistency: Low conviction with positive edge and decent win rate. ✓ clean

- **ESIP:**
  - R/R math: (67 * 1.10 - 67) / (67 - 67 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement - SL placement: -5% below close is arbitrary and not tied to a specific support level.
  - TP placement: +10% above close is not tied to a specific resistance level.
  - Tier consistency: Medium conviction with strong historical edge and large number of past trades. ✓ clean

- **TPIA:**
  - R/R math: (4170 * 1.10 - 4170) / (4170 - 4170 * 0.95) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not tied to a specific support level.
  - TP placement: +10% above close is not tied to a specific resistance level.
  - Tier consistency: Low conviction with positive edge and reasonable win rate. ✓ clean

## 2. Contradiction Hunter

1. **ASPR and ESIP:**
   - **Location quote:** "ASPR and ESIP stand out with their strong historical edges, while AMMN and TPIA offer solid RSI oversold signals."
   - **Why contradictory:** Both ASPR and ESIP are given medium conviction despite ASPR having a lower win rate (47.8%) compared to ESIP (52.6%).

2. **CUAN and TPIA:**
   - **Location quote:** "CUAN is included for its recent volume action and positive edge, despite its lower tier. TPIA is included for its positive edge and reasonable win rate, and recent volume action."
   - **Why contradictory:** Both CUAN and TPIA are given low conviction despite similar reasoning (recent volume action and positive edge).

## 3. Hidden Risks

- **Sector concentration:** The analysis does not specify the sectors of the stocks. If multiple stocks belong to the same sector (e.g., mining/coal/metal/bank), there is a risk of single-sector concentration. Single-day VaR if the sector reverses could be significant.
- **Liquidity risk:** The analysis does not mention the average daily volume (ADV) of the stocks. Any tier-1 picks with thin ADV relative to the proposed position size could pose liquidity risks.
- **Correlation:** The analysis does not consider the correlation between the stocks. Stocks that move together (e.g., same conglomerate group, same commodity exposure) could lead to over-concentration disguised as diversification.
- **Timing:** The analysis does not account for stocks that have already moved >15% today. Chasing such stocks increases the risk of a gap-down at the next open.
- **Stale data:** The analysis does not specify the training window for indicators like Markov "long-run mix." If the training window is stale, the signals could be outdated.
- **Indicator overlap:** The analysis uses multiple indicators (SMC, DA8, Markov) without considering whether they are truly independent signals. This could lead to false confluence.

## 4. What the Author Got Right

The author correctly identified the historical edge and win rate for each stock, providing a quantitative basis for the trades. The use of multiple signals (RSI oversold, volume breakout) adds robustness to the analysis.

## 5. Critical Recommendations

1. **Reduce ASPR position from 15% to 5% because the win rate (47.8%) is lower compared to ESIP (52.6%) despite both having medium conviction.**
2. **Specify the sectors of the stocks and calculate the single-sector concentration risk. Ensure that no more than 30% of the portfolio is allocated to a single sector.**
3. **Check the average daily volume (ADV) of each stock and ensure that the proposed position size does not exceed 5% of the ADV to avoid liquidity risks.**
