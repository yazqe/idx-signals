# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **KAQI**: R/R = (12) / (8) = 1.5, but stated as “+12% / -8%” → R/R = 1.5, not stated. **MISSED CALCULATION** — author implies R/R but never states it. Also, SL at -8% arbitrary — no support level cited. Conviction 5⭐ for 60% win rate with 7.96% edge? Inflated. Win rate is mediocre, edge is low-mid. **Tier inflation**.
- **BUVA**: R/R = (10) / (7) ≈ 1.43. Not stated. SL -7% arbitrary. Win rate 90% over 10 trades? That’s 9 wins. But 90% win rate with 6.38% edge? If 9 wins avg +10%, 1 loss avg -7%, then expected return = (0.9 * 10) - (0.1 * 7) = 9 - 0.7 = 8.3%, not 6.38%. **MATH ERROR** — edge calculation inconsistent with win/loss structure. Conviction 5⭐ for 10-trade sample? **Tier inflation**.
- **KOTA**: R/R = 11/8 = 1.375. Not stated. SL -8% arbitrary. Win rate 58.3% over 12 trades — 7 wins, 5 losses. If TP=11%, SL=8%, expected return = (7/12)*11 - (5/12)*8 = 6.42 - 3.33 = 3.09%, but stated edge is 6.21%. **MATH ERROR**. Conviction 5⭐ for 12 trades? **Tier inflation**.
- **BRMS**: R/R = 9/7 ≈ 1.29. Not stated. SL -7% arbitrary. Win rate 71.4% over 14 trades → 10 wins, 4 losses. Expected return = (10/14)*9 - (4/14)*7 = 6.43 - 2.00 = 4.43% — close to stated 4.12%. **✓ clean**.
- **MINA**: R/R = 10/8 = 1.25. Not stated. SL -8% arbitrary. Win rate 50% → 6 wins, 6 losses. Expected return = (6/12)*10 - (6/12)*8 = 5 - 4 = 1%, but stated edge is 4.01%. **MATH ERROR**. Conviction Medium? Edge is below 5% with 50% win rate — should be Low. **Tier inflation**.
- **GTSI**: R/R = 8/8 = 1.0. Not stated. SL -8% arbitrary. Win rate 46.7% over 15 trades → ~7 wins, 8 losses. Expected return = (7/15)*8 - (8/15)*8 = 3.73 - 4.27 = -0.54% — but stated edge is +3.52%. **MATH ERROR**. Conviction Medium? Negative expected return? **Tier deflation**.
- **RAJA**: R/R = 9/7 ≈ 1.29. Not stated. SL -7% arbitrary. Win rate 64.3% over 14 trades → 9 wins, 5 losses. Expected return = (9/14)*9 - (5/14)*7 = 5.79 - 2.50 = 3.29% — close to stated 3.01%. **✓ clean**.
- **VKTR**: R/R = 8/8 = 1.0. Not stated. SL -8% arbitrary. Win rate 50% → 8 wins, 8 losses. Expected return = (8/16)*8 - (8/16)*8 = 0. But stated edge is 2.95%. **MATH ERROR**. Conviction Medium? Zero expected return. **Tier inflation**.
- **PTRO**: R/R = 10/7 ≈ 1.43. Not stated. SL -7% arbitrary. Win rate 63.6% over 11 trades → 7 wins, 4 losses. Expected return = (7/11)*10 - (4/11)*7 = 6.36 - 2.55 = 3.81% — but stated edge is 1.8%. **MATH ERROR**. Conviction Low? Edge is above 3% — should be Medium. **Tier deflation**.
- **MDKA**: R/R = 9/7 ≈ 1.29. Not stated. SL -7% arbitrary. Win rate 40% over 15 trades → 6 wins, 9 losses. Expected return = (6/15)*9 - (9/15)*7 = 3.6 - 4.2 = -0.6% — stated edge +1.72%. **MATH ERROR**. Conviction Low? Negative edge. **Tier deflation**.
- **BULL**: R/R = 8/8 = 1.0. Not stated. SL -8% arbitrary. Win rate 54.5% over 11 trades → 6 wins, 5 losses. Expected return = (6/11)*8 - (5/11)*8 = 4.36 - 3.64 = 0.72% — stated edge 1.23%. **MATH ERROR**. Conviction Low? Edge barely positive. **Tier deflation**.
- **CUAN**: R/R = 9/8 = 1.125. Not stated. SL -8% arbitrary. Win rate 57.1% over 21 trades → 12 wins, 9 losses. Expected return = (12/21)*9 - (9/21)*8 = 5.14 - 3.43 = 1.71% — stated edge 1.2%. **MATH ERROR**. Conviction Low? Edge >1.5% with 57% win rate — should be Medium. **Tier deflation**.
- **MBMA**: R/R = 8/8 = 1.0. Not stated. SL -8% arbitrary. Win rate 52.4% over 21 trades → 11 wins, 10 losses. Expected return = (11/21)*8 - (10/21)*8 = 4.20 - 3.81 = 0.39% — stated edge 0.96%. **MATH ERROR**. Conviction Low? Edge barely positive. **Tier deflation**.
- **WBSA**: R/R = 10/8 = 1.25. Not stated. SL -8% arbitrary. **No historical data** — conviction “Untested” is correct. **✓ clean**.
- **HRTA**: R/R = 9/7 ≈ 1.29. Not stated. SL -7% arbitrary. Win rate 54.5% over 11 trades → 6 wins, 5 losses. Expected return = (6/11)*9 - (5/11)*7 = 4.91 - 3.18 = 1.73% — stated edge 0.78%. **MATH ERROR**. Conviction Low? Edge >1.5% — should be Medium. **Tier deflation**.

