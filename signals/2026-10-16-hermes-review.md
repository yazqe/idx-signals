# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **TINS**: ✓ clean  
- **WIFI**: ✓ clean  
- **WMUU**: ✓ clean  
- **KAQI**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **BREN**: ✓ clean  
- **RAJA**: ✓ clean  
- **VKTR**: ✓ clean  
- **GJTL**: ✓ clean  
- **ENRG**: ✓ clean  
- **INKP**: ✓ clean  
- **PTRO**: ✓ clean  
- **ESSA**: ✓ clean  

**SL placement**: All stop losses are set at a flat 6–8% below entry — *arbitrary*, not anchored to technical structure (e.g., prior swing low, volume cluster, or ATR-based buffer). This ignores volatility context: TINS at 3500 (15% daily ATR?) vs. INKP at 7000 (likely <2% daily ATR) — same SL % = wildly different risk profiles.  

**TP placement**: All TPs are fixed % targets with *no reference to resistance levels, prior highs, or volume zones*. For example, TINS TP at +15% — but no mention of resistance at 4100 or 4200. This is a mechanical target, not a price-action-based exit.  

**Tier consistency**:  
- **KAQI**: Conviction = High, but only 5 trades in sample — *tier inflation*. Win rate 60% with n=5 is statistically noise.  
- **ENRG/INKP/ESSA**: Conviction = Low, but win rates 44–46% with n=18 — *tier deflation*. These have larger samples than KAQI or KOTA.  
- **BRMS**: Win rate 71.4% with n=14 — higher than TINS (88.9% but n=9) — yet conviction is *Medium*, while TINS is *High*. Inconsistent weighting.  
- **BREN**: n=21, win rate 66.7% — highest sample size in medium tier — yet conviction is only Medium. Under-rated.  

## 2. Contradiction Hunter

1. **“No multi-strategy confluence observed — all signals are RSI-only”** vs. **“Strong historical edge and win rate”** — If RSI is the *only* signal, then “historical edge” is just backtested RSI oversold performance. This is not a “strategy” — it’s a single-indicator rule. Claiming “historical edge” implies systematic edge beyond randomness, but with no filter (volume, trend, sector, volatility), this is data mining. Contradiction: You can’t claim “strong edge” if you admit no confluence.  

2. **“Prioritize high-conviction RSI plays with low volatility and high win rates”** vs. **TINS, WIFI, WMUU all have >15% TP targets** — These are *high-volatility* targets. Low-volatility stocks (like KOTA) have 12% TP. Contradiction: You can’t prioritize “low volatility” while targeting 15%+ moves — those are inherently high-volatility outcomes.  

3. **“Volume action is muted except for INKP and PTRO”** vs. **INKP and PTRO have “high liquidity” and “institutional buyers stepping in”** — If volume is *muted overall*, how can INKP/PTRO show “institutional accumulation”? Institutional activity requires *significant* volume. Contradiction: “Muted volume” cannot coexist with “institutional accumulation” without evidence of volume spike relative to avg.  

4. **Conviction tiers assigned based on “win rate” and “historical edge”** — but **ENRG** has 13 trades, 46.2% win rate, 1.89% edge → Low conviction. **BREN** has 21 trades, 66.7% win rate, 3.33% edge → Medium conviction. Yet **KAQI** has 5 trades, 60% win rate, 7.96% edge → High conviction. Contradiction: Higher edge + higher win rate + smaller sample = higher conviction? That’s the opposite of statistical rigor.  

## 3. Hidden Risks

- **Sector concentration**: All 15 stocks are small/mid-cap Indonesian equities with no sector breakdown provided. But RSI oversold signals are *systemic* — if this is a broad market pullback, *all* picks are exposed to the same macro risk. If mining or banking stocks dominate the sample (common in IDX), a sector-wide reversal could trigger 10+ SLs simultaneously. No diversification — just 15 RSI trades in the same regime.  
- **Liquidity risk**: KAQI (entry 65–70) has avg daily volume likely <500k shares. If position size is 15% of portfolio, and you’re buying 100k shares, you’re 20%+ of daily volume — slippage will crush your entry. Same for WMUU (21–23) — low float, thin bids.  
- **Correlation**: All picks are triggered by RSI oversold — meaning they’re all reacting to the *same* market-wide sentiment shock. These are not diversified — they’re 15 copies of the same trade. True diversification requires uncorrelated triggers (e.g., earnings, news, macro).  
- **Timing**: RSI oversold signals are *intraday* events. If these stocks already rallied >15% today (common in IDX small caps on oversold bounce), you’re buying the *top* of the bounce. Gap-down risk at next open is high — especially for low-volume names like WMUU or KAQI.  
- **Stale data**: “Historical edge” implies backtesting — but no training window is stated. If the data includes pre-2022 (when IDX was less liquid, more manipulated), or excludes recent 2024 FOMC-driven volatility, the “edge” is obsolete. RSI oversold worked in 2020 — not in 2024 with algorithmic trading.  
- **Indicator overlap**: All signals are RSI-only. No SMC, no DA8, no Markov — yet the Market Read mentions “SMC + DA8 + Markov” as if they’re used. Contradiction: The analysis uses *only* RSI. Claiming “confluence” is false.  

## 4. What the Author Got Right

The author correctly identified that RSI oversold has *statistical persistence* in IDX small caps — and the win rates (50–89%) are not random. The sample sizes, while small for some, are sufficient to suggest non-random behavior in this specific market context.

## 5. Critical Recommendations

1. **Reduce KAQI position from 15% to 5%** because its 5-trade sample is statistically insignificant — using it as a high-conviction anchor creates dangerous overexposure to noise.  
2. **Replace flat 8% SL with ATR-based SL (e.g., 1.5x 14-day ATR)** — TINS needs ~12% SL, INKP needs ~3% SL. Flat % SL misprices risk and will either stop you out too early or let you bleed.  
3. **Add sector exposure cap (max 20% per sector)** and disclose sector breakdown — if 8 of these 15 are mining or bank stocks, you’re not diversified — you’re betting on one macro bet 15 times.
