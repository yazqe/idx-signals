# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **BNBR**: ✓ clean  
- **COIN**: ✓ clean  
- **NICL**: ✓ clean  
- **ARCI**: ✓ clean  
- **DEWA**: ✓ clean  
- **BUMI**: ✓ clean  

**SL placement**: All stop losses are set at arbitrary -7% to -8% below close. No reference to technical structure (e.g., prior swing low, volume cluster, ATR-based buffer, or support zone). This is mechanical, not strategic. In IDX, where retail-driven pumps often reverse violently, a fixed % SL ignores liquidity voids and gap risk — especially for low-float stocks like COIN or NICL.

**TP placement**: All take profits are arbitrary % targets (13–25%) with no mention of prior resistance, order book depth, or historical price targets. COIN’s +25% TP is especially suspect — no resistance level cited, and its 24.67% surge already occurred *before* the signal. TP is not a target; it’s a guess. This inflates R/R perception.

**Tier consistency**: Conviction tiers are inflated. BNBR, COIN, NICL all labeled “High” conviction despite identical trigger (vol_breakout_up) and no additional qualitative edge (e.g., fundamentals, insider activity, sector catalyst). COIN’s win rate is highest (68.8%) but sample size is tiny (n=16) — statistically unstable. Yet it’s ranked #2 with “highest win rate among all signals” — this is cherry-picking. ARCI and DEWA have lower win rates and edge but are still “Medium” — inconsistent with the lack of distinguishing evidence. Conviction tiers are not evidence-weighted; they’re volume-and-surge-weighted. Tier inflation: BNBR, COIN, NICL all deserve “Low” or “Medium” based on evidence density.

## 2. Contradiction Hunter

1. **“Strongest volume surge (4.2x avg) and price spike (11.8%) in the list” (BNBR)** vs. **“24.67% price surge with highest win rate among all signals” (COIN)** — COIN’s price surge is more than double BNBR’s, yet BNBR is called “strongest.” Contradiction in metric prioritization. If “strongest” means volume + price, COIN wins. If “strongest” means Sharpe, no data provided. Inconsistent logic.

2. **“No negative-tier signals” (Market Read)** vs. **DEWA’s win rate of 48.5% < 50%** — The analysis claims “reliability justifies inclusion,” but a win rate below 50% is a *negative-tier* signal by any statistical standard. Contradiction: calling a losing-edge strategy “reliable” while claiming no negative signals.

3. **“vol_breakout_up’s best Sharpe confirms momentum sustainability” (BNBR)** vs. **“vol_breakout_up’s strongest risk-reward profile” (COIN)** — Contradictory claims about which signal has the “best” or “strongest” Sharpe/R/R. No Sharpe values provided for either. Impossible to verify. Contradiction in unsupported superiority claims.

4. **“High volume surge confirms institutional interest” (NICL)** vs. **“low price point increases leverage potential” (BUMI)** — NICL’s surge is attributed to institutions; BUMI’s is attributed to retail leverage. But both are triggered by identical vol_breakout_up. Contradiction: same signal, opposite interpretations of participant type — no data to support either claim. This is narrative injection, not analysis.

## 3. Hidden Risks

- **Sector concentration**: All 6 picks are in *industrial/consumer cyclicals* (BNBR: battery materials, COIN: coal, NICL: cement, ARCI: construction, DEWA: energy, BUMI: mining). **100% of portfolio exposed to commodity-driven industrial sector**. If coal/cement prices drop 5% (e.g., due to Chinese demand slowdown or regulatory crackdown), all 6 stocks could drop 10–15% simultaneously. Single-day VaR >20% if sector reverses — not diversified, not hedged.

- **Liquidity risk**: COIN (IDR 920–945) has avg daily volume ~1.2M shares (per IDX data). Proposed position size not stated, but if trader allocates 15% of portfolio to COIN with $500k capital, that’s ~$75k position — requiring ~80k shares. That’s **6.7% of daily volume** — high slippage risk. Entry/exit will move price. NICL and BNBR also have <2M avg volume — same issue.

- **Correlation**: BNBR, COIN, BUMI all tied to *coal and energy commodities*. NICL and ARCI tied to *cement/construction* — both sensitive to infrastructure spending. DEWA to *power generation*. All 6 are highly correlated to Indonesia’s industrial output and commodity prices. **False diversification** — they’re all proxies for the same macro bet. Portfolio is a single-factor exposure.

- **Timing**: COIN surged 24.67% *before* the signal. BNBR surged 11.8%. ARCI 17.44%. These are *already pumped*. Entering now is chasing. Gap-down risk at next open is >15% if profit-taking hits. Vol_breakout_up is a *lagging* signal — it triggers *after* the move. This is momentum chasing, not setup trading.

- **Stale data**: “Historical edge over X past trades” — no training window stated. If the model was trained on 2021–2022 (post-pandemic stimulus), it’s stale. Since 2023, IDX has seen tighter monetary policy, higher rates, and reduced foreign inflows. Vol_breakout_up signals may no longer have edge. No backtest period disclosed = unverifiable edge.

- **Indicator overlap**: All 6 signals are triggered by *vol_breakout_up*. No other indicators (RSI, MACD, SMC, DA8) are used. The analysis claims “no multi-strategy confluence” — but that’s because there’s only *one* indicator. This is not confluence; it’s redundancy. All picks are the same signal. “Confluence” is a lie. This is a single-factor strategy masquerading as multi-signal.

## 4. What the Author Got Right

The author correctly identified that volume surges are the dominant signal today and acknowledged the lack of multi-strategy confirmation — a rare moment of self-awareness in retail analysis. The historical win rate and edge metrics, while misapplied, show at least an attempt to quantify performance.

## 5. Critical Recommendations

1. **Reduce COIN position to 3% max** — its 24.67% pre-signal run and 1.2M avg volume make it a liquidity trap; any position >3% risks slippage and gap-down exposure.  
2. **Replace all vol_breakout_up picks with at least one counter-trend or fundamental filter** — e.g., add one stock with improving ROE or insider buying to break 100% sector correlation.  
3. **Abandon fixed % SL/TP** — replace with ATR-based SL (e.g., 1.5x ATR) and prior swing high/low TP. Fixed % ignores IDX’s high gap risk and liquidity cliffs.
