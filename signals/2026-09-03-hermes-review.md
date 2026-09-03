# Hermes Review — 2026‑09‑03  

## 1. Sanity Check (math + logic)  

- **SINI**:  
  - R/R ≈ (16,225 − 14,750) / (14,750 − 14,013) ≈ 2.0 :1 – not explicitly stated, but the math checks out.  
  - **SL** is a flat “‑5 % below close” (≈ 14,013). This is a *percentage* stop, not anchored to a recent support level or volatility‑based ATR; it appears arbitrary.  
  - **TP** is a flat “+10 % above close” (≈ 16,225). No reference to a concrete resistance zone (e.g., prior swing high, Fibonacci‑38.2 %).  
  - **Conviction** is “High” while the edge is derived from a 52‑trade back‑test (13.23 % edge, 67.3 % win). The sample is decent, but the edge is modest relative to the high conviction rating.  

- **MINA**:  
  - R/R ≈ (308 − 280) / (280 − 266) = 28 / 14 = 2.0 :1 – clean.  
  - **SL** again a flat “‑5 % below close” (≈ 266). No technical justification (e.g., recent swing low at 260‑265).  
  - **TP** a flat “+10 % above close” (≈ 308). No mention of a resistance level (e.g., prior high at 312).  
  - **Conviction** “High” but the historical edge is based on only **5** past trades (10.78 % edge, 60 % win). Sample size is thin for a high‑tier label.  

- **CBDK**:  
  - R/R ≈ (4,521 − 4,100) / (4,100 − 3,905) ≈ 421 / 195 ≈ 2.16 :1 – acceptable.  
  - **SL** again a flat “‑5 % below close” (≈ 3,905). No support‑based justification.  
  - **TP** a flat “+10 % above close” (≈ 4,521). No resistance reference.  
  - **Conviction** “Medium” while the edge is only 3.36 % over 15 trades with a 40 % win rate – a weak statistical foundation for a breakout trade.  

**Summary**: All three picks are mathematically clean on R/R (≈2:1). However, every stop‑loss and take‑profit is set by a *fixed percentage* rather than a price‑action‑derived level, which inflates the apparent precision. Conviction tiers are not fully aligned with the strength of the underlying evidence (especially MINA and CBDK).  

---

## 2. Contradiction Hunter  

1. **“High” conviction for SINI vs. modest edge** – the author touts a “high” conviction while the historical edge (13.23 %) is modest and the win‑rate (67.3 %) is only marginally above random. This mismatches the implied confidence.  
2. **Medium conviction for CBDK despite a 40 % win rate** – a 40 % win rate is below a neutral expectation (≈50 % for a random walk). Labeling the signal as “medium” contradicts the statistical weakness.  
3. **Market bias “short‑to‑medium‑term bullish”** while all three picks are *volume‑driven breakouts* that have already surged >7 % (SINI 15.7 %, CBDK 7.6 %). The analysis treats the breakout as a fresh entry, yet the price action suggests the bulk of the move is already priced in, contradicting a genuine bullish bias.  

---

## 3. Hidden Risks  

- **Sector concentration**: All three stocks are mining‑related (coal, base metals, etc.). A sector‑specific shock (e.g., a sudden drop in commodity prices or a regulatory change) would simultaneously hit the entire mini‑portfolio, inflating sector VaR.  

- **Liquidity risk**:  
  - *SINI* (ticker often trades < 200 k shares/day).  
  - *MINA* and *CBDK* are similarly thin‑traded. A 5 % position could easily move the market, raising slippage risk.  

- **Correlation risk**: The three tickers share exposure to global commodity cycles and likely move together (high correlation > 0.7 historically). The apparent diversification is superficial.  

- **Timing / chase risk**: All three have already experienced a >7 % price jump on the breakout day. Entering after such a move raises the chance of a short‑term pull‑back (mean‑reversion) rather than a continuation.  

- **Stale back‑test data**: The “historical edge” figures are derived from the author’s proprietary back‑test (52 trades for SINI, 5 for MINA, 15 for CBDK). No indication of the rolling window, regime‑shift handling, or out‑of‑sample validation. The edge could be overstated if the market regime has changed (e.g., post‑COVID commodity dynamics).  

- **Indicator overlap**: The analysis relies on *vol_breakout_up* for SINI and CBDK and *ma_golden_cross* for MINA. Both are essentially momentum‑type signals; they are not independent. The confluence claim is therefore weak.  

---

## 4. What the Author Got Right  

The author correctly identified that a **sharp volume surge** (2.2× for SINI, 5.2× for CBDK) often precedes short‑term continuation, and they quantified a historical edge for those breakouts, providing a data‑driven rationale rather than a purely anecdotal call.  

---

## 5. Critical Recommendations  

1. **Re‑anchor stops to technical support** – replace the flat “‑5 %” stop with the nearest recent swing low or an ATR‑based stop (e.g., 1.5 × ATR). This will align risk with market volatility and prevent arbitrary stop placement.  

2. **Trim sector exposure** – cap the combined mining‑sector allocation to ≤ 20 % of the total portfolio. Consider adding a non‑correlated sector (e.g., consumer staples) or a market‑neutral hedge to mitigate sector‑specific shocks.  

3. **Adjust conviction tiers** – downgrade MINA to “Medium” (given only 5 back‑tested trades) and CBDK to “Low” (40 % win rate). Only SINI should retain a “High” label, and even then, temper the confidence with a note on the modest edge.  

---
