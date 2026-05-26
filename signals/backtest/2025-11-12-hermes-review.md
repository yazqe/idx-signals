# Hermes Review — 2026-05-25

## 1. Sanity Check (math + logic)

- **BNBR:**
  - R/R math: (52.8 - 48.0) / (48.0 - 45.6) = 4.8 / 2.4 = 2.0 (stated R/R: 2.0) — ✓ clean
  - SL placement: -5% below close (45.6) — logical
  - TP placement: +10% above close (52.8) — logical
  - Tier consistency: High conviction with strong historical edge and win rate — ✓ clean

- **BRPT:**
  - R/R math: (4158.0 - 3780.0) / (3780.0 - 3591.0) = 378 / 189 = 2.0 (stated R/R: 2.0) — ✓ clean
  - SL placement: -5% below close (3591.0) — logical
  - TP placement: +10% above close (4158.0) — logical
  - Tier consistency: High conviction with strong historical edge and win rate — ✓ clean

- **INET:**
  - R/R math: (497.2 - 452.0) / (452.0 - 429.4) = 45.2 / 22.6 = 2.0 (stated R/R: 2.0) — ✓ clean
  - SL placement: -5% below close (429.4) — logical
  - TP placement: +10% above close (497.2) — logical
  - Tier consistency: Medium conviction with good historical edge and win rate — ✓ clean

- **INKP:**
  - R/R math: (8497.5 - 7725.0) / (7725.0 - 7338.75) = 772.5 / 386.25 = 2.0 (stated R/R: 2.0) — ✓ clean
  - SL placement: -5% below close (7338.75) — logical
  - TP placement: +10% above close (8497.5) — logical
  - Tier consistency: Medium conviction with strong win rate — ✓ clean

- **AMMN:**
  - R/R math: (7166.25 - 6825.0) / (6825.0 - 6483.75) = 341.25 / 341.25 = 1.0 (stated R/R: 2.0) — **Incorrect R/R calculation**
  - SL placement: -5% below close (6483.75) — logical
  - TP placement: +10% above close (7166.25) — logical
  - Tier consistency: Medium conviction with strong historical edge and win rate — ✓ clean

- **MEDC:**
  - R/R math: (1368.0 - 1280.0) / (1280.0 - 1216.0) = 88 / 64 = 1.375 (stated R/R: 2.0) — **Incorrect R/R calculation**
  - SL placement: -5% below close (1216.0) — logical
  - TP placement: +10% above close (1368.0) — logical
  - Tier consistency: Low conviction with positive historical edge and decent win rate — ✓ clean

- **SMDR:**
  - R/R math: (334.4 - 304.0) / (304.0 - 288.8) = 30.4 / 15.2 = 2.0 (stated R/R: 2.0) — ✓ clean
  - SL placement: -5% below close (288.8) — logical
  - TP placement: +10% above close (334.4) — logical
  - Tier consistency: Low conviction with positive historical edge — ✓ clean

- **BIPI:**
  - R/R math: (85.6 - 82.0) / (82.0 - 77.9) = 3.6 / 4.1 = 0.878 (stated R/R: 2.0) — **Incorrect R/R calculation**
  - SL placement: -5% below close (77.9) — logical
  - TP placement: +10% above close (85.6) — logical
  - Tier consistency: Negative conviction with negative historical edge and low win rate — ✓ clean

- **EMAS:**
  - R/R math: (4211.0 - 4010.0) / (4010.0 - 3809.5) = 201 / 200.5 = 1.0025 (stated R/R: 2.0) — **Incorrect R/R calculation**
  - SL placement: -5% below close (3809.5) — logical
  - TP placement: +10% above close (4211.0) — logical
  - Tier consistency: Negative conviction with negative historical edge and zero win rate — ✓ clean

- **MDKA:**
  - R/R math: (2542.0 - 2420.0) / (2420.0 - 2299.0) = 122 / 121 = 1.008 (stated R/R: 2.0) — **Incorrect R/R calculation**
  - SL placement: -5% below close (2299.0) — logical
  - TP placement: +10% above close (2542.0) — logical
  - Tier consistency: Negative conviction with negative historical edge and low win rate — ✓ clean

## 2. Contradiction Hunter

1. **AMMN:**
   - **Location:** "High historical edge and solid win rate with the RSI oversold signal."
   - **Contradiction:** The R/R calculation is incorrect (1.0 instead of 2.0), which contradicts the stated high conviction.

2. **MEDC:**
   - **Location:** "Low tier but with a positive historical edge and a decent win rate, indicating potential for a bounce."
   - **Contradiction:** The R/R calculation is incorrect (1.375 instead of 2.0), which contradicts the stated positive historical edge.

3. **BIPI:**
   - **Location:** "Negative tier but with a strong RSI oversold signal, which could indicate a potential reversal."
   - **Contradiction:** The R/R calculation is incorrect (0.878 instead of 2.0), which contradicts the stated strong RSI oversold signal.

4. **EMAS:**
   - **Location:** "Negative tier but with a strong RSI oversold signal, which could indicate a potential reversal."
   - **Contradiction:** The R/R calculation is incorrect (1.0025 instead of 2.0), which contradicts the stated strong RSI oversold signal.

5. **MDKA:**
   - **Location:** "Negative tier but with a strong MA golden cross signal, which could indicate a potential reversal."
   - **Contradiction:** The R/R calculation is incorrect (1.008 instead of 2.0), which contradicts the stated strong MA golden cross signal.

## 3. Hidden Risks

- **Sector concentration:** The analysis includes multiple stocks from the same sectors (e.g., mining, coal, metal, bank). For example, BNBR and BRPT are both in the mining sector. This concentration increases the portfolio's vulnerability to sector-specific risks. If the mining sector reverses, the portfolio could suffer significant losses.
- **Liquidity risk:** INKP has a relatively thin average daily volume. The proposed position size could lead to liquidity issues, making it difficult to enter or exit the position without significantly impacting the stock price.
- **Correlation:** Stocks like INET and INKP are in the same sector (telecommunications) and may move together. This correlation could lead to over-concentration disguised as diversification.
- **Timing:** BIPI and EMAS have already moved significantly today (over 15%). Entering these positions now increases the risk of a gap-down at the next open, as the market may have already priced in the oversold signal.
- **Stale data:** The analysis relies on historical data for the RSI and MA signals. If the training window is not recent, the signals could be stale, especially if the market regime has shifted recently.
- **Indicator overlap:** The use of multiple indicators (SMC, DA8, Markov) may not be truly independent. If these indicators are correlated, the confluence of signals may be overestimated, leading to false positives.

## 4. What the Author Got Right

The author correctly identified the strong volume breakout signals for BNBR and BRPT, which have a high historical edge and win rate. This indicates a solid potential for short-term momentum and is a strong reason to consider these stocks for a short-term trade.

## 5. Critical Recommendations

1. **Re-evaluate R/R calculations:** Correct the R/R calculations for AMMN, MEDC, BIPI, EMAS, and MDKA. The incorrect R/R values could lead to overestimating the potential reward and underestimating the risk.
2. **Diversify sector exposure:** Reduce the concentration of stocks in the same sectors (e.g., mining, telecommunications) to mitigate sector-specific risks. Consider adding stocks from different sectors to balance the portfolio.
3. **Monitor liquidity and timing:** For INKP, ensure that the proposed position size is manageable given the stock's average daily volume. For BIPI and EMAS, consider waiting for a pullback or a more favorable entry point to avoid the risk of a gap-down at the next open.
