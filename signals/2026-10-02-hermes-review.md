# Hermes Review — 2024‑10‑02  

## 1. Sanity Check (math + logic)  

- **WIFI**: ✓ clean (R/R ≈ 2.0, SL = ‑3 % of close, TP = +6 %).  
- **WMUU**: ✓ clean (R/R ≈ 2.0).  
- **KAQI**: ✓ clean.  
- **ESIP**: ✓ clean.  
- **BRMS**: ✓ clean.  
- **MINA**: ✓ clean.  
- **BREN**: ✓ clean.  
- **RAJA**: ✓ clean.  
- **ASHA**: ✓ clean.  
- **GJTL**: ✓ clean.  
- **PANI**: ✓ clean.  

**Issues identified**  
- **SL placement** – All stops are a flat “‑3 % below close” with no reference to technical support, trend‑line, ATR, or volatility. This is an arbitrary percentage rule, not a structure‑based stop.  
- **TP placement** – All targets are a flat “+6 % above close” with no identified resistance, Fibonacci, or profit‑taking zone. The reward is therefore a mechanical 6 % rather than a price‑level‑driven target.  
- **Conviction tier inflation** – “High” conviction is assigned to **WIFI**, **WMUU**, **KAQI** despite only 5‑13 back‑tested trades each (9.3 %, 8.2 %, 8.0 % edge). A high tier should require a larger sample size and a statistically significant edge; the current evidence is thin.  
- **Medium tier over‑use** – Seven picks are labelled “Medium” but the only justification is a modest edge (2.4‑4.5 %) and a win‑rate that ranges from 42.9 % to 71.4 %. The win‑rate alone does not justify a medium conviction when the edge is marginal.  
- **Low tier mis‑labelled** – **PANI** is marked “Low” despite a positive edge (1.4 %) and a win‑rate above 55 %. If the edge is positive and the win‑rate >50 %, a low conviction is inconsistent with the other criteria used for the high‑conviction picks.  

## 2. Contradiction Hunter  

1. **Conviction vs. Evidence** – The analysis states “high tier with solid edge and win‑rate” for **WIFI**, **WMUU**, **KAQI**, yet the sample sizes (5‑13 trades) are far below what would be required for statistical confidence. This contradicts the implied robustness of a “high” rating.  
2. **Uniform RSI‑oversold trigger** – Every pick is triggered solely by an RSI‑oversold signal, yet the analysis presents them as a diversified basket. Using a single indicator for all entries creates internal inconsistency: the implied diversification is superficial because the same trigger will likely fire simultaneously across the basket, exposing the portfolio to a common false‑positive risk.  

## 3. Hidden Risks  

- **Sector concentration** – A quick ticker lookup shows that **WMUU**, **MINA**, **BREN**, **RAJA**, and **PANI** are all heavily weighted toward the mining & commodities sector. This creates a sector‑bias > 40 % of the suggested basket, leaving the portfolio vulnerable to a sector‑wide reversal (e.g., commodity price shock).  
- **Liquidity risk** – Several low‑priced tickers (**WMUU** at ~27 IDR, **KAQI** at ~79 IDR, **ASHA** at ~40 IDR) have historically thin average daily turnover. Position sizing based on a flat 3 % stop could easily exceed 5 % of daily volume, leading to slippage or inability to exit cleanly.  
- **Correlation risk** – All picks are based on the same RSI‑oversold condition, meaning they will likely cluster in price action. Correlated entries inflate portfolio risk despite the appearance of a “basket” of ideas.  
- **Timing / chase risk** – If any of these stocks have already rallied > 15 % today (common for oversold rebounds), the entry zone (±1 % around current price) may already be on the tail of the move, turning the trade into a chase rather than a mean‑reversion. No price‑trend filter is applied to avoid this.  
- **Stale data / regime shift** – RSI is a momentum oscillator that can remain oversold for extended periods in a down‑trend. The analysis does not verify whether the broader market regime (e.g., a bearish macro environment) supports a rebound, risking false‑positive signals.  
- **Indicator overlap** – The entire list relies on a single indicator (RSI‑oversold). There is no independent confirmation (e.g., volume surge, MACD cross, or fundamental catalyst). The confluence claim is therefore illusory.  

## 4. What the Author Got Right  

The author correctly identified that a subset of the basket (**BRMS**, **GJTL**, **BREN**) exhibits relatively high win‑rates (> 66 %) despite modest edges, indicating that the RSI‑oversold condition has historically produced a positive expectancy for these particular securities.  

## 5. Critical Recommendations  

1. **Re‑calibrate stop‑losses** – Replace the flat ‑3 % rule with a structure‑based stop (e.g., below the nearest swing low, ATR‑based multiple, or a clear support level) for each ticker to avoid arbitrary risk sizing.  
2. **Trim sector exposure** – Reduce the mining/commodity weight to ≤ 20 % of the basket. Replace excess mining picks with stocks from unrelated sectors (e.g., consumer, technology, finance) that also meet the RSI‑oversold criteria but add true diversification.  
3. **Add independent confirmation** – Require at least one additional signal per ticker (e.g., volume spike, bullish candlestick pattern, or positive earnings surprise) before assigning a “high” conviction. This will filter out false‑positive RSI oversold alerts and align conviction levels with the strength of the multi‑factor setup.
