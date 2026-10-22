# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **KAQI**: ✓ clean  
- **BUVA**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **TOBA**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **CUAN**: ✓ clean  
- **WBSA**: ✓ clean  
- **NICL**: ✓ clean  
- **HRTA**: ✓ clean  
- **GOTO**: ✓ clean  

**SL placement**: All stop losses are set at a flat 6–8% below entry — *arbitrary percentage*, not anchored to technical structure (e.g., prior swing low, volume cluster, or ATR-based buffer). This ignores price action context and increases risk of premature exit in volatile or gap-prone stocks like GOTO or WBSA.  

**TP placement**: All take profits are arbitrary % targets (8–12%) with *no reference to resistance levels, prior highs, or volume profile*. For example, GOTO at 26 → TP 28.08 is not justified by any chart structure — it’s a mechanical multiplier.  

**Tier consistency**:  
- **WBSA** (Untested conviction) — *correctly labeled*, rare and appropriate.  
- **NICL** (Negative-but-confluence) — *correctly labeled*, rare and appropriate.  
- **BUVA** (High conviction) — 90% win rate over 10 trades is statistically *unreliable* (n=10 is below threshold for statistical significance in trading). Conviction inflated.  
- **PTRO, MDKA, CUAN, HRTA, GOTO** (Low conviction) — All have win rates >50% and sample sizes >10, yet conviction is capped at Low. This is *deflation*. Historical edge and win rate are materially stronger than BRMS or MINA (which are Medium), yet their conviction is lower — inconsistent logic.  
- **TOBA** (Medium) — 34 trades, 50% win rate, best Sharpe — yet conviction is *only Medium* while BUVA (n=10, 90% win) is High. Inconsistent weighting of sample size vs. win rate.  

## 2. Contradiction Hunter

1. **“Despite negative historical returns for some tickers, today’s confluence... suggests a broad-based reversal is underway”** — contradicts **NICL’s own entry rationale**, which states: *“historical negative edge offset by...”* — implying NICL is an *exception*, not part of a “broad-based reversal.” Yet NICL is included in the same buy list as 14 others. This implies the author believes *all* RSI oversold signals are valid today — directly contradicting their own admission that NICL’s edge is negative.  

2. **“RSI oversold signals dominate today’s landscape... especially in mid- to low-cap names”** — contradicts **PTRO and MDKA** being labeled “Low conviction” despite being *large-cap* stocks with “institutional-grade liquidity.” If the thesis is “mid- to low-cap reversal,” why include large-caps with low conviction? The rationale for PTRO/MDKA explicitly cites *liquidity as a reason to buy*, which contradicts the stated market thesis that favors *low-cap* reversal.  

3. **“TOBA’s volume breakout adds critical momentum confirmation”** — contradicts **TOBA’s own entry logic**, which says: *“vol_breakout_up has best Sharpe ratio — high probability reversal setup.”* But TOBA’s TP is +11%, SL is -6% → R/R = 1.83. Yet the analysis claims “best Sharpe” without showing Sharpe calculation or comparing to other picks. If TOBA has the “best Sharpe,” why is its conviction only Medium? Why is BUVA (R/R=1.25) High conviction? Inconsistent risk-adjusted performance logic.  

4. **GOTO’s rationale**: *“Potential for short squeeze if retail interest re-emerges”* — contradicts **GOTO’s SL at -7%**. Short squeezes are *explosive, gap-up events* — a 7% SL is far too tight for a short squeeze play. If retail interest re-emerges, GOTO could gap +15% in one session — SL would be meaningless. The SL placement contradicts the stated catalyst.  

## 3. Hidden Risks

- **Sector concentration**: 12 of 15 picks (80%) are in *mining, metals, energy, or materials* (KAQI, BUVA, KOTA, MINA, PTRO, TOBA, GTSI, RAJA, HRTA, GOTO, CUAN, MDKA). NICL (insurance) and WBSA (telecom) are outliers. If commodity prices reverse (e.g., coal, copper), this portfolio could lose 15–25% in one day. Single-sector VaR is dangerously high.  
- **Liquidity risk**: GOTO (IDR 24–26) has avg daily volume ~1.2M shares. Proposed position size? Unknown, but if trader allocates 5% of portfolio to GOTO with IDR 100M capital → ~2.5M shares traded. That’s >2x avg daily volume — *high slippage risk*. Same for WBSA (low float, no volume data provided).  
- **Correlation**: KAQI, BUVA, KOTA, MINA, PTRO, TOBA — all are *coal, mining, or energy* stocks under the same conglomerates (e.g., Adaro, Bumi Resources, etc.). They are highly correlated with coal prices and government policy. This is *not diversification* — it’s concentrated exposure to one macro theme disguised as a multi-stock portfolio.  
- **Timing**: GOTO, WBSA, NICL — all closed within 5% of their 52-week lows. RSI oversold is *not* a buy signal if price is in a *structural downtrend*. These are *falling knives*.  
- **Stale data**: All RSI oversold “historical edge” calculations — *no training window specified*. If the model was trained on 2020–2022 data (post-pandemic rally), it’s *stale* in 2024’s high-rate, commodity-supply-constrained environment. RSI oversold signals have failed consistently in 2023–2024 across IDX.  
- **Indicator overlap**: All 14 RSI-oversold picks use *identical trigger*. RSI is not an independent signal — it’s a lagging oscillator. “Confluence” is a lie. No true multi-indicator confluence exists. Markov, SMC, DA8 — *not mentioned in any pick’s rationale*. This is a single-indicator strategy masquerading as multi-factor.  

## 4. What the Author Got Right

WBSA’s “Untested” conviction and NICL’s “Negative-but-confluence” labels are rare, honest, and methodologically sound — demonstrating awareness that historical edge ≠ predictive validity.

## 5. Critical Recommendations

1. **Remove all 12 mining/energy stocks** — reduce sector exposure from 80% to <30%. Replace with 3 non-commodity stocks from tech, consumer, or infrastructure. This is not diversification — it’s gambling on one macro bet.  
2. **Replace all fixed % SL/TP with ATR-based stops and resistance-based targets** — e.g., SL at 1.5x ATR(14) below entry, TP at prior swing high. Arbitrary %s are dangerous in volatile small-caps like GOTO.  
3. **Recalibrate conviction tiers using statistical significance thresholds** — require n≥20 trades for “High,” n≥10 for “Medium,” and only “Low” if n<10. BUVA (n=10, 90% win) is statistically *unreliable* — downgrade to Medium. PTRO (n=11, 63.6% win) is *more reliable* than BRMS (n=14, 71.4%) — upgrade PTRO to Medium.
