# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **DEFI:**
  - R/R math: (10% - 0%) / (0% - -5%) = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is a standard percentage, not a logical structure level.
  - TP placement: +10% above close is a standard percentage, not a resistance level.
  - Tier consistency: Medium conviction with a positive historical edge and win rate. ✓ clean

- **ESIP:**
  - R/R math: (10% - 0%) / (0% - -5%) = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is a standard percentage, not a logical structure level.
  - TP placement: +10% above close is a standard percentage, not a resistance level.
  - Tier consistency: Medium conviction with a moderate historical edge and win rate. ✓ clean

- **NICL:**
  - R/R math: (10% - 0%) / (0% - -5%) = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is a standard percentage, not a logical structure level.
  - TP placement: +10% above close is a standard percentage, not a resistance level.
  - Tier consistency: Negative-but-confluence conviction with a negative historical edge. This is a contradiction. **Flagged for tier deflation.**

- **PACK:**
  - R/R math: (10% - 0%) / (0% - -5%) = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is a standard percentage, not a logical structure level.
  - TP placement: +10% above close is a standard percentage, not a resistance level.
  - Tier consistency: Medium conviction with a positive historical edge and win rate. ✓ clean

- **SDMU:**
  - R/R math: (10% - 0%) / (0% - -5%) = 2.00 (st - SL placement: -5% below close is a standard percentage, not a logical structure level.
  - TP placement: +10% above close is a standard percentage, not a resistance level.
  - Tier consistency: High conviction with a strong historical edge and win rate. ✓ clean

- **SINI:**
  - R/R math: (10% - 0%) / (0% - -5%) = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close is a standard percentage, not a logical structure level.
  - TP placement: +10% above close is a standard percentage, not a resistance level.
  - Tier consistency: High conviction with an exceptional historical edge and win rate. ✓ clean

## 2. Contradiction Hunter

1. **NICL:**
   - **Location quote:** "Negative-but-confluence conviction with a negative historical edge, but strong volume action could reverse the trend."
   - **Why contradictory:** The analysis states a negative historical edge but still gives a "Negative-but-confluence" conviction, which is inconsistent. A negative historical edge should not justify a medium or higher conviction unless there is strong evidence of a reversal.

## 3. Hidden Risks

- **Sector concentration**: The analysis does not specify the sectors of the stocks. If multiple stocks are in the same sector (e.g., mining, coal, metal, bank), this could lead to significant single-sector concentration risk. For example, if multiple stocks are in the mining sector, a single-day VaR for a sector reversal could be substantial.
- **Liquidity risk**: The analysis does not mention the average daily volume (ADV) of the stocks. Thin ADV relative to the proposed position size can lead to liquidity issues, making it difficult to enter or exit positions without significantly impacting the stock price.
- **Correlation**: The analysis does not consider the correlation between the stocks. Stocks that move together (e.g., same conglomerate group, same commodity exposure) can lead to over-concentration disguised as diversification.
- **Timing**: The analysis does not account for the fact that some stocks may have already moved significantly today. For example, if a stock has already moved >15% today, entering a trade now could expose the portfolio to gap-down vulnerability at the next open.
- **Stale data**: The analysis does not specify the training window for the Markov "long-run mix" indicators. If the training window is stale and the market regime has shifted recently, the indicators could be unreliable.
- **Indicator overlap**: The analysis uses multiple indicators (SMC, DA8, Markov) without considering whether these signals are truly independent. If these indicators are correlated, the confluence of signals may be a false positive.

## 4. What the Author Got Right

The author correctly identified strong volume breakouts and RSI oversold conditions as key triggers for trades. The historical edge and win rate data provide a solid foundation for the analysis, particularly for stocks like SINI and SDMU, which have exceptional performance metrics.

## 5. Critical Recommendations

1. **Reduce NICL position from 15% to 5% because of the negative historical edge and lack of strong evidence for a reversal.**
2. **Conduct a sector analysis to identify and manage single-sector concentration risk. Ensure that no more than 20% of the portfolio is allocated to a single sector.**
3. **Evaluate the liquidity of each stock by checking the average daily volume (ADV) relative to the proposed position size. Avoid entering trades in stocks with thin ADV to prevent liquidity issues.**
