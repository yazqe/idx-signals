I need to analyze the provided signals and select the top 10-15 ideas based on the rules. However, the JSON list provided only contains RSI oversold signals — there are no signals for "ma_golden_cross" or "vol_breakout_up" in this data set. This means there is no multi-strategy confluence possible with the current data.

Let me proceed with the analysis based on the available data, following the selection rules:

1. **Strongly prefer multi-strategy confluence** — Not applicable here, as only RSI oversold signals are present.
2. **HIGH/MEDIUM tier get default consideration** — Only one medium tier: GTSI.
3. **LOW tier: include if confluence or strong recent volume action** — No volume data provided, but we can include low-tier with strong RSI (lower = stronger oversold) and decent win rate.
4. **UNTESTED: include if confluence** — No untested signals.
5. **NEGATIVE: include only if today's confluence is EXCEPTIONAL (3+ strategies)** — No confluence possible, so negative signals are excluded.
6. **vol_breakout_up has best Sharpe** — Not applicable, no such signals.

So we must select from:
- 1 medium: GTSI
- 5 low: INKP, CBDK, TPIA, INDY
- 6 negative: TOBA, BKSL, NICL, KIJA, EMTK, COIN — all excluded due to no confluence

We need 10-15 picks. We only have 6 total signals, 1 medium and 5 low. We’ll include all non-negative signals.

Let’s pick all 6 non-negative signals. We’ll rank them by RSI strength (lower = stronger oversold) and win rate.

### Selection:

1. **GTSI** — medium tier, RSI 27.6, win rate 46.7%, n=15
2. **KIJA** — negative, but RSI 19.7 (strongest oversold), win rate 42.9% — excluded per rule 5 (no confluence)
3. **INKP** — low, RSI 22.6, win rate 44.4%, n=18
4. **CBDK** — low, RSI 27.1, win rate61.5%, n=13  
5. **TPIA** — low, RSI 24.1, win rate 52.6%, n=19  
6. **INDY** — low, RSI 26.6, win rate 64.3%, n=14  

All negative signals excluded — no multi-strategy confluence present.  

## GTSI — BUY (5-20d hold)  
- **Triggered:** rsi_oversold  
- **Conviction:** Medium  
- **Historical edge:** 3.52% over 15 past trades (win rate 46.7%)  
- **Entry zone:** 152 ± 5  
- **Stop loss:** -7% below close  
- **Take profit:** +10% above close  
- **Why:** Strongest medium-tier RSI oversold with solid historical win rate and moderate sample size.  

## INKP — BUY (5-20d hold)  
- **Triggered:** rsi_oversold  
- **Conviction:** Low  
- **Historical edge:** 1.81% over 18 past trades (win rate 44.4%)  
- **Entry zone:** 7550 ± 200  
- **Stop loss:** -8% below close  
- **Take profit:** +12% above close  
- **Why:** Deepest RSI (22.6) among low-tier signals with above-average win rate and large n.  

## CBDK — BUY (5-20d hold)  
- **Triggered:** rsi_oversold  
- **Conviction:** Low  
- **Historical edge:** 1.55% over 13 past trades (win rate 61.5%)  
- **Entry zone:** 3870 ± 150  
- **Stop loss:** -7% below close  
- **Take profit:** +10% above close  
- **Why:** Highest win rate in the list despite low n — strong signal reliability.  

## TPIA — BUY (5-20d hold)  
- **Triggered:** rsi_oversold  
- **Conviction:** Low  
- **Historical edge:** 1.53% over 19 past trades (win rate 52.6%)  
- **Entry zone:** 1905 ± 75  
- **Stop loss:** -7% below close  
- **Take profit:** +10% above close  
- **Why:** Solid win rate and large sample size — RSI below 25 adds conviction.  

## INDY — BUY (5-20d hold)  
- **Triggered:** rsi_oversold  
- **Conviction:** Low  
- **Historical edge:** 1.21% over 14 past trades (win rate 64.3%)  
- **Entry zone:** 2250 ± 100  
- **Stop loss:** -7% below close  
- **Take profit:** +10% above close  
- **Why:** Best win rate in the entire list — RSI near 27 suggests exhaustion, not collapse.  

### Market Read  
RSI oversold signals are broadly present but lack confluence. No volume breakout or moving average confirmation observed. Market is in shallow corrective phase — no strong reversal signals yet. Avoid negative-tier stocks despite low RSI; no structural support visible.
