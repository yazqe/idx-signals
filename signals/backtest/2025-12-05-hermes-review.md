# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **BNBR:**
  - R/R math: (103.35 - 89.0) / (89.0 - 84.55) = 14.35 / 4.45 ≈ 3.22 (stated R/R: 3.0) — **Math error**
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by strong historical edge and recent volume breakout — **✓ clean**

- **IMPC:**
  - R/R math: (4358.5 - 3790.0) / (3790.0 - 3600.5) = 568.5 / 189.5 ≈ 3.00 (stated R/R: 3.0) — **✓ clean**
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: High conviction is justified by strong historical edge and recent volume breakout — **✓ clean**

- **KOTA:**
  - R/R math: (50.6 - 44.0) / (44.0 - 41.8) = 6.6 / 2.2 ≈ 3.00 (stated R/R: 3.0) — **✓ clean**
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Medium conviction is justified by solid historical edge and recent volume breakout — **✓ clean**

- **SMDR:**
  - R/R math: (386.4 - 336.0) / (336.0 - 319.2) = 50.4 / 16.8 ≈ 3.00 (stated R/R: 30) — **✓ clean**
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Negative-but-confluence conviction is justified by the confluence of two strategies, despite negative historical edge — **✓ clean**

- **ZATA:**
  - R/R math: (75.9 - 66.0) / (66.0 - 62.7) = 9.9 / 3.3 ≈ 3.00 (stated R/R: 3.0) — **✓ clean**
  - SL placement: -5% below close is arbitrary and not based on a logical structure level.
  - TP placement: +15% above close is not justified by any specific resistance level.
  - Tier consistency: Low conviction is justified by the positive historical edge and recent volume breakout, despite low overall win rate — **✓ clean**

## 2. Contradiction Hunter

1. **BNBR:**
   - "High conviction" is stated, but the R/R math is incorrect (3.22 vs. 3.0). This could undermine the confidence in the trade setup.
   - **Contradiction:** "High conviction" with incorrect R/R math.

2. **SMDR:**
   - "Negative-but-confluence" conviction is stated, but the historical edge for `ma_golden_cross` is negative (-3.7%).
   - **Contradiction:** "Negative historical edge" with "high conviction" due to confluence.

3. **ZATA:**
   - "Low conviction" is stated, but the analysis mentions a "positive historical edge" and "recent volume breakout."
   - **Contradiction:** "Low conviction" with positive historical edge and recent volume breakout.

## 3. Hidden Risks

- **Sector concentration:**
  - The analysis does not specify the sectors of the stocks. If multiple stocks are in the same sector (e.g., mining, coal, metal, bank), this could lead to significant single-sector concentration risk. For example, if BNBR, IMPC, and KOTA are all in the same sector, a sector-wide reversal could significantly impact the portfolio.
  - **Single-day VaR:** If the portfolio is heavily concentrated in a single sector, a single-day reversal could lead to a large VaR.

- **Liquidity risk:**
  - The analysis does not mention the average daily volume (ADV) of the stocks. If any of the tier-1 picks (BNBR, IMPC, KOTA) have thin ADV relative to the proposed position size, this could lead to liquidity issues and slippage.
  - **Example:** If BNBR has an ADV of 100,000 shares and the proposed position size is 50,000 shares, this could lead to significant slippage and execution risk.

- **Correlation:**
  - The analysis does not consider the correlation between the stocks. If multiple stocks are part of the same conglomerate group or have similar commodity exposure, this could lead to over-concentration disguised as diversification.
  - **Example:** If BNBR and IMPC are both part of the same conglomerate group, a single event affecting the group could impact both stocks simultaneously.

- **Timing:**
  - The analysis does not mention the intraday movement of the stocks. If any of the stocks have already moved more than 15% today, this could indicate a high chase risk and vulnerability to a gap-down at the next open.
  - **Example:** If BNBR has already moved 15% today, entering a position now could be risky due to the potential for a gap-down at the next open.

- **Stale data:**
  - The analysis does not specify the training window for the Markov "long-run mix" indicators. If the training window is stale and the market regime has shifted recently, the indicators could be unreliable.
  - **Example:** If the Markov indicators are trained on data from a different market regime, they may not accurately reflect current market conditions.

- **Indicator overlap:**
  - The analysis uses multiple indicators (SMC, DA8, Markov) that may not be truly independent. If these indicators are correlated, the confluence of signals may be less significant than it appears.
  - **Example:** If SMC and DA8 are highly correlated, the confluence of these signals may not provide additional information.

## 4. What the Author Got Right

The author correctly identified the strong historical edge and recent volume breakouts for BNBR and IMPC, which are solid reasons for high conviction. The use of multiple indicators for SMDR, despite the negative historical edge, is a reasonable approach to balance risk and opportunity.

## 5. Critical Recommendations

1. **BNBR:**
   - **Reduce position size from 15% to 5%** because the R/R math is incorrect and the SL placement is arbitrary. This will reduce the risk exposure and align the position size with the actual R/R.

2. **SMDR:**
   - **Re-evaluate the conviction level** and consider reducing the position size from 10% to 5% due to the negative historical edge for `ma_golden_cross`. The confluence of signals is a positive, but the negative edge should not be ignored.

3. **ZATA:**
   - **Increase the stop loss to -10% below the close** to provide a more robust risk management strategy, given the low conviction and positive historical edge. This will reduce the risk of a significant drawdown if the trade goes against the position.
