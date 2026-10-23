# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **BUVA**: ✓ clean  
- **MINA**: ✓ clean  
- **VKTR**: ✓ clean  
- **WMUU**: ✓ clean  
- **TOBA**: ✓ clean  
- **RAJA**: ✓ clean  
- **BRMS**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **KAQI**: ✓ clean  
- **CUAN**: ✓ clean  
- **GOTO**: ✓ clean  
- **NICL**: R/R math error — (275 - 270) / (270 - 253.5) = 5 / 16.5 ≈ 0.303, but stated R/R is 1:1.2 (implied 0.83). Actual R/R is 0.3:1, not “high-reward.”  
- **IMPC**: R/R math error — (872.5 - 872.5) / (872.5 - 816) = 0 / 56.5 = 0. Stated R/R is 1:1.3. Zero reward.  
- **INET**: R/R math error — (191.5 - 191.5) / (191.5 - 178.5) = 0 / 13 = 0. Stated R/R is 1:1.4. Zero reward.  
- **NICL, IMPC, INET**: SL placement arbitrary — all set at -5% below close with no reference to support, prior swing low, or volume cluster. Pure percentage-based, not structural.  
- **WMUU**: TP at +20% is unjustified — no resistance level cited, no prior price target, no technical confluence. Pure reward fantasy.  
- **BRMS**: Conviction inflated — 14 trades with 71.4% win rate sounds strong, but edge is only 4.12%. Win rate ≠ edge. High win rate with low edge suggests small gains, high frequency — not “Medium” conviction. Should be Low.  
- **PTRO**: Conviction deflated — 63.6% win rate, large cap, low edge. Yet conviction is “Low.” This is a textbook high-probability, low-reward setup — conviction should be Medium.  
- **KAQI**: Conviction deflated — 58.8% win rate, volume >2x avg, edge 1.21%. Win rate >50% with volume confirmation is not “Low.” Should be Medium.  
- **NICL, IMPC, INET**: Conviction “Negative-but-confluence” is incoherent — if edge is negative, it’s a losing strategy. “Confluence” doesn’t override negative edge. Tier is logically invalid.  
- **All vol_breakout picks**: SL at -7% to -8% — inconsistent with entry zones. WMUU at 35–37, SL at -8% = 32.2–34.2. But WMUU’s 52W low is 28.5. SL is below support. SL placement is not logical — it’s a fixed %, not structural.  
- **All RSI oversold picks**: TP set at +7% to +20% with no resistance levels cited. No prior swing highs, no Fibonacci, no volume profile. Arbitrary.  
- **All picks**: Historical edge calculated as average return per trade — but win rate is given. No mention of average win size vs. average loss size. Edge = (win rate × avg win) - (loss rate × avg loss). Without avg win/loss, edge is unverifiable. Edge claims are mathematically hollow.

## 2. Contradiction Hunter

1. **“Vol breakout signals dominate... best risk-reward”** (Market Read) vs. **KAQI, CUAN, GOTO, NICL, IMPC, INET** — all have negative or low edge despite being labeled “BUY.” Contradiction: If vol breakouts are “best risk-reward,” why are low/negative edge vol breakouts (KAQI) included? Why are negative-edge RSI plays included at all?  
2. **“RSI oversold plays show strong win rates but lower edge — best used as secondary entries”** (Market Read) vs. **BRMS, PTRO, MDKA, CUAN, GOTO, NICL, IMPC, INET** — all RSI plays are ranked as primary BUYs with no distinction between “primary” and “secondary.” Contradiction: The analysis treats all RSI plays as equal opportunities, directly contradicting its own stated hierarchy.  
3. **“Negative-tier signals are included only where RSI is deeply oversold and volume supports reversal”** vs. **INET** — RSI = 29.7 (not “deeply oversold,” typically <20), volume not quantified, edge = -3.13%. Contradiction: INET violates its own inclusion criteria — RSI not deep enough, edge negative, yet included as BUY.  
4. **Conviction ratings** — BUVA, MINA, VKTR, RAJA all have similar win rates (45–60%) and edge (6–8.7%), yet conviction is “High” for all. But KAQI (58.8% win rate, edge 1.21%) is “Low.” Contradiction: No consistent logic for conviction tier assignment. Same win rate, same volume, different conviction — arbitrary.  
5. **“Large cap liquidity” cited for TOBA** vs. **NICL, IMPC, INET** — all have similar or higher liquidity (market cap >$1B), yet NICL/IMPC/INET are labeled “Negative-but-confluence.” Contradiction: Liquidity is not a differentiator — yet used to justify TOBA while penalizing others with identical liquidity.

## 3. Hidden Risks

- **Sector concentration**: 7 of 15 picks (BUVA, MINA, VKTR, WMUU, TOBA, RAJA, KAQI) are in mining, energy, or materials. MINA (mining), BUVA (coal), VKTR (metals), KAQI (coal) — all commodity-linked. If coal/metal prices drop 5%, these 7 stocks could drop 8–15% in unison. Portfolio VaR for a 5% sector shock: ~12% portfolio loss if equally weighted.  
- **Liquidity risk**: WMUU (entry 35–37) — avg daily volume 1.2M shares. Proposed position size? Not stated, but if trader allocates 10% of portfolio ($1M = $100k position), that’s ~2,857 shares. 2.8k / 1.2M = 0.24% of daily volume — acceptable. But GOTO (entry 24–25) — avg daily volume 850k. If same $100k position, that’s 4,000 shares = 0.47% of volume — borderline. NICL (265–275) — avg volume 320k. $100k position = 370–380 shares = 0.12% — fine. But if trader overcommits (e.g., $200k in GOTO), liquidity risk spikes.  
- **Correlation**: MINA, BUVA, KAQI, VKTR all exposed to coal/metal prices. NICL and IMPC are both in energy infrastructure. GOTO and WMUU are both retail/e-commerce adjacent. Portfolio is not diversified — it’s 3 clusters: coal/mining (4), retail/e-commerce (2), RSI mean-reversion (6). Over-concentration masked as “diversification.”  
- **Timing**: MINA spiked 21% today. BUVA 22%. WMUU 33%. All are already >15% up today. High risk of gap-down at next open. No mention of pre-market volume or news catalyst. High probability of exhaustion.  
- **Stale data**: All “historical edge” claims rely on Markov “long-run mix” — but no training window is disclosed. If training data is from 2020–2022 (low volatility, low commodity prices), and current regime is post-pandemic inflation + commodity boom, the model is stale. Edge metrics are invalid.  
- **Indicator overlap**: All vol_breakout picks use “vol_breakout_up” — same trigger. All RSI oversold picks use “rsi_oversold” — same trigger. SMC, DA8, Markov not even mentioned in analysis. Claimed “confluence” is false — all signals are single-indicator. No true confluence. Just repetition.

## 4. What the Author Got Right

The author correctly identifies that high win rate does not equal high edge — and explicitly flags low-edge RSI plays as “secondary.” This nuanced understanding of expectancy over win rate is rare and valuable.

## 5. Critical Recommendations

1. **Remove NICL, IMPC, and INET entirely** — negative edge signals with arbitrary SL/TP and no structural support are gambling, not trading. Their inclusion invalidates the entire risk framework.  
2. **Reduce BUVA, MINA, VKTR, WMUU positions to 3% each (max 12% total)** — all spiked >20% today. High probability of mean reversion. Holding them as “High conviction” with 8% SL is reckless.  
3. **Recalculate all R/R ratios using actual support/resistance levels, not fixed %s** — SL must be below prior swing low or volume cluster. TP must align with prior resistance or 1.618 Fib extension. Otherwise, R/R is fiction.
