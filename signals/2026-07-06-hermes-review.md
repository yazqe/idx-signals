# Hermes Review — 2026‑07‑06  

## 1. Sanity Check (math + logic)  

- **KRYA**:  
  - R/R not disclosed. Assuming entry ≈ close, SL = –3 % and TP = +6 % → R/R = 2.0. The author never states this, violating the “risk‑reward” disclosure requirement.  
  - SL is a flat ‑3 % rule, not anchored to a support level, trend‑line, or ATR‑based volatility stop. It is therefore arbitrary.  
  - TP is a flat +6 % target with no reference to a resistance zone, prior swing high, or Fibonacci‑derived level.  
  - Conviction “High” is at odds with the historical edge: 12.34 % edge over 32 trades but a **win‑rate of only 37.5 %** – a win‑rate that would normally merit a **medium** or even **low** conviction.  

- **ASHA**:  
  - Same R/R issue: implied 2.0 : 1 but never shown.  
  - SL again a blunt –3 % below close, not tied to a price structure (e.g., recent swing low, Bollinger‑Band lower bound).  
  - TP +6 % above close lacks justification (no identified resistance).  
  - Conviction “High” versus a 5.86 % edge over 35 trades and a **57.1 % win‑rate** – the win‑rate is decent, but the edge is modest; a “high” label may be overstated given the modest expectancy.  

- **APLN**:  
  - R/R again implicit 2.0 : 1 (TP +4 % vs SL –2 %). Not disclosed.  
  - SL –2 % below close is arbitrary; no mention of a recent low, EMA‑20 breach, or volatility‑adjusted stop.  
  - TP +4 % above close is not linked to a concrete resistance (e.g., prior high, pivot point).  
  - Conviction “Low” while the win‑rate is **50 %** and edge **0.49 %** over only 12 trades – the sample size is tiny, making any conviction level dubious.  

**Result**:  
- KRYA: ❗ SL/TP arbitrary, R/R omitted, conviction inflated.  
- ASHA: ❗ SL/TP arbitrary, R/R omitted, conviction possibly overstated.  
- APLN: ❗ SL/TP arbitrary, R/R omitted, conviction ambiguous due to thin sample.  

## 2. Contradiction Hunter  

1. **KRYA win‑rate vs conviction** – The author writes “high‑conviction breakout” yet the historical win‑rate is **37.5 %**, which contradicts a high‑confidence stance.  
2. **ASHA edge vs conviction** – The “high” conviction is justified by a 57.1 % win‑rate, but the edge (5.86 %) is modest; the narrative leans heavily on win‑rate while ignoring low expectancy, creating a mixed signal.  
3. **APLN low‑conviction vs “low‑risk, low‑edge add‑on”** – The author calls the trade “low‑risk” yet provides no risk‑adjusted justification (e.g., stop‑loss at a true support). The label conflicts with the lack of a concrete risk mitigation framework.  

No outright contradictory statements (e.g., a stock flagged “avoid” elsewhere) were found, but the internal consistency between statistical evidence and conviction tiers is weak.  

## 3. Hidden Risks  

- **Sector concentration** – Both KRYA and ASHA are mining‑related tickers (KRYA = Karya, ASHA = Ashanti). Concentrating two of the three picks in the same commodity sector inflates sector‑specific VaR; a sudden metal‑price shock could wipe out >60 % of the suggested short‑term allocation.  

- **Liquidity risk** – Neither ticker’s average daily volume is disclosed. If either is a micro‑cap (common for breakout‑focused stocks on IDX), a 5‑10 % position could easily exceed the daily turnover, leading to slippage and execution risk.  

- **Correlation** – The three picks are all driven by **volume‑breakout** criteria, meaning they are likely to co‑move on the same market‑wide volatility surge. The portfolio is therefore not diversified across signal types.  

- **Timing / chase risk** – KRYA already jumped **5.56 %** and ASHA **7.84 %** on the breakout day. Entering after such moves raises the risk of a **pull‑back** or **gap‑down** on the next session, especially if the breakout was a false breakout.  

- **Stale data / regime shift** – The analysis relies on a “today’s market bias toward volume‑driven breakouts”. If the market regime flips to a **value‑oriented** or **macro‑driven** day, the breakout signal may lose its predictive power. No contingency for regime change is discussed.  

- **Indicator overlap** – Both KRYA and ASHA are flagged solely on **vol_breakout_up**. This is a single‑indicator signal; the author treats it as a robust multi‑signal confirmation, inflating confidence without independent corroboration (e.g., momentum, trend, or order‑flow confirmation).  

## 4. What the Author Got Right  

The author correctly identified that today’s market environment is dominated by high‑volume breakouts, and the quantitative back‑test (12.34 % edge over 32 trades for KRYA, 5.86 % over 35 trades for ASHA) does show a modest historical edge for the volume‑breakout rule set.  

## 5. Critical Recommendations  

1. **Define explicit R/R** – Publish the exact risk‑reward ratio for each trade (e.g., “R/R = 2.0”) and ensure it matches the TP/SL distances. If the ratio deviates, adjust TP or SL accordingly.  

2. **Anchor SL/TP to market structure** – Replace the flat ‑3 % / +6 % (or ‑2 % / +4 % for APLN) stops with levels tied to recent swing lows, ATR‑based volatility stops, or clear resistance zones. This will prevent arbitrary exits and improve risk management.  

3. **Re‑balance sector exposure** – Limit the combined exposure to the mining sector to **≤30 %** of the short‑term allocation. Consider adding at least one non‑correlated signal (e.g., a financial‑sector mean‑reversion or a consumer‑goods momentum play) to mitigate sector‑specific tail risk.
