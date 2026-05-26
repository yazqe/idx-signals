# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **ADMR:**
  - R/R math: (1166.88 - 1060.80) / (1060.80 - 1007.76) = 106.08 / 53.04 = 2.00 (stated R/R is 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **DEWA:**
  - R/R math: (367.40 - 334.00) / (334.00 - 317.30) = 33.40 / 16.70 = 2.00 (stated R/R is 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **GTSI:**
  - R/R math: (121.00 - 110.00) / (110.00 - 104.50) = 11.00 / 5.50 = 2.00 (stated R/R is 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **RAJA:**
  - R/R math: (3574.32 - 3249.38) / (3249.38 - 3086.91) = 324.94 / 162.47 =2.00 (stated R/R is 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

## 2. Contradiction Hunter

1. **Contradiction in Conviction Rating:**
   - **Location:** All picks have a "Medium" conviction rating.
   - **Why:** The historical edge and volume breakout vary significantly between the stocks, yet all are rated "Medium." This suggests a lack of differentiation in the conviction rating.

2. **Contradiction in Historical Edge:**
   - **Location:** ADMR has a historical edge of 2.23% with a win rate of 50%, while GTSI has a historical edge of 9.77% with a win rate of 48.6%.
   - **Why:** Despite GTSI having a much higher historical edge, both stocks are given the same "Medium" conviction rating, which is contradictory.

3. **Contradiction in Volume Breakout:**
   - **Location:** All picks are triggered by a "vol_breakout_up" signal.
   - **Why:** The analysis does not provide a detailed explanation of the volume breakout for each stock, making it difficult to justify the uniform "vol_breakout_up" trigger across all picks.

## 3. Hidden Risks

- **Sector Concentration:**
  - The analysis does not specify the sectors of the selected stocks. If multiple stocks belong to the same sector (e.g., mining, coal, metal, bank), the portfolio could be heavily concentrated in that sector, increasing single-day VaR if the sector reverses.

- **Liquidity Risk:**
  - The analysis does not mention the average daily volume (ADV) of the selected stocks. Thin ADV relative to the proposed position size could lead to liquidity issues, making it difficult to enter or exit positions without significantly impacting the stock price.

- **Correlation:**
  - The analysis does not address the potential correlation between the selected stocks. If the stocks move together (e.g., due to the same conglomerate group or commodity exposure), the portfolio may be over-concentrated, disguised as diversification.

- **Timing:**
  - The analysis does not specify the intraday movement of the selected stocks. If any of the stocks have already moved more than 15% today, entering a trade could be risky due to the potential for a gap-down at the next open.

- **Stale Data:**
  - The analysis does not mention the training window for any indicators that rely on Markov "long-run mix." If the training window is stale and the market regime has shifted recently, the indicators may be less reliable.

- **Indicator Overlap:**
  - The analysis does not clarify whether the signals (SMC, DA8, Markov) are truly independent. If these indicators are correlated, the confluence of signals may be less significant than it appears.

## 4. What the Author Got Right

The author correctly identified strong volume breakouts as a key trigger for the trades, which is a valid and often reliable signal in short-term trading. The historical edge provided for each stock adds a quantitative dimension to the analysis, helping to justify the trades.

## 5. Critical Recommendations

1. **Differentiate Conviction Ratings:**
   - Adjust the conviction ratings to reflect the varying historical edges and volume breakouts. For example, GTSI, with a much higher historical edge, should have a higher conviction rating than ADMR.

2. **Specify Sector and Liquidity:**
   - Clearly state the sectors of the selected stocks and their average daily volumes. Ensure that the proposed position sizes are appropriate for the liquidity of each stock to avoid liquidity risks.

3. **Address Correlation and Timing:**
   - Evaluate the potential correlation between the selected stocks and the intraday movement of each stock. Avoid entering trades in stocks that have already moved significantly today to reduce the risk of a gap-down at the next open.
