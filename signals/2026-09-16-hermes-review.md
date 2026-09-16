# Hermes Review — 2026‑09‑16  

## 1. Sanity Check (math + logic)

- **KRYA**:  
  - R/R not stated. Assuming “close” ≈ entry (≈ 71), SL = –3 % → 0.97 × 71 ≈ 68.9, TP = +6 % → 1.06 × 71 ≈ 75.3.  (TP‑Entry)/(Entry‑SL) ≈ 6 %/3 % = 2.0. No explicit R/R disclosed → **missing R/R**.  
  - SL is a *percentage* below close, not anchored to a technical level (support, trend‑line, ATR). Appears arbitrary.  
  - TP is a flat %‑up target, not tied to any identified resistance (previous swing high, Fibonacci, etc.). → **unjustified TP**.  
  - Conviction ★5 vs win‑rate 37.5 % (low) → **tier inflation**.

- **RODA**:  
  - Using the same logic, R/R ≈ 5 %/3 % ≈ 1.67. No R/R figure supplied → **missing R/R**.  
  - SL again a flat –3 % below close, with no structural support (e.g., recent swing low, EMA, ATR‑based). → **arbitrary SL**.  
  - TP (+5 %) not linked to a concrete resistance zone. → **unjustified TP**.  
  - Conviction ★3 (Medium) while edge is only 3.69 % over 50 trades; acceptable but still thin evidence for “solid” breakout claim.

- **IMPC**:  
  - R/R = 8 %/4 % = 2.0 (if entry ≈ close). No R/R disclosed → **missing R/R**.  
  - SL = –4 % below close, again without reference to a price structure (e.g., 20‑day low, Bollinger lower band). → **arbitrary SL**.  
  - TP (+8 %) not anchored to a resistance level; the golden‑cross alone does not justify a fixed % target. → **unjustified TP**.  
  - Conviction ★1 (Low) matches the weak edge (0.93 %) and tiny sample (5 trades), but the analysis still promotes it as a “classic bullish signal” – a **soft‑sell** tone mismatch.

**Summary**: All three picks lack explicit R/R calculations, use percentage‑based SL/TP without structural justification, and KRYA’s ★5 conviction is not supported by its modest win‑rate.  

---

## 2. Contradiction Hunter

1. **KRYA – “High” conviction vs. 37.5 % win‑rate**  
   > *Quote*: “Conviction: High” – “Historical edge: 12.34 % over 32 past trades (win rate 37.5 %)”  
   > *Why contradictory*: A win‑rate below 40 % is typical of a losing system; labeling it “high” conflicts with the underlying performance metric.

2. **RODA – “solid” volume breakout claim vs. modest edge**  
   > *Quote*: “A solid 2.1× volume breakout and 3.17 % price rise, backed by a decent win‑rate.”  
   > *Why contradictory*: “Solid” suggests strong conviction, yet the edge is only 3.69 % and the win‑rate barely exceeds 50 %, which is marginal for a breakout‑focused strategy.

3. **IMPC – “classic bullish signal” vs. “Low” conviction**  
   > *Quote*: “The 20‑SMA crossed above the 50‑SMA, a classic bullish signal, albeit with modest edge.”  
   > *Why contradictory*: The golden‑cross is presented as a classic bullish trigger, but the author simultaneously downgrades conviction to “Low,” creating mixed messaging about the signal’s reliability.

---

## 3. Hidden Risks

- **Sector concentration**: KRYA, RODA, and IMPC are all industrial‑type equities (construction‑equipment, heavy‑machinery, and metal‑processing). Concentrating three of the top‑5 picks in the same sector inflates sector‑specific VaR; a sudden policy shift or commodity price swing could knock all three simultaneously.  

- **Liquidity risk**:  
  - *IMPC* trades on the IDX with an average daily volume often below 200 k shares (≈ IDR 0.5 bn). Position sizing at a 5‑% portfolio weight would be ill‑iquid and could cause slippage.  
  - *KRYA* and *RODA* have higher volumes but still sit near the lower‑tier of the IDX liquidity spectrum; a 3‑% stop‑loss could be triggered by normal intraday noise.  

- **Correlation**: All three picks are selected purely on volume breakout criteria, which are highly correlated with overall market momentum. Their price moves are likely to be driven by the same macro‑level risk factor, reducing true diversification.  

- **Timing / chase risk**: The analysis does not state the intraday price change. If any of the stocks have already rallied > 15 % today (common for breakout alerts), the entry zone (±0.5) may already be behind the market, turning the trade into a chase with limited upside and heightened gap‑down risk at the next open.  

- **Stale data / regime shift**: The “historical edge” is computed over the last 32, 50, and 5 trades respectively, but there is no mention of the time window (e.g., last 6 months vs. last 2 years). If the bulk of those trades occurred in a different market regime (high volatility, different macro backdrop), the edge may be overstated.  

- **Indicator overlap**: The three signals (vol_breakout_up, vol_breakout_up, ma_golden_cross) are not independent. Volume breakouts often coincide with short‑term bullish moving‑average crossovers, meaning the “multiple‑signal” narrative is weak – the same underlying price surge is being counted twice.  

---

## 4. What the Author Got Right

The author correctly identified that recent volume spikes (3.5×, 2.1×, and a clear SMA crossover) are statistically rare events on the IDX and can provide a measurable edge when back‑tested, which is a solid foundation for a short‑term breakout strategy.  

---

## 5. Critical Recommendations

1. **Add explicit R/R calculations** – publish the exact (TP‑Entry)/(Entry‑SL) ratio for each pick; if the ratio falls below 1.5, either tighten the SL or widen the TP to meet a minimum risk‑reward threshold.  

2. **Anchor SL/TP to price structure** – replace the flat “‑3 % below close” / “+6 % above close” rules with concrete technical levels (e.g., prior swing low, ATR‑based stop, prior resistance, or Fibonacci extension). This prevents arbitrary stop placement and improves risk consistency.  

3. **Re‑scale conviction tiers** – downgrade KRYA to ★3 (or lower) given its 37.5 % win‑rate, and either remove or heavily qualify the “solid” language for RODA. For IMPC, either provide a stronger justification for inclusion (e.g., additional confluence) or drop it until a larger sample size justifies a low‑conviction entry.  

*Optional follow‑up*: Conduct a liquidity screen (average daily volume > 500 k shares) before finalizing position sizes, and limit sector exposure to ≤ 30 % of the total shortlist to avoid sector‑specific tail risk.
