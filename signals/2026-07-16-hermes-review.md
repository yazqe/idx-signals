# Hermes Review — 2023-11-14

## 1. Sanity Check (math + logic)

- **SDMU**: 
  - R/R math: (90.2 - 82) / (82 - 77.9) = 8.2 / 4.1 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned.
  - Tier consistency: High conviction for a 40% win rate is questionable. Flagged for tier inflation.

- **WIFI**: 
  - R/R math: (2334.5 - 2030) / (2030 - 1928.5) = 304.5 / 101.5 = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any resistance level mentioned.
  - Tier consistency: High conviction for a 50% win rate is reasonable, but the historical edge is relatively low. Flagged for potential tier inflation.

- **INET**: 
  - R/R math: (244.2 - 222) / (222 - 210.9) = 22.2 / 11.1 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned.
  - Tier consistency: High conviction for a 48.7% win rate is reasonable, but the historical edge is relatively low. Flagged for potential tier inflation.

- **RAJA**: 
  - R/R math: (952.3 - 890) / (890 - 845.5) = 62.3 / 44.5 = 1.40 (stated R/R: 1.40) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +7% above close is not justified by any resistance level mentioned.
  - Tier consistency: Medium conviction for a 64.3% win rate is reasonable, but the historical edge is relatively low. Flagged for potential tier inflation.

- **KIJA**: 
  - R/R math: (151.87 - 141) / (141 - 133.95) = 10.87 / 7.05 = 1.54 (stated R/R: 1.50) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +7% above close is not justified by any resistance level mentioned.
  - Tier consistency: Medium conviction for a 36.4% win rate is questionable. Flagged for tier inflation.

- **INDY**: 
  - R/R math: (2750 - 2500) / (2500 - 2375) = 250 / 125 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level mentioned.
  - Tier consistency: Medium conviction for a 43.8% win rate is reasonable, but the historical edge is relatively low. Flagged for potential tier inflation.

- **HRTA**: 
  - R/R math: (2118.2 - 1960) / (1960 - 1862) = 158.2 / 98 = 1.61 (stated R/R: 1.60) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +7% above close is not justified by any resistance level mentioned.
  - Tier consistency: Low conviction for a 48.1% win rate is reasonable, but the historical edge is relatively low. Flagged for potential tier inflation.

- **RATU**: 
  - R/R math: (5457 - 5100) / (5100 - 4845) = 357 / 255 = 1.40 (stated R/R: 1.40) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +7% above close is not justified by any resistance level mentioned.
  - Tier consistency: Negative-but-confluence conviction for a 33.3% win rate and negative historical edge is highly questionable. Flagged for tier inflation.

## 2. Contradiction Hunter

1. **Contradiction in RATU**:
   - **Location quote:** "Golden cross with a negative edge, but included due to the potential for a reversal."
   - **Why contradictory:** A golden cross with a negative historical edge and a low win rate (33.3%) is a weak signal. Including it due to "potential for a reversal" without additional supporting evidence is contradictory to the high conviction given to other picks with better metrics.

2. **Contradiction in KIJA**:
   - **Location quote:** "Volume breakout with a positive edge, despite a lower win rate."
   - **Why contradictory:** The analysis states a "positive edge" but the win rate (36.4%) is significantly lower than other picks, which are given the same or higher conviction. This inconsistency in conviction rating is contradictory.

3. **Contradiction in SDMU**:
   - **Location quote:** "Golden cross with a strong historical edge, despite a low win rate."
   - **Why contradictory:** The analysis states a "strong historical edge" but the win rate (40%) is low. This is contradictory to the high conviction given to this pick, as a high conviction should be supported by both a strong edge and a higher win rate.

## 3. Hidden Risks

- **Sector concentration**: The analysis does not specify the sectors of the stocks. If multiple picks are from the same sector (e.g., technology or finance), this could lead to significant sector concentration risk. For example, if SDMU, WIFI, and INET are all tech stocks, a single sector event could impact the entire portfolio.

- **Liquidity risk**: RAJA and HRTA have relatively low average daily volumes. If the proposed position sizes are large relative to the daily volume, this could lead to liquidity issues, making it difficult to enter or exit positions without significantly impacting the stock price.

- **Correlation**: Stocks like WIFI, INET, and INDY are all triggered by a volume breakout. If these stocks are part of the same industry or have similar market exposure, they may move together, leading to over-concentration disguised as diversification.

- **Timing**: WIFI and INET have already moved significantly today. Chasing these stocks after a large move increases the risk of a gap-down at the next open, especially if the volume breakout was driven by short-term momentum.

- **Stale data**: The historical edge and win rates are based on past trades, but the training window for these metrics is not mentioned. If the market regime has shifted recently, these historical metrics may no longer be relevant.

- **Indicator overlap**: The use of multiple indicators (e.g., volume breakout, RSI, golden cross) may not be truly independent. For example, a volume breakout and a golden cross often occur together, leading to false confluence and overconfidence in the signal.

## 4. What the Author Got Right

The author correctly identified the importance of historical edge and win rate in evaluating the strength of a trading signal. The use of multiple indicators (e.g., volume breakout, RSI, golden cross) to confirm signals is a good practice, as it helps filter out false positives.

## 5. Critical Recommendations

1. **Reduce RATU position from 15% to 5% because** the golden cross with a negative historical edge and low win rate is a weak signal. The high conviction given to this pick is not justified by the metrics.

2. **Re-evaluate the conviction ratings for KIJA and SDMU** due to their low win rates. The high conviction given to these picks is not supported by the underlying evidence. Consider lowering the conviction to reflect the weaker metrics.

3. **Diversify the portfolio across sectors** to reduce sector concentration risk. Ensure that no more than 20% of the portfolio is allocated to a single sector to mitigate the impact of sector-specific events.
