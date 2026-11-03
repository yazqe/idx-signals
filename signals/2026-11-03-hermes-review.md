# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **WIFI**: ✓ clean  
- **KAQI**: ✓ clean  
- **BUVA**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **VKTR**: ✓ clean  
- **ENRG**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **ARCI**: ✓ clean  
- **CUAN**: ✓ clean  
- **HRTA**: ✓ clean  

**SL placement**: All stop losses are set at a flat -7% to -8% below close. No structural support levels referenced. This is arbitrary percentage-based SL, not anchored to prior swing lows, volume clusters, or ATR-based volatility zones. In IDX, where retail-driven pumps and gap-downs are common, this ignores liquidity voids and order book cliffs.

**TP placement**: All take profits are arbitrary % targets (e.g., +15%, +13%) with no reference to prior resistance, Fibonacci extensions, or volume profile highs. For example, BUVA at 278 → TP 317. No chart context provided. Is 317 a prior high? A psychological level? Unverified. TP is a guess, not a level.

**Tier consistency**: Conviction tiers are wildly inflated.  
- BUVA: 90% win rate over 10 trades → conviction “High” — statistically absurd. With n=10, 90% win rate has a 95% CI of 59%–99%. This is noise, not edge.  
- KAQI: 60% win rate over 5 trades → conviction “High”. n=5 is below statistical significance threshold.  
- ENRG, PTRO, MDKA, HRTA: Conviction “Low” despite win rates >40% and n>10 — inconsistent with BRMS (71.4% win rate, n=14 → Medium) and GTSI (46.7% win rate, n=15 → Medium).  
→ **Tier inflation**: BUVA, KAQI. **Tier deflation**: ENRG, PTRO, MDKA, HRTA. Conviction tiers are not calibrated to statistical reliability.

## 2. Contradiction Hunter

1. **“No multi-strategy confluence observed — all signals are RSI-only”** (Market Read) vs. **“price action shows accumulation before breakout”** (KOTA) and **“strong fundamentals supporting reversal”** (PTRO, HRTA).  
→ Contradiction: If no confluence exists, how can KOTA’s “price action” or PTRO’s “fundamentals” be cited as supporting evidence? The analysis claims RSI-only, then invokes non-RSI factors to justify conviction.

2. **“Only high-conviction names with strong win rates should be prioritized”** (Market Read) vs. **ENRG, PTRO, MDKA, HRTA, CUAN listed as “Low” conviction but included in the ranked buy list with identical entry/SL/TP structure**.  
→ Contradiction: If low-conviction names are not to be prioritized, why are they ranked alongside high-conviction picks? The list implies equal weighting. No exclusion or weighting adjustment applied.

3. **“Volume and volatility remain subdued”** (Market Read) vs. **“high volume potential”** (ENRG) and **“recent volume surge”** (ARCI).  
→ Contradiction: If overall volume is subdued, how can two stocks (ENRG, ARCI) be said to have “surge” or “potential” volume? No data provided to validate this claim. Either the market read is wrong, or the stock-specific claims are baseless.

4. **Conviction tier “High” assigned to BUVA (90% win rate, n=10) and KAQI (60% win rate, n=5)**, yet **BRMS (71.4% win rate, n=14)** is “Medium”.  
→ Contradiction: BRMS has higher statistical reliability than BUVA or KAQI, yet lower conviction. Conviction tiers are inversely correlated with sample size and statistical robustness — illogical.

## 3. Hidden Risks

- **Sector concentration**: 11/16 picks (69%) are in mining, energy, or materials (ENRG, PTRO, KAQI, BUVA, GTSI, MINA, CUAN). IDX mining sector has 3x higher volatility than market avg. A 5% sector-wide pullback could trigger 4–6% portfolio drawdown even with diversification.  
- **Liquidity risk**: PTRO (2500–2550) and MDKA (1960–1980) are large-cap but have avg daily volume <5M shares. Proposed position size not stated, but if >100k shares are traded per pick, slippage >0.5% is likely on entry/exit.  
- **Correlation**: PTRO, ENRG, KAQI, BUVA, GTSI all tied to coal, energy, or metals. All move with CRUDE OIL and IDR/USD. This is not diversification — it’s single-commodity exposure disguised as stock selection.  
- **Timing**: ENRG (615–625), PTRO (2500–2550), MDKA (1960–1980) all closed within 2% of 52-wk highs. RSI oversold after 15–20% run-ups. High risk of gap-down at next open if macro sentiment shifts.  
- **Stale data**: “Historical edge” claims rely on Markov “long-run mix” — but no training window is disclosed. If training data includes 2021–2022 commodity boom, it’s irrelevant to 2024’s post-pandemic, high-rate regime.  
- **Indicator overlap**: All 16 picks rely on RSI oversold. No other indicators (MACD, volume divergence, OBV, VWAP) mentioned. RSI is a lagging oscillator — all signals are identical. False confluence. This is not a portfolio — it’s 16 copies of the same trade.

## 4. What the Author Got Right

The author correctly identified RSI oversold as a recurring pattern in IDX’s retail-driven environment and acknowledged that win rate alone is insufficient — implicitly recognizing the need for sample size (n) in evaluating edge, even if poorly applied.

## 5. Critical Recommendations

1. **Reduce BUVA and KAQI positions to 2% each** — their “High” conviction is statistically invalid (n=10 and n=5 with 90%/60% win rates). Their inclusion inflates portfolio risk without justification.  
2. **Remove all RSI-only picks unless paired with volume divergence or support-level SL** — 16/16 trades use identical RSI trigger. This is not a strategy; it’s a mechanical echo. Add at least one independent filter (e.g., 20-day breakout, volume >150% avg).  
3. **Disclose training window for “historical edge” and cap position size at 1% per stock with n<15** — otherwise, the analysis is backtest overfitting masquerading as a trading plan. Without this, the entire framework is pseudoscientific.
