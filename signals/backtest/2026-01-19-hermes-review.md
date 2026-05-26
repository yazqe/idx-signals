# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **ASHA**: ✓ clean
- **ASPR**: ✓ clean
- **CUAN**: ✓ clean
- **INET**: ✓ clean
- **PACK**: ✓ clean
- **TOBA**: ✓ clean
- **ZATA**: ✓ clean
- **PANI**: ✓ clean

## 2. Contradiction Hunter

1. **PANI: Negative historical edge but high confluence**:
   - **Location quote**: "Negative historical edge but exceptional confluence with multiple strategies."
   - **Why contradictory**: The analysis states a negative historical edge (-0.73%) but still includes PANI with high conviction due to confluence. This is contradictory because a negative edge should generally be a strong reason to avoid a trade, regardless of confluence.

## 3. Hidden Risks

- **Sector concentration**: The analysis does not specify the sectors of the selected stocks. However, if multiple stocks are from the same sector (e.g., banking, mining), the portfolio could be highly concentrated in that sector, increasing single-day VaR if the sector reverses.
- **Liquidity risk**: The analysis does not mention the average daily volume (ADV) of the selected stocks. Thin ADV relative to proposed position size can lead to slippage and difficulty in exiting positions.
- **Correlation**: The analysis does not consider the correlation between the selected stocks. Stocks from the same conglomerate group or with similar commodity exposure can move together, leading to over-concentration disguised as diversification.
- **Timing**: The analysis does not account for the intraday movement of the stocks. If a stock has already moved >15% today, entering a trade could expose the portfolio to gap-down vulnerability at the next open.
- **Stale data**: The analysis does not specify the training window for the historical edge calculations. If the training window is stale (e.g., from a different market regime), the historical edge may not be relevant.
- **Indicator overlap**: The analysis uses multiple indicators (vol_breakout_up, confluence with other strategies) but does not specify if these indicators are truly independent. If they are correlated, the confluence may be a false positive.

## 4. What the Author Got Right

The author correctly identifies the strong volume breakout signals across multiple tickers and provides a clear rationale for each pick based on historical performance and confluence with otherstrategies. The use of historical edge and win rate to justify the conviction levels is a strong approach to risk management.

## 5. Critical Recommendations

1. **Reduce PANI position from 15% to 5% because of the negative historical edge**:
   - Despite the confluence, a negative historical edge (-0.73%) is a significant red flag. Reducing the position size can mitigate the risk of a potential loss.

2. **Conduct a sector analysis to ensure diversification**:
   - Verify the sectors of the selected stocks and ensure that the portfolio is not overly concentrated in any single sector. This will help manage single-day VaR and reduce sector-specific risks.

3. **Evaluate liquidity and intraday movement before entering trades**:
   - Check the average daily volume (ADV) of each stock and the intraday movement. Avoid entering trades in stocks with thin ADV or those that have already moved significantly today to reduce slippage and gap-down risk.

---
