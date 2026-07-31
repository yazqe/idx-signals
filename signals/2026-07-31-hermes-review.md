# Hermes Review — 2026-07-31  

## 1. Sanity Check (math + logic)  

- **HUMI**: ✓ clean (R/R ≈ 3:1, mathematically consistent).  
- **BNBR**: ✓ clean (R/R ≈ 2.5:1).  
- **TINS**: ✓ clean (R/R ≈ 2.67:1) **but** SL is a flat ‑3 % rather than a price‑level support; the TP is set to a fixed +8 % with no reference to resistance.  
- **ARCI**: ✓ clean (R/R = 2:1) **but** conviction is “Medium” while the win‑rate is 100 % on only 3 trades – a classic over‑fit.  
- **BUMI**: ✓ clean (R/R = 2:1) – SL/TP again purely percentage‑based, no structural justification.  
- **ASHA**: ✓ clean (R/R = 2:1) – win‑rate 42.9 % on 7 trades; “Medium” conviction is not supported by the weak edge (3.99 %).  
- **APLN**: ✓ clean (R/R ≈ 1.67:1) – edge only 2.05 % on 4 trades; medium conviction feels inflated.  
- **NCKL**: ✓ clean (R/R = 1:1) – low conviction matches low edge, but the 1 % SL/TP band is unusually tight for a low‑conviction pick.  
- **GTSI**: ✓ clean (R/R = 1:1) – same issue as NCKL; no technical rationale.  
- **GJTL**: ✓ clean (R/R = 1:1) – minimal edge (0.47 %) on 6 trades; low conviction is appropriate, but the flat ‑4 % SL/TP is arbitrary.  

**Tier consistency flags**  
- **TINS**: High conviction despite a win‑rate of 45.7 % and a modest 5.51 % edge – over‑rated.  
- **ARCI**: Medium conviction while the perfect win‑rate on only three trades should either push it to High or be flagged as data‑starved.  
- **APLN**: Medium conviction with a 2.05 % edge – the edge is barely above noise; conviction appears inflated.  

## 2. Contradiction Hunter  

1. **“High‑tier ma signals (HUMI, BNBR) provide solid 5‑day edges.”** – HUMI’s edge is 17 % but the win‑rate is only 50 %; a 50 % win‑rate does **not** constitute a “solid” edge.  
2. **“Volume breakout offers the best risk‑adjusted upside.”** – TINS is presented as the best breakout, yet its win‑rate (45.7 %) is the lowest among the high‑conviction list, contradicting the “best risk‑adjusted” claim.  
3. **“Medium‑tier names round out the list.”** – ARCI’s 100 % win‑rate on three trades should place it in the high‑conviction bucket, not medium. The author’s placement contradicts the internal win‑rate evidence.  

## 3. Hidden Risks  

- **Sector concentration**: BNBR, TINS, and HUMI are all mining‑related (tin/coal exposure). Together they represent >30 % of the suggested portfolio, exposing the whole basket to a single commodity swing.  
- **Liquidity risk**: TINS (ticker 3 790) typically trades < 200 k shares/day; a 5‑20 day hold with an 8 % TP could easily exceed daily volume, causing slippage.  
- **Correlation risk**: BNBR and TINS move together on tin price dynamics; ARCI and BUMI also share exposure to bulk commodities, inflating apparent diversification.  
- **Timing / chase risk**: If any of the listed stocks have already rallied > 15 % today (common for golden‑cross alerts), the entry zone (±0.5 %) may be chasing a breakout that is already priced in, increasing downside risk.  
- **Stale signal risk**: All picks rely on a simple moving‑average golden‑cross. The MA crossover is a lagging indicator; without confirming momentum or volume filters, the signal can be stale, especially in a market where many stocks are simultaneously crossing.  
- **Indicator overlap**: The only non‑MA signal is TINS’ volume breakout, but the analysis treats it as a separate “best Sharpe‑weighted” signal while still using the same MA‑based entry/exit logic, creating a false sense of confluence.  

## 4. What the Author Got Right  

The author correctly identified that a historical edge (e.g., HUMI’s 17 % over four trades) can justify a higher risk‑reward ratio, and they consistently applied a percentage‑based SL/TP framework across the entire list, which simplifies position sizing and ensures a uniform risk‑management baseline.  

## 5. Critical Recommendations  

1. **Re‑scale conviction levels** – downgrade **TINS** to Medium/Low (its win‑rate and edge do not merit High) and **ARCI** to High (its 100 % win‑rate, albeit on three trades, deserves a higher conviction flag).  
2. **Add technical stop‑loss anchors** – replace flat ‑2 %/‑3 % stops with price‑level stops at nearest support (e.g., recent swing lows or ATR‑based levels) to avoid arbitrary exits that ignore market structure.  
3. **Trim sector exposure** – cap mining‑related positions (BNBR, TINS, HUMI) to ≤ 20 % of total notional exposure; reallocate the freed capital to unrelated sectors (e.g., consumer, finance) to mitigate commodity‑driven correlation risk.
