# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **WIFI**: ✓ clean  
- **KAQI**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **CUAN**: ✓ clean  
- **MBMA**: ✓ clean  
- **GOTO**: ✓ clean  
- **APLN**: ✓ clean  
- **NICL**: R/R math fails. (TP - Entry) = 11% / (Entry - SL) = 9% → R/R = 1.22, NOT stated as “+11% / -9% = 1.22” — but author implies positive edge despite negative historical return. This is mathematically correct but logically incoherent: if historical edge is -0.65%, claiming R/R of 1.22 is misleading. It suggests a favorable risk-reward profile while admitting the strategy loses money on average.  
- **DEWA**: R/R math: (10% / 9%) = 1.11 — stated as “+10% / -9%” but no R/R ratio is given. Inconsistent formatting. More critically: historical edge is -0.72% — meaning over 10 trades, this setup lost money. Claiming “strong RSI divergence + volume spike” as justification for trade contradicts the data. R/R is not the issue — the *edge* is.  
- **BUMI**: R/R: (10% / 9%) = 1.11 — again, no ratio stated. Historical edge: -0.82%. Same issue as NICL/DEWA: positive R/R with negative edge is not a valid trading edge — it’s a trap.  
- **SL placement**: All SLs are fixed % below close (6–9%). No reference to technical structure (e.g., prior swing low, VWAP, ATR-based). In IDX, where gap risk is high and liquidity uneven, fixed % SLs are arbitrary and dangerous.  
- **TP placement**: All TPs are arbitrary % targets (8–15%) with no mention of prior resistance, Fibonacci levels, or volume clusters. No technical justification beyond “above close.”  
- **Tier consistency**:  
  - WIFI, KAQI, KOTA: Conviction = High, but n=10, 5, 12 — all small samples. KAQI has n=5 with 60% win rate — statistically insignificant (p=0.49 for null hypothesis). Tier inflation.  
  - NICL, DEWA, BUMI: Conviction = Negative-but-confluence — but still listed as “BUY.” Contradictory labeling. If historical edge is negative, it should be “SELL” or “AVOID,” not “BUY.” Tier deflation in logic.  
  - GOTO: Low conviction, but 36.4% win rate with high liquidity — why not medium? Inconsistent tier logic.  
  - MDKA: Low conviction despite 40% win rate and deep RSI — but entry price is 1930–1970 (IDR ~$125–130), making it a large-cap. Why low conviction? No rationale given. Tier inflation or deflation? Unclear.  

## 2. Contradiction Hunter

1. **Location**: “NICL — BUY... Historical edge: -0.65%” + “Why: Deep oversold... despite negative history.”  
   **Contradiction**: You cannot rationally “BUY” an asset with negative historical edge and call it a “confluence.” Confluence implies reinforcing signals — but here, the only signal (RSI oversold) has a proven negative expectancy. This is not confluence — it’s denial of data.

2. **Location**: “Market Read: Volume is rising in low-tier and negative-tier names, suggesting institutional accumulation.”  
   **Contradiction**: Institutional accumulation should correlate with *positive* historical edge and *positive* price momentum. Yet NICL, DEWA, BUMI have negative historical edge — meaning institutions have lost money on this setup before. Claiming “institutional accumulation” as justification for buying negative-edge trades is logically incoherent. Institutions don’t accumulate to lose money.

3. **Location**: “GTSI — Conviction: Medium... win rate 46.7%” and “APLN — Conviction: Low... win rate 50%”  
   **Contradiction**: APLN has a higher win rate (50%) than GTSI (46.7%), yet APLN is rated “Low” and GTSI “Medium.” No rationale provided for this inversion. Conviction tiers are arbitrary and inconsistent.

4. **Location**: “PTRO — Conviction: Low... volume likely accelerating — confluence with macro energy rebound.”  
   **Contradiction**: PTRO is an energy stock. BUMI (infrastructure) and DEWA (utilities) are also flagged with “sector-wide rotation.” But no mention of sector concentration — all three are energy/utilities/infrastructure. If energy reverses, all three collapse simultaneously. Yet all are “BUY” with no diversification warning. Positioning is monocausal.

## 3. Hidden Risks

- **Sector concentration**: 5 of 15 picks (PTRO, BUMI, DEWA, NICL, MDKA) are in energy, utilities, or infrastructure. That’s 33% of the portfolio. If oil/gas/coal prices reverse (e.g., due to OPEC+ or global recession), these stocks will drop in tandem. Single-day VaR for this sector block could exceed 12% — far above the 7–9% SLs. Portfolio is not diversified — it’s a sector bet disguised as multi-stock selection.

- **Liquidity risk**: GOTO (IDR 24–26) has “high liquidity” claimed — but IDX small-cap tech stocks often have avg daily volume < 500k shares. At 25 IDR/share, 500k shares = IDR 12.5M (~$800). If position size is >IDR 50M (~$3k), slippage will be >2%. Author ignores this. Same for MBMA (IDR 325–335) — low volume, wide bid-ask. No volume data provided — dangerous.

- **Correlation**: PTRO, BUMI, DEWA, NICL all exposed to energy/infrastructure macro. GOTO and APLN both tech. KOTA and KAQI both industrial. This is not diversification — it’s 3–4 correlated clusters. Author’s “diversified picks” are illusions.

- **Timing**: NICL, DEWA, BUMI all triggered on “today’s volume surge.” If today’s move is already >15% (common in IDX on oversold bounce days), these are chasing entries. High gap-down risk tomorrow if volume dries up. No mention of intraday price action or volume profile — pure end-of-day RSI trigger.

- **Stale data**: All historical edges are based on “past trades” with no time window specified. If the training data includes 2021–2022 (post-pandemic stimulus) and current regime is 2024 (high rates, weak rupiah), the RSI oversold edge is likely obsolete. RSI mean-reversion fails in trending markets — and IDX has been in a multi-month downtrend. Markov “long-run mix” (mentioned in intro) is not referenced here — but if used, training window is unstated. Stale model risk.

- **Indicator overlap**: All 15 picks rely on RSI oversold. No other indicators (MACD, volume profile, OBV, VWAP) are mentioned. “Confluence” is a lie — it’s one indicator repeated 15 times. False confluence. SMC, DA8, Markov referenced in intro but not applied. This is not a multi-indicator system — it’s RSI monoculture.

## 4. What the Author Got Right

The author correctly identified that win rate alone is insufficient — they included historical edge (expected return), which is rare and commendable. The attempt to tier conviction by sample size (e.g., KOTA’s n=12) shows awareness of statistical reliability, even if poorly applied.

## 5. Critical Recommendations

1. **Remove NICL, DEWA, and BUMI entirely** — they have negative historical edge. No amount of “confluence” justifies trading a strategy with -0.65% to -0.82% expected return. This is gambling, not trading.

2. **Reduce KAQI and WIFI positions to 3% each** — n=5 and n=10 are statistically invalid for claiming “high conviction.” Use Bonferroni correction: with 15 trades, p<0.003 needed for significance. Neither meets it. High conviction is unjustified.

3. **Add sector exposure cap: max 15% per sector** — currently 33% in energy/utilities. Rebalance by replacing PTRO, DEWA, BUMI with stocks from consumer, healthcare, or telecom. Also, require minimum 500k avg daily volume for all picks — exclude GOTO and MBMA.
