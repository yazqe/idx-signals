# Hermes Review — 2026‑08‑06  

## 1. Sanity Check (math + logic)

- **HUMI**: ✓ clean (R/R ≈ 2.66, matches 8%/‑3%). SL set at a flat ‑3 % rather than a technical support level – arbitrary. TP is a flat +8 % target, not tied to any identified resistance. Conviction “High” is overstated given a modest win‑rate (41.9 %).  
- **BNBR**: ✓ clean (R/R ≈ 2.66). SL again a blunt ‑3 % rule; no support reference. TP +8 % lacks resistance justification. Conviction “High” despite a win‑rate of 58 % but edge only 12.67 % – still borderline for “high”.  
- **GTSI**: ✓ clean (R/R ≈ 2.66). SL/TP same flat percentages – no structural rationale. Conviction “High” while win‑rate is 48.6 % and edge 9.77 % – thin edge for a high tier.  
- **KOTA**: ✓ clean (R/R ≈ 2.66). SL/TP flat; no support/resistance anchoring. Conviction “High” despite win‑rate just above 50 % and edge 7.11 % – likely tier inflation.  
- **BKSL**: ✓ clean (R/R ≈ 2.66). SL/TP flat; no technical justification. Conviction “High” with win‑rate 54 % but edge only 5.63 % – thin edge for high tier.  
- **ARCI**: ✓ clean (R/R ≈ 2.66). SL/TP flat; price level ~1180 IDR suggests low‑liquidity cap – flat‑% SL may be too wide. Conviction “Medium” but edge 4.53 % and win‑rate 54 % – still modest; tier seems acceptable.  
- **RODA**: ✓ clean (R/R ≈ 2.66). SL/TP flat; no support level. Conviction “Medium” with edge 3.69 % – borderline for even medium tier.  
- **BIPP**: ✓ clean (R/R ≈ 2.66). SL/TP flat; edge 2.71 % – low‑edge for a “Medium” pick; tier likely overstated.  
- **HRTA**: ✓ clean (R/R ≈ 2.66). SL/TP flat; conviction labeled “Low” yet still placed in the same “Buy” list with identical risk parameters – inconsistent treatment.  

**Overall Tier Consistency Issues**  
- All picks use identical ‑3 % SL and +8 % TP regardless of price level, volatility, or chart‑based support/resistance. This uniformity inflates “high” conviction for many marginal edges and deflates “low” conviction for HRTA (same risk‑reward as the rest).  

## 2. Contradiction Hunter

1. **HRTA Conviction vs. Risk Parameters** – Quote: “Conviction: Low (but high volume)”. Yet HRTA receives the same ‑3 % SL and +8 % TP as the high‑conviction picks, contradicting the stated low confidence.  
2. **Uniform R/R vs. Varying Edge** – The analysis treats a 13 % edge (HUMI) and a 1.5 % edge (HRTA) as equally attractive by applying identical R/R, ignoring that a lower edge should demand a tighter SL or higher TP to preserve expectancy.  
3. **Medium‑Tier Picks with Weak Win‑Rates** – BIPP’s win‑rate is exactly 50 % (break‑even) but is still listed as a “Medium” conviction, conflicting with the implied expectation that medium tier requires >50 % win‑rate and >3 % edge.  

## 3. Hidden Risks

- **Sector Concentration**: Six of the nine picks (HUMI, BNBR, GTSI, KOTA, BKSL, HRTA) are mid‑cap Indonesian consumer/industrial stocks heavily correlated with domestic consumption cycles. A sector‑wide shock (e.g., policy tightening on consumer credit) could wipe out >30 % of the suggested portfolio.  
- **Liquidity Risk**: ARCI (price ~1180 IDR) and HRTA (price ~2110 IDR) are low‑priced, low‑volume stocks. A 5 % position could easily exceed 20 % of average daily volume, raising slippage risk, especially with a flat ‑3 % SL that may be breached on a single gap.  
- **Correlation / Over‑Concentration**: All picks are selected on the same “vol_breakout_up” signal, meaning they will likely fire together on a market‑wide volatility surge. This creates a hidden correlation cluster rather than true diversification.  
- **Timing / Chase Risk**: Each ticker has already experienced a price jump of 2‑12 % on the breakout day. Entering after the jump leaves little upside before the +8 % TP is reached, increasing the chance of a pull‑back eroding the expected edge.  
- **Stale Data / Regime Shift**: The “historical edge” is derived from the last 30‑50 trades, but no mention is made of the time window (e.g., pre‑COVID vs. post‑2024 regime). If the underlying market dynamics have shifted, the edge estimate may be stale.  
- **Indicator Overlap**: The sole filter is “vol_breakout_up”. No secondary confirmation (e.g., trend, macro, earnings) is used, so the signal set is not independent – it merely reflects a single volume spike, inflating false confidence.  

## 4. What the Author Got Right

The author correctly identified that a volume‑driven breakout can generate short‑term momentum, and they quantified a historical edge for each signal, providing a transparent back‑test win‑rate that can be useful for a quick‑turnover strategy.

## 5. Critical Recommendations

1. **Redefine SL/TP on a per‑stock basis** – Replace the blanket ‑3 % SL with support‑based stops (e.g., recent swing lows, ATR‑based buffers) and adjust TP to the nearest technical resistance. This will align risk‑reward with each ticker’s volatility profile.  
2. **Trim the portfolio’s sector exposure** – Limit the combined weight of consumer/industrial mid‑cap stocks to ≤ 30 % of the total allocation. Replace excess exposure with unrelated sectors (e.g., utilities, telecom) to mitigate sector‑specific shocks.  
3. **Add a secondary filter for medium/low conviction picks** – Require an additional confirmation (e.g., positive MACD crossover, earnings beat, or macro‑trend alignment) before entering BIPP, ARCI, RODA, and especially HRTA. This will prevent over‑reliance on a single volume breakout and improve the true expectancy of the medium/low tier signals.
