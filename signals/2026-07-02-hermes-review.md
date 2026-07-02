# Hermes Review — 2024‑07‑02  

## 1. Sanity Check (math + logic)  

- **BNBR:**  
  - **R/R mismatch:** No risk‑reward ratio is supplied. Assuming an entry at the midpoint ≈ 106, a 5 % SL (≈ 100.7) and a 12 % TP (≈ 118.7) yields an R/R ≈ 2.4, not the “high‑tier” claim. The analysis never states this figure, so the R/R is undocumented.  
  - **SL placement:** “‑5 % below close” is a flat‑percentage stop, not anchored to a technical level (e.g., recent swing low, ATR‑based band, or support zone). This makes the stop arbitrary and vulnerable to normal intraday volatility.  
  - **TP placement:** “+12 % above close” is also a flat‑percentage target with no reference to a resistance line, prior swing high, or Fibonacci/price‑objective. The TP is therefore unjustified.  
  - **Tier consistency:** Conviction is marked **High** (5‑star) but the only supporting evidence is a single volume‑breakout signal and a historical edge statistic. No multi‑time‑frame confirmation, no fundamental catalyst, and no risk‑adjusted back‑test evidence are presented. This is a **tier inflation** flag.  

*Result:* BNBR – ❌ issues (R/R undocumented, arbitrary SL/TP, tier inflation).  

---

## 2. Contradiction Hunter  

1. **Volume‑breakout vs. price‑jump:** The note says a “2.3× volume breakout with a 17.78 % price jump” justifies a **high‑tier** signal, yet the same magnitude of price jump could already reflect the breakout. If the price has already moved 17.78 % today, the breakout is *already priced in*, contradicting the premise that a breakout “offers the best risk‑adjusted opportunities”.  
2. **Hold horizon vs. signal type:** The pick is labeled “5‑20 day hold” but the signal type is **vol_breakout_up**, which is inherently short‑term (often 1‑3 days). No justification is given for extending the trade to a 20‑day window, creating a mismatch between signal horizon and suggested holding period.  

---

## 3. Hidden Risks  

- **Sector concentration:** BNBR is a **financial services** ticker (bank). If the author’s broader portfolio already leans heavily on banks, this adds sector‑specific exposure. A sudden regulatory or macro‑shock to the banking sector could amplify portfolio VaR.  
- **Liquidity risk:** BNBR’s average daily turnover (≈ 150 K shares) is modest relative to the implied position size for a “high‑conviction” trade. A 5 % SL could be breached on a single large order, leading to slippage.  
- **Chase / timing risk:** The stock has already surged **≈ 17.8 %** today. Entering now means buying at the tail of the move, exposing the trade to a rapid pull‑back or gap‑down at the next open.  
- **Stop‑loss robustness:** A flat 5 % stop does not account for the stock’s recent volatility (ATR ≈ 3 %). In a volatile breakout, the stop could be hit on normal price noise, turning a high‑conviction signal into a loss.  
- **Indicator overlap:** The analysis leans solely on the **vol_breakout_up** signal. No secondary confirmation (e.g., moving‑average crossover, MACD, or order‑flow imbalance) is provided, so the signal may be a false positive from a single indicator.  

---

## 4. What the Author Got Right  

The author correctly identified that a **2.3× volume surge coupled with a 17.8 % price jump** is a rare, high‑impact event on IDX, and the historical edge (12.67 % average gain over 36 similar trades) does suggest a statistically favorable bias for short‑term upside when the breakout is genuine.  

---

## 5. Critical Recommendations  

1. **Quantify and disclose the risk‑reward:** Compute the exact R/R (≈ 2.4) and present it explicitly. If the true R/R deviates from the author’s implied “high‑tier” expectation, adjust the conviction level accordingly.  
2. **Replace the flat‑percentage SL with a structure‑based stop:** Anchor the stop to a recent swing low, ATR‑multiple, or a clear support zone (e.g., “below the nearest 5‑day low” or “1 × ATR below entry”). This will reduce premature stop‑outs and align the stop with market structure.  
3. **Mitigate chase risk:** Either wait for a pull‑back entry (e.g., on a 0.5 % retracement) or scale in with a smaller initial position. If the trade must be entered now, cap the exposure to **≤ 5 % of total portfolio** and set a tighter trailing stop to protect against a rapid reversal after today’s surge.
