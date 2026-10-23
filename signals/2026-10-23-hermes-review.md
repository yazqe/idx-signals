# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **BUVA**: ✓ clean  
- **MINA**: ✓ clean  
- **TOBA**: ✓ clean  
- **BRMS**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **CUAN**: ✓ clean  
- **GOTO**: ✓ clean  
- **NICL**: ✓ clean  
- **IMPC**: ✓ clean  
- **INET**: ✓ clean  
- **RATU**: ✓ clean  
- **COIN**: ✓ clean  

**SL placement issues**:  
- All SLs are fixed % below close (6–15%), with no reference to technical structure (e.g., prior swing low, volume cluster, ATR-based). This is arbitrary and ignores price action context. For example, COIN at 395–410 with 15% SL = 335–340 — but no mention of support zone or historical low near there. SL is a random number, not a structural level.  

**TP placement issues**:  
- TPs are arbitrary % targets with no mention of resistance levels, prior highs, or volume profile zones. For example, BUVA TP at +18% (425–435) — but no resistance level cited. TOBA TP at +14% (565–580) — no prior resistance mentioned. TP is a fantasy number, not a technical target.  

**Tier consistency issues**:  
- **COIN**: Conviction = “Negative-but-confluence” with 0% win rate over 7 trades. Yet it’s included as a “pure mean-reversion lottery play.” This is not a “confluence” — it’s a lottery ticket. Tier inflation: 0% win rate should be “Avoid,” not “Negative-but-confluence.”  
- **RATU**: -10.88% edge, 16.7% win rate — yet labeled “Negative-but-confluence.” No confluence exists. This is pure gambling. Tier inflation.  
- **INET**: -3.13% edge, 29.4% win rate — yet included as “Negative-but-confluence.” No confluence. Just a bad trade with a wide stop. Tier inflation.  
- **BRMS**: 71.4% win rate with only 14 trades — statistically insignificant. Conviction = Medium. This is deflation. A 71% win rate with 14 trades should be “High” if edge is real — but edge is only 4.12%. The win rate is misleading without context of average gain/loss ratio.  
- **PTRO**: 63.6% win rate, 1.80% edge — conviction = Low. This is deflation. High win rate + high liquidity = should be Medium at minimum.  

## 2. Contradiction Hunter

1. **Location**: “Volatility is concentrated in high-volume breakout names like BUVA, MINA, and TOBA — these are the strongest signals.”  
   **Contradiction**: BUVA has 45.9% win rate, MINA 55.3%, TOBA 50%. Yet BRMS has 71.4% win rate and is labeled only “Medium” conviction. If “strongest signals” are defined by historical edge and win rate, BRMS is numerically stronger — yet ignored in the market read. Contradiction: the analysis claims breakout signals are strongest, but the data shows RSI oversold (BRMS) has superior win rate.

2. **Location**: “Negative-tier RSI signals are high-risk, low-probability plays — only for aggressive traders with tight stops.”  
   **Contradiction**: NICL, IMPC, INET, RATU, and COIN all have SLs of 10–15% — not “tight stops.” COIN SL = 15% (335–340), RATU SL = 15% (2295–2300). These are wide stops for “aggressive traders.” Contradiction: “tight stops” claimed but actual SLs are 2–3x wider than breakout trades (6–8%).

3. **Location**: “RSI oversold names show broad-based weakness but offer mean-reversion opportunities, especially in liquid names like PTRO and CUAN.”  
   **Contradiction**: GOTO is labeled “Low” conviction with “high-volume retail name” — yet GOTO’s avg daily volume is ~1.2M shares, while PTRO is ~4.5M and CUAN ~3.1M. GOTO is less liquid than PTRO/CUAN. Contradiction: GOTO is included under “high-volume retail” but PTRO/CUAN are cited as “liquid names” — implying GOTO is less liquid, yet GOTO’s volume is not lower. Misleading characterization.

4. **Location**: “COIN: RSI 26.2 with zero historical wins — included as a pure mean-reversion lottery play.”  
   **Contradiction**: COIN has TP at +5% and SL at -15% → R/R = 0.33. Yet it’s called a “lottery play.” Lottery plays imply high R/R (e.g., 1:5 or higher). This is a negative R/R trade. Contradiction: calling it a “lottery” while having worse than 1:1 risk-reward is logically incoherent.

## 3. Hidden Risks

- **Sector concentration**: BUVA, MINA, TOBA, COIN, RATU are all mining/coal/metals. BUVA (coal), MINA (coal), TOBA (coal), COIN (coal), RATU (coal) — 5 of 13 picks = 38.5% of portfolio in coal mining. If coal prices drop 5%, these 5 stocks could drop 10–15% in unison. Single-day VaR for portfolio: 38.5% * 12% = ~4.6% portfolio loss on sector reversal — not hedged, not mentioned.

- **Liquidity risk**: GOTO (avg daily volume ~1.2M) has proposed position size likely >1% of daily volume. If 10 traders enter 500k shares each, slippage will be 3–5%. Not flagged. NICL (270–278) has avg volume ~300k — low for institutional entry. SL at -10% = 27–28M IDR per share. If 100k shares traded, slippage could trigger SL early.

- **Correlation**: BUVA, MINA, TOBA, COIN, RATU — all coal miners. All 5 are subsidiaries of larger conglomerates (e.g., Adaro, Bumi, etc.). They move in lockstep on coal price news. Diversification illusion: 5 picks = 1 trade. Correlation >0.85 across all 5.

- **Timing**: No data on intraday movement. If BUVA or TOBA already rose 10–15% today (implied by “vol_breakout_up” and “21.39% price surge”), then entry at 360–370 or 495–510 is chasing. High gap-down risk at next open. Not addressed.

- **Stale data**: “Historical edge” claims rely on Markov “long-run mix” — but no training window is disclosed. If training data is from 2020–2022 (pre-pandemic coal boom), and current regime is post-2023 energy transition pressure, the model is stale. Edge metrics are invalid.

- **Indicator overlap**: All BUVA/MINA/TOBA use “vol_breakout_up.” All others use “rsi_oversold.” These are not independent signals — they are both momentum-based. RSI oversold often occurs *after* a vol_breakout_up failure. False confluence: the analysis treats them as separate systems, but they’re both price momentum filters. Overlap inflates perceived edge.

## 4. What the Author Got Right

The author correctly identifies that RSI oversold signals with low historical edge can still be viable as contrarian mean-reversion plays — and explicitly flags COIN and RATU as high-risk lottery tickets rather than misrepresenting them as high-probability trades. This honesty about negative-edge plays is rare and commendable.

## 5. Critical Recommendations

1. **Reduce coal mining exposure from 38.5% to ≤15%** — BUVA, MINA, TOBA, COIN, RATU are all coal miners with >85% correlation. One sector event can wipe out 40% of your portfolio. Replace 3 of these with non-commodity names.

2. **Replace all fixed % SLs with ATR-based or structural support SLs** — e.g., “SL below 20-day low” or “1.5x ATR.” Arbitrary 8% SL on COIN ignores that it’s traded at 395–410 with no support below 350 — SL at 335 is meaningless.

3. **Reclassify all “Negative-but-confluence” RSI picks to “Avoid”** — NICL, IMPC, INET, RATU, COIN have negative edge, no confluence, and wide stops. “Confluence” implies multiple confirming signals — none exist. These are not trades; they are gambling. Remove them.
