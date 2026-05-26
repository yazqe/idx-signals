# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **BIPI:**
  - R/R math: (274.0 + 10% * 274.0 - 274.0) / (274.0 - 274.0 * 5%) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by strong historical edge and win rate.

- **BIPP:**
  - R/R math: (93.0 + 10% * 93.0 - 93.0) / (93.0 - 93.0 * 5%) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by solid historical edge and moderate win rate.

- **RODA:**
  - R/R math: (77.0 + 10% * 77.0 - 77.0) / (77.0 - 77.0 * 5%) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by strong historical edge and good win rate.

- **TAPG:**
  - R/R math: (1510.0 + 10% * 1510.0 - 1510.0) / (1510.0 - 1510.0 * 5%) - R/R math: (1510.0 + 10% * 1510.0 - 1510.0) / (1510.0 - 1510.0 * 5%) = 10% / 5% = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by high win rate and positive historical edge.

## 2. Contradiction Hunter

1. **Contradiction in Conviction Rating:**
   - **Location:** "BIPI and TAPG stand out with strong historical performance, while BIPP and RODA offer solid medium-tier opportunities."
   - **Why:** BIPI is rated as "High" conviction, while TAPG is rated as "Medium" conviction despite having a higher win rate (69.6% vs 57.6%).

2. **Contradiction in Historical Edge:**
   - **Location:** "BIPI and TAPG stand out with strong historical performance, while BIPP and RODA offer solid medium-tier opportunities."
   - **Why:** BIPI has a higher historical edge (7.04%) compared to TAPG (3.36%), yet TAPG is given a higher win rate and is still rated as "Medium" conviction.

3. **Contradiction in Entry Zone and Stop Loss:**
   - **Location:** "Stop loss: -5% below close" for all picks.
   - **Why:** The stop loss is set at a fixed percentage below the close, which is arbitrary and not based on any logical structure level. This could lead to premature exits if the market volatility is high.

## 3. Hidden Risks

- **Sector Concentration:**
  - The analysis does not specify the sectors of the stocks. If multiple stocks are from the same sector (e.g., mining, coal, metal, bank), this could lead to significant single-sector exposure and increase the portfolio's vulnerability to sector-specific risks.
  - **Single-day VaR:** If a significant portion of the portfolio is concentrated in a single sector, a single-day reversal in that sector could result in substantial losses.

- **Liquidity Risk:**
  - **BIPI:** Average daily volume is not provided. If the volume is thin relative to the proposed position size, it could lead to difficulty in entering or exiting the position without significantly impacting the stock price.
  - **TAPG:** Given the higher entry price, the liquidity risk is higher if the average daily volume is low.

- **Correlation:**
  - **BIPI and BIPP:** Both stocks are triggered by the same signal (vol_breakout_up). If they are part of the same conglomerate or have similar commodity exposure, they may move together, leading to over-concentration disguised as diversification.

- **Timing:**
  - **BIPI, BIPP, RODA, TAPG:** All stocks are triggered by the same signal (vol_breakout_up) on the same day. If the market has already moved significantly today, there is a risk of chasing the market, which could lead to a gap-down vulnerability at the next open.

- **Stale Data:**
  - The analysis does not mention the training window for the historical edge and win rate. If the training window is stale and the market regime has shifted, the historical performance may not be relevant.

- **Indicator Overlap:**
  - The analysis relies on the same signal (vol_breakout_up) for all picks. This could lead to false confluence if the signals are not truly independent.

## 4. What the Author Got Right

- The author correctly identified the strong historical edge and win rate for BIPI and TAPG, which are key factors in high-conviction trades. The use of a consistent and well-defined entry and stop loss strategy is also a positive aspect of the analysis.

## 5. Critical Recommendations

1. **Reduce BIPI position from 15% to 5% because the stop loss is arbitrary and not based on a logical structure level, increasing the risk of premature exits.**
2. **Re-evaluate the conviction ratings for TAPG and BIPI to ensure consistency with their historical performance and win rates.**
3. **Conduct a sector analysis to identify and manage single-sector concentration risks, and ensure that the portfolio is not over-concentrated in any one sector.**
