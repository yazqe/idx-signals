# Hermes Review — 2024‑08‑06  

## 1. Sanity Check (math + logic)  

- **ARCI**: ✓ clean *on the surface* (TP ≈ +5 % / SL ≈ ‑2 % → R/R ≈ 2.5).  
  *Issue*: No explicit R/R stated; the author never quantifies the 2.5 ratio, violating the “R/R math” requirement.  

- **RODA**: ✓ clean mathematically (R/R ≈ 2.5).  
  *Issue*: Same as ARCI – missing explicit R/R figure.  

- **BIPP**: ✓ clean mathematically (R/R ≈ 2.5).  
  *Issue*: No R/R disclosed; also the win‑rate is only 50 % – a “medium” conviction is questionable given the thin edge (2.71 %).  

- **HRTA**: ✓ clean mathematically (R/R ≈ 2.5).  
  *Issue*: Conviction is labeled “Low” yet the pick is still presented alongside “medium‑tier” stocks, creating a tier‑inflation mismatch.  

- **SL placement** (all picks): All stop‑losses are set at a flat **‑2 %** below the close, **not** anchored to any technical support, trend‑line, ATR‑based volatility stop, or market‑structure level. This is an arbitrary percentage stop, exposing the trade to premature exits on normal intraday noise.  

- **TP placement** (all picks): All take‑profits are a flat **+5 %** above the close, with no reference to identified resistance zones, Fibonacci extensions, or historical swing highs. The TP is therefore speculative rather than price‑level justified.  

- **Tier consistency**:  
  - ARCI, RODA, BIPP are all tagged **Medium** despite win‑rates hovering just above 50 % and edges under 5 %. The evidence density is thin; a “Medium” label suggests stronger conviction than the data support.  
  - HRTA is marked **Low** but still makes the top‑4 list, effectively receiving a **Medium** exposure in the portfolio. This inflates its perceived weight relative to its statistical edge (1.57 %).  

## 2. Contradiction Hunter  

1. **“Low conviction but strong volume” vs. inclusion** – The author writes:  
   > “HRTA, though low‑tier, earns a spot thanks to its solid volume surge.”  
   Yet the same paragraph states HRTA’s conviction is *Low*. Including a low‑conviction stock in a *medium‑tier* ranked list contradicts the internal hierarchy that low‑conviction picks should be filtered out.  

2. **Medium‑tier label vs. win‑rate** – For BIPP the win‑rate is **50 %** (exactly break‑even). Yet the pick is still labeled **Medium**. Elsewhere the author treats a >54 % win‑rate as “Medium”. The inconsistency in the win‑rate threshold for tier assignment is a logical contradiction.  

3. **“Only negative‑tier candidate (ESSA) omitted”** – The market read claims ESSA is a *negative‑tier* candidate, yet the analysis never defines what constitutes a negative tier (e.g., win‑rate < 45 % or edge < 0 %). The omission leaves the reader without a clear rule, contradicting the implied systematic filter.  

## 3. Hidden Risks  

- **Sector concentration** – ARCI and RODA are both **automotive/transportation** stocks (both part of the broader vehicle manufacturing sector). HRTA is a **health‑care** name, while BIPP is a **biotech** ticker, but the three‑stock concentration in *auto‑related* equities raises sector‑specific exposure to any macro‑level shock (e.g., policy change on vehicle subsidies). If the portfolio were to allocate > 30 % to auto, a sector‑specific reversal could wipe out a large chunk of the trade book.  

- **Liquidity risk** – All four picks are **Tier‑1** (small‑cap) equities on IDX with average daily turnover often below **IDR 200 bn**. Position sizing is not disclosed, but a typical 5‑day hold at 2 % risk per trade could easily exceed 10 % of daily volume, inviting slippage and execution risk.  

- **Correlation risk** – The volume‑breakout signal is applied uniformly, creating a *signal‑correlation* cluster. If market‑wide volume spikes (e.g., due to a macro news flow) trigger multiple breakouts, the strategy may be over‑exposed to a single market driver, inflating apparent diversification.  

- **Timing / chase risk** – Each stock has already **gained > 4 %** intraday (ARCI 4.33 %, RODA 4.84 %, BIPP 9.09 %, HRTA 5.5 %). Entering after such moves means the trader is chasing the tail of the breakout, increasing the probability of a rapid pull‑back (mean‑reversion) and reducing the expected edge.  

- **Stale data / regime risk** – The “historical edge” figures (e.g., 4.53 % over 37 trades) are derived from *all* past breakout trades, without any weighting for recent market regimes. If the last 12 months have seen a shift in volatility regime, the edge may be overstated.  

- **Indicator overlap** – The sole filter is **vol_breakout_up**. No secondary confirmation (e.g., momentum oscillator, order‑flow imbalance, or macro catalyst) is used. This single‑indicator reliance inflates the false‑positive rate, especially in a market where volume spikes can be noise‑driven.  

## 4. What the Author Got Right  

The author correctly identified that **large, sudden volume surges** on IDX historically precede short‑term price spikes, and they quantified a modest edge (≈ 2‑5 % over a 5‑day horizon) for each breakout, providing a data‑backed rationale for a directional bias.  

## 5. Critical Recommendations  

1. **Anchor SL/TP to market structure** – Replace the flat ‑2 % / +5 % stops with **technical‑level** stops (e.g., below the nearest swing low, ATR‑based multiples, or key support zones) and **TPs at identified resistance** (previous swing highs, Fibonacci extensions, or volume‑profile peaks). This will align risk‑reward to actual price‑action rather than arbitrary percentages.  

2. **Re‑calibrate conviction tiers** – Introduce a transparent win‑rate / edge threshold matrix (e.g., *Low* < 45 % win, *Medium* 45‑55 % win, *High* > 55 % win) and re‑assign HRTA to the appropriate tier. If HRTA truly merits a *Low* label, either **downgrade its position size** or **exclude it** from the top‑4 list to avoid tier inflation.  

3. **Limit sector exposure** – Cap **auto‑sector exposure** (ARCI + RODA) to **≤ 20 %** of the total allocated capital for this breakout strategy. Consider swapping one auto pick for a **non‑correlated** sector (e.g., consumer staples or utilities) to mitigate sector‑specific tail risk.
