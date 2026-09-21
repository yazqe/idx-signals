# Hermes Review — 2026‑09‑21  

## 1. Sanity Check (math + logic)  

- **HUMI**: ✓ clean on arithmetic (TP ≈ +7 % vs SL ≈ ‑3 % → R/R ≈ 2.33).  
- **GTSI**: ✓ clean on arithmetic (same %‑based R/R).  
- **COIN**: ✓ clean on arithmetic (same %‑based R/R).  
- **PANI**: ✓ clean on arithmetic (TP ≈ +5 % vs SL ≈ ‑3 % → R/R ≈ 1.67).  

**Issues identified**  
- **SL placement** – All four stocks use a flat “‑3 % below close” stop regardless of each security’s volatility, support zones, or ATR. This is an arbitrary rule, not a logical structure level.  
- **TP placement** – Likewise, a uniform “+7 % (or +5 % for PANI) above close” target ignores actual resistance, prior swing highs, or Fibonacci levels. No justification is provided.  
- **Conviction vs evidence** – HUMI is labeled **High** conviction despite a **41.9 % win‑rate** (below breakeven) and a modest edge of 13.04 %. GTSI and COIN also carry high conviction but rely on the same blunt %‑based SL/TP, which does not reflect their individual risk‑reward profiles. Conversely, PANI is marked **Low** conviction while its win‑rate (55.6 %) exceeds the others and its edge, albeit small, is positive. This suggests tier inflation for the breakout picks and deflation for the RSI‑oversold pick.  

## 2. Contradiction Hunter  

1. **“High‑conviction ticker” vs. win‑rate** – HUMI’s description:  
   > “Volume 2.5× average and a 6.3 % price jump signal strong upward momentum for a **high‑conviction** ticker.”  
   Yet the win‑rate is **41.9 %**, contradicting the implied high confidence.  

2. **Uniform risk parameters across heterogeneous signals** – The author applies identical SL/TP rules to both **vol_breakout_up** (HUMI, GTSI, COIN) and **rsi_oversold** (PANI) despite the latter having a different risk profile (lower TP, same SL). This inconsistency conflicts with the stated “low conviction” for PANI.  

3. **Market read vs. portfolio construction** – The market read claims the list is “dominated by high‑conviction volume breakouts,” yet the inclusion of a low‑conviction RSI‑oversold trade (PANI) undermines the narrative of a uniformly bullish stance.  

## 3. Hidden Risks  

- **Sector concentration** – HUMI, GTSI, and COIN are all flagged on volume breakouts but belong to **high‑beta, low‑liquidity sectors** (e.g., mining‑related, tech‑small‑caps, and crypto‑adjacent). Concentrating three of the four picks in volatile, commodity‑linked segments inflates sector‑specific VaR.  

- **Liquidity risk** – No volume‑average or average daily turnover figures are supplied. If any of these tickers trade < 200 k shares/day, a 3 % stop could be breached by normal intraday noise, leading to slippage.  

- **Correlation / signal overlap** – All three breakout picks rely on the same **vol_breakout_up** signal (volume > 2× average). This is a single‑source indicator; the three trades are not independent signals but essentially the same trigger applied to different symbols, inflating the apparent diversification.  

- **Chase risk / timing** – Each breakout already exhibited a **≥ 6 % price jump** prior to the signal. Entering at the “entry zone” (±0.5 % around the current close) means buying after the bulk of the move, exposing the trader to immediate pull‑back risk.  

- **Stale historical edge** – The “historical edge” percentages are aggregated over **31, 37, and 16 past trades** without any weighting for recency. Market microstructure can shift quickly; older trades may no longer be predictive.  

- **Indicator redundancy** – The analysis treats **vol_breakout_up** and **rsi_oversold** as independent, yet both are essentially momentum‑type filters. No orthogonal confirmation (e.g., trend‑strength, macro backdrop) is presented, so the confluence is superficial.  

## 4. What the Author Got Right  

The author correctly identified that **sharp volume spikes coupled with sizable price jumps** often precede short‑term continuation moves, and they appropriately flagged the **RSI‑oversold** condition for PANI, which historically yields a modest positive edge despite a low conviction rating.  

## 5. Critical Recommendations  

1. **Redefine stop‑loss and take‑profit levels** – Replace the flat ‑3 % / +7 % (or +5 %) rules with **price‑level‑based stops** anchored to recent support zones (e.g., prior swing low, ATR‑based multiples) and **target zones** tied to identifiable resistance (e.g., prior high, Fibonacci extension).  

2. **Align conviction tiers with statistical evidence** – Re‑grade HUMI, GTSI, and COIN to **Medium** conviction given win‑rates below 50 % and modest edge, while PANI’s **Low** conviction should be upgraded to at least **Medium** given its >55 % win‑rate and positive edge.  

3. **Limit exposure to the breakout‑heavy sector** – Cap the aggregate **sector exposure** (e.g., mining/crypto‑adjacent) to **≤ 20 %** of the total allocated capital. Consider substituting at least one breakout pick with a **non‑correlated** signal (e.g., earnings‑driven catalyst, macro‑driven sector) to reduce correlation risk.
