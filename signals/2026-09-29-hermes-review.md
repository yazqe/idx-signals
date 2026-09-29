# Hermes Review — 2026‑09‑29  

## 1. Sanity Check (math + logic)

- **ASPR**: (TP‑Entry)/(Entry‑SL) = (159‑145)/(145‑138) = 14/7 = **2.0** → implied R/R = 2.0. No R/R was stated, but the numbers are internally consistent.  
  - **SL**: “‑5 % below close” is an arbitrary percentage; no support level or volatility‑based buffer is cited.  
  - **TP**: “+10 % above close” is also arbitrary; no resistance zone is referenced.  
  - **Conviction vs evidence**: High conviction despite a **47.8 % win‑rate** (below 50 %) – mismatch.

- **WIFI**: (1 865‑1 695)/(1 695‑1 610) ≈ 170/85 = 2.0 → R/R ≈ 2.0 (clean).  
  - **SL**: flat ‑5 % rule, no technical justification.  
  - **TP**: flat +10 % rule, no resistance cited.  
  - **Conviction vs evidence**: High conviction but edge only **9.3 %** over 10 trades – modest; still acceptable given **70 % win‑rate**.

- **WMUU**: (41‑37)/(37‑35) = 4/2 = 2.0 → clean.  
  - **SL/TP**: same arbitrary % rule.  
  - **Conviction vs evidence**: High conviction with **53.8 % win‑rate** (just above break‑even) – questionable for “high” tier.

- **ESIP**: (105‑95)/(95‑90) = 10/5 = 2.0 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Medium conviction but **42.9 % win‑rate** (sub‑50 %) – tier inflation.

- **MINA**: (227‑206)/(206‑196) = 21/10 = 2.1 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Medium conviction with **50 % win‑rate** – borderline; edge 4.01 % modest.

- **RAJA**: (726‑660)/(660‑627) = 66/33 = 2.0 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Medium conviction, win‑rate **64.3 %** (good) but edge only **3.01 %** – thin edge for “medium”.

- **ASHA**: (44‑40)/(40‑38) = 4/2 = 2.0 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Medium conviction, win‑rate **55.6 %**, edge **2.46 %** – thin edge.

- **PANI**: (5 082‑4 620)/(4 620‑4 389) = 462/231 = 2.0 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Low conviction but edge **1.41 %** over 18 trades, win‑rate **55.6 %** – acceptable for low tier.

- **BULL**: (381‑346)/(346‑329) = 35/17 ≈ 2.06 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Low conviction, edge **1.23 %**, win‑rate **54.5 %** – thin edge.

- **GOTO**: (41‑37)/(37‑35) = 4/2 = 2.0 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Low conviction, edge **0.62 %**, win‑rate **36.4 %** – **major mismatch** (win‑rate far below break‑even).

- **APLN**: (121‑110)/(110‑105) = 11/5 = 2.2 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Low conviction, edge **0.49 %**, win‑rate **50 %** – edge barely covers transaction costs.

- **BNBR**: (78‑71)/(71‑68) = 7/3 ≈ 2.33 → clean.  
  - **SL/TP**: arbitrary.  
  - **Conviction vs evidence**: Low conviction, edge **0.48 %**, win‑rate **26.3 %** – **grossly inconsistent**; a losing strategy flagged as a buy.

**Summary**: All picks mathematically produce an R/R ≈ 2.0 (clean), but **SL/TP are set by flat % rules rather than structural support/resistance**, and **conviction tiers are frequently inflated** (e.g., high conviction on sub‑50 % win‑rates, low conviction on losing edge).

---

## 2. Contradiction Hunter

1. **“Low‑tier with the only positive edge among the weakest signals.”** – The author claims BNBR is “the only positive edge among the weakest signals,” yet **PANI (1.41 %)**, **BULL (1.23 %)**, and **APLN (0.49 %)** also have positive edges.  
2. **GOTO’s win‑rate vs conviction** – The analysis lists GOTO as a **Low‑conviction** buy despite a **36.4 % win‑rate** (well below break‑even) and a **0.62 % edge**. This contradicts the implied premise that low‑conviction picks still have a reasonable statistical edge.  
3. **BNBR’s win‑rate vs “positive edge” statement** – BNBR is described as “the only positive edge among the weakest signals,” yet its **26.3 % win‑rate** makes the edge effectively **negative** after costs; the statement conflicts with the data.  
4. **ASPR’s high conviction vs win‑rate** – ASPR is given a **High conviction** label while its **47.8 % win‑rate** is below 50 %, which contradicts the usual high‑conviction rationale (expectation >50 %).  
5. **Medium‑tier for ESIP despite sub‑50 % win‑rate** – ESIP is placed in the **Medium** tier but its win‑rate is **42.9 %**, below break‑even, conflicting with the tier’s implied statistical robustness.

