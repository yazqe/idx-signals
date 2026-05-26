# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **ASHA:**
  - R/R math: (72.6 - 66.0) / (66.0 - 62.7) = 6.6 / 3.3 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (62.7) is a logical structure level based on a fixed percentage.
  - TP placement: +10% above close (72.6) is a logical structure level based on a fixed percentage.
  - Tier consistency: Medium-tier RSI oversold signal with a positive historical edge and a 55.6% win rate. ✓ clean

- **MINA:**
  - R/R math: (190.3 - 173.0) / (173.0 - 164.35) = 17.3 / 8.65 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (164.35) is a logical structure level based on a fixed percentage.
  - TP placement: +10% above close (190.3) is a logical structure level based on a fixed percentage.
  - Tier consistency: Medium-tier RSI oversold signal with a strong historical edge and a 50% win rate. ✓ clean

- **CBDK:**
  - R/R math: (6452.5 - 5875.0) / (5875.0 - 5581.25) = 577.5 / 293.75 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (5581.25) is a logical structure level based on a fixed percentage.
  - TP placement: +10% above close (6452.5) is a logical structure level based on a fixed percentage.
  - Tier consistency: Low-tier RSI oversold signal with a positive historical edge and a high win rate. ✓ clean

- **- **PANI:**
  - R/R math: (14280.0 - 13500.0) / (13500.0 - 12825.0) = 780.0 / 675.0 = 1.15 (stated R/R: 2.00) **Issue: R/R math is incorrect.**
  - SL placement: -5% below close (12825.0) is a logical structure level based on a fixed percentage.
  - TP placement: +10% above close (14280.0) is a logical structure level based on a fixed percentage.
  - Tier consistency: Low-tier RSI oversold signal with a positive historical edge and a 55.6% win rate. **Issue: R/R inconsistency with stated R/R.**

- **BIPI:**
  - R/R math: (91.3 - 83.0) / (83.0 - 78.85) = 8.3 / 4.15 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (78.85) is a logical structure level based on a fixed percentage.
  - TP placement: +10% above close (91.3) is a logical structure level based on a fixed percentage.
  - Tier consistency: Negative-but-confluence RSI oversold signal with a negative historical edge and a 33.3% win rate. **Issue: Negative-tier signal with a negative historical edge.**

- **MBMA:**
  - R/R math: (666.5 - 635.0) / (635.0 - 603.25) = 31.5 / 31.75 = 1.00 (stated R/R: 2.00) **Issue: R/R math is incorrect.**
  - SL placement: -5% below close (603.25) is a logical structure level based on a fixed percentage.
  - TP placement: +10% above close (666.5) is a logical structure level based on a fixed percentage.
  - Tier consistency: Negative-tier vol_breakout_up signal with a negative historical edge and a 54.2% win rate. **Issue: Negative-tier signal with a negative historical edge.**

## 2. Contradiction Hunter

1. **BIPI:**
   - **Location quote:** "Negative-tier RSI oversold signal, but included due to strong recent volume action and potential for a reversal."
   - **Why contradictory:** The stock is flagged as a negative-tier signal with a negative historical edge (-1.04% over 9 past trades, win rate 33.3%), yet it is included in the allocation due to "strong recent volume action and potential for a reversal." This contradicts the negative-tier classification and the historical edge.

2. **MBMA:**
   - **Location quote:** "Negative-tier vol_breakout_up signal, but included due to the strategy's strong Sharpe ratio and potential for a breakout."
   - **Why contradictory:** The stock is flagged as a negative-tier signal with a negative historical edge (-0.19% over 24 past trades, win rate 54.2%), yet it is included in the allocation due to the "strategy's strong Sharpe ratio and potential for a breakout." This contradicts the negative-tier classification and the historical edge.

## 3. Hidden Risks

- **Sector concentration:** The analysis does not specify the sectors of the stocks. If multiple stocks are in the same sector (e.g., mining, coal, metal, bank), this could lead to significant single-sector concentration risk. For example, if 50% of the portfolio is in the mining sector and the sector reverses, the portfolio could face a significant single-day VaR.
- **Liquidity risk:** The analysis does not provide average daily volume (ADV) for the stocks. Any tier-1 picks with thin ADV relative to the proposed position size could pose liquidity risk, making it difficult to enter or exit positions without impacting the market.
- **Correlation:** The analysis does not consider the correlation between the stocks. If multiple stocks move together (e.g., same conglomerate group, same commodity exposure), this could lead to over-concentration disguised as diversification.
- **Timing:** The analysis does not mention the intraday movement of the stocks. If any of the stocks have already moved >15% today, this could indicate a high chase risk and vulnerability to a gap-down at the next open.
- **Stale data:** The analysis does not specify the training window for the indicators. If the indicators rely on Markov "long-run mix," the training window should be mentioned to ensure the data is not stale, especially if the market regime has shifted recently.
- **Indicator overlap:** The analysis uses multiple indicators (SMC, DA8, Markov) without specifying whether these signals are truly independent. If these indicators correlate, it could lead to false confluence and overconfidence in the signals.

## 4. What the Author Got Right

The author correctly identified the historical edge and win rate for each stock, providing a clear and quantifiable basis for the trades. The use of fixed percentage stop loss and take profit levels ensures a consistent risk management approach.

## 5. Critical Recommendations

1. **Re-evaluate BIPI and MBMA:** Remove BIPI and MBMA from the allocation due to their negative-tier signals and negative historical edges. The inclusion of these stocks contradicts the negative-tier classification and the historical edge.
2. **Check sector concentration and correlation:** Ensure that the portfolio is not over-concentrated in a single sector and that the stocks do not move together. Diversify the portfolio to reduce single-sector and correlation risks.
3. **Verify liquidity and timing:** Check the average daily volume (ADV) for each stock and ensure that the proposed position sizes are within the ADV. Also, verify the intraday movement of the stocks to avoid chasing high-momentum stocks that are vulnerable to a gap-down at the next open.
