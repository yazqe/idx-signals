I need to analyze the provided signals and select the top 10-15 ideas based on the rules. Let me first extract and organize the data to identify multi-strategy confluences and prioritize based on conviction tier and vol_breakout_up weighting.

First, I'll scan for any tickers that appear with multiple strategies. Looking at the list, all signals are from rsi_oversold except one: ZATA with vol_breakout_up. There are no multi-strategy confluences in this dataset — every ticker has only one strategy triggered.

Now I'll rank the signals by:
1. Conviction tier (High > Medium > Low > Untested > Negative)
2. Historical edge (higher is better)
3. Win rate (higher is better)
4. Volume breakout (ZATA is the only one, and it has strong price action)

High tier: WIFI (edge: 9.3%, win: 70%)
Medium tier: BRMS (4.12%, 71.4%), GTSI (3.52%, 46.7%)
Low tier: INKP, ARCI, CBDK, TPIA, PANI, INDY, MBMA, SMDR, ZATA (vol breakout)
Negative: all others

ZATA is the only vol_breakout_up signal, and it has 7.41% price move and 2.8x volume — this qualifies as exceptional context even though it's low tier. It should be included.

I'll select:
- WIFI (high)
- BRMS (medium)
- GTSI (medium)
- INKP (low, high RSI, high n)
- CBDK (low, high win rate)
- TPIA (low, high n)
- PANI (low, high n)
- INDY (low, high win rate)
- ZATA (vol breakout, exceptional context)
- SMDR (low, decent n)
- MBMA (low, decent n)
- ARCI (low, decent n)

That's 12 picks. I'll include 3 more from negative tier with strongest confluence — but there's no multi-strategy confluence. So I'll skip negative unless 3+ strategies — none qualify. So 12 is fine.

Now I'll format each pick as requested.

## WIFI — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **- **Conviction:** High
- **Historical edge:** 9.3% over 10 past trades (win rate 70%)
- **Entry zone:** 1700 ± 50
- **Stop loss:** -8% below close
- **Take profit:** +15% above close
- **Why:** Strong RSI oversold with high historical edge and win rate, confirming mean-reversion reliability.

## BRMS — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Medium
- **Historical edge:** 4.12% over 14 past trades (win rate 71.4%)
- **Entry zone:** 525 ± 25
- **Stop loss:** -7% below close
- **Take profit:** +12% above close
- **Why:** Consistent medium-tier performer with high win rate and solid volume confirmation.

## GTSI — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Medium
- **Historical edge:** 3.52% over 15 past trades (win rate 46.7%)
- **Entry zone:** 116 ± 10
- **Stop loss:** -8% below close
- **Take profit:** +10% above close
- **Why:** Deep RSI oversold with above-average historical edge and stable win rate.

## INKP — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 1.81% over 18 past trades (win rate 44.4%)
- **Entry zone:** 7050 ± 200
- **Stop loss:** -7% below close
- **Take profit:** +11% above close
- **Why:** Strong RSI reading with high n-value, suggesting durability despite low tier.

## CBDK — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 1.55% over 13 past trades (win rate 61.5%)
- **Entry zone:** 3540 ± 150
- **Stop loss:** -7% below close
- **Take profit:** +10% above close
- **Why:** High win rate and moderate RSI oversold — best risk-reward among low-tier signals.

## TPIA — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 1.53% over 19 past trades (win rate 52.6%)
- **Entry zone:** 1375 ± 75
- **Stop loss:** -8% below close
- **Take profit:** +10% above close
- **Why:** High occurrence count and consistent positive edge, justifying inclusion.

## PANI — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 1.41% over 18 past trades (win rate 55.6%)
- **Entry zone:** 6525 ± 250
- **Stop loss:** -7% below close
- **Take profit:** +11% above close
- **Why:** Strong win rate and high n-value — low tier due to small edge, but reliable.

## INDY — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 1.21% over 14 past trades (win rate 64.3%)
- **Entry zone:** 1990 ± 100
- **Stop loss:** -7% below close
- **Take profit:** +10% above close
- **Why:** Highest win rate in low tier with solid n-value — excellent probability profile.

## ZATA — BUY (5-20d hold)
- **Triggered:** vol_breakout_up
- **Conviction:** Low
- **Historical edge:** 0.52% over 31 past trades (win rate 38.7%)
- **Entry zone:** 58 ± 3
- **Stop loss:** -6% below close
- **Take profit:** +14% above close
- **Why:** Exceptional volume breakout (2.8x avg) and 7.41% price surge — vol_breakout_up has best Sharpe ratio.

## SMDR — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 0.63% over 15 past trades (win rate 40%)
- **Entry zone:** 284 ± 15
- **Stop loss:** -8% below close
- **Take profit:** +9% above close
- **Why:** Decent n-value and clean RSI signal — low edge but low risk due to small price level.

## MBMA — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 0.96% over 21 past trades (win rate 52.4%)
- **Entry zone:** 426 ± 20
- **Stop loss:** -7% below close
- **Take profit:** +10% above close
- **Why:** High occurrence count and above-average win rate — low edge offset by high probability.

## ARCI — BUY (5-20d hold)
- **Triggered:** rsi_oversold
- **Conviction:** Low
- **Historical edge:** 1.64% over 9 past trades (win rate 44.4%)
- **Entry zone:** 1005 ± 50
- **Stop loss:** -7% below close
- **Take profit:** +11% above close
- **Why:** Solid RSI and moderate edge — small n-value but consistent directionality.

### Market Read
RSI oversold dominance suggests broad market exhaustion, not sector-specific weakness. ZATA’s volume breakout is the only true momentum signal — its inclusion is critical for capturing breakout momentum. Negative-tier signals show RSI is oversold but not predictive here — avoid them unless confluence emerges.
