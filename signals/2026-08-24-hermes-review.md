# Hermes Review — 2026‑08‑24  

## 1. Sanity Check (math + logic)  

- **SDMU**: R/R = 6 % / 3 % = **2.0** (not explicitly stated).  
  - ✅ mathematically consistent, but **SL is a flat –3 % below today’s close**, not anchored to a technical support level (e.g., prior swing low, ATR‑based stop).  
  - TP is a flat +6 % above close, **not tied to any identified resistance**.  

- **SINI**: R/R = 6 % / 3 % = **2.0** – clean mathematically.  
  - SL again a generic –3 % rule; no mention of a price‑level (e.g., 20‑day SMA breach).  
  - TP lacks reference to a concrete resistance zone.  

- **PACK**: R/R = 6 % / 3 % = **2.0** – clean.  
  - Same arbitrary SL/TP logic; no structural justification.  

- **EMAS**: R/R = 5 % / 3 % ≈ **1.67** – clean mathematically.  
  - SL still a flat –3 % rule; TP not linked to a resistance.  

- **COIN**: R/R = 5 % / 3 % ≈ **1.67** – clean mathematically.  
  - **Issue**: Conviction is listed as “Untested” yet the pick is a **BUY** with a “high‑conviction” tone in the market read‑out. This is a **tier inflation** (no track record, yet treated as a serious play).  

- **Tier consistency**:  
  - SDMU: **High conviction** but win‑rate only **40 %** (below a typical threshold for “high” confidence).  
  - PACK: **High conviction** with a **50 %** win‑rate and modest 7.58 % edge – borderline at best‑case.  
  - EMAS: **Medium conviction** yet win‑rate **62.5 %** and edge **4.09 %** – reasonable.  
  - COIN: **Untested** but still placed in the “high‑conviction” narrative of the market read.  

**Summary**: All picks are mathematically clean on the R/R front, but **SL/TP are arbitrarily set at fixed % offsets from today’s close rather than at logical support/resistance levels**, and **conviction tiers are mismatched to the underlying statistical evidence**.  

---

## 2. Contradiction Hunter  

1. **COIN conviction mismatch** – The analysis tags COIN as “Untested” (no historical edge, no win‑rate) yet the market read states “high‑conviction breakout and golden‑cross signals” and includes COIN in the BUY list.  
2. **SDMU high conviction vs low win‑rate** – The author claims “High” conviction for SDMU while the win‑rate is only **40 %**, contradicting the implied confidence level.  
3. **PACK high conviction vs modest edge** – A 7.58 % edge over 44 trades with a **50 %** win‑rate is marginal; labeling it “High” conflicts with the modest statistical edge.  
4. **EMAS medium conviction but placed among “high‑conviction breakout” narrative** – The market read lumps EMAS with the “high‑conviction” group, yet its own conviction is “Medium”.  

---

## 3. Hidden Risks  

- **Sector concentration** – SDMU, SINI, PACK, EMAS, and COIN are all **small‑cap, volume‑driven stocks** that tend to cluster in the **materials / consumer‑discretionary** space on IDX. A sector‑wide shock (e.g., commodity price swing) could simultaneously impair the entire list, inflating portfolio VaR.  

- **Liquidity risk** – Breakout‑type picks often have **thin average daily volume** relative to the implied position size (no sizing guidance is given). Slippage and execution risk are therefore high, especially for COIN (no prior trades).  

- **Correlation risk** – All five signals are **volume‑breakout or golden‑cross** triggers, which are highly correlated with short‑term market momentum. The portfolio is effectively a single‑factor bet, not a diversified set.  

- **Timing / chase risk** – The analysis does not state how much the stocks have already moved today. If any have already **gained >15 %** (common for breakout alerts), the suggested entry zone may be already past the optimal entry point, exposing the trader to a pull‑back or gap‑down risk.  

- **Stale / over‑fit data** – The “historical edge” figures are derived from **tiny sample sizes** (SDMU = 5 trades, EMAS = 8 trades). Such small‑N backtests are prone to over‑fitting and may not survive a regime shift.  

- **Indicator overlap** – The entire list relies on **only two signal families** (golden‑cross & volume breakout). There is **no independent confirmation** (e.g., momentum, macro‑fundamentals, earnings surprise), so the confluence is superficial.  

---

## 4. What the Author Got Right  

The author correctly identified that **volume‑spike breakouts** have historically delivered a **positive edge** on the IDX, and they quantified that edge (e.g., 13.42 % for SDMU) and win‑rates, providing a transparent performance‑based rationale for each signal.  

---

## 5. Critical Recommendations  

1. **Re‑anchor stops to structural levels** – Replace the flat “‑3 % below close” rule with a stop at the nearest **support zone** (e.g., prior swing low, ATR‑based stop, or 20‑day SMA breach). This will align risk with market structure and avoid arbitrary stop placement.  

2. **Align conviction tiers with statistical evidence** – Downgrade “High” conviction for any ticker whose win‑rate is ≤ 45 % (e.g., SDMU, PACK) or, alternatively, require a minimum **5‑trade sample** with **≥ 55 % win‑rate** before assigning a high tier.  

3. **Add a sizing guideline and diversification filter** – Limit the aggregate exposure to **≤ 20 %** of the portfolio for this single‑factor cluster, and cap any individual position at **≤ 5 %** of total capital. This curtails sector‑concentration, liquidity, and correlation risks before execution.
