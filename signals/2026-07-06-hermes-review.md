# Hermes Review — 2026‑07‑06  

## 1. Sanity Check (math + logic)  

- **KRYA**:  
  - R/R not disclosed. Assuming entry ≈ close, SL = –3 % and TP = +6 % → R/R ≈ 2.0. The analysis never states this figure, so the “high conviction” claim lacks a quantified risk‑reward.  
  - SL is a flat –3 % below the close, not anchored to a support level, volatility‑adjusted ATR, or structural price floor. Arbitrary percentage → potential over‑risk.  
  - TP is a flat +6 % above the close, not tied to a visible resistance zone (e.g., prior swing high, Fibonacci‑38.2 %).  
  - Conviction ★5 but win‑rate only **37.5 %** – a mismatch that inflates the tier.  

- **ASHA**:  
  - Same R/R issue as KRYA (≈2.0) – not explicitly shown.  
  - SL again a blunt –3 % below close, no technical justification.  
  - TP a blunt +6 % above close, no resistance reference.  
  - Conviction ★5 vs win‑rate **57.1 %** – still acceptable but the “robust upside bias” is not backed by a concrete price target.  

- **RODA**:  
  - R/R again ≈2.0, not disclosed.  
  - SL –3 % below close, TP +6 % above close – both arbitrary.  
  - Conviction ★3 (Medium) while win‑rate **54.0 %** and edge **3.69 %** – the medium tier is arguably overstated given the modest edge.  

**Result:** No pick passes a clean‑mathics test. All three suffer from missing R/R disclosure, arbitrary stop‑loss/take‑profit placement, and tier inflation relative to the underlying win‑rate/edge evidence.  

---

## 2. Contradiction Hunter  

1. **KRYA – “High” conviction vs. 37.5 % win‑rate**  
   > “Conviction: High” – but a win‑rate below 40 % contradicts a high‑confidence stance.  

2. **ASHA – “robust upside bias” vs. modest 5.86 % edge**  
   > “A 4.7× volume breakout … suggests a robust upside bias” – yet the historical edge is only 5.86 %, barely above noise, undermining the robustness claim.  

3. **RODA – Medium tier but identical SL/TP to high‑conviction picks**  
   > “Medium” conviction yet the risk‑reward framework (‑3 % / +6 %) is identical to the ★5 picks, ignoring its weaker edge and win‑rate.  

4. **Overall – Uniform SL/TP across disparate conviction levels**  
   > The analysis treats a 12 % edge (KRYA) the same as a 3.7 % edge (RODA) with identical stop‑loss/take‑profit distances, contradicting the premise that conviction should affect risk parameters.  

---

## 3. Hidden Risks  

- **Sector concentration** – All three tickers belong to the **consumer‑goods / industrial** cluster on IDX. A 100 % exposure to a single sector magnifies sector‑specific shocks (e.g., commodity price swing, policy change).  

- **Liquidity risk** – The analysis never cites average daily volume. If any of the three are sub‑500 k shares‑per‑day, a 5 % position could move the market, inflating slippage and execution risk.  

- **Correlation risk** – The three signals are *all* derived from the same “vol_breakout_up” filter. This creates a hidden correlation: a market‑wide volatility spike will trigger all three simultaneously, eroding true diversification.  

- **Timing / chase risk** – Each ticker already posted a **≥6 % price surge** on the breakout day. Entering after such a move raises the probability of a short‑term pull‑back (mean reversion) and leaves little upside room.  

- **Stale data / over‑fitted edge** – The “historical edge” is computed over the *last 30‑50 trades* for each ticker. If the market regime has shifted (e.g., post‑COVID liquidity swing), the edge may be stale; no out‑of‑sample validation is presented.  

- **Indicator overlap** – The sole indicator is “vol_breakout_up”. No secondary confirmation (e.g., trend, momentum, macro) is used, so the confluence claim is weak; the three picks share the same signal source, inflating confidence artificially.  

---

## 4. What the Author Got Right  

The author correctly identified that a **sharp volume expansion (≥3× average)** often precedes short‑term price acceleration on IDX, and they quantified a historical edge for each ticker, providing a data‑backed rationale for a momentum‑based entry.  

---

## 5. Critical Recommendations  

1. **Re‑calibrate SL/TP to technical levels** – Replace the flat –3 % / +6 % rule with stop‑loss at the nearest **support zone** (e.g., prior swing low, ATR‑based volatility stop) and take‑profit at the **next resistance** (e.g., prior high, Fibonacci‑61.8 %). This aligns risk with market structure.  

2. **Adjust position sizing to conviction and win‑rate** – Scale KRYA to a **larger** portion (e.g., 2–3 % of capital) given its higher edge, but **shrink RODA** to ≤1 % of capital because its edge and conviction are modest.  

3. **Diversify signal sources** – Add at least one *independent* filter (e.g., moving‑average crossover, RSI divergence, macro catalyst) to each pick, or drop any ticker that does not meet a second‑layer confirmation, thereby reducing the hidden correlation from a single volume‑breakout filter.
