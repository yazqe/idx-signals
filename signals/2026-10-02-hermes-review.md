# Hermes Review — 2024‑10‑02  

## 1. Sanity Check (math + logic)  

- **WIFI:** ✓ clean (mid‑point entry ≈ 1375 → R/R = (1457‑1375)/(1375‑1334) ≈ 2.0).  
- **WMUU:** ✓ clean (mid‑point ≈ 28.0 → R/R ≈ 2.0).  
- **KAQI:** ✓ clean (mid‑point ≈ 78 → R/R ≈ 2.0).  
- **ESIP:** ✓ clean (mid‑point ≈ 94 → R/R ≈ 2.0).  
- **MINA:** ✓ clean (mid‑point ≈ 204 → R/R ≈ 2.0).  
- **BREN:** ✓ clean (mid‑point ≈ 2810 → R/R ≈ 2.0).  
- **RAJA:** ✓ clean (mid‑point ≈ 640 → R/R ≈ 2.0).  
- **ASHA:** ✓ clean (mid‑point ≈ 41 → R/R ≈ 2.0).  
- **GOTO:** ✗ **R/R mismatch** – historical edge is **‑1.7 %** yet the TP/SL still imply a 2:1 reward‑to‑risk. A negative edge should not be paired with a positive R/R without a clear “edge‑adjusted” rationale.  
- **CBDK:** ✓ clean (mid‑point ≈ 3290 → R/R ≈ 2.0).  
- **PANI:** ✓ clean (mid‑point ≈ 4250 → R/R ≈ 2.0).  

**SL placement issues**  
- All SLs are set at a flat **‑3 %** below the assumed “close”. No reference to actual support levels, trendlines, ATR‑based volatility, or recent swing lows. This is an arbitrary percentage stop, which can be too tight for volatile stocks (e.g., WMUU, BREN) and too loose for low‑vol stocks (e.g., GOTO).  

**TP placement issues**  
- All TPs are a flat **+6 %** above the assumed “close”. No mention of upcoming resistance zones, Fibonacci extensions, or earnings‑driven catalysts. The uniform 6 % target ignores the differing price‑action dynamics across the tickers.  

**Conviction‑tier consistency**  
- **High conviction** is assigned to WIFI, WMUU, KAQI despite each having **≤ 10** historical trades backing the edge. That is a **tier inflation** – a 5‑star label for a thin sample.  
- **Medium conviction** is given to six stocks (ESIP, MINA, BREN, RAJA, ASHA, GOTO) even though GOTO’s historical edge is **negative**; the “Untested‑but‑confluence” label does not justify a medium‑tier rating.  
- **Low conviction** is applied to CBDK and PANI, yet they are still listed in the same “BUY” bucket without any risk‑adjusted sizing guidance.  

## 2. Contradiction Hunter  

1. **GOTO’s edge vs. recommendation** – “Historical edge: –1.7 % … despite a high‑Sharpe breakout, we BUY.”  
   *Quote:* “Historical edge: –1.7% … the 98.9× volume surge … provides a rare confluence.”  
   *Why contradictory:* A negative edge means the systematic back‑test predicts a loss; yet the author still recommends a long position, effectively ignoring the back‑test result.  

2. **Conviction language inconsistency** – “High‑conviction tickers (WIFI, WMUU, KAQI) offering the strongest historical edges” versus “Medium‑tier names add breadth, while a rare volume breakout on GOTO provides a high‑Sharpe outlier despite a poor track record.”  
   *Quote:* “The overall bias leans bullish for the short‑to‑mid‑term as multiple confluences surface.”  
   *Why contradictory:* The author simultaneously claims a bullish bias based on “multiple confluences” while acknowledging that the most conspicuous confluence (GOTO) actually has a **negative** edge, undermining the bullish narrative.  

3. **Position sizing vs. conviction** – No sizing guidance is given, yet “High” conviction is used for all three high‑conviction picks. If conviction were truly high, the author would likely allocate a larger capital share, but the uniform 5‑20 day horizon suggests a short‑term scalp where over‑exposure could be dangerous. The omission creates a hidden inconsistency between conviction level and implied risk exposure.  

## 3. Hidden Risks  

- **Sector concentration** – The list is heavily weighted toward **financial‑related tickers** (e.g., WMUU, BREN, RAJA) and **commodity‑linked** names (MINA, GOTO). If a macro‑event hits the banking or commodity sector, the portfolio could suffer a >30 % drawdown in a single day.  

- **Liquidity risk** – Several tier‑1 picks (e.g., WMUU, GOTO, PANI) trade **< 200 k shares/day** on IDX. Using a flat 3 % SL on such thinly‑traded stocks can cause slippage that exceeds the stop‑loss buffer, especially in a volatile breakout scenario.  

- **Correlation risk** – All signals are derived from **RSI‑oversold** conditions. This creates a hidden correlation: a market‑wide rebound or a sudden shift in momentum will move the entire basket together, reducing true diversification.  

- **Timing / chase risk** – The analysis does not check whether any of the stocks have already **gapped up > 15 %** today. Entering at the top of the entry zone after a strong rally could lock in a loss if the price retraces to the RSI‑oversold region.  

- **Stale data / regime shift** – RSI thresholds are static (e.g., 16.5, 4.1). The author does not mention whether the **look‑back window** (14‑day, 21‑day) is still appropriate in a regime where market volatility has spiked. A regime shift could render the oversold signal less predictive.  

- **Indicator overlap** – Apart from GOTO, **all picks rely on the same indicator (RSI oversold)**. The supposed “confluence” for GOTO (volume breakout) is still evaluated using the same RSI metric, meaning the two signals are not independent; the volume surge may simply be a reaction to the same oversold condition.  

## 4. What the Author Got Right  

The author correctly identified that a **massive volume breakout (≈ 99× average)** on GOTO is an outlier event that can generate a short‑term price swing, and they appropriately highlighted the high Sharpe‑ratio nature of that move despite the negative historical edge.  

## 5. Critical Recommendations  

1. **Re‑calibrate SL/TP to market‑based levels** – Replace the flat ‑3 % / +6 % rules with **support‑resistance‑derived stops** (e.g., recent swing low, ATR‑based volatility bands) and **target‑based exits** (e.g., prior swing high, Fibonacci extension). This will align risk‑reward to each stock’s price structure.  

2. **Down‑grade conviction tiers** – Re‑assign “high” conviction only to stocks with **≥ 20 historical trades** and a **win‑rate ≥ 60 %**. WIFI, WMUU, and KAQI should be re‑rated to **medium** given their limited sample size, reducing over‑exposure.  

3. **Trim sector‑concentrated exposure** – Limit the **financial‑sector weight** to **≤ 30 %** of the total allocated capital and add at least two **non‑correlated sectors** (e.g., consumer staples, infrastructure) to the shortlist, thereby mitigating sector‑specific tail risk.
