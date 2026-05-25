# Hermes Review — May 25, 2026

## 1. Sanity Check (math + logic)

- **SINI:**
  - R/R math: (18067.5 - 16425) / (16425 - 15603.75) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close — **Arbitrary %, not at a logical structure level**
  - TP placement: +10% above close — **Arbitrary %, not at a resistance level**
  - Tier consistency: High conviction for strong historical edge and volume breakout — **✓ clean**

- **VKTR:**
  - R/R math: (1050.5 - 955) / (955 - 907.25) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close — **Arbitrary %, not at a logical structure level**
  - TP placement: +10% above close — **Arbitrary %, not at a resistance level**
  - Tier consistency: High conviction for strong historical edge and volume breakout — **✓ clean**

- **ENRG:**
  - R/R math: (1688.5 - 1535) / (1535 - 1458.25) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close — **Arbitrary %, not at a logical structure level**
  - TP placement: +10% above close — **Arbitrary %, not at a resistance level**
  - Tier consistency: Medium conviction for moderate historical edge and volume breakout — **✓ clean**

- **BREN:**
  - R/R math: (8800 - 8000) / (8000 - 7600) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close — **Arbitrary %, not at a logical structure level**
  - TP placement: +10% above close — **Arbitrary %- **BREN:**
  - R/R math: (8800 - 8000) / (8000 - 7600) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close — **Arbitrary %, not at a logical structure level**
  - TP placement: +10% above close — **Arbitrary %, not at a resistance level**
  - Tier consistency: Medium conviction for strong historical edge and high win rate — **✓ clean**

- **ADMR:**
  - R/R math: (1996.5 - 1815) / (1815 - 1724.25) = 1.00 (stated R/R: 2.00) — **Incorrect**
  - SL placement: -5% below close — **Arbitrary %, not at a logical structure level**
  - TP placement: +10% above close — **Arbitrary %, not at a resistance level**
  - Tier consistency: Low conviction for low historical edge and moderate win rate — **✓ clean**

## 2. Contradiction Hunter

1. **Contradiction in Conviction and Historical Edge:**
   - **Location:** "SINI — **Conviction:** High, **Historical edge:** 13.23% over 52 past trades (win rate 67.3%)"
   - **Why:** Despite a high historical edge and win rate, the conviction is still marked as "High" without additional supporting evidence for such a strong rating.

2. **Contradiction in Conviction and Historical Edge:**
   - **Location:** "ADMR — **Conviction:** Low, **Historical edge:** 0.77% over 15 past trades (win rate 53.3%)"
   - **Why:** The low conviction is justified by a low historical edge, but the win rate is moderate, which could warrant a higher conviction.

3. **Contradiction in Trigger and Conviction:**
   - **Location:** "BREN — **Triggered:** rsi_oversold, **Conviction:** Medium"
   - **Why:** The RSI oversold condition is a contrarian signal, yet the conviction is medium, which might be too high for a contrarian trade without additional supporting factors.

## 3. Hidden Risks

- **Sector Concentration:**
  - **Mining/Coal/Metal:** No specific sector concentration mentioned, but if multiple picks are in the same sector, it could lead to significant single-day VaR if the sector reverses.
  - **Bank:** No specific bank picks mentioned, but if present, it could also lead to concentration risk.

- **Liquidity Risk:**
  - **SINI:** High volume, likely liquid.
  - **VKTR:** High volume, likely liquid.
  - **ENRG:** Moderate volume, check average daily volume relative to proposed position size.
  - **BREN:** Moderate volume, check average daily volume relative to proposed position size.
  - **ADMR:** Low volume, check average daily volume relative to proposed position size.

- **Correlation:**
  - **SINI and VKTR:** Both triggered by vol_breakout_up, could move together.
  - **ENRG and BREN:** Both triggered by different signals, but check for any common underlying factors.

- **Timing:**
  - **SINI:** Check if the stock has already moved >15% today.
  - **VKTR:** Check if the stock has already moved >15% today.
  - **ENRG:** Check if the stock has already moved >15% today.
  - **BREN:** Check if the stock has already moved >15% today.
  - **ADMR:** Check if the stock has already moved >15% today.

- **Stale Data:**
  - **No specific indicators relying on Markov "long-run mix" mentioned, but check if any indicators are using stale training windows.**

- **Indicator Overlap:**
  - **SMC + DA8 + Markov:** Check if these indicators are truly independent or if they correlate, leading to false confluence.

## 4. What the Author Got Right

The author correctly identified strong historical edges and significant volume breakouts for SINI and VKTR, which are key factors in high-conviction trades. The use of multiple indicators to support the trades is also a strong point, providing a robust foundation for the analysis.

## 5. Critical Recommendations

1. **Correct R/R Calculations:**
   - Recalculate the R/R ratios for all picks to ensure they are accurate. For example, SINI, VKTR, ENRG, BREN, and ADMR all have incorrect R/R calculations.

2. **Reevaluate SL and TP Placement:**
   - Place stop losses at logical structure levels (e.g., previous support levels) rather than arbitrary percentages. Similarly, place take profits at resistance levels mentioned in the analysis.

3. **Adjust Conviction Ratings:**
   - Reevaluate the conviction ratings for SINI and ADMR to ensure they are consistent with the underlying evidence. SINI's high conviction may be overinflated, while ADMR's low conviction may be deflated given its moderate win rate.
