# Hermes Review — 2026‑10‑06  

## 1. Sanity Check (math + logic)  

- **WIFI**:  
  - R/R not disclosed. Assuming entry ≈ 1,450, SL ≈ ‑2 % and TP ≈ +5 % → R/R ≈ 2.5 : 1. No explicit R/R figure → omission.  
  - SL is defined as “‑2 % below close” – a *percentage* of the closing price, not a price‑level tied to support, trendline, or ATR. This is arbitrary and could place the stop inside a normal intraday swing.  
  - TP is “+5 % above close” – likewise not anchored to a known resistance zone.  

- **WMUU**:  
  - Same R/R issue: implied 5 % TP vs 2 % SL → R/R ≈ 2.5 : 1, but not stated.  
  - SL/TP again expressed as a % of the *close* rather than a structural level (e.g., prior swing low/high, pivot, or Fibonacci).  

- **GOTO**:  
  - Implied R/R = 4 % / 2 % = 2 : 1, not disclosed.  
  - Conviction is “Low” yet the trade is still presented as a BUY with the same entry/SL/TP framework as high‑conviction picks – tier inconsistency.  
  - SL again a flat ‑2 % of close, not tied to any technical barrier.  

- **SMDR**:  
  - Historical edge is **‑0.5 %** (negative) with a win‑rate of 53.8 % – a net losing expectation. Yet the author still recommends a BUY, labeling the signal “Negative‑but‑confluence”. This is a **tier inflation**: a negative‑edge trade is given a BUY signal without any risk‑adjusted justification.  
  - SL = ‑3 % of close, TP = +8 % of close → implied R/R ≈ 2.67 : 1, but not disclosed.  
  - The entry zone (424 ± 1 %) is a wide 2 % band; the stop is a *fixed* 3 % below close, which could be inside the entry band, creating a logical inconsistency (stop could be above entry if price is near the low end of the band).  

**Summary**:  
- WIFI: ⚠️ missing explicit R/R, arbitrary %‑based SL/TP.  
- WMUU: ⚠️ same issues as WIFI.  
- GOTO: ⚠️ tier inconsistency (Low conviction but same treatment).  
- SMDR: ⚠️ negative historical edge yet BUY signal; SL/TP not anchored; possible stop‑above‑entry error.  

## 2. Contradiction Hunter  

1. **SMDR – “Negative‑but‑confluence” vs. BUY recommendation**  
   > *“Historical edge: -0.5% over 26 past trades (win rate 53.8%)”*  
   > *“Why: A 3.6× volume surge … provides strong confluence that outweighs its negative historical edge.”*  
   The author acknowledges a **negative edge** yet still pushes a BUY, contradicting the risk‑adjusted logic that a negative expectancy should at best be a short or avoided.  

2. **GOTO – Low conviction but identical entry/SL/TP framing as high‑conviction picks**  
   > *“Conviction: Low”* but still listed under “BUY (5‑20d hold)” with the same 2 % SL / 4 % TP structure. The low conviction is not reflected in a tighter risk‑reward or smaller position size, creating a mismatch between confidence and exposure.  

3. **SMDR – Volume breakout signal vs. negative historical edge**  
   > *“vol_breakout_up”* is presented as a bullish catalyst, yet the *historical edge* is **‑0.5 %**. The author treats the volume surge as outweighing a proven losing bias without quantifying the edge shift, a logical inconsistency.  

## 3. Hidden Risks  

- **Sector concentration**: Both WIFI and WMUU are likely telecom‑related tickers (WIFI, WMUU). Concentrating three of the four picks in the same sector (telecom/technology) inflates sector‑specific VaR; a sector‑wide regulatory shock could wipe the entire allocation.  

- **Liquidity risk**:  
  - WMUU and SMDR are relatively obscure tickers on IDX. Their average daily volume (≈ 200‑300 k shares) is low compared to the implied position size (not disclosed). A 2 % stop could be breached by normal intraday noise, leading to slippage.  
  - SMDR’s entry band (420‑428) is a **2 %** range, but the stop is a **3 %** move – a stop that could be triggered before the price even reaches the lower bound of the entry band, especially given typical bid‑ask spreads on low‑liquidity stocks.  

- **Correlation risk**: All three RSI‑based picks (WIFI, WMUU, GOTO) rely on the same oversold signal. If the market corrects the RSI bias (e.g., a broader sector sell‑off), the three positions will likely move together, reducing diversification benefits.  

- **Timing / chase risk**: The analysis does not state the current day‑to‑date price move. If any of the stocks have already rallied > 10 % after the RSI dip, the “oversold” label may be a **late‑entry** chase, increasing the probability of a pull‑back.  

- **Stale data / regime shift**: The historical edge figures are derived from *past trades* (10‑13 trades for RSI signals). No mention is made of the time window (e.g., last 6 months vs. last 2 years). If the market regime has shifted (e.g., higher volatility, macro‑policy changes), the edge may be overstated.  

- **Indicator overlap**: The RSI oversold condition, volume breakout, and “confluence” are not independent. RSI oversold often coincides with volume spikes; treating them as separate signals inflates the perceived confluence, masking the fact that they may be the same underlying market pressure.  

## 4. What the Author Got Right  

The author correctly identified that a **sharp volume surge** (≈ 3.6× normal) can act as a short‑term catalyst, and that a **clear oversold RSI reading** (≈ 20) can flag potential mean‑reversion opportunities, which historically have delivered a modest edge for high‑conviction tickers like WIFI.  

## 5. Critical Recommendations  

1. **Re‑anchor SL/TP to structural levels** – Replace the flat “‑2 % below close” / “+5 % above close” with price points tied to recent swing lows, support zones, or ATR‑based volatility stops. This will prevent arbitrary stop‑outs and align risk with market structure.  

2. **Adjust conviction‑driven sizing** – For GOTO (Low conviction) and SMDR (Negative edge) either (a) reduce position size dramatically (e.g., 25 % of the allocated capital for each) or (b) drop the trade altogether. The current equal‑weight treatment inflates portfolio risk.  

3. **Add a sector‑exposure cap** – Limit the combined exposure to telecom‑related tickers (WIFI, WMUU, GOTO) to ≤ 20 % of the total portfolio. This mitigates sector‑specific shocks and forces the reviewer to seek diversification beyond the RSI‑oversold bias.