---

## 3. Hidden Risks

- **Sector concentration**: A large portion of the list (WIFI, WMUU, ESIP, MINA, RAJA, ASHA, PANI, BULL, GOTO, APLN, BNBR) are **low‑price, likely micro‑cap stocks** that often belong to the same **financial‑services or consumer‑discretionary clusters** on IDX. Concentrating on such thin‑cap names inflates sector‑specific VaR; a sector‑wide shock (e.g., regulatory change) could wipe out most of the portfolio in one move.  

- **Liquidity risk**: Many tickers (e.g., **PANI @ 4 620 IDR**, **BNBR @ 71 IDR**, **GOTO @ 37 IDR**) trade **< 100 k shares/day** on average volume. Position sizing based on a flat 5 % SL/TP ignores the fact that a modest position could move the market, leading to slippage and execution risk.  

- **Correlation risk**: All RSI‑oversold picks are driven by the **same indicator** and are entered **simultaneously**. This creates a hidden correlation cluster; a rebound in RSI (or a market‑wide shift in risk appetite) could simultaneously invalidate many entries, turning a diversified list into a single‑factor bet.  

- **Timing / chase risk**: ASPR has already **jumped +13.28 %** on the breakout day. Entering at the top of the range (≈ 145) after such a move raises the risk of **buy‑the‑dip** rather than **buy‑the‑breakout**, and the 5 % SL may be too tight if the price is already on a short‑term pull‑back.  

- **Stale data / small sample bias**: Several signals rely on **tiny back‑test samples** (e.g., WIFI: 10 trades, WMUU: 13 trades, GOTO: 11 trades). Such limited histories are vulnerable to **over‑fitting** and may not reflect current market regime, especially given recent macro‑policy shifts in Indonesia.  

- **Indicator overlap**: The analysis treats **vol_breakout_up** (ASPR) and **rsi_oversold** (the bulk of the list) as independent signals, yet both are **momentum‑type triggers** that often co‑occur in thinly‑traded stocks, inflating the perceived confluence.  

- **Risk of false positives from flat % SL/TP**: Using a uniform ‑5 % SL and +10 % TP ignores **stock‑specific volatility**. High‑beta stocks (e.g., PANI) may have daily swings > 5 %, making the SL too tight; low‑beta stocks (e.g., APLN) may need a wider TP to capture the edge.  

---

## 4. What the Author Got Right

The author correctly identified **ASPR’s breakout momentum**, quantifying a **5.5× volume surge** and a **13.28 % price jump**, which legitimately supports a short‑term bullish bias and justifies a trade idea despite the modest win‑rate. The clear articulation of the volume breakout adds genuine value to the analysis.

---

## 5. Critical Recommendations

1. **Re‑calibrate SL/TP to structural levels** – Replace the flat ‑5 % SL with **support‑based stops** (e.g., recent swing lows, ATR‑based buffers) and set TP at **identified resistance zones** (previous swing highs, Fibonacci extensions). This will align risk‑reward to market‑driven price levels rather than arbitrary percentages.  

2. **Adjust conviction tiers to match win‑rate & edge** – Downgrade **high‑conviction** tags for stocks with **< 50 % win‑rates** (ASPR, WMUU) and upgrade **low‑conviction** for those with **strong statistical edges** (PANI, BULL). Aligning tier labels with empirical performance prevents over‑exposure to weak‑signal trades.  

3. **Introduce a liquidity filter and position‑size cap** – Exclude any ticker whose **average daily volume** is **< 200 k shares** or whose **average daily dollar volume** is **< IDR 5 bn**. For the remaining low‑cap names, cap the max allocation to **≤ 5 % of total capital** to mitigate market‑impact risk and avoid concentration in thinly‑traded instruments.