## 2. Contradiction Hunter

1. **“High-conviction names like BUVA and KAQI show exceptional historical reliability”** — BUVA has 90% win rate over 10 trades, KAQI has 60% over 5 trades. But BUVA’s edge is 6.38% (calculated wrong), KAQI’s is 7.96%. Yet both are ranked as “High” conviction. Meanwhile, PTRO has 63.6% win rate over 11 trades and 1.8% edge — also called “High win rate” in its description — yet assigned Low conviction. **Contradiction**: Why is BUVA/KAQI “exceptional” but PTRO’s similar win rate is “Low”? Inconsistent criteria.

2. **“Focus on high-win-rate RSI plays with liquidity”** — yet WBSA has no historical data (0 trades), no win rate, no edge — yet it’s included as a BUY with full SL/TP. **Contradiction**: The market read says to avoid untested names unless multi-strategy confluence exists — but WBSA has no strategy beyond RSI. Inclusion violates stated rule.

3. **“RSI oversold signals are dominating today’s landscape, with 30+ tickers triggering”** — yet all 15 picks are RSI oversold. This implies the entire universe is oversold. But then the analysis assigns conviction tiers based on “historical edge” — which requires past trades. If RSI oversold is *universally* triggered today, then *all* these historical edges are invalid — they were calculated under different market regimes. **Contradiction**: Using historical RSI edge when the current regime is *unprecedentedly* oversold invalidates the premise of historical reliability.

4. **“Avoid negative-tier names unless they show multi-strategy confluence — none do here”** — yet all 15 picks are *only* RSI oversold. No volume filters, no candle patterns, no moving averages, no volume confirmation. Yet all are BUYs. **Contradiction**: The rule says “avoid unless multi-strategy” — but no pick has multi-strategy. So all should be avoided. Yet all are bought. **Systemic contradiction**.

## 3. Hidden Risks

- **Sector concentration**: 7 of 15 picks (KAQI, BUVA, KOTA, MINA, GTSI, BRMS, WBSA) are in mining, metals, or energy-related sectors (based on IDX ticker conventions). That’s 47% of portfolio exposed to commodity price swings. If coal or nickel prices drop 5%, these stocks could drop 10–15% in unison. Single-day VaR >12% for portfolio.
- **Liquidity risk**: PTRO (3050–3100) and MDKA (2200–2240) are high-priced stocks. Avg daily volume? Likely <500k shares. If position size is 15% of portfolio and entry is 3000, a 100k-share position = ~300B IDR. If avg volume is 200k, that’s 50% of daily volume — **liquidity squeeze risk** on entry/exit.
- **Correlation**: BUVA, KAQI, KOTA, MINA, GTSI — all are Indonesian mining/metal stocks. All move with global commodity prices and IDR volatility. Not diversified — **false diversification**. Portfolio is effectively a single bet on Indonesian mining.
- **Timing**: RSI oversold across 30+ stocks implies broad capitulation — but if this is *today’s* trigger, and stocks already dropped 15–20% in the last 2 days, then RSI oversold is lagging. **Chase risk**: Reversal may not occur — could be continuation of downtrend. High gap-down risk at next open.
- **Stale data**: Markov “long-run mix” mentioned in context? No. But RSI edge calculations assume stationarity. If recent regime shift occurred (e.g., post-election volatility, new mining tax), past RSI edge is meaningless. **Stale model**.
- **Indicator overlap**: All signals are RSI oversold. No other indicators. “SMC + DA8 + Markov” referenced in Hidden Risks section — but **none appear in the analysis**. This is a red herring. The only signal is RSI. **False confluence** — author claims multi-indicator system but uses only one.

## 4. What the Author Got Right

WBSA’s “Untested” conviction is the only honest call in the document — acknowledging lack of historical data is rare and commendable.

## 5. Critical Recommendations

1. **Remove all RSI-only picks except WBSA** — the entire analysis is built on a single, unvalidated indicator. Replace with at least one volume confirmation (e.g., OBV breakout) or price action (e.g., bullish engulfing) for every position. RSI alone is not a strategy — it’s noise.

2. **Reduce BUVA, KAQI, KOTA to 3% each, not 10–15%** — they’re highly correlated mining stocks with no sector diversification. Portfolio VaR spikes if commodity prices reverse. Sector exposure >40% is unacceptable for IDX.

3. **Recalculate all historical edges using actual P&L from past trades** — not assumed TP/SL. If you don’t have the actual trade data, don’t claim “historical edge.” Either remove all edge claims or provide trade logs. Otherwise, this is backtest fiction.
