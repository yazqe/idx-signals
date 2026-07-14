# Hermes Review — 2023-11-28

## 1. Sanity Check (math + logic)

- **WIFI**: 
  - R/R math: (1790 * 1.15 - 1790) / (1790 - 1790 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by the strong historical edge and volume breakout.

- **BIPI**: 
  - R/R math: (143 * 1.15 - 143) / (143 - 143 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by the strong historical edge and volume breakout.

- **VKTR**: 
  - R/R math: (725 * 1.15 - 725) / (725 - 725 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by the strong historical edge and volume breakout.

- **INET**: 
  - R/R math: (212 * 1.15 - 212) / (212 - 212 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by the positive edge and large number of historical occurrences.

- **TOBA**: 
  - R/R math: (454 * 1.15 - 454) / (454 - 454 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by the positive edge and balanced win rate.

- **ENRG**: 
  - R/R math: (1440 * 1.15 - 1440) / (1440 - 1440 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by the positive edge and recent large price increase.

- **INDY**: 
  - R/R math: (2230 * 1.15 - 2230) / (2230 - 2230 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by the positive edge and recent significant price increase.

- **BULL**: 
  - R/R math: (368 * 1.15 - 368) / (368 - 368 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Low conviction is justified by the lower historical edge and recent significant price increase.

- **MEDC**: 
  - R/R math: (1235 * 1.15 - 1235) / (1235 - 1235 * 0.95) = 15% / 5% = 3.00 (stated R/R: 3.00) ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Negative-but-confluence conviction is justified by the recent significant price increase, despite the negative historical edge.

## 2. Contradiction Hunter

1. **Contradiction in MEDC conviction**:
   - Location quote: "Negative-but-confluence conviction" with a negative historical edge.
   - Why contradictory: A negative historical edge should generally lower conviction, yet the author maintains a "confluence" conviction without clear justification.

## 3. Hidden Risks

- **Sector concentration**: The analysis does not specify the sectors of these stocks. If multiple stocks are in the same sector (e.g., technology or energy), this could lead to significant sector concentration risk. For example, if 50% of the portfolio is in the technology sector and a major tech event occurs, the portfolio could suffer substantial losses.
- **Liquidity risk**: The analysis does not provide average daily volume (ADV) for each stock. If any of these stocks have thin ADV relative to the proposed position size, it could lead to difficulty in exiting positions without significant price impact.
- **Correlation**: The analysis does not consider the correlation between the selected stocks. If multiple stocks are part of the same conglomerate or have similar commodity exposure, they may move together, leading to over-concentration disguised as diversification.
- **Timing**: The analysis does not account for the fact that some of these stocks may have already moved significantly today. For example, if a stock has already gained 15% today, entering a trade at this level increases the risk of a gap-down at the next open.
- **Stale data**: The historical edge is based on past trades, but the training window for these indicators is not mentioned. If the market regime has shifted recently, the historical edge may no longer be relevant.
- **Indicator overlap**: The analysis relies on the "vol_breakout_up" trigger for all picks. While this can be a strong signal, using the same indicator for all picks may lead to false confluence, where the signals are not truly independent.

## 4. What the Author Got Right

The author correctly identified a strong volume breakout as a key trigger for all picks, which is a valid and often reliable signal for short-term momentum trades. The historical edge and win rate are provided for each stock, which adds a quantitative dimension to the analysis.

## 5. Critical Recommendations

1. **Reduce MEDC position from 5% to 1% because** it has a negative historical edge and the "confluence" conviction is not well-justified. A smaller position size will help mitigate the risk of a potential reversal.
2. **Conduct a sector analysis to identify and manage sector concentration risk**. Ensure that no more than 20% of the portfolio is allocated to a single sector to avoid over-concentration.
3. **Verify the liquidity of each stock** by checking the average daily volume (ADV) relative to the proposed position size. If any stock has thin ADV, consider reducing the position size to avoid price impact during exits.
