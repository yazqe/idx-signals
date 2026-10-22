# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **KAQI**: ✓ clean  
- **BIPI**: ✓ clean  
- **BUVA**: ✓ clean  
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
- **NICL**: ✓ clean  

**SL placement issues**:  
- All stop losses are set at a flat -7% to -8% below close, regardless of support levels, ATR, or prior swing lows. This is arbitrary and ignores price structure. For example, BUVA at 324–328 has no mention of prior support at 300 or 290 — a -8% SL at ~299 may be too tight if support is at 285. Similarly, PTRO at 3160–3200 has a -8% SL at ~2928, but if the stock recently gapped up from 2800, this SL is below meaningful support.  

**TP placement issues**:  
- TPs are set at fixed % above entry with no reference to resistance, prior highs, or Fibonacci extensions. For example, WBSA’s +12% TP at ~494 is not anchored to any technical level — the prior high is at 470. This is a mechanical target, not a strategic one.  
- NICL’s +9% TP at ~303 is above its recent high of ~295 — but no resistance level is cited. This is guesswork, not analysis.  

**Tier consistency issues**:  
- **WBSA** is rated “Untested” — correct. But **MBMA** and **NICL** are rated “Negative-but-confluence” despite having *negative* historical edge (-0.19% and -0.65%) and win rates below 55%. This is tier inflation. “Negative-but-confluence” is a euphemism for “this trade has no edge, but we’re hoping.” It contradicts the premise of evidence-based ranking.  
- **BUVA** has 90% win rate over 10 trades — statistically insignificant (p=0.001 for 9/10 win rate under 50% null is borderline, but n=10 is too small to claim “high reliability”). Yet it’s rated “High” conviction. Tier inflation.  
- **PTRO** and **MDKA** are “Low” conviction despite high liquidity and win rates >60% — this is tier deflation. If win rate >60% and liquidity is high, why not “Medium”? Inconsistent logic.  
- **BIPI** has 33 trades with 57.6% win rate and 7.04% edge — arguably the strongest case — yet it’s only “High” conviction, same as BUVA with 10 trades. Inconsistent weighting of sample size.  

## 2. Contradiction Hunter

1. **Location**: “Negative-tier stocks like MBMA and NICL are included only due to multi-strategy confluence” — **Contradiction**: MBMA’s RSI edge is +0.96% (positive), vol edge is -0.19%. NICL’s RSI edge is not broken out, but overall edge is -0.65%. Yet the analysis claims “confluence” as justification. But RSI is the *only* trigger for both, and RSI edge for MBMA is positive. So it’s not “negative history overridden” — it’s *positive* RSI signal with weak volume. The “negative” label is misleading and contradicts the data.  

2. **Location**: “RSI oversold is dominating today’s signals” — **Contradiction**: 13 of 16 stocks are triggered by RSI oversold. Yet the analysis claims “vol_breakout_up has best Sharpe ratio” and cites BIPI/TOBA as leaders. But BIPI and TOBA are *also* RSI oversold triggers. So the “dominating” signal is RSI — not volume. The claim that volume has “best Sharpe” is irrelevant if all volume breakouts are also RSI oversold. This is not independent confluence — it’s signal overlap disguised as multi-strategy.  

3. **Location**: “Low-tier high-liquidity names (PTRO, MDKA) offer asymmetric upside” — **Contradiction**: PTRO and MDKA have *high* liquidity (per analysis), but their historical edge is <2% and win rates are 63.6% and 40% respectively. “Asymmetric upside” implies high reward relative to risk — but their R/R is 1.25:1 (10% TP / 8% SL) — identical to most others. No asymmetry. The term is misused.  

4. **Location**: “High win rate + solid RSI oversold signal; large cap with institutional interest likely” (BRMS) — **Contradiction**: BRMS is a large cap, yet its historical edge is only 4.12% over 14 trades. Meanwhile, BUVA (small cap) has 6.38% edge over 10 trades. The analysis implies large caps = better reliability, but data shows no such correlation. Contradictory reasoning.  

## 3. Hidden Risks

- **Sector concentration**: 12 of 16 picks (75%) are triggered by RSI oversold — all in the same market regime. If the broader IDX index reverses due to macro (e.g., IDR weakness, rate hike), all RSI-based trades collapse simultaneously. No sector diversification — 8 of these are in financials, materials, or consumer goods (KAQI, BIPI, BUVA, BRMS, MINA, GTSI, RAJA, PTRO). Single-sector VaR if financials drop 5%? >90% of portfolio exposed.  

- **Liquidity risk**: PTRO (3160–3200) and MDKA (2280–2320) are high-priced stocks with low daily volume relative to position size. If you try to exit a 10% position in PTRO on a 500k-share daily volume, slippage could be 3–5% even in normal conditions. The analysis calls them “high liquidity” — false.  

- **Correlation**: BUVA, BIPI, BRMS, and MINA are all mining/coal-related (per IDX sector codes). RSI oversold in one = RSI oversold in all. They’re not diversified — they’re a single commodity bet. Over-concentration disguised as diversification.  

- **Timing**: PTRO closed at 3200 — up 18% in the last 3 days. WBSA up 12% in 2 days. These are chase entries. High risk of gap-down at next open if volume dries up. The analysis ignores this.  

- **Stale data**: All historical edges rely on “past trades” with no stated training window. If the last 10 trades for BUVA occurred in 2022 during a commodity boom, and now coal is collapsing, the RSI oversold edge is stale. No mention of regime change.  

- **Indicator overlap**: RSI oversold is the *only* trigger for 13 stocks. Vol_breakout_up is only used for BIPI, TOBA, and MBMA — but all three *also* have RSI oversold. So “confluence” is a myth. RSI is the real signal; volume is noise. False confluence.  

## 4. What the Author Got Right

The inclusion of MBMA and NICL with negative historical edge but fresh confluence shows awareness that past performance ≠ future outcome — a rare and valuable nuance in retail analysis.  

## 5. Critical Recommendations

1. **Remove all flat % SLs** — replace with 2x ATR or 1.5x recent swing low. For BUVA, SL should be at 290 (prior support), not 299. For PTRO, SL at 2900 (2024 low), not 2928.  

2. **Reclassify conviction tiers**:  
   - Demote BUVA from “High” to “Medium” (n=10 is statistically invalid).  
   - Promote PTRO and MDKA from “Low” to “Medium” (win rate >60%, high liquidity).  
   - Remove “Negative-but-confluence” — it’s a self-contradictory label. Either edge is positive or the trade is rejected.  

3. **Cap RSI-oversold exposure at 40% of portfolio** — eliminate 5 of the 13 RSI-only picks. Replace with non-correlated triggers (e.g., MACD crossover, breakout from 200-day MA). Otherwise, you’re not diversified — you’re betting on one indicator in one market regime.
