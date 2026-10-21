# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **KAQI**: ✓ clean  
- **BUVA**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **VKTR**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **TPIA**: ✓ clean  
- **BREN**: ✓ clean  
- **WBSA**: ✓ clean  
- **TOBA**: ✓ clean  
- **HRTA**: ✓ clean  

**SL placement**: All stop losses are set at a flat -7% to -8% below close. No structural support (e.g., prior swing low, volume cluster, VWAP) is referenced. This is an arbitrary %-based SL — not anchored to price action or liquidity zones. High risk of premature exit in volatile markets or during gap-down opens.  

**TP placement**: All take profits are arbitrary % targets (+6% to +12%) with no reference to prior resistance, Fibonacci levels, or volume profile peaks. For example, BUVA’s TP at +10% is not aligned with any mentioned resistance — contradicts the claim of “clean technical setup.”  

**Tier consistency**:  
- **WBSA** (Untested) has 0 historical trades but is given a TP/SL and “strong signal confluence” — tier inflation. “Untested” should mean no trade recommendation.  
- **TOBA** has negative historical edge (-0.06%) but is still recommended as a “low-conviction contrarian play.” Conviction tier is misapplied — negative edge should trigger “avoid,” not “buy.”  
- **BREN** triggered by *vol_breakout_up* but its conviction is “Low” despite being labeled “strongest Sharpe ratio strategy” — tier deflation. High Sharpe + volume surge should warrant “High” conviction.  
- **MDKA** and **TPIA** have low conviction but large entry ranges (2180–2220, 1275–1295) — implies large position sizing potential without justification.  

## 2. Contradiction Hunter

1. **“Focus on high-win-rate RSI plays (BUVA, KAQI, KOTA)”** — yet BUVA has 90% win rate but only 6.38% edge, while TOBA has 53.3% win rate and *negative* edge. Contradiction: Win rate ≠ edge. Author promotes high win rate as proxy for profitability, but TOBA’s example proves high win rate can be unprofitable. This undermines the entire rationale for prioritizing BUVA/KOTA.  

2. **“Negative-tier tickers show RSI divergence but lack structural support — avoid unless confluence is extreme”** — yet TOBA is explicitly recommended as a “low-conviction contrarian play” with RSI at 23.7 and volume spike. Contradiction: TOBA is the *only* negative-tier stock listed, yet it’s the only one with explicit confluence (volume spike) and still gets a “BUY” recommendation. This violates the stated rule.  

3. **“Volume breakout in BREN adds momentum confirmation”** — BREN’s trigger is *vol_breakout_up*, yet its conviction is “Low.” Contradiction: The analysis calls it the “strongest Sharpe ratio strategy,” implying superior risk-adjusted return — yet assigns lowest conviction tier. Inconsistent logic: high Sharpe = high conviction.  

4. **“RSI oversold signals dominate today’s landscape”** — yet WBSA has 0 historical trades and is recommended with full TP/SL. Contradiction: If signals “dominate,” why is WBSA untested? If untested, why recommend it? The claim of dominance contradicts the absence of data for WBSA.  

## 3. Hidden Risks

- **Sector concentration**: 13 of 15 picks are triggered by RSI oversold — all are mean-reversion plays. No sector diversification disclosed. If mining/energy/banking stocks (common in IDX) are all oversold simultaneously due to macro shock (e.g., commodity sell-off), all 13 could collapse together. Single-day VaR could exceed 15% across portfolio.  
- **Liquidity risk**: MDKA (2180–2220) and TPIA (1275–1295) have high nominal prices. If avg daily volume is <500k shares, a 5% position could be 10–20% of daily volume — slippage risk >2%. No volume data provided.  
- **Correlation**: All picks rely on RSI oversold — a single macro event (e.g., Fed hawkishness, IDR depreciation) can trigger synchronized oversold conditions across sectors. These are not diversified — they’re a single strategy with 15 exposures. False diversification.  
- **Timing**: RSI oversold signals are often *lagging*. If any of these stocks (e.g., BUVA, KAQI) already rallied >15% today, the “oversold” signal is stale — entry is chasing, not catching. No timestamp on “close” or RSI reading.  
- **Stale data**: All historical edges are based on “past trades” with no training window disclosed. If the last 12 months included pandemic recovery or post-election volatility, the model is invalid in current regime (2024 rate hikes, IDR weakness).  
- **Indicator overlap**: RSI oversold is the *only* trigger for 14/15 picks. BREN is the only exception (vol breakout), but its analysis says “confluence with RSI oversold (implied).” All signals are RSI-based. False confluence — not independent factors.  

## 4. What the Author Got Right

The author correctly identifies that win rate ≠ edge — demonstrated by TOBA’s negative edge despite 53% win rate. This is a rare and valuable insight in retail trading analysis.

## 5. Critical Recommendations

1. **Remove WBSA entirely** — “Untested” means no historical edge. Recommending a trade with zero data is reckless, not “contrarian.” Delete it.  
2. **Reclassify TOBA as “Avoid”** — Negative historical edge + no structural support = no buy. The “contrarian” justification is a cognitive bias, not a risk model.  
3. **Replace all fixed % SL/TP with structural levels** — For KAQI, BUVA, KOTA: identify prior swing lows (e.g., 65, 310, 95) as SL. For TP, use 1.5x ATR or prior resistance. Arbitrary % exits destroy risk-reward integrity.
