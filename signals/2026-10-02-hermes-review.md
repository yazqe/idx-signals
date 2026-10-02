# Hermes Review — 2026‑10‑02  

## 1. Sanity Check (math + logic)

- **WIFI:** ✓ clean (R/R = 10 %/5 % = 2.0). SL set at –5 % arbitrarily, no support level cited.  
- **WMUU:** ✓ clean (R/R = 2.0). SL again a flat –5 % rather than a structural low.  
- **KAQI:** ✓ clean (R/R = 2.0). Only 5 historic trades – sample too thin for “high” conviction.  
- **ESIP:** ✓ clean (R/R = 2.0). Medium conviction but win‑rate 42.9 % vs edge 4.5 % – weak signal.  
- **BRMS:** ✓ clean (R/R = 2.0). Medium conviction, yet win‑rate 71.4 % with only 4.1 % edge – possible over‑fit.  
- **MINA:** ✓ clean (R/R = 2.0). Medium conviction, win‑rate 50 % – borderline.  
- **RAJA:** ✓ clean (R/R = 2.0). Medium conviction, win‑rate 64.3 % vs edge 3.0 % – thin edge.  
- **ASHA:** ✓ clean (R/R = 2.0). Medium conviction, win‑rate 55.6 % vs edge 2.5 % – marginal.  
- **GJTL:** ✓ clean (R/R = 2.0). Medium conviction, win‑rate 70 % vs edge 2.4 % – edge barely exceeds noise.  
- **CBDK:** ✓ clean (R/R = 2.0). Low conviction, win‑rate 61.5 % vs edge 1.6 % – thin edge, low confidence.  
- **PANI:** ✓ clean (R/R = 2.0). Low conviction, win‑rate 55.6 % vs edge 1.4 % – marginal.  
- **GOTO:** **⚠️ issue** – RSI reported as “0” (impossible; RSI ranges 0‑100). Win‑rate 36.4 % with a positive edge of only 0.6 % is contradictory; SL/TP still flat 5 %/10 % – likely over‑optimistic.  
- **APLN:** ✓ clean (R/R = 2.0). Low conviction, win‑rate 50 % vs edge 0.5 % – edge within noise.  
- **BNBR:** **⚠️ issue** – Win‑rate 26.3 % with a positive edge of 0.5 % is statistically implausible; suggests data error or over‑fitting. SL/TP still flat 5 %/10 %.  

**Tier consistency concerns**  
- High conviction assigned to KAQI (5 trades) and WMUU (13 trades) despite modest win‑rates (60 % & 53.8 %).  
- Medium conviction given to ESIP (42.9 % win) and APLN (50 % win) – win‑rates barely above random.  
- Low conviction still applied to GOTO (36.4 % win) and BNBR (26.3 % win) – both below break‑even, yet still “BUY”.  

Overall, the R/R math is internally consistent, but **SL and TP levels are purely percentage‑based, not anchored to technical support/resistance**, inflating the apparent risk‑reward quality.

---

## 2. Contradiction Hunter

1. **GOTO’s win‑rate vs conviction** – “Buy (Low conviction)” but the win‑rate (36.4 %) is *worse* than a coin‑flip, contradicting any rational “edge” claim.  
2. **BNBR’s win‑rate vs edge** – Win‑rate 26.3 % with a positive edge of 0.5 % is statistically impossible unless the risk‑adjusted payoff is extreme; no such justification is provided.  
3. **RSI values** – GOTO listed RSI = 0 (outside the 0‑100 scale) while all other stocks have plausible RSI values (e.g., 19.8, 4.1). This suggests a data entry error that conflicts with the “oversold” narrative.  
4. **Conviction vs sample size** – High conviction assigned to KAQI (only 5 historic trades) and WMUU (13 trades) while medium/low conviction is given to stocks with *more* data points (e.g., ESIP 14 trades). The internal logic of conviction scaling is inconsistent.  

---

## 3. Hidden Risks

- **Sector concentration** – The list is heavily weighted toward *consumer‑discretionary / technology* tickers (WIFI, WMUU, KAQI, GJTL, etc.). If the sector faces a macro‑pullback, the portfolio could suffer >30 % drawdown.  
- **Liquidity risk** – Several low‑tier picks (e.g., GOTO, BNBR, APLN) are thin‑cap stocks on IDX; average daily volume often < 100 k shares, making a 5 % stop‑loss vulnerable to slippage.  
- **Correlation clustering** – All picks are selected solely on RSI‑oversold signals. This creates a hidden correlation: a market‑wide rebound could lift many positions together, but a reversal would hit them all at once.  
- **Timing / chase risk** – The analysis does not check recent price action. If any of these stocks have already rallied > 15 % today (common for oversold rebounds), the entry zone may be already compromised, increasing gap‑down risk at the open.  
- **Stale data / over‑fit** – Historical “edge” is calculated on a *tiny* number of trades (5‑14). No out‑of‑sample validation is shown, so the edge could be a statistical artifact, especially for low‑tier stocks.  
- **Indicator overlap** – The entire universe relies on a single indicator (RSI oversold). No secondary confirmation (e.g., volume surge, MACD cross, fundamental catalyst) is presented, inflating false‑positive signals.  

---

## 4. What the Author Got Right

The author correctly identified that **WIFI** exhibits a strong historical edge (9.3 % over 10 trades) with a solid win‑rate (70 %) and a genuinely deep oversold RSI (19.8), which justifies a higher conviction relative to the other names.  

---

## 5. Critical Recommendations

1. **Re‑anchor SL/TP to price structure** – Replace the flat “‑5 % / +10 %” stops with levels tied to recent swing lows (for SL) and identified resistance zones (for TP). This will prevent over‑optimistic R/R calculations and reduce stop‑loss hunting.  

2. **Cull or downgrade the low‑conviction, statistically dubious picks** – Remove **GOTO** (impossible RSI, win‑rate 36.4 %) and **BNBR** (win‑rate 26.3 % with a 0.5 % edge) from the shortlist until a robust sample size (> 30 trades) validates their edge.  

3. **Diversify the signal set** – Add at least one non‑RSI filter (e.g., volume breakout, earnings surprise, or a trend‑following indicator) to break the RSI‑only correlation bias. This will lower portfolio‑wide exposure to a single market‑condition trigger.
