# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **BIPI**: ✓ clean
- **NICL**: ✓ clean
- **PACK**: ✓ clean
- **RAJA**: ✓ clean
- **RODA**: 
  - **SL placement**: -110% below close is not a logical structure level and seems arbitrary.
  - **R/R math**: (7400.81 * 1.15 - 7400.81) / (7400.81 - 7400.81 * 0.89) = 15% / 110% = 0.136, not 1.5 as stated.
- **TOBA**: ✓ clean
- **ADMR**: ✓ clean
- **INKP**: ✓ clean
- **KIJA**: ✓ clean
- **MDKA**: ✓ clean
- **GJTL**: 
  - **Conviction rating**: "Negative-but-confluence" is a contradiction in terms. If the historical edge is negative, the conviction should not be high.
  - **R/R math**: (1115.0 * 1.15 - 1115.0) / (1115.0 - 1115.0 * 0.90) = 15% / 10% = 1.5, but the historical edge is negative, making the R/R less favorable.

## 2. Contradiction Hunter

1. **GJTL**:
   - **Location quote**: "GJTL — BUY (5-20d hold) - **Triggered:** ma_golden_cross, vol_breakout_up - **Conviction:** Negative-but-confluence - **Historical edge:** -0.97% over 16 past trades (win rate 31.2%)"
   - **Why contradictory**: The conviction rating "Negative-but-confluence" is a contradiction. If the historical edge is negative, the conviction should not be high.

## 3. Hidden Risks

- **Sector concentration**: 
  - **Mining/Coal/Metal**: No specific sector concentration mentioned, but if multiple stocks are in the same sector, it could lead to single-day VaR issues if the sector reverses.
  - **Bank**: No- **Liquidity risk**: 
  - **RODA**: With a stop loss of -110% below close, the position size should be carefully considered to avoid thin average daily volume relative to the proposed position size.
  - **GJTL**: Given the negative historical edge, the liquidity of the stock should be verified to ensure it can handle the proposed position size without significant slippage.

- **Correlation**: 
  - **BIPI, NICL, PACK, RAJA, TOBA, ADMR, INKP, KIJA, MDKA**: These stocks are all triggered by the same signal (vol_breakout_up), which suggests they might move together, leading to over-concentration disguised as diversification.
  - **GJTL**: Triggered by both ma_golden_cross and vol_breakout_up, which could indicate a higher correlation with other stocks in the list.

- **Timing**: 
  - **RODA**: A stop loss of -110% below close suggests a very aggressive trade, which could be vulnerable to a gap-down at the next open if the market reverses sharply.
  - **GJTL**: Given the negative historical edge, entering a trade based on confluence might be chasing a trend that is already overextended.

- **Stale data**: 
  - **All stocks**: The analysis does not mention the training window for the historical edge, which could be stale if the market regime has shifted recently.

- **Indicator overlap**: 
  - **BIPI, NICL, PACK, RAJA, TOBA, ADMR, INKP, KIJA, MDKA**: All triggered by vol_breakout_up, which suggests a lack of independent signals and potential false confluence.

## 4. What the Author Got Right

The author correctly identified a mix of high and medium conviction signals, with a strong emphasis on volume breakout signals. The historical edge and win rate for each stock are clearly stated, providing a quantitative basis for the trades.

## 5. Critical Recommendations

1. **RODA**: Reduce the position size for RODA due to the aggressive stop loss of -110% below close and verify the liquidity of the stock to ensure it can handle the proposed position size without significant slippage.
2. **GJTL**: Re-evaluate the conviction rating for GJTL. Given the negative historical edge, the conviction should not be high. Consider a more conservative approach or avoid the trade altogether.
3. **Diversification**: Ensure that the portfolio is not over-concentrated in a single sector or correlated stocks. Verify the liquidity and correlation of the stocks to avoid hidden risks.
