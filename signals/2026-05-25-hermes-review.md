# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **BUVA:**
  - R/R math: (790.6 - 705) / (705 - 648.4) = 85.6 / 56.6 ≈ 1.51 (stated R/R is 1.5, so ✓ clean)
  - SL placement: -8% below close is a fixed percentage, not a logical structure level. **Arbitrary SL placement.**
  - TP placement: +12% above close is a fixed percentage, not a resistance level. **Arbitrary TP placement.**
  - Tier consistency: High conviction is justified by a strong historical edge and high win rate. **✓ clean**

- **AMMN:**
  - R/R math: (3268.2 - 2910) / (2910 - 2682.8) = 358.2 / 227.2 ≈ 1.58 (stated R/R is 1.5, so ✓ clean)
  - SL placement: -8% below close is a fixed percentage, not a logical structure level. **Arbitrary SL placement.**
  - TP placement: +12% above close is a fixed percentage, not a resistance level. **Arbitrary TP placement.**
  - Tier consistency: Medium conviction is justified by a decent historical edge and reasonable win rate. **✓ clean**

- **BREN:**
  - R/R math: (2676.8 - 2390) / (2390 - 2204.8) = 286.8 / 185.2 ≈ 1.55 (stated R/R is 1.5, so ✓ clean)
  - SL placement: -8% below close is a fixed percentage, not a logical structure level. **Arbitrary SL placement.**
  - TP placement: +12% above close is a fixed percentage, not a resistance level. **Arbitrary TP placement.**
  - Tier consistency: Medium conviction is justified by a good win rate and solid historical edge. **✓ clean**

## 2. Contradiction Hunter

1. **Contradiction in SL and TP placement:**
   -  - **Location:** All picks (BUVA, AMMN, BREN)
   - **Why:** The stop loss and take profit levels are set as fixed percentages (-8% and +12%) rather than at logical support and resistance levels. This can lead to arbitrary risk management and potentially suboptimal trade outcomes.

2. **Contradiction in conviction ratings:**
   - **Location:** AMMN and BREN
   - **Why:** Both AMMN and BREN have a medium conviction rating despite having different historical edges and win rates. AMMN has a lower historical edge (3.58%) and win rate (60.9%) compared to BREN (3.33% and 66.7%). The conviction ratings should reflect these differences more clearly.

## 3. Hidden Risks

- **Sector concentration:**
  - **Risk:** The analysis does not specify the sectors of the stocks. If BUVA, AMMN, and BREN are in the same sector (e.g., mining/coal/metal/bank), the portfolio could be heavily concentrated in that sector, increasing single-day VaR if the sector reverses.

- **Liquidity risk:**
  - **Risk:** The analysis does not provide average daily volume (ADV) for the stocks. If any of the tier-1 picks (BUVA, AMMN, BREN) have thin ADV relative to the proposed position size, it could lead to liquidity issues and difficulty in entering or exiting positions.

- **Correlation:**
  - **Risk:** The analysis does not consider the correlation between the stocks. If BUVA, AMMN, and BREN are part of the same conglomerate group or have similar commodity exposure, the portfolio may be over-concentrated and not truly diversified.

- **Timing:**
  - **Risk:** The analysis does not mention the intraday movement of the stocks. If any of the stocks have already moved more than 15% today, entering a trade could be risky due to the potential for a gap-down at the next open.

- **Stale data:**
  - **Risk:** The analysis does not specify the training window for the historical edge and win rate calculations. If the training window is stale (e.g., from a different market regime), the historical performance may not be relevant to the current market conditions.

- **Indicator overlap:**
  - **Risk:** The analysis uses multiple indicators (rsi_oversold, historical edge, win rate) that may not be independent. For example, the rsi_oversold signal and the historical edge could be correlated, leading to a false confluence of signals.

## 4. What the Author Got Right

The author correctly identified strong historical performance and high win rates for BUVA, which justifies the high conviction rating. The use of a consistent R/R ratio across all picks helps in maintaining a standardized risk management approach.

## 5. Critical Recommendations

1. **Adjust SL and TP levels:**
   - **Action:** For BUVA, AMMN, and BREN, set stop loss and take profit levels at logical support and resistance levels instead of fixed percentages. This will ensure more accurate risk management and better trade outcomes.

2. **Re-evaluate conviction ratings:**
   - **Action:** Adjust the conviction ratings for AMMN and BREN to reflect their different historical edges and win rates. AMMN should have a lower conviction rating due to its lower historical edge and win rate.

3. **Conduct a sector and correlation analysis:**
   - **Action:** Perform a detailed analysis of the sectors and correlations between BUVA, AMMN, and BREN to ensure the portfolio is not over-concentrated in a single sector or group of correlated stocks. This will help in managing sector-specific and correlation risks.
