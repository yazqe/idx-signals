# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **WIFI**: ✓ clean  
- **BIPI**: ✓ clean  
- **BUVA**: ✓ clean  
- **KOTA**: ✓ clean  
- **TOBA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **VKTR**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **CUAN**: ✓ clean  
- **MBMA**: ✓ clean  
- **WBSA**: ✓ clean  

**SL placement**: All stop losses are set at a flat -6% to -8% below close. No reference to support levels, prior swing lows, ATR bands, or volume clusters. This is arbitrary percentage-based SL, not structure-based. In IDX, where retail-driven pumps often reverse violently, this SL is too tight for low-float stocks (e.g., MINA, WBSA) and too wide for high-volatility breakouts (e.g., TOBA).  

**TP placement**: All TPs are set at fixed +10% to +16% — no mention of prior resistance, Fibonacci extensions, or volume profile highs. For example, TOBA jumped 24% on breakout — yet TP is only +12%. This contradicts the stated “breakout momentum” rationale. TP should be at least 2x the move that triggered it.  

**Tier consistency**:  
- **WBSA (Untested)**: No historical edge, 0 past trades — yet TP/SL are defined with same precision as proven picks. Tier inflation: “Untested” should mean “no position” or “<1% allocation,” not same risk parameters.  
- **MBMA (Negative-but-confluence)**: Negative historical edge (-0.19%) yet given same TP/SL as others. Conviction tier is a lie — if history is negative, no confluence justifies trade.  
- **PTRO, MDKA, CUAN (Low conviction)**: All have >60% win rate but low edge. Conviction should be “Medium” — edge is the true measure of expectancy, not win rate. Tier deflation.  
- **BUVA**: 90% win rate over 10 trades — statistically insignificant sample. Yet labeled “High” conviction. Tier inflation.  

## 2. Contradiction Hunter

1. **“RSI oversold dominates the landscape — deep oversold conditions across 18 tickers signal broad exhaustion”** — yet 14 of 15 buys are triggered by RSI oversold. This is not “broad exhaustion,” it’s a single-signal monoculture. Contradiction: claiming diversification of signals while 93% of picks rely on identical trigger.  

2. **“Vol_breakout_up has best Sharpe ratio”** (BIPI, TOBA, MBMA) — yet TOBA’s volume spike is 18.2x avg with 24% move, and MBMA’s is 3.6x with -0.19% edge. If vol_breakout_up has “best Sharpe,” why is TOBA only Medium conviction and MBMA Negative? Contradiction: high Sharpe signal assigned low/no conviction while low-edge RSI gets High.  

3. **“Avoid negative-tier stocks without multi-strategy confluence”** — yet MBMA is the *only* negative-tier stock with dual triggers (RSI + vol_breakout_up) and is still included. Contradiction: the avoidance rule is violated by the only stock it was meant to protect against.  

4. **“Low-tier and untested picks show strong RSI confluence, suggesting retail-driven bounce”** — yet PTRO (3000–3100) and MDKA (2200–2280) are high-priced large caps. Contradiction: “retail-driven bounce” cannot apply to stocks trading at 2,200–3,100 IDR with high liquidity. Retail doesn’t move these.  

## 3. Hidden Risks

- **Sector concentration**: 13 of 15 picks are RSI oversold — all are likely in the same market regime (retail-driven mean-reversion). No sector diversification. If IDX retail sentiment flips (e.g., due to BI rate hike or foreign outflow), all 15 could drop 10–15% simultaneously. Single-day VaR >20% for portfolio.  
- **Liquidity risk**: PTRO (3000–3100) and MDKA (2200–2280) are large caps but have low daily volume relative to position size implied by 5–20d hold. If 10% position = 100k shares, and avg volume is 50k/day, slippage on exit could be 3–5%.  
- **Correlation**: All RSI oversold picks are likely correlated via retail FOMO behavior. BUVA, KOTA, BRMS, RAJA, VKTR — all under 500 IDR — are micro-cap retail magnets. They move together. Not diversification — cluster risk.  
- **Timing**: TOBA jumped 24% on breakout. If this analysis is published after that move, TP at +12% is chasing. High risk of gap-down at next open if volume dries up.  
- **Stale data**: “Historical edge” claims (e.g., 9.3% over 10 trades) — no training window provided. If data is from 2021–2022 (pre-inflation surge), regime shift in IDX liquidity (post-2023 retail boom) invalidates past edge.  
- **Indicator overlap**: RSI oversold, DA8, Markov — all are momentum-reversion indicators. RSI and DA8 are mathematically derived from same price series. False confluence. “Clean technical setup” is just RSI with a fancy name.

## 4. What the Author Got Right

The recognition that TOBA’s 24% volume-driven move warrants a breakout strategy — even if poorly executed — shows awareness that momentum can override mean-reversion models. That insight, though underdeveloped, is the only non-trivial observation in the analysis.

## 5. Critical Recommendations

1. **Remove all RSI oversold picks with <10 trades in history** — BUVA (10 trades), WBSA (0 trades), PTRO (11 trades). Their “high conviction” is statistical fraud. Replace with 3 stocks with >30 trades and >5% edge.  
2. **Replace flat % SL with ATR-based SL (2x ATR)** — especially for MINA, GTSI, VKTR. Flat 8% SL is too tight for low-float stocks (gap risk) and too loose for volatile breakouts (TOBA).  
3. **Cap total RSI oversold exposure at 40% of portfolio** — current 13/15 picks = 87% exposure. Sector and signal concentration will cause catastrophic drawdown if retail sentiment reverses. Reallocate to vol_breakout_up or fundamental catalysts with actual data.
