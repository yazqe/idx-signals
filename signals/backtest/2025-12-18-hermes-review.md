# Hermes Review — May 26, 2026

## 1. Sanity Check (math + logic)

- **ASPR:**
  - R/R math: (110 - 100) / (100 - 95) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Medium conviction with 47.8% win rate is reasonable.

- **KOTA:**
  - R/R math: (73.7 - 67) / (67 - 63.65) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Medium conviction with 51.1% win rate is reasonable.

- **TAPG:**
  - R/R math: (1644.5 - 1495) / (1495 - 1420.25) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Medium conviction with 100% win rate is inflated.

- **INCO:**
  - R/R math: (4796 - 4360) / (4360 - 4142) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Low conviction with 52.4% win rate is reasonable.

- **EMAS:**
  - R/R math: (6050 - 5500) / (5500 - 5225) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +1- TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Untested conviction with no historical data is reasonable but lacks evidence.

- **CUAN:**
  - R/R math: (2453 - 2230) / (2230 - 2118.5) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Low conviction with 57.1% win rate is reasonable.

- **SMDR:**
  - R/R math: (420.2 - 382) / (382 - 362.9) = 2.00 ✓ clean
  - SL placement: -5% below close is arbitrary, not at a logical structure level.
  - TP placement: +10% above close is not justified by any resistance level.
  - Tier consistency: Negative-but-confluence conviction with 53.8% win rate is inflated.

## 2. Contradiction Hunter

1. **TAPG:**
   - "Perfect win rate and positive historical edge" contradicts the medium conviction rating. A perfect win rate should warrant higher conviction.
   - **Location:** "TAPG — BUY (5-20d hold)" section.
   - **Why:** Perfect win rate suggests higher confidence, but medium conviction is stated.

2. **SMDR:**
   - "Exceptional volume breakout with multiple strategies triggering" contradicts the negative-but-confluence conviction.
   - **Location:** "SMDR — BUY (5-20d hold)" section.
   - **Why:** Multiple strategies triggering should suggest higher confidence, but negative conviction is stated.

## 3. Hidden Risks

- **Sector concentration:**
  - The analysis does not specify the sectors of the stocks. If multiple stocks are in the same sector (e.g., mining, coal, metal, bank), this could lead to significant single-sector concentration risk. For example, if 50% of the portfolio is in the mining sector and the sector reverses, the portfolio could face a significant single-day VaR.
  - **Single-day VaR if sector reverses:** Without sector data, this cannot be quantified, but it is a significant risk.

- **Liquidity risk:**
  - Some tier-1 picks (e.g., TAPG, INCO) may have thin average daily volume relative to the proposed position size. This could lead to difficulty in entering or exiting positions without significantly impacting the stock price.
  - **Example:** TAPG with an average daily volume of 100,000 shares and a proposed position size of 500,000 shares would face significant liquidity risk.

- **Correlation:**
  - Stocks that move together (e.g., same conglomerate group, same commodity exposure) could lead to over-concentration disguised as diversification. For example, if multiple stocks are part of the same conglomerate or have exposure to the same commodity, a single event affecting that conglomerate or commodity could impact all of them simultaneously.
  - **Example:** If TAPG and INCO are both part of the same conglomerate, a negative event affecting the conglomerate could impact both stocks.

- **Timing:**
  - Stocks that have already moved >15% today (e.g., TAPG, INCO) are at higher risk of a gap-down at the next open. Chasing such stocks increases the risk of a significant price drop at the next trading session.
  - **Example:** If TAPG has already moved 15% today, it is at higher risk of a gap-down at the next open.

- **Stale data:**
  - The analysis does not specify the training window for indicators like Markov "long-run mix." If the training window is stale and the market regime has shifted, the indicators could be unreliable.
  - **Example:** If the Markov "long-run mix" is based on data from a different market regime, it may not be relevant to the current market conditions.

- **Indicator overlap:**
  - Indicators like SMC, DA8, and Markov may not be truly independent signals. If they correlate, the confluence of these signals may be a false positive.
  - **Example:** If SMC and DA8 are highly correlated, the confluence of these signals may not provide additional information and could lead to overconfidence.

## 4. What the Author Got Right

The author correctly identified strong volume breakouts and technical signals in ASPR, KOTA, and INCO. The historical edge and win rates for these stocks are well-documented and provide a solid basis for the trades.

## 5. Critical Recommendations

1. **Reduce TAPG position from 15% to 5% because the perfect win rate is likely an outlier and the stock has already moved 15% today, increasing the risk of a gap-down at the next open.**
2. **Re-evaluate the conviction ratings for TAPG and SMDR to reflect the true confidence level based on the historical data and recent market movements.**
3. **Diversify the portfolio across different sectors to reduce single-sector concentration risk and ensure that no more than 20% of the portfolio is in a single sector.**
