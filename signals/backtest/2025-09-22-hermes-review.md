# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **BUMI:**
  - R/R math: (133.1 - 121.0) / (121.0 - 114.95) = 12.1 / 6.05 ≈ 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **BUVA:**
  - R/R math: (532.4 - 484.0) / (484.0 - 459.8) = 48.4 / 24.2 ≈ 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **DEFI:**
  - R/R math: (503.8 - 458.0) / (458.0 - 435.1) = 45.8 / 22.9 ≈ 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **DEWA:**
  - R/R math: (261.8 - 238.0) / (238.0 - 226.1) = 23.8 / 11.9 ≈ 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

-- **ESIP:**
  - R/R math: (81.89 - 74.66) / (74.66 - 70.927) = 7.23 / 3.733 ≈ 1.94 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is appropriate given the historical edge and volume breakout.

- **CDIA:**
  - R/R math: (1948.06 - 1770.97) / (1770.97 - 1682.4215) = 177.09 / 88.5485 ≈ 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Low conviction is appropriate given the low historical edge and win rate.

- **PANI:**
  - R/R math: (14025.0 - 13350.0) / (13350.0 - 12682.5) = 675.0 / 667.5 ≈ 1.01 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Low conviction is appropriate given the low historical edge and win rate.

## 2. Contradiction Hunter

1. **Contradiction in Conviction and Historical Edge:**
   - **Location:** CDIA and PANI are both rated as "Low" conviction, yet CDIA has a much lower historical edge (0.79% over 10 past trades, win rate 30%) compared to PANI (1.41% over 18 past trades, win rate 55.6%).
   - **Why:** The lower historical edge and win rate of CDIA do not justify a "Low" conviction rating, especially when compared to PANI, which has a higher edge and win rate but the same conviction rating.

2. **Contradiction in Stop Loss Placement:**
   - **Location:** All picks have a stop loss set at -5% below the close, which is arbitrary and not based on any logical structure level.
   - **Why:** This uniform approach to stop loss placement does not account for the unique characteristics of each stock, such as volatility and support levels.

3. **Contradiction in Take Profit Placement:**
   - **Location:** All picks have a take profit set at +10% above the close, which is not justified by any specific resistance levels.
   - **Why:** This uniform approach to take profit placement does not account for the unique characteristics of each stock, such as resistance levels and price targets.

## 3. Hidden Risks

- **Sector Concentration:**
  - **Mining/Coal/Metal:** BUMI, BUVA, DEFI, DEWA, and ESIP are all in the mining/coal/metal sector. This represents a significant concentration of the portfolio in a single sector, increasing the risk if the sector reverses.
  - **Single-day VaR:** If the mining/coal/metal sector reverses, the portfolio could experience a significant single-day loss due to the high concentration.

- **Liquidity Risk:**
  - **CDIA and PANI:** Both stocks have relatively thin average daily volume compared to the proposed position sizes, which could lead to liquidity issues and difficulty in exiting positions.

- **Correlation:**
  - **BUMI, BUVA, DEFI, DEWA, and ESIP:** These stocks are likely to move together due to their exposure to the same sector (mining/coal/metal), which could lead to over-concentration disguised as diversification.

- **Timing:**
  - **CDIA and PANI:** Both stocks have already moved significantly today, increasing the risk of a gap-down at the next open.

- **Stale Data:**
  - **Historical Edge:** The historical edge data is based on past trades, but the training window is not mentioned. If the market regime has shifted recently, the historical edge may be stale and not reflective of current conditions.

- **Indicator Overlap:**
  - **Vol Breakout Up:** All picks are triggered by a "vol_breakout_up" signal, which suggests a lack of diversification in the signals used to generate the picks.

## 4. What the Author Got Right

The author correctly identified strong volume breakouts as a key factor for the selected stocks, which is a valid and often reliable signal for short-term momentum. The historical edge data provides a useful reference for the potential performance of each stock, although the consistency of the data should be further validated.

## 5. Critical Recommendations

1. **Reduce CDIA position from 15% to 5% because of its low historical edge and thin average daily volume.**
2. **Diversify the portfolio by including stocks from different sectors to reduce sector concentration risk.**
3. **Re-evaluate the stop loss and take profit placements to ensure they are based on logical structure levels and resistance levels, rather than arbitrary percentages.**
