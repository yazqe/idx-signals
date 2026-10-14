# Hermes Review — 2024‑10‑14  

## 1. Sanity Check (math + logic)  

- **WIFI:** (TP‑Entry)/(Entry‑SL) = (1 468‑1 385)/(1 385‑1 343) ≈ **1.98** – matches a ~2 :1 R/R, but the author never states the ratio.  
- **WMUU:** R/R ≈ **2.00** – clean mathematically.  
- **SDMU:** R/R ≈ **2.00** – clean.  
- **BRPT:** R/R ≈ **1.98** – clean.  
- **KOTA:** R/R ≈ **1.75** – clean.  
- **CBDK:** R/R ≈ **1.99** – clean.  
- **BREN:** R/R ≈ **1.99** – clean.  
- **PTRO:** R/R ≈ **1.67** – clean.  
- **CUAN:** R/R ≈ **1.62** – clean.  
- **GOTO:** R/R ≈ **1.75** – clean.  
- **BNBR:** R/R ≈ **1.65** – clean.  

**SL placement:** All stops are a flat **‑3 %** (or ‑5 % for the low‑tier list) regardless of each stock’s recent volatility, ATR, or support level. This is an arbitrary rule‑of‑thumb; many of the securities (e.g., low‑priced, thin‑float stocks) could be stopped out by normal intraday noise, inflating turnover without a structural stop.  

**TP placement:** Take‑profits are uniformly **+6 %** (or +5 % for low‑tier picks). No reference is made to actual resistance zones, prior swing highs, or Fibonacci/price‑action levels. The uniform TP creates a mechanical R/R that may not reflect the true upside potential.  

**Tier consistency:**  
- High conviction is awarded to **WIFI, WMUU, SDMU, BRPT, KOTA** despite win‑rates ranging from 56 % to 70 % and historical edges from 6.2 % to 9.3 %. The “high” label is not justified by the modest win‑rate or by any forward‑looking catalyst.  
- Medium conviction is given to **CBDK (40 % win, 3.4 % edge)** and **BREN (66.7 % win, 3.3 % edge)** – a mismatch; BREN’s win‑rate is higher than many “high” picks, yet it is downgraded.  
- Low conviction is attached to **PTRO, CUAN, GOTO, BNBR** even though PTRO’s win‑rate (63.6 %) exceeds the medium‑tier average. The tiering appears inconsistent with the underlying performance metrics.  

**Overall:** All picks are mathematically tidy, but the stop‑loss / take‑profit logic is mechanical and ignores price‑action context; conviction tiers are not aligned with win‑rate or edge magnitude.  

---

## 2. Contradiction Hunter  

1. **Conviction vs win‑rate mismatch** – “High” conviction is applied to SDMU (56.5 % win) while “Low” conviction is applied to PTRO (63.6 % win). The analysis simultaneously claims a “solid base of ~7 % average 5‑day edge” yet includes BNBR with a **0.48 %** edge and a **26.3 %** win‑rate, contradicting the “solid base” narrative.  

2. **Uniform TP/SL vs stated risk‑reward** – The author never states the R/R explicitly, yet the uniform ±3 % SL and +6 % TP imply a ~2 :1 R/R for every trade. This contradicts the claim that each signal carries a *different* historical edge (e.g., 9.3 % vs 0.48 %).  

3. **Medium‑tier label for CBDK despite low win‑rate** – CBDK is given a “Medium” conviction while its win‑rate is **40 %**, lower than many “Low” picks (e.g., GOTO at 36.4 %). The internal logic of tier assignment is inconsistent.  

---

## 3. Hidden Risks  

- **Sector concentration:** Several tickers (WIFI, WMUU, SDMU, BRPT) belong to the **technology / consumer‑electronics** niche on IDX, creating a hidden sector bias. A sector‑wide pull‑back would simultaneously hit multiple positions, inflating portfolio VaR.  

- **Liquidity risk:** Many of the low‑price stocks (e.g., BNBR at IDR 66, GOTO at IDR 27) have **average daily volume < 100 k shares**. Entering a 5 % portfolio allocation on such thinly‑traded instruments could cause slippage and price impact, especially with a fixed ‑3 % stop that may be triggered by normal market noise.  

- **Correlation of signals:** The entire list is built on **RSI‑oversold** or **volume‑breakout** triggers. These are not independent signals; a market‑wide oversold condition will generate multiple entries, leading to a false sense of diversification.  

- **Timing / chase risk:** All entries are placed **after** a sharp price move (e.g., SDMU up >4 % on volume breakout). The price may have already captured the bulk of the move, leaving limited upside while the stop is still ‑3 % away, increasing the chance of a stop‑out on a normal pull‑back.  

- **Stale data / regime shift:** The analysis relies on historical edge percentages calculated over a *fixed* number of past trades (e.g., 10‑13 trades). No mention is made of recent macro‑regime changes (e.g., tightening monetary policy, upcoming earnings season) that could render the past edge obsolete.  

- **Indicator overlap:** RSI oversold and volume breakout are both **momentum‑type** indicators; they often fire together in a volatile market, providing little additional information. The apparent “confluence” is therefore weak.  

---

## 4. What the Author Got Right  

The author correctly identified that a **systematic RSI‑oversold** rule can generate a statistically positive edge (average 7 % 5‑day return) when applied consistently, and the back‑tested win‑rates (70 % for WIFI, 63.6 % for PTRO) demonstrate that the signal is not pure noise.  

---

## 5. Critical Recommendations  

1. **Re‑calibrate stop‑loss levels** – Replace the flat ‑3 % stop with a volatility‑adjusted stop (e.g., 1.5 × ATR) or a structural support level. This will prevent premature exits on normal price swings, especially for low‑price, high‑volatility stocks.  

2. **Align conviction tiers to objective metrics** – Redefine “High/Medium/Low” conviction based on a composite score (win‑rate ≥ 60 % + edge ≥ 5 % → High, etc.). Re‑rank CBDK, BREN, PTRO, and BNBR accordingly to avoid tier inflation/deflation.  

3. **Diversify signal sources** – Introduce at least one additional, non‑momentum filter (e.g., earnings surprise, sector‑relative strength, or macro‑trend) to break the heavy reliance on RSI/volume. This will reduce correlation risk and improve the robustness of the trade set.
