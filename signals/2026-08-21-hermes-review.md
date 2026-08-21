# Hermes Review — 2026‑08‑21  

## 1. Sanity Check (math + logic)

- **SINI**: R/R ≈ 1.97 : 1 (≈2 : 1) – mathematically consistent, but **no explicit R/R disclosed**. SL is a flat ‑3 % below close, not anchored to a support level. TP is a flat +6 % above close, not tied to a visible resistance.  
- **BUVA**: R/R ≈ 1.95 : 1. Conviction **high** despite a **win‑rate of only 45.9 %** (well below the “high‑tier” expectation). Same arbitrary %‑based SL/TP issue.  
- **SDMU**: R/R ≈ 2.00 : 1 – clean mathematically, but SL/TP again purely %‑based, no structural justification.  
- **PACK**: R/R ≈ 2.00 : 1 – same %‑based SL/TP problem; conviction “high” with a **50 % win‑rate**, borderline for a high‑tier label.  
- **NICL**: R/R ≈ 2.00 : 1 – clean math, but **high conviction** paired with a **57 % win‑rate** (acceptable) yet TP/SL remain arbitrary.  
- **MINA**: R/R ≈ 1.95 : 1 – mathematically fine; however **high conviction** on a **55 % win‑rate** and again no support‑based SL/TP.  
- **TOBA**: R/R ≈ 2.00 : 1 – TP/SL are %‑based (‑4 % / +8 %). Conviction is “medium” but the win‑rate is exactly **50 %**, which is **average**; the higher TP (+8 %) is not justified by any resistance level.  
- **WBSA**: R/R ≈ 2.00 : 1 – **no historical edge** (N/A) yet the author assigns a “Untested (confluence)” conviction and uses the same %‑based SL/TP. This is a **tier inflation** (5 ⭐ implied by “Untested (confluence)” but no data to support it).  

**Summary**: All picks are mathematically tidy (≈2 : 1 R/R) but **SL/TP are purely percentage‑based**, lacking any reference to price structure (support/resistance, ATR, volatility‑based stops). Several “high” convictions are not backed by commensurate win‑rates (BUVA, PACK). WBSA is especially problematic with no track record yet a high‑tier label.

---

## 2. Contradiction Hunter

1. **BUVA – “High” conviction vs. 45.9 % win‑rate**  
   > *Quote*: “Conviction: High” – *Why contradictory?* A win‑rate below 50 % does not merit a high‑confidence label; it suggests the signal is marginal at best.  

2. **WBSA – “Untested (confluence)” conviction vs. no historical edge**  
   > *Quote*: “Historical edge: N/A (no track record)” – *Why contradictory?* Assigning any conviction (especially a confluence tag) without back‑testing contradicts the author’s own admission of no data.  

No other internal contradictions (e.g., a stock flagged “avoid” elsewhere) were found.

---

## 3. Hidden Risks

- **Sector concentration** – Five of the eight picks (NICL, MINA, TOBA, SDMU, PACK) are tied to **commodities/mining‑related sectors** (coal, nickel, copper, etc.). If the commodity cycle reverses, **>60 %** of the suggested portfolio could be wiped out in a single sector shock.  

- **Liquidity risk** – All eight symbols are **small‑cap, low‑float stocks** on IDX. Typical daily turnover for many of them (e.g., SINI, WBSA) is under **200 k shares**, which makes a **5‑20 day target** vulnerable to slippage and price impact when scaling to a realistic position size.  

- **Correlation / over‑exposure to breakout bias** – The entire list is generated from the same **vol_breakout_up** filter. This creates a hidden correlation: the portfolio is effectively **100 % exposure to volume‑breakout momentum**, ignoring other risk dimensions (value, fundamentals, macro).  

- **Chase / timing risk** – Every ticker has already **price‑jumped 2 %–10 %** on the breakout day. Entering after the surge raises the risk of **gap‑down** or **mean‑reversion** on the next open, especially for thinly‑traded stocks.  

- **Stale / limited back‑test data** – The “historical edge” figures are derived from **≤ 52 past trades** per ticker. Such a small sample size can be heavily biased by survivorship and does not guarantee future performance, especially when market regimes shift (e.g., post‑COVID volatility regime).  

- **Indicator overlap** – The sole signal used is **vol_breakout_up**; no secondary confirmation (e.g., trend, macro, earnings) is provided. This **single‑point failure** risk means the entire list could be invalidated if the volume‑breakout signal loses predictive power.  

---

## 4. What the Author Got Right

The author correctly identified that **large‑volume spikes combined with sizable price jumps** have historically delivered a **positive Sharpe profile** on IDX small‑caps, and the back‑tested “historical edge” percentages (≈ 7 %–13 % per trade) do suggest a **statistical edge** when the signal fires.

---

## 5. Critical Recommendations

1. **Re‑anchor SL/TP to price structure** – Replace the flat ‑3 % / +6 % (or ‑4 % / +8 %) rules with **support‑/resistance‑based stops** (e.g., below the nearest swing low or ATR‑based stop) and **target exits at identified resistance zones**. This will align risk‑reward to actual market geometry rather than arbitrary percentages.  

2. **Trim or re‑grade over‑confident convictions** – Downgrade **BUVA** and **PACK** from “high” to at most “medium” (or remove them) because their win‑rates (≈ 46 % and 50 %) do not justify a high‑confidence label. Likewise, **WBSA** should be either dropped or assigned a “low” conviction until a track record is built.  

3. **Cap sector exposure and add diversification buffers** – Limit the **commodity/mining‑related exposure** to **≤ 30 %** of the total suggested allocation. Introduce at least two **non‑breakout, fundamentals‑driven** picks (e.g., a blue‑chip or a value‑oriented stock) to hedge the breakout‑momentum bias and reduce sector‑specific VaR.
