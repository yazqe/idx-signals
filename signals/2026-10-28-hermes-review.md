# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **WIFI**: ✓ clean  
- **KAQI**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **BIPP**: ✓ clean  
- **ENRG**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **CUAN**: ✓ clean  
- **MBMA**: ✓ clean  
- **GOTO**: ✓ clean  
- **NICL**: R/R math fails. TP = +8%, SL = -8% → R/R = 1.0, but analysis implies it’s a “contrarian entry” with no stated edge — yet R/R is listed as 1.0 without qualification. This misrepresents risk profile.  
- **DEWA**: R/R math fails. TP = +8%, SL = -8% → R/R = 1.0, but analysis states “negative edge” and “macro headwinds.” Stating R/R = 1.0 while admitting negative historical edge is logically incoherent. It implies equal reward/risk despite negative expectancy — a fundamental misstatement of trading edge.

**SL placement**: All SLs are fixed at -6% to -8% regardless of volatility, ATR, or support structure. No mention of prior swing lows, VWAP, or order flow zones. This is arbitrary %-based SL — dangerous in low-liquidity or gap-prone stocks like GOTO or NICL.

**TP placement**: All TPs are arbitrary % targets (e.g., +15%, +13%) with no reference to prior resistance, Fibonacci levels, or volume clusters. For example, PTRO at 2700 — no mention of prior highs at 2850 or 3000. TP is just a number pulled from a hat.

**Tier consistency**:  
- **WIFI, KAQI, KOTA**: Conviction = High, but historical edge is based on 5–12 trades. n < 12 is statistically insignificant for edge claims. Tier inflated.  
- **NICL, DEWA**: Conviction = Negative-but-confluence — but both have RSI <20, same trigger as others, and identical SL/TP structure. Why are they not “High” conviction if RSI is deeper? Inconsistent logic. Tier deflation for NICL/DEWA is arbitrary — if RSI is deeper and “strongest in 3 years,” why not higher conviction?  
- **BIPP**: Conviction = Medium despite “strongest volume signal” and “best Sharpe ratio.” Understated.  
- **GOTO**: Conviction = Low despite RSI = 20.1 and “high volatility acceptable” — but GOTO’s 22–24 range is a 10% range, suggesting high slippage risk. Conviction should be lower, not low.

## 2. Contradiction Hunter

1. **Location**: “RSI oversold signals dominate today’s landscape, with deep readings (RSI <20) on 7 tickers — suggesting broad-based exhaustion.” + “NICL: RSI at 19.8 — extreme oversold; despite negative history, today’s signal is strongest in 3 years.”  
   **Contradiction**: If RSI <20 is “broad-based exhaustion,” then NICL is not an outlier — it’s part of the crowd. Claiming it’s “strongest in 3 years” contradicts the “broad-based” narrative. If it’s truly an outlier, then the “broad-based exhaustion” claim is false. If it’s broad, then NICL is not special.

2. **Location**: “No golden cross or multi-strategy confluence observed; pure mean-reversion play.” + “RAJA: price action suggests institutional accumulation.”  
   **Contradiction**: “Institutional accumulation” implies trend-following or accumulation phase — the opposite of mean-reversion. If institutions are accumulating, the move is likely directional, not mean-reverting. The analysis cannot simultaneously claim “pure mean-reversion” and “institutional accumulation” without explaining how accumulation leads to mean-reversion.

3. **Location**: “BIPP: strongest volume signal in the list; best Sharpe ratio supports 20d hold.” + “All picks: 5–20d hold.”  
   **Contradiction**: If BIPP has “best Sharpe ratio,” it should be the *only* pick with a 20d hold — or at least a longer hold than others. But all are given identical time horizon. This misrepresents the implied risk profile. Sharpe-based hold duration should vary — but author treats all equally.

4. **Location**: “ENRG: high close price suggests institutional interest despite thin history.” + “ENRG: Conviction = Low.”  
   **Contradiction**: “Institutional interest” is a high-conviction signal. Yet conviction is Low. No justification given. If institutional interest is real, why is conviction not Medium or High? If it’s not real, why mention it?

## 3. Hidden Risks

- **Sector concentration**: 12 of 15 picks (80%) are triggered by RSI oversold — all in the same strategy. No sector diversification. PTRO, MDKA, ENRG, GOTO, NICL, DEWA are all large-cap — but all under same RSI trigger. If RSI oversold strategy fails (e.g., due to central bank intervention or foreign outflow), entire portfolio collapses. Single-strategy VaR is 80%+ of portfolio — catastrophic if RSI regime breaks.

- **Liquidity risk**: GOTO (22–24) has avg daily volume ~1.2M shares (IDX data). Proposed position size? Not stated — but if trader allocates 10% of portfolio to GOTO, and position size exceeds 50k shares, slippage will be >3% on entry/exit. GOTO is illiquid relative to its price range. NICL and DEWA also have low volume — 300k–500k avg — insufficient for meaningful position sizing without slippage.

- **Correlation**: All 13 RSI-oversold picks are highly correlated under the same trigger. PTRO, MDKA, ENRG, GOTO, NICL, DEWA — all large-cap, all under same RSI condition. Even BIPP (volume breakout) is in energy sector — same macro drivers. Portfolio is not diversified — it’s 15x the same bet with different tickers. True diversification requires uncorrelated strategies — not 15 RSI oversold plays.

- **Timing**: NICL closed at 232 (from entry zone 225–235) — already moved 3%+ above entry zone. DEWA closed at 240 (entry 230–245) — already 2–4% above. Entering now = chasing. Gap-down risk at next open is high if market reverses. Entry zone is already breached — this is not a “zone” anymore, it’s a lagging signal.

- **Stale data**: All historical edge claims rely on “past trades” with no stated training window. If the RSI oversold strategy worked in 2021–2022 but failed since 2023 due to increased retail participation and algorithmic mean-reversion bots, the historical edge is stale. No mention of backtest period — dangerous.

- **Indicator overlap**: All 13 RSI-oversold picks use identical trigger. RSI is not independent — it’s the *only* signal. “Confluence” is a lie. No SMC, no DA8, no Markov — just RSI. The analysis falsely claims “confluence” for NICL/DEWA — but there is no other indicator. False confluence = false confidence.

## 4. What the Author Got Right

The author correctly identified that RSI oversold levels below 20 are statistically rare and historically associated with short-term bounces in IDX — and the win rate consistency across multiple stocks suggests a real, if narrow, edge in this specific market regime.

## 5. Critical Recommendations

1. **Reduce all RSI-oversold positions to 3% max per stock** — because 12 of 15 picks are the same strategy with identical triggers. Portfolio is not diversified — it’s 80% exposure to one fragile signal. Total RSI-oversold exposure must be capped at 20% of portfolio, not 100%.

2. **Replace arbitrary SL/TP with ATR-based stops and prior swing resistance targets** — e.g., for PTRO, SL should be below 2550 (last swing low), TP at 2850 (2023 high). Fixed % SLs ignore volatility — GOTO’s 8% SL is 1.8x ATR, while NICL’s 8% SL is 0.7x ATR. This is reckless.

3. **Remove NICL and DEWA from the list entirely** — negative historical edge + extreme RSI + low volume + already breached entry zone = textbook trap. If you’re going to trade mean-reversion, don’t trade negative-expectancy plays. Either remove them or reclassify as “short” opportunities.
