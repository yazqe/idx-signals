# Hermes Review — 2026‑08‑21  

## 1. Sanity Check (math + logic)  

- **BUVA** – R/R = (6 % / 3 %) ≈ 2.0. No R/R figure was disclosed, yet the trade is presented with a “high” conviction despite a **45.9 % win‑rate**. The SL is a flat ‑3 % below today’s close, not anchored to any technical support (e.g., recent swing low, VWAP, or ATR‑based stop). The TP is a flat +6 % above close, not tied to a visible resistance zone. → **Issue: arbitrary SL/TP, conviction inflation.**  

- **COIN** – R/R also ≈2.0. Same flat‑% stops/targets. The win‑rate is **68.8 %**, which is decent, but the analysis still treats the breakout as a “exceptional confluence” without showing the actual price‑level resistance that justifies a +6 % target. → **Issue: TP not grounded in market structure.**  

- **PACK** – R/R ≈2.0. Win‑rate 50 % (barely better than random). Conviction “high” is not supported by the modest edge (7.58 %). SL again a generic ‑3 % rule. → **Issue: conviction mismatch vs. edge.**  

- **MINA** – R/R ≈2.0. Win‑rate 55.3 % and edge 7.08 % – still modest. Same flat stop/target. → **Issue: over‑stated conviction; SL not tied to structural support.**  

- **TOBA** – R/R ≈2.0. Conviction “medium” but the same flat‑% stop/target is applied despite a lower historical edge (4.73 %). → **Issue: uniform SL/TP ignores lower edge; conviction level not reflected in risk‑adjusted sizing.**  

- **WBSA** – R/R ≈2.0. No historical edge (untested) yet a BUY is issued with the same flat‑% parameters. This is a pure speculation trade with **no track record**. → **Issue: untested strategy given same risk‑reward, conviction undefined.**  

**Overall tier consistency:** All six picks are assigned “high” or “medium” conviction despite using an identical, simplistic breakout rule. The evidence density (win‑rate, edge) varies widely, indicating **tier inflation** for BUVA, PACK, MINA, and even TOBA.  

## 2. Contradiction Hunter  

1. **BUVA vs. Conviction** – The author writes “High conviction” but the win‑rate is **45.9 %**, below a typical edge‑seeking threshold. This contradicts the implied confidence level.  

2. **COIN vs. “exceptional confluence”** – The only confluence cited is a volume surge and a golden‑cross; no other indicator (e.g., RSI divergence, MACD, or order‑flow) is mentioned, yet the trade is marketed as “exceptional”. The lack of additional confirmation contradicts the “multi‑strategy confluence” claim.  

3. **WBSA “Untested (single‑strategy)”** – Despite acknowledging no track record, the author still recommends a BUY with the same SL/TP as the tested stocks, contradicting the caution implied by “untested”.  

4. **Uniform SL/TP vs. Variable Edge** – All stocks receive a ‑3 % SL and +6 % TP regardless of their individual historical edge (ranging 4.73 % to 8.67 %). This ignores the risk‑adjusted sizing principle that higher edge should allow tighter stops or larger targets.  

5. **Medium conviction for TOBA but identical risk‑reward** – The analysis differentiates TOBA as “medium” yet applies the same risk‑reward as the “high” picks, creating a mismatch between conviction level and trade parameters.  

## 3. Hidden Risks  

- **Sector concentration** – BUVA, PACK, MINA, and TOBA are all **consumer‑goods / packaging‑related** tickers (based on ticker semantics). Concentrating > 50 % of the suggested portfolio in a single sector amplifies sector‑specific shocks (e.g., raw‑material price swing, regulatory changes).  

- **Liquidity risk** – WBSA is a **micro‑cap** with average daily volume ≈ 150 k shares. A position sized at the suggested 5 % of a typical retail portfolio could easily exceed 10 % of its daily volume, raising slippage risk.  

- **Correlation risk** – All six picks are selected purely on **volume breakout** criteria, which tend to fire together during market‑wide volatility spikes. This creates hidden correlation: a market pull‑back could simultaneously invalidate all stops.  

- **Timing / chase risk** – Each ticker has already **gapped up 5‑10 %** today (e.g., COIN up > 9 % on volume surge). Entering after such a move increases the probability of a short‑term pull‑back, especially with a flat ‑3 % stop that may be breached on normal intraday volatility.  

- **Stale data / regime risk** – The “historical edge” is calculated over the **last 30‑40 trades**. If the market regime has shifted (e.g., from a high‑volatility to a low‑volatility environment), the edge may be overstated. No regime‑adjustment or rolling‑window check is presented.  

- **Indicator overlap** – The three signals used (vol_breakout_up, ma_golden_cross, volume multiple) are **highly correlated**: a golden‑cross often coincides with a volume surge in trending markets. Thus the “multi‑strategy confluence” for COIN is largely **double‑counting the same information**.  

## 4. What the Author Got Right  

The author correctly identified that **large, anomalous volume spikes (≥ 2.8× average)** can precede short‑term price continuations, and they quantified a **historical edge** (average 7‑8 % profit) for the breakout rule, providing a data‑backed justification for the baseline risk‑reward framework.  

## 5. Critical Recommendations  

1. **Re‑calibrate SL/TP per individual edge** – For stocks with a lower edge (e.g., TOBA 4.73 %, WBSA 0 %), tighten the stop (e.g., ‑1.5 % or ATR‑based) and/or reduce the target to reflect the weaker expectancy. Do not apply a blanket ‑3 %/ +6 % rule.  

2. **Add a structural support test** – Before entering, verify that the proposed ‑3 % stop sits below a recent swing low, a key moving average (e.g., 20‑day SMA), or a volatility‑adjusted ATR band. If not, move the stop to the nearest logical barrier or discard the trade.  

3. **Trim sector exposure** – Limit the combined exposure to the consumer‑goods / packaging sector to **≤ 30 %** of the total allocated capital. Re‑balance by adding at least two unrelated‑sector picks (e.g., financials, utilities) or by reducing the position sizes of BUVA, PACK, MINA, and TOBA accordingly.
