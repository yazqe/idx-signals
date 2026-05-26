# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **ADMR:**
  - R/R math: (1477.3 - 1343) / (1343 - 1275.85) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: High conviction with strong evidence — **✓ clean**

- **SINI:**
  - R/R math: (5280 - 4800) / (4800 - 4560) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: High conviction with strong evidence — **✓ clean**

- **RAJA:**
  - R/R math: (5494.5 - 5232.9) / (5232.9 - 4971.255) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Medium conviction with strong evidence — **✓ clean**

- **ARCI:**
  - R/R math: (1159.84 - 1104.4) / (1104.4 - 1049.18) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Medium conviction with strong evidence — **✓ clean**

-- **CBDK:**
  - R/R math: (8227.5 - 7550) / (7550 - 7172.5) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Medium conviction with positive evidence — **✓ clean**

- **INDY:**
  - R/R math: (2562 - 2440) / (2440 - 2318) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Medium conviction with positive evidence — **✓ clean**

- **RATU:**
  - R/R math: (9356.34 - 8915.09) / (8915.09 - 8469.3355) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Medium conviction with positive evidence — **✓ clean**

- **ELSA:**
  - R/R math: (555.5 - 505) / (505 - 479.75) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Medium conviction with positive evidence — **✓ clean**

- **AADI:**
  - R/R math: (8194.15 - 7813.05) / (7813.05 - 7422.3975) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close (arbitrary %) — **Arbitrary**
  - TP placement: +10% above close (arbitrary %) — **Arbitrary**
  - Tier consistency: Negative historical edge, but included due to strong volume breakout — **✓ clean**

## 2. Contradiction Hunter

1. **Contradiction in AADI:**
   - **Location:** "Negative historical edge, but included due to strong volume breakout and potential for a reversal."
   - **Why:** The analysis states a negative historical edge (-3.22% over 14 past trades with a win rate of 21.4%) but still includes AADI with a "Negative-but-confluence" conviction. This is contradictory because a negative historical edge should generally be a strong reason to avoid the stock, unless there is a very strong fundamental or technical reason to believe the trend will reverse.

## 3. Hidden Risks

- **Sector concentration:**
  - The analysis does not specify the sectors of the stocks. However, if multiple stocks are from the same sector (e.g., mining, coal, metal, bank), it could lead to significant sector concentration risk. For example, if 50% of the portfolio is in mining stocks, a single-day VaR (Value at Risk) for a sector reversal could be substantial.

- **Liquidity risk:**
  - Some of the stocks, particularly mid-cap and small-cap stocks like AADI and ELSA, may have thin average daily volume relative to the proposed position size. This could lead to difficulty in entering or exiting positions without significantly impacting the stock price.

- **Correlation:**
  - The analysis does not account for the correlation between the stocks. If multiple stocks are part of the same conglomerate group or have similar commodity exposure, the portfolio may be over-concentrated in certain risks, disguised as diversification.

- **Timing:**
  - The analysis does not mention whether any of the stocks have already moved significantly today. If a stock has already moved >15% today, it increases the chase risk and the vulnerability to a gap-down at the next open.

- **Stale data:**
  - The analysis does not specify the training window for any indicators that rely on Markov "long-run mix." If the training window is not recent, the data could be stale, especially if the market regime has shifted recently.

- **Indicator overlap:**
  - The analysis uses multiple indicators (SMC, DA8, Markov) that may not be truly independent. This could lead to false confluence, where the signals are correlated and do not provide the expected diversification.

## 4. What the Author Got Right

The author correctly identified strong volume breakouts and multiple strategy confluences, particularly in mid-cap and small-cap stocks. The focus on stocks with strong historical performance and significant volume action is a solid approach for identifying potential opportunities.

## 5. Critical Recommendations

1. **Reduce AADI position from 15% to 5%:**
   - **Reason:** AADI has a negative historical edge (-3.22% over 14 past trades with a win rate of 21.4%). Despite the strong volume breakout, the negative edge suggests a higher risk of loss. Reducing the position size will mitigate this risk.

2. **Diversify across sectors:**
   - **Reason:** Ensure that the portfolio is not overly concentrated in a single sector. If multiple stocks are from the same sector, consider reducing the position sizes or adding stocks from other sectors to balance the portfolio.

3. **Monitor liquidity and correlation:**
   - **Reason:** For mid-cap and small-cap stocks, monitor average daily volume and ensure that the proposed position sizes are manageable. Additionally, check for correlation between the stocks to avoid over-concentration in similar risks.
