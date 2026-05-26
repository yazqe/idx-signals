# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **AADI:**
  - R/R math: (8140 - 7400) / (7400 - 7030) = 740 / 370 ≈ 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (7030) is a logical structure level.
  - TP placement: +10% above close (8140) is a logical structure level.
  - Tier consistency: Medium conviction with strong historical edge and high win rate. ✓ clean

- **CUAN:**
  - R/R math: (2035 - 1850) / (1850 - 1757.5) = 185 / 92.5 ≈ 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (1757.5) is a logical structure level.
  - TP placement: +10% above close (2035) is a logical structure level.
  - Tier consistency: High conviction with strong historical edge and good win rate. ✓ clean

- **PTRO:**
  - R/R math: (8250 - 7500) / (7500 - 7125) = 750 / 375 = 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (7125) is a logical structure level.
  - TP placement: +10% above close (8250) is a logical structure level.
  - Tier consistency: High conviction with very strong historical edge and high win rate. ✓ clean

- **BREN:**
  - R/R math: (9532.5 - 8675) / (8675 - 8241.25) = 857.5 / 433.75 ≈ 2.00 (stated R/R: 2.00) ✓ clean
  - SL - SL placement: -5% below close (8241.25) is a logical structure level.
  - TP placement: +10% above close (9532.5) is a logical structure level.
  - Tier consistency: Low conviction with a positive historical edge and recent volume action. ✓ clean

- **CDIA:**
  - R/R math: (128.1 - 122) / (122 - 115.9) = 6.1 / 6.1 ≈ 1.00 (stated R/R: 2.00) **Incorrect R/R calculation**
  - SL placement: -5% below close (115.9) is a logical structure level.
  - TP placement: +10% above close (128.1) is a logical structure level.
  - Tier consistency: Low conviction with a positive historical edge and recent volume action. **Inconsistent R/R calculation**

- **ENRG:**
  - R/R math: (1331 - 1210) / (1210 - 1149.5) = 121 / 60.5 ≈ 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (1149.5) is a logical structure level.
  - TP placement: +10% above close (1331) is a logical structure level.
  - Tier consistency: Low conviction with a positive historical edge and recent volume action. ✓ clean

- **ESSA:**
  - R/R math: (737 - 670) / (670 - 636.5) = 67 / 33.5 ≈ 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (636.5) is a logical structure level.
  - TP placement: +10% above close (737) is a logical structure level.
  - Tier consistency: Negative historical edge but exceptional confluence with strong recent volume action. **Inconsistent conviction rating**

- **GOTO:**
  - R/R math: (69.3 - 63) / (63 - 59.85) = 6.3 / 3.15 ≈ 2.00 (stated R/R: 2.00) ✓ clean
  - SL placement: -5% below close (59.85) is a logical structure level.
  - TP placement: +10% above close (69.3) is a logical structure level.
  - Tier consistency: Negative historical edge but exceptional confluence with strong recent volume action. **Inconsistent conviction rating**

- **KIJA:**
  - R/R math: (245.8 - 224) / (224 - 212.8) = 21.8 / 11.2 ≈ 1.95 (stated R/R: 2.00) **Incorrect R/R calculation**
  - SL placement: -5% below close (212.8) is a logical structure level.
  - TP placement: +10% above close (245.8) is a logical structure level.
  - Tier consistency: Negative historical edge but exceptional confluence with strong recent volume action. **Inconsistent conviction rating**

## 2. Contradiction Hunter

1. **CDIA:**
   - **Location:** "Low conviction but strong recent volume action and a positive historical edge."
   - **Why:** The R/R calculation is incorrect (1.00 instead of 2.00), which contradicts the stated R/R of 2.00.

2. **ESSA:**
   - **Location:** "Negative historical edge but exceptional confluence with strong recent volume action."
   - **Why:** The conviction rating is "Negative-but-confluence" despite the strong recent volume action, which is inconsistent with the positive historical edge.

3. **GOTO:**
   - **Location:** "Negative historical edge but exceptional confluence with strong recent volume action."
   - **Why:** The conviction rating is "Negative-but-confluence" despite the strong recent volume action, which is inconsistent with the positive historical edge.

4. **KIJA:**
   - **Location:** "Negative historical edge but exceptional confluence with strong recent volume action."
   - **Why:** The R/R calculation is incorrect (1.95 instead of 2.00), which contradicts the stated R/R of 2.00.

## 3. Hidden Risks

- **Sector concentration:**
  - **Mining/Coal/Metal:** No specific sector concentration mentioned, but if multiple stocks are in the same sector, it could lead to single-day VaR issues if the sector reverses.
  - **Bank:** No specific bank stocks mentioned, but if present, it could lead to similar risks.

- **Liquidity risk:**
  - **CDIA:** Low average daily volume relative to the proposed position size could lead to liquidity issues.
  - **KIJA:** Low average daily volume relative to the proposed position size could lead to liquidity issues.

- **Correlation:**
  - **ENRG and KIJA:** Both are triggered by RSI oversold conditions, which could indicate a correlation in their movements.
  - **BREN, CDIA, ENRG, ESSA, GOTO, KIJA:** All are triggered by volume breakout up, which could indicate a correlation in their movements.

- **Timing:**
  - **CDIA:** If the stock has already moved >15% today, it could be at risk of a gap-down at the next open.
  - **KIJA:** If the stock has already moved >15% today, it could be at risk of a gap-down at the next open.

- **Stale data:**
  - **RSI oversold:** The training window for the RSI indicator is not mentioned, which could be stale if the market regime has shifted recently.

- **Indicator overlap:**
  - **SMC + DA8 + Markov:** These indicators might not be truly independent signals, leading to false confluence.

## 4. What the Author Got Right

The author correctly identified the strong historical edge and high win rate for CUAN and PTRO, which are high conviction signals with recent volume action. This is a strong foundation for the analysis.

## 5. Critical Recommendations

1. **Correct the R/R calculations for CDIA and KIJA:**
   - **CDIA:** The R/R should be 1.00, not 2.00.
   - **KIJA:** The R/R should be 1.95, not 2.00.

2. **Re-evaluate the conviction ratings for ESSA, GOTO, and KIJA:**
   - **ESSA:** Consider lowering the conviction rating due to the negative historical edge.
   - **GOTO:** Consider lowering the conviction rating due to the negative historical edge.
   - **KIJA:** Consider lowering the conviction rating due to the negative historical edge.

3. **Address the liquidity risk for CDIA and KIJA:**
   - **CDIA:** Reduce the position size to ensure adequate liquidity.
   - **KIJA:** Reduce the position size to ensure adequate liquidity.
