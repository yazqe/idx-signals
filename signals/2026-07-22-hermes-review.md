# Hermes Review — 2023-11-28

## 1. Sanity Check (math + logic)

- **BNBR**: ✓ clean
- **GTSI**: ✓ clean
- **PTRO**: ✓ clean
- **COIN**: ✓ clean
- **KOTA**: ✓ clean
- **WMUU**: ✓ clean
- **BREN**: ✓ clean
- **ZATA**: ✓ clean
- **ITMG**: ✓ clean
- **MBMA**: ✓ clean
- **AMMN**: ✓ clean

## 2. Contradiction Hunter

1. **Contradiction in Conviction Rating**:
   - **Location**: "ITMG — BUY (5-20d hold)" and "MBMA — BUY (5-20d hold)" and "AMMN — BUY (5-20d hold)"
   - **Quote**: "Conviction: Negative-but-confluence"
   - **Why**: The author includes these stocks with a negative historical edge and low win rates, yet still labels them as "BUY" with a 5-20d hold. This contradicts the typical risk management principle of avoiding trades with negative historical performance.

## 3. Hidden Risks

- **Sector Concentration**: The analysis does not specify the sectors of the selected stocks. Given the focus on volume breakouts, there is a risk of over-concentration in sectors like mining, coal, or metals, which could lead to significant single-day VaR if the sector reverses.
- **Liquidity Risk**: The analysis does not provide average daily volume (ADV) data for the selected stocks. Stocks like **ITMG** (entry zone: 24375 ± 2%) and **AMMN** (entry zone: 4170 ± 2%) may have thin ADV relative to the proposed position sizes, leading to liquidity issues.
- **Correlation**: The analysis does not address the potential correlation between the selected stocks. For example, if multiple stocks are part of the same conglomerate or have similar commodity exposure, a single market event could affect all of them simultaneously, leading to over-concentration disguised as diversification.
- **Timing**: The analysis does not mention the intraday movement of the stocks. If any of these stocks have already moved more than 15% today, there is a significant chase risk and vulnerability to a gap-down at the next open.
- **Stale Data**: The historical edge and win rates are based on past trades, but the training window for these metrics is not specified. If the market regime has shifted recently, these historical metrics may be stale and not reflective of current conditions.
- **Indicator Overlap**: The analysis relies heavily on the `vol_breakout_up` trigger, which may not be independent from other indicators like the golden cross. This could lead to false confluence and overconfidence in the trades.

## 4. What the Author Got Right

The author correctly identifies the importance of strong volume and price action as key factors for short-term trades. The use of historical edge and win rates provides a quantitative basis for evaluating the potential of each trade, which is a strong approach for risk management.

## 5. Critical Recommendations

1. **Reduce ITMG, MBMA, and AMMN positions**: Given their negative historical edges and low win rates, reduce the position sizes for these stocks to 2% of the portfolio each. This will help manage the risk of including trades with poor historical performance.
2. **Conduct a sector analysis**: Before entering trades, perform a sector analysis to ensure that the portfolio is not over-concentrated in a single sector. If the selected stocks are heavily weighted in a particular sector, consider diversifying into other sectors to reduce single-day VaR.
3. **Check liquidity and intraday movement**: Verify the average daily volume (ADV) for each stock and ensure that the proposed position sizes are within a reasonable range of the ADV. Additionally, check the intraday movement of each stock to avoid entering trades that have already moved significantly today, as this increases the risk of a gap-down at the next open.
