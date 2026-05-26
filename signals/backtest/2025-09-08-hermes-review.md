# Hermes Review — 2026-05-25

## 1. Sanity Check (math + logic)

- **ANTM:**
  - R/R math: (3610 * 1.10 - 3610) / (3610 - 3610 * 0.95) = 10% / 5% = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by strong historical performance and win rate.

- **INDY:**
  - R/R math: (1660 * 1.10 - 1660) / (1660 - 1660 * 0.95) = 10% / 5% = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by solid historical edge and win rate.

- **RODA:**
  - R/R math: (50 * 1.10 - 50) / (50 - 50 * 0.95) = 10% / 5% = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by high historical edge and strong win rate.

- **SDMU:**
  - R/R math: (60 * 1.10 - 60) / (60 - 60 * 0.95) = 10% / 5% = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by exceptional historical performance and win rate.

- **TINS:**
  - R/R math: (1090 * 1.10 - 1090) / (1090 - 1090 * 0.95) = 10% / 5% = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by strong historical edge and consistent performance.

- **PANI:**
  - R/R math: (14325 * 1.10 - 14325) / (14325 - 14325 * 0.95) = 10% / 5% = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +10% above close is not justified by any specific resistance level.
  - Tier consistency: Low conviction is justified by recent volume action and positive historical edge.

## 2. Contradiction Hunter

1. **PANI:**
   - **Location quote:** "PANI, while lower in conviction, shows promise due to recent volume action and positive historical edge."
   - **Why contradictory:** The analysis states that PANI has low conviction but still includes it in the buy list, which contradicts the stated low conviction.

## 3. Hidden Risks

- **Sector concentration**: The analysis includes multiple mining and metal stocks (ANTM, RODA, TINS). This could lead to significant sector concentration risk. If the mining sector reverses, the portfolio could suffer substantial losses.
- **Liquidity risk**: PANI has a high entry price and a large position size. If the daily volume is thin, it could be difficult to enter or exit the position without significantly impacting the price.
- **Correlation**: ANTM, RODA, and TINS are all in the mining sector and are likely to move together. This over-concentration could disguise the lack of diversification.
- **Timing**: ANTM, INDY, RODA, SDMU, and TINS are all triggered by a volume breakout, which suggests they may have already moved significantly. This increases the risk of a gap-down at the next open.
- **Stale data**: The historical edge and win rates are based on past trades, but the training window is not mentioned. If the market regime has shifted recently, these indicators could be stale.
- **Indicator overlap**: The analysis uses multiple indicators (vol_breakout_up, rsi_oversold) that may not be independent. This could lead to false confluence and overconfidence in the trades.

## 4. What the Author Got Right

The author correctly identified strong historical performance and win rates for ANTM, RODA, and SDMU, which are key factors in high conviction trades. The use of multiple indicators (vol_breakout_up, rsi_oversold) provides a robust basis for the trades, although the independence of these indicators should be verified.

## 5. Critical Recommendations

1. **Reduce PANI position size**: Given the low conviction and high entry price, reduce the position size to 2% of the portfolio to mitigate liquidity risk.
2. **Diversify sector exposure**: Consider reducing the weight of mining and metal stocks (ANTM, RODA, TINS) to avoid over-concentration in a single sector.
3. **Verify indicator independence**: Ensure that the indicators used (vol_breakout_up, rsi_oversold) are truly independent and not correlated to avoid false confluence and overconfidence in the trades.
