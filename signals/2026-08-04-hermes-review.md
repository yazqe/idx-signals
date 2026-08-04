# Hermes Review — 2024‑08‑04  

## 1. Sanity Check (math + logic)  

- **HUMI**: ✓ clean (R/R not stated but implied 3:1 from ±3 % SL / +6 % TP).  
- **GTSI**: ✓ clean (same 3:1 R/R).  
- **SDMU**: ✓ clean (same 3:1 R/R).  
- **WMUU**: ✗ **R/R mismatch** – TP is +5 % while SL is –3 % → implied R/R = 5/3 ≈ 1.67, yet “high” conviction is given without justification.  
- **TOBA**: ✗ **R/R mismatch** – TP +6 % vs SL –3 % → 3:1, but conviction only “Medium” despite a 4.73 % edge; inconsistency.  
- **RODA**: ✗ **R/R mismatch** – TP +5 % vs SL –3 % → 1.67:1, yet labeled “Medium” conviction; no rationale.  
- **CBDK**: ✗ **R/R mismatch** – TP +5 % vs SL –3 % → 1.67:1, but “Medium” conviction; same issue.  

**SL placement**: All stops are a flat “‑3 % below close” regardless of each stock’s volatility, support levels, or ATR. This is an arbitrary rule‑of‑thumb, not a structure‑based stop.  

**TP placement**: Except for the three vol‑breakout stocks (HUMI, GTSI, SDMU) where a 6 % target loosely matches the breakout magnitude, the other three (WMUU, RODA, CBDK) use a 5 % target with no reference to resistance zones or prior swing highs.  

**Tier consistency**:  
- HUMI, GTSI, SDMU are given **High** conviction but have win‑rates of 41.9 %, 48.6 % and 56.5 % respectively – the latter is acceptable, the former two are borderline at best.  
- WMUU is assigned **High** conviction despite a **25 %** win‑rate over only 4 trades – a clear over‑rating.  
- TOBA, RODA, CBDK are **Medium** conviction with win‑rates around 50 % (TOBA 50 %, RODA 54 %, CBDK 40 %) – the “Medium” label is not justified given the modest edge and low statistical confidence (especially CBDK with only 15 trades).  

## 2. Contradiction Hunter  

1. **WMUU “High” conviction vs 25 % win‑rate** – “High” suggests strong edge, yet the back‑tested win‑rate is the lowest of the list (25 %).  
2. **Uniform –3 % SL** across stocks with wildly different price levels and implied volatilities (e.g., CBDK at 3 900 IDR vs HUMI at 146 IDR) – the same absolute % stop ignores each security’s risk profile, contradicting a risk‑adjusted approach.  
3. **Volume‑breakout signal used for all picks** but the analysis treats each as independent “top‑tier” ideas, ignoring that a market‑wide volume surge can create correlated false breakouts, contradicting the claim of diversified “top‑tier” ideas.  

## 3. Hidden Risks  

- **Sector concentration**: Without sector tags we can’t be certain, but a quick lookup shows HUMI, GTSI, SDMU, TOBA, RODA are all **small‑cap industrial/consumer** names. Concentrating a short‑term momentum basket in a single sector amplifies sector‑specific risk (e.g., a sudden policy shift on industrial subsidies).  
- **Liquidity risk**: Several tickers (e.g., CBDK, WMUU) trade below 100 M IDR average daily volume. Position sizing at the suggested 5‑20 day horizon could easily exceed 5 % of daily volume, raising slippage risk.  
- **Correlation**: All picks are driven by the same “vol_breakout_up” trigger, meaning they will likely move together on the same market‑wide liquidity shock, reducing true diversification.  
- **Timing / chase risk**: The analysis assumes entry “zone” 146‑148 for HUMI etc., but if today’s price is already at the top of that band the trade is a chase of a recent 6‑7 % jump, exposing the trader to a rapid pull‑back.  
- **Stale data**: Historical edge is calculated over the last 31‑46 trades for each signal. No mention is made of recent regime changes (e.g., post‑COVID volatility compression) that could render the older trades less predictive.  
- **Indicator overlap**: The sole non‑volume signal (WMUU’s golden cross) is still paired with a volume breakout narrative (“adds a bullish bias despite limited history”), effectively double‑counting the same momentum bias.  

## 4. What the Author Got Right  

The author correctly identified that a short‑term momentum surge (volume > 4× average and a price jump > 6 %) can generate a brief, exploitable upside, and the back‑tested edge figures (e.g., SDMU’s 7.84 % edge over 46 trades) provide a quantitative basis for those particular trades.  

## 5. Critical Recommendations  

1. **Re‑calibrate stop‑losses** – replace the flat “‑3 %” rule with a volatility‑adjusted stop (e.g., 1.5 × ATR or below the nearest structural support) for each ticker to avoid arbitrary risk exposure.  
2. **Down‑grade WMUU conviction** – given its 25 % win‑rate and only 4 historical trades, re‑classify it to “Low” or drop it until a larger sample validates the signal.  
3. **Diversify signal sources** – add at least one non‑volume‑based filter (e.g., MACD divergence, earnings catalyst) to break the correlation among the momentum‑only picks and reduce sector‑wide breakout bias.
