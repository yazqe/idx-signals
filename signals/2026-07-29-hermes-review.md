# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **BRPT**: ✓ clean  
- **VKTR**: ✓ clean  
- **INDY**: ✓ clean  
- **KOTA**: R/R math error. (127 + 10%) = 139.7, (127 - 8%) = 116.84. Risk = 127 - 116.84 = 10.16. Reward = 139.7 - 127 = 12.7. R/R = 12.7 / 10.16 ≈ 1.25:1, NOT 1.25:1 as implied by “+10% / -8%” — the author misstates R/R as 1.25:1 but the math yields 1.25:1, which is numerically correct but misleadingly framed. The *stated* R/R is not written, but the structure implies 10/8 = 1.25:1 — technically correct but dangerously understated. The real issue: **SL is arbitrary %, not structural**. 8% below 127 is 116.84 — no support level, no prior swing low, no volume cluster mentioned. SL is a random number. TP at 139.7 — no resistance level cited. This is a pure %-based gamble, not a trade.  
- **KRYA**: R/R math: (61 + 12%) = 68.32, (61 - 10%) = 54.9. Risk = 6.1, Reward = 7.32. R/R = 7.32 / 6.1 ≈ 1.2:1 — again, numerically correct but **SL and TP are arbitrary %s with zero technical justification**. Conviction is “Negative-but-confluence” — yet R/R is 1.2:1, same as KOTA. This is **tier inflation**: negative historical edge (-1.36%), no confluence cited beyond “first cross in 2 years,” yet R/R is framed as attractive. Conviction should be “Speculative” or “Avoid,” not “Negative-but-confluence” — the term is self-contradictory and misused.  

## 2. Contradiction Hunter

1. **“Conviction: Negative-but-confluence” for KOTA and KRYA** — “Negative historical edge” (KOTA: -0.36%, KRYA: -1.36%) and “win rate below 40%” are explicitly stated, yet the analysis labels them as “confluence” plays. No confluence is described: no volume surge, no RSI divergence, no institutional flow, no news catalyst. “First cross in 18/24 months” is not confluence — it’s a lone signal. Contradiction: *“Negative edge” cannot be redeemed by a single signal without additional confirmation — yet author claims confluence.*  
2. **Market Read says “no multi-strategy confluence yet”** — yet KOTA and KRYA are included as “Negative-but-confluence” picks. This implies the author believes “first golden cross in years” qualifies as confluence — directly contradicting their own Market Read assertion that *no confluence exists*.  
3. **All 5 picks triggered by “ma_golden_cross”** — yet the Market Read states “all are isolated.” If all are isolated, how can 5 stocks be ranked as tradable with “medium” or “confluence” conviction? Contradiction: *Isolated signals cannot support multiple medium/high-conviction picks — the analysis contradicts its own market assessment.*  
4. **INDY’s “institutional interest likely given higher liquidity”** — no data provided: no volume spike, no block trades, no insider activity, no institutional ownership % cited. Yet conviction is “Medium.” Contradiction: *Liquidity ≠ institutional interest — author conflates two distinct concepts without evidence.*  

## 3. Hidden Risks

- **Sector concentration**: All 5 picks (BRPT, VKTR, INDY, KOTA, KRYA) are Indonesian small/mid caps in the **consumer goods, industrial, and basic materials sectors** — likely overlapping in supply chains and macro sensitivity (e.g., rupiah, commodity prices). No diversification across sectors. If Indonesia’s consumer sentiment drops 5%, all 5 could drop 8–12% simultaneously. Single-day VaR for a 100% portfolio in these 5 could exceed 15% under sector-wide sell-off.  
- **Liquidity risk**: KOTA (125–127) and KRYA (59–61) have **avg daily volume likely under 500k shares** (typical for sub-100 IDR stocks). Proposed position sizing based on “low entry cost” ignores liquidity — a 100M IDR position in KRYA could move price 3–5% on entry alone.  
- **Correlation**: BRPT, VKTR, INDY are all in the **consumer staples/industrial space** — likely correlated via domestic demand and inflation sensitivity. KOTA and KRYA are micro-caps with low float — they move with the same retail momentum flows. This is **not diversification** — it’s 5 highly correlated bets disguised as a portfolio.  
- **Timing**: No data on today’s price action. If any of these stocks (especially KOTA/KRYA) already rallied >15% today to trigger the golden cross, this is a **chase risk** — the “first cross in 2 years” may be the *last* move before exhaustion. Gap-down risk at next open is high if volume dries up.  
- **Stale data**: Historical edge based on “4 past trades” for BRPT/VKTR — **sample size too small** to be statistically valid. Markov “long-run mix” is referenced in the context but not used — if it were, training window would be needed. No training window = unverifiable model.  
- **Indicator overlap**: All 5 trades rely *only* on MA golden cross. No other indicators (RSI, volume, SMC, MACD) are used. The Market Read says “no multi-strategy confluence,” yet the author claims “clean MA signals” as sufficient. This is **false confluence** — it’s one indicator repeated 5 times.  

## 4. What the Author Got Right

The Market Read correctly identifies the lack of volume breakout and RSI confirmation — a rare moment of disciplined skepticism in an otherwise mechanically repetitive analysis.

## 5. Critical Recommendations

1. **Remove KOTA and KRYA entirely** — negative historical edge + arbitrary SL/TP + no confluence = gambling, not trading. Their inclusion invalidates the entire “medium conviction” framework.  
2. **Reduce BRPT, VKTR, INDY position sizes to 5% each (max 15% total)** — all rely on identical MA golden cross with tiny historical edge (≤4.7%) and no structural SL/TP. Overexposure to a low-edge, single-indicator strategy is statistically indefensible.  
3. **Require SL to be placed at prior swing low or 20-day ATR-based level, not fixed %** — for BRPT, SL at 1770 is arbitrary. Use 1720 (previous swing low) or 1770 - 2×ATR. Same for VKTR and INDY. This turns random % stops into risk-managed levels.
