# Hermes Review — 2026‑10‑01  

## 1. Sanity Check (math + logic)  

- **WIFI**: ✓ clean on math (TP +5 % vs SL ‑2 % → R/R = 2.5). **Issue** – No R/R disclosed; SL set at a flat ‑2 % rather than a technical support level. Conviction “High” is not justified by a single RSI signal.  
- **WMUU**: ✓ clean mathematically. **Issue** – SL again a flat ‑2 %; no mention of nearby support. “High” conviction mismatches a win‑rate of only 53.8 % and a modest 8.2 % edge.  
- **KAQI**: ✓ clean mathematically. **Issue** – Same flat‑2 % SL; “High” conviction despite a 60 % win‑rate and only five historic trades (thin sample).  
- **ESIP**: ✓ clean mathematically. **Issue** – Medium conviction but win‑rate 42.9 % (below break‑even). R/R still 2.5, but no justification for TP level.  
- **BRMS**: ✓ clean mathematically. **Issue** – Medium conviction with a strong 71.4 % win‑rate, yet TP set at a generic +5 % rather than a concrete resistance.  
- **MINA**: ✓ clean mathematically. **Issue** – Medium conviction, 50 % win‑rate (coin‑flip). Flat SL/TP ignores price structure.  
- **RAJA**: ✓ clean mathematically. **Issue** – Medium conviction, 64.3 % win‑rate, but again flat levels.  
- **ENRG**: ✓ clean mathematically. **Issue** – Claims “strongest Sharpe‑weighted signal” yet still uses the same flat ‑2 % SL and +5 % TP as pure RSI picks; mismatch between signal strength and risk‑reward framing.  
- **ASHA**: ✓ clean mathematically. **Issue** – Medium conviction, low edge (2.5 %). Flat SL/TP.  
- **GJTL**: ✓ clean mathematically. **Issue** – Medium conviction, high win‑rate (70 %) but TP not tied to any identified resistance.  
- **CBDK**: ✓ clean mathematically. **Issue** – Low conviction but still a flat ‑2 % SL; edge only 1.6 % – R/R = 2.5 is acceptable but the risk‑adjusted edge is marginal.  
- **PANI**: ✓ clean mathematically. **Issue** – Low conviction, edge 1.4 % (barely above noise). Flat SL/TP; no support/resistance justification.  

**Overall Tier Consistency** – The author inflates “High” conviction for three RSI‑only picks (WIFI, WMUU, KAQI) despite modest win‑rates and thin historical samples. Conversely, “Medium” tags are applied to picks with comparable or better win‑rates (BRMS, RAJA) without clear differentiation.  

## 2. Contradiction Hunter  

1. **WIFI vs. WMUU vs. KAQI** – All three are labeled **High** conviction yet each relies solely on an RSI < 30 signal. No additional bullish confirmation (e.g., volume, trend, chart pattern) is presented, contradicting the “high‑conviction” label.  
2. **ENRG** – The author states it has the “strongest Sharpe‑weighted signal” (volume breakout) but still assigns it the same flat ‑2 % SL and +5 % TP as pure RSI picks, ignoring the stronger signal that would merit a tighter stop or a larger upside target.  
3. **BRMS** – Win‑rate 71.4 % is higher than the “high‑conviction” picks, yet it is only given a **Medium** conviction, creating an internal inconsistency between performance evidence and conviction rating.  

## 3. Hidden Risks  

- **Sector concentration** – Six of the twelve picks (WIFI, WMUU, KAQI, ENRG, BRMS, MINA) belong to the broader **energy & commodities** umbrella (telecom‑related, mining, power, etc.). A sector‑wide reversal would simultaneously hit a large portion of the suggested portfolio, inflating sector VaR.  
- **Liquidity risk** – Several low‑conviction stocks (CBDK, PANI, ASHA) trade below 100 k shares average daily volume. Position sizing is not disclosed, but a 5‑20 day hold with a flat ‑2 % SL could be breached by normal intraday slippage, turning a modest edge into a loss.  
- **Correlation / clustering** – All picks are triggered by the same **RSI‑oversold** condition. This creates a hidden correlation: a market‑wide rebound would benefit all, but a continued down‑trend would hurt the entire basket simultaneously. The analysis does not address this clustering risk.  
- **Timing / chase risk** – The author proposes entry zones that sit **already 2 % above** the current price for many stocks (e.g., WIFI entry 1,635 ≈ current price). If the price is already moving upward, the trade may be “late” and the 2 % SL could be hit quickly on a short‑term pull‑back.  
- **Stale indicator risk** – RSI is a lagging momentum oscillator. The analysis does not mention the look‑back period or whether the RSI calculation window has been adjusted for recent volatility spikes (e.g., after earnings). A sudden volatility surge could render the RSI‑oversold signal obsolete.  
- **Indicator overlap** – The entire list relies on a single indicator (RSI) plus a generic volume breakout for ENRG. No diversification of signal types (e.g., trend, volatility, order flow) is present, meaning the “confluence” is illusory.  

## 4. What the Author Got Right  

The author correctly identified that a **sub‑30 RSI** can historically generate a modest positive edge (average 2‑5 % across the sample set) and transparently disclosed the historical win‑rate and edge for each ticker, providing a clear quantitative baseline for the suggested trades.  

## 5. Critical Recommendations  

1. **Redefine stop‑loss levels** – Replace the flat ‑2 % SL with **structure‑based stops** (nearest support, ATR‑based volatility stop, or a percentage tied to recent swing lows). This will align risk with actual market geometry and prevent arbitrary stop‑loss breaches.  
2. **Re‑calibrate conviction tiers** – Downgrade “High” conviction for pure‑RSI picks (WIFI, WMUU, KAQI) to **Medium** unless additional bullish confirmations are added. Conversely, upgrade BRMS (and possibly ENRG) to “High” given its superior win‑rate and sector‑specific edge.  
3. **Diversify signal sources and sector exposure** – Trim the portfolio to a maximum of **30 % exposure** to the energy/commodity cluster and introduce at least two picks driven by **different technical signals** (e.g., moving‑average cross, volume‑price trend, or macro‑fundamental catalyst). This will mitigate the hidden correlation risk inherent in a pure‑RSI‑driven basket.
