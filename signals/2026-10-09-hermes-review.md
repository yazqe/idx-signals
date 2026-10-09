# Hermes Review — 2026‑10‑09  

## 1. Sanity Check (math + logic)  

- **WIFI**:  
  - R/R = (5 % / 2 %) ≈ 2.5 : 1, not explicitly stated → **missing R/R**.  
  - SL = –2 % below close – purely percentage‑based, no support‑level justification → **arbitrary SL**.  
  - TP = +5 % above close – no identified resistance → **arbitrary TP**.  
  - Conviction “High” vs only one‑signal (RSI) → **tier inflation**.  

- **WMUU**:  
  - R/R ≈ 2.5 : 1 (same issue).  
  - SL again a flat –2 % with no structural anchor → **arbitrary SL**.  
  - TP +5 % without resistance reference → **arbitrary TP**.  
  - “High” conviction despite win‑rate only 53.8 % and modest edge → **tier inflation**.  

- **KOTA**:  
  - R/R ≈ 2.5 : 1 (not disclosed).  
  - SL –2 % below close, no support level → **arbitrary SL**.  
  - TP +5 % above close, no resistance → **arbitrary TP**.  
  - Conviction “High” but edge 6.2 % over 12 trades, win‑rate 58.3 % → **tier inflation**.  

- **BREN**:  
  - R/R ≈ 2.5 : 1 (absent).  
  - SL –2 % below close, no structural rationale → **arbitrary SL**.  
  - TP +5 % above close, no resistance level → **arbitrary TP**.  
  - Conviction “Medium” while edge only 3.3 % and win‑rate 66.7 % – still thin evidence → **tier inflation**.  

- **GOTO**:  
  - R/R ≈ 2.5 : 1 (absent).  
  - SL –2 % below close, no support – **arbitrary SL**.  
  - TP +5 % above close, no resistance – **arbitrary TP**.  
  - Conviction “Low” but still listed as a BUY despite win‑rate 36.4 % and edge 0.6 % – **questionable inclusion**.  

- **BNBR**:  
  - R/R ≈ 2.5 : 1 (absent).  
  - SL –2 % below close, no support – **arbitrary SL**.  
  - TP +5 % above close, no resistance – **arbitrary TP**.  
  - Conviction “Low” with win‑rate 26.3 % and edge 0.5 % – **questionable inclusion**.  

**Summary**: All six picks lack an explicit R/R calculation, rely on flat %‑based SL/TP, and assign conviction levels that are not supported by the limited evidence presented.  

---

## 2. Contradiction Hunter  

1. **“High” conviction vs thin evidence** – The author tags WIFI, WMUU, and KOTA as *High* conviction while the only supporting signal is a single‑indicator (RSI oversold) and the historical edge is modest (≤9.3 %). No multi‑timeframe or price‑action confirmation is provided, contradicting the implied robustness of a “high‑conviction” label.  

2. **Inclusion of low‑tier picks as BUY** – GOTO and BNBR are labelled *Low* conviction yet are still recommended as BUY positions alongside high‑conviction stocks, creating a mixed‑signal list that blurs the intended risk hierarchy.  

3. **“Medium” tier for BREN despite a solid win‑rate (66.7 %)** – The author assigns only *Medium* conviction to BREN, yet its win‑rate exceeds that of the “High” tier stocks (WIFI 70 %, WMUU 53.8 %). The inconsistency suggests a mis‑aligned tiering system.  

---

## 3. Hidden Risks  

- **Sector concentration** – All six tickers are presented without sector tags, but three (WIFI, WMUU, KOTA) are high‑tier “tech‑type” tickers. If they belong to the same sector (e.g., telecommunications), the portfolio could be heavily exposed to a sector‑specific shock, inflating sector VaR.  

- **Liquidity risk** – No volume data is supplied. If any of the low‑tier stocks (GOTO, BNBR) are thinly traded, a 5‑day target (+5 %) could be unattainable without significant market impact, raising execution risk.  

- **Correlation risk** – All picks are driven by the same RSI‑oversold signal. Correlated entry timing means the portfolio is effectively a single‑signal bet; a market‑wide rebound that invalidates the RSI mean‑reversion premise would hurt the entire list simultaneously.  

- **Timing / chase risk** – The analysis does not state the intraday price move. If any of these stocks have already rallied >15 % on the day (common for oversold rebounds), the suggested entry zone may be already past the optimal point, exposing the trader to a “late‑entry” trap.  

- **Stale data / regime shift** – The historical edge is derived from the last 10‑day RSI‑oversold trades. No assessment of whether the market regime (e.g., high‑volatility vs low‑volatility periods) has changed. A shift to a trending market would diminish mean‑reversion efficacy, rendering the edge stale.  

- **Indicator overlap** – Every pick relies on the same RSI‑oversold condition. There is no diversification of signal types (e.g., volume breakout, moving‑average cross, macro catalyst). The apparent “confluence” is illusory; it is a single‑indicator overlay, inflating confidence artificially.  

---

## 4. What the Author Got Right  

The author correctly identified that a deep RSI‑oversold reading (below 30) historically produced a modest positive edge for the selected tickers, and they transparently disclosed win‑rates and historical edge percentages, which is a useful quantitative foundation for a mean‑reversion strategy.  

---

## 5. Critical Recommendations  

1. **Add structural SL/TP anchors** – Replace the flat –2 % / +5 % levels with price‑based stops at nearest support (e.g., prior swing low, ATR‑based stop) and exits at identified resistance or a trailing‑stop mechanism. This will align risk with market structure.  

2. **Re‑tier conviction based on multi‑signal evidence** – Require at least two independent confirmations (e.g., volume surge, price‑action pattern, higher‑timeframe trend) before assigning “High” conviction. Downgrade or remove stocks that lack such corroboration (especially GOTO, BNBR).  

3. **Trim low‑conviction entries** – Eliminate GOTO and BNBR from the BUY list until they achieve a win‑rate >50 % and a documented edge >1 % over a meaningful sample size, or re‑classify them as “watch‑only” to avoid unnecessary exposure.
