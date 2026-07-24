# Hermes Review — 2023-10-04

## 1. Sanity Check (math + logic)

- **ESIP:**
  - R/R math: (144 * 1.10 - 144) / (144 - 144 * 0.95) = 10.8 / 7.2 ≈ 1.5. Stated R/R is 2.0. **Incorrect**.
  - SL placement: -5% below close is arbitrary and not based on a logical structure level. **Arbitrary**.
  - TP placement: +10% above close is not justified by any resistance level mentioned. **Unjustified**.
  - Tier consistency: High conviction for a single volume breakout with a 45.8% win rate. **Inflated**.

- **TAPG:**
  - R/R math: (1720 * 1.07 - 1720) / (1720 - 1720 * 0.95) = 120.4 / 86 ≈ 1.4. Stated R/R is 1.4. **✓ clean**.
  - SL placement: -5% below close is arbitrary and not based on a logical structure level. **Arbitrary**.
  - TP placement: +7% above close is not justified by any resistance level mentioned. **Unjustified**.
  - Tier consistency: Low conviction for a golden cross with a 100% win rate over 2 trades. **Deflated**.

- **DEWA:**
  - R/R math: (466 * 1.05 - 466) / (466 - 466 * 0.95) = 23.3 / 23.3 ≈ 1.0. Stated R/R is 1.0. **✓ clean**.
  - SL placement: -5% below close is arbitrary and not based on a logical structure level. **Arbitrary**.
  - TP placement: +5% above close is not justified by any resistance level mentioned. **Unjustified**.
  - Tier consistency: Low conviction for a golden cross with a 50% win rate over 4 trades. **Deflated**.

## 2. Contradiction Hunter

1. **Contradiction in Conviction Rating:**
   - **Location:** "ESIP stands out with a significant volume surge and price gain, while TAPG and DEWA offer promising technical setups despite lower conviction levels."
   - **Why:** ESIP has a high conviction rating despite a 45.8% win rate, while TAPG and DEWA have low conviction ratings despite higher win rates (100% and 50%, respectively).

2. **Contradiction in Historical Edge:**
   - **Location:** "TAPG — BUY (5-20d hold) ... **Historical edge:** 4.72% over 2 past trades (win rate 100%)"
   - **Why:** A 100% win rate over 2 trades is statistically insignificant and should not be used to justify a high historical edge.

3. **Contradiction in TP/SL Placement:**
   - **Location:** "ESIP — BUY (5-20d hold) ... **Stop loss:** -5% below close ... **Take profit:** +10% above close"
   - **Why:** The stop loss and take profit levels are arbitrary percentages and not based on any technical analysis or resistance levels.

## 3. Hidden Risks

- **Sector concentration:** The analysis does not specify the sectors of these stocks. If they are in the same sector (e.g., mining/coal/metal/bank), a single-sector event could significantly impact the portfolio.
- **Liquidity risk:** ESIP, TAPG, and DEWA are not evaluated for average daily volume relative to the proposed position size. Thin liquidity can lead to slippage and difficulty in exiting positions.
- **Correlation:** The analysis does not consider whether these stocks move together due to shared industry exposure or other factors, which could lead to over-concentration disguised as diversification.
- **Timing:** ESIP has already moved +10.77% today, which increases the risk of a gap-down at the next open if the momentum wanes.
- **Stale data:** The historical edge and win rates are based on past trades, but the training window is not mentioned. If the market regime has shifted, these indicators could be stale.
- **Indicator overlap:** The use of multiple indicators (vol_breakout_up, ma_golden_cross) may not be independent signals and could lead to false confluence.

## 4. What the Author Got Right

The author correctly identified ESIP's significant volume breakout and price gain, which are strong technical signals. The use of historical win rates, although limited in some cases, provides a basis for evaluating the potential success of the trades.

## 5. Critical Recommendations

1. **Re-evaluate ESIP's conviction rating:** Reduce the conviction from High to Medium due to the 45.8% win rate and the arbitrary TP/SL placement.
2. **Adjust TAPG's position size:** Given the limited historical data (2 trades), reduce the position size to reflect the higher uncertainty.
3. **Reassess TP/SL levels:** Use technical analysis to set stop loss and take profit levels based on support and resistance levels, rather than arbitrary percentages.
