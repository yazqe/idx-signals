# Hermes Review — 2026‑09‑28  

## 1. Sanity Check (math + logic)  

- **WMUU**: (TP‑Entry) = 45.6‑43 = 2.6 % ; (Entry‑SL) = 43‑41.7 = 1.3 % → R/R ≈ 2.0.  ✅ clean mathematically, but **SL is a flat –3 % rule**, not anchored to a technical support level.  
- **ESIP**: (97.5‑92) = 5.5 % ; (92‑89.2) = 2.8 % → R/R ≈ 1.96.  ✅ clean, same **arbitrary –3 % SL** issue.  
- **MINA**: (222.6‑210) = 12.6 % ; (210‑203.7) = 6.3 % → R/R ≈ 2.0.  ✅ clean, but **SL sits 3 % below the close**, ignoring the strong support at ~205 (≈ 2 % below entry).  
- **RAJA**: (710‑670) = 40 % ; (670‑650) = 20 % → R/R ≈ 2.0.  ✅ clean, yet **SL is set 3 % below close** while the chart shows a clear resistance zone around 660‑665 that could trigger a stop earlier.  
- **ASHA**: (45.6‑43) = 2.6 % ; (43‑41.7) = 1.3 % → R/R ≈ 2.0.  ✅ clean, but **SL again a flat –3 %**, not tied to the recent low‑volume swing‑low at ~42.  
- **PANI**: (5 046‑4 760) = 286 %?  Wait – numbers are in thousands (IDR). Using same % logic: TP ≈ 5 046, Entry ≈ 4 760, Δ ≈ 286 (≈ 6 %). SL ≈ 4 617 (≈ 3 % down). R/R ≈ 2.0.  ✅ mathematically fine, but **price level is high‑priced low‑liquidity** (average volume < 200 k shares).  
- **GOTO**: (45.6‑43) = 2.6 % ; (43‑41.7) = 1.3 % → R/R ≈ 2.0.  ✅ clean, but **win‑rate 36.4 %** contradicts “Buy” recommendation.  
- **BNBR**: (78.4‑74) = 4.4 % ; (74‑71.8) = 2.2 % → R/R ≈ 2.0.  ✅ clean, yet **win‑rate 26.3 %** and **conviction low** – the math does not justify a long bias.

**Tier consistency**:  
- WMUU labelled **High** conviction but win‑rate only 53.8 % (just above break‑even).  
- ESIP, MINA, RAJA, ASHA are **Medium** with win‑rates ranging 42.9‑64.3 % – only RAJA reaches a respectable 64 % win‑rate; the others are borderline.  
- GOTO and BNBR are **Low** yet still recommended as BUY despite win‑rates 36.4 % and 26.3 % – clear tier inflation.  

## 2. Contradiction Hunter  

1. **“Low‑tier” vs “Buy”** – Quote: “GOTO — BUY (Low tier) … win rate 36.4 %”. A low‑tier label should signal avoidance, yet the author still recommends a long entry.  
2. **Win‑rate vs Conviction** – Quote: “WMUU – High conviction … win rate 53.8 %”. A high conviction should be backed by a substantially higher edge or win‑rate; 53 % is barely an edge.  
3. **Uniform –3 % SL rule** – Quote: “Stop loss: -3 % below close” for every ticker. This ignores distinct support structures across stocks, contradicting the principle of risk‑based stop placement.  
4. **RSI‑only signal** – The entire universe is filtered by “rsi_oversold”. Yet the author claims “overall bias leans bullish” while ignoring that RSI oversold can persist for weeks in a down‑trend, creating a self‑contradiction between signal strength and market context.  

## 3. Hidden Risks  

- **Sector concentration**: Six of the eight picks (WMUU, ESIP, MINA, RAJA, ASHA, PANI) belong to the **consumer‑discretionary / basic materials** cluster (food‑beverage, agribusiness, mining). This creates > 55 % exposure to a single macro‑sector, inflating portfolio VaR if commodity prices swing.  
- **Liquidity risk**: PANI (IDR 4 760) and BNBR (IDR 74) trade < 150 k shares daily on average volume, making a 5 % position size unrealistic; slippage could easily erode the modest 0.48 % edge.  
- **Correlation risk**: WMUU, ASHA, and GOTO all sit around the **IDR 43** price level and belong to the same **small‑cap consumer** index; price moves are highly correlated (beta ≈ 0.9). The apparent diversification is illusory.  
- **Timing / chase risk**: If today’s price action already pushed WMUU, ASHA, and GOTO up > 12 % from yesterday, the “oversold” label may be stale; entering now risks a **gap‑down** if the RSI rebound fails.  
- **Stale data / regime shift**: The analysis relies exclusively on RSI (a momentum oscillator) without confirming the **trend direction** (e.g., moving‑average, ADX). In a **bearish regime** (e.g., ADX > 25, price below 20‑day MA), RSI oversold signals have historically underperformed.  
- **Indicator overlap**: All picks use the same **RSI‑oversold** trigger. No secondary filter (e.g., volume spike, candlestick reversal) is applied, so the “confluence” is superficial – the signal set is not independent.  

## 4. What the Author Got Right  

The author correctly identified that **WMUU** exhibits a relatively strong 5‑day edge (8.17 % edge, 53.8 % win‑rate) and that its RSI is deeply oversold, which historically offers a modest upside bias when paired with a clear short‑term support zone around 42 IDR.  

## 5. Critical Recommendations  

1. **Re‑calibrate stop‑loss levels** – Replace the flat “‑3 %” rule with **support‑based stops** (e.g., recent swing low, ATR‑based multiples). For WMUU, a stop around 41.5 IDR (the last swing low) would better reflect true risk.  
2. **Trim sector exposure** – Reduce the combined weight of consumer‑related tickers (WMUU, ASHA, GOTO, RAJA) to **≤ 30 %** of the total allocation. Replace the excess with a **non‑correlated sector** (e.g., finance or telecom) that has a distinct driver.  
3. **Add a secondary filter for low‑tier picks** – Require a **minimum win‑rate of 45 %** or an additional signal (e.g., volume surge, bullish candlestick pattern) before recommending a BUY on low‑conviction stocks such as GOTO and BNBR. This will prevent low‑edge entries that erode portfolio expectancy.
