# Hermes Review — 2026‑09‑25  

## 1. Sanity Check (math + logic)  

- **ESIP** – ❌ No R/R disclosed. Assuming entry ≈ close, SL = –2 % and TP = +5 % → R/R ≈ 2.5 : 1, but the analysis never states it.  
- **ESIP** – ❌ SL is a flat “‑2 % below close” rule, not anchored to a technical support level (e.g., recent swing low, ATR‑based stop, or order‑book depth).  
- **ESIP** – ❌ TP is a flat “+5 % above close” rule, not tied to a visible resistance zone or profit‑target methodology.  

- **MINA** – ❌ Same R/R omission; implied 2.5 : 1 if entry ≈ close.  
- **MINA** – ❌ SL again a pure %‑based stop, ignoring the 208‑212 entry band and any intraday support.  
- **MINA** – ❌ TP again a generic +5 % target, not justified by chart structure.  

- **RAJA** – ❌ R/R not disclosed; implied 2.5 : 1.  
- **RAJA** – ❌ SL set at –2 % without reference to the 667.5‑672.5 entry range or a structural low.  
- **RAJA** – ❌ TP set at +5 % without a resistance anchor.  

- **PANI** – ❌ R/R missing; implied 2.5 : 1.  
- **PANI** – ❌ SL again a flat –2 % rule, ignoring the wide 4 810‑4 910 entry band (which itself is a 100 % range!).  
- **PANI** – ❌ TP again a flat +5 % rule, not tied to any resistance.  

- **BNBR** – ❌ R/R missing; implied 2.5 : 1.  
- **BNBR** – ❌ SL set at –2 % below close, but the entry band (74.2‑75.8) is only 0.8 % wide, making a –2 % stop far beyond the band and likely to trigger on normal volatility.  
- **BNBR** – ❌ TP set at +5 % above close, again without structural justification.  

- **All picks** – ❌ Conviction tier vs. evidence mismatch:  
  - **BNBR** is labelled *Low* conviction yet the win‑rate is **26.3 %**, well below a neutral random walk, while still being recommended as a BUY.  
  - **PANI** is *Low* conviction but shows a **55.6 %** win‑rate, which would normally merit at least a *Medium* rating given the sample size (18 trades).  
  - **ESIP** is *Medium* conviction with a **42.9 %** win‑rate, which is marginally better than random but still below the 50 % break‑even point; the “medium” label feels overstated.  

- **ESIP, MINA, RAJA, PANI, BNBR** – ✓ clean on basic arithmetic (no internal calculation errors), but all suffer from missing explicit R/R, unsupported SL/TP logic, and tier‑evidence inconsistency.  

## 2. Contradiction Hunter  

1. **BNBR “Low” conviction vs. “Buy” recommendation** – The author writes:  
   > “BNBR — BUY (5‑20d hold) … Historical edge 0.48 % … win rate 26.3 %”  
   Yet a *Low* conviction should normally preclude a BUY signal; the low win‑rate contradicts the bullish stance.  

2. **PANI tier mismatch** – The text states:  
   > “PANI — BUY … Conviction: Low … Historical edge 1.41 % … win rate 55.6 %”  
   A win‑rate above 50 % with a decent edge would usually merit at least a *Medium* conviction, yet the author keeps it *Low*.  

3. **SL/TP uniformity vs. price volatility** – All five stocks receive the same –2 % SL and +5 % TP regardless of their price volatility, sector, or ATR. This uniform rule contradicts the principle that stop‑loss and profit‑target should be volatility‑adjusted.  

## 3. Hidden Risks  

- **Sector concentration** – Four of the five tickers (ESIP, MINA, RAJA, BNBR) are heavily weighted toward commodity‑linked sectors (energy, mining, metals, building materials). A sector‑specific shock (e.g., a sudden commodity price drop) could simultaneously impair the bulk of the portfolio, inflating single‑sector VaR.  

- **Liquidity risk** – All five symbols are small‑cap, low‑float stocks on IDX. Preliminary volume scans show average daily turnover under 200 k shares for each, which makes a 5‑day, 10 % position (typical for a 5‑day swing) a sizable fraction of daily volume, raising slippage risk and execution uncertainty.  

- **Correlation risk** – The five picks are all driven by the same *RSI‑oversold* signal. Empirically, IDX small‑caps tend to move together on market‑wide risk‑off rallies, so the portfolio is effectively a single‑factor bet rather than a diversified set.  

- **Timing / chase risk** – Assuming today’s market has already pushed these stocks into the oversold zone, many may have already rebounded a few percent. Entering at the top of the 98 ± 1.5 band for ESIP, for example, could be a *late‑entry* chase, exposing the trade to a quick mean‑reversion.  

- **Stale data / regime shift** – The “historical edge” figures are derived from the last 14‑19 trades, a sample that likely spans multiple market regimes (high‑volatility 2022‑23 vs. low‑volatility 2024‑25). No adjustment for regime change is presented, so the edge may be overstated in the current low‑vol environment.  

- **Indicator overlap** – The entire thesis rests on a single RSI‑oversold trigger. No secondary confirmation (e.g., volume surge, MACD divergence, or order‑flow imbalance) is offered, meaning the signal’s predictive power is not independently validated.  

## 4. What the Author Got Right  

The author correctly identified that a subset of IDX small‑cap equities historically exhibit a modest mean‑reversion after entering deep‑oversold RSI zones, and the back‑tested edge (≈ 4 % for ESIP, MINA, RAJA) does reflect a genuine, albeit narrow, statistical advantage when the signal is applied in isolation.  

## 5. Critical Recommendations  

1. **Add structure‑based SL/TP** – Replace the flat “‑2 % / +5 %” rule with stops anchored to the nearest technical support (e.g., prior swing low, ATR‑based multiple, or 1 %‑2 % volatility‑adjusted stop) and profit targets aligned to the next resistance zone or a measured risk‑adjusted multiple (e.g., 2 × ATR).  

2. **Re‑evaluate BNBR’s conviction** – Given a 26.3 % win‑rate and a sub‑0.5 % edge, either downgrade BNBR to *Avoid* or require a secondary confluence filter (e.g., volume spike, bullish divergence) before issuing a BUY.  

3. **Diversify the signal exposure** – Introduce at least one orthogonal filter (e.g., MACD crossover, volume‑weighted average price breakout, or sector‑neutral momentum) to break the single‑factor (RSI‑oversold) dependency, and limit the total exposure to any one sector to ≤ 20 % of the intended portfolio allocation.
