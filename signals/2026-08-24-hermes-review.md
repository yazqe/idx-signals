# Hermes Review — 2026‑08‑24  

## 1. Sanity Check (math + logic)

- **SDMU**:  
  - **R/R mismatch** – Using entry ≈ 95, SL ≈ 93.1, TP ≈ 99.8 gives an R/R ≈ 2.53. The analysis never states an R/R figure, so the claim “high‑conviction edge” is unsupported by a disclosed risk‑reward metric.  
  - **SL placement** – A flat “‑2 % below close” is an arbitrary percentage, not anchored to a technical support level (e.g., recent swing low, ATR‑based stop, or trend‑line breach). This makes the stop fragile to normal intraday volatility.  
  - **TP placement** – “+5 % above close” is not tied to any identified resistance zone (previous high, Fibonacci extension, or volume‑profile barrier). The TP appears to be a fixed‑percentage target rather than a price‑based exit.  
  - **Conviction vs evidence** – Conviction is marked **High**, yet the win‑rate is only 40 % over a tiny sample of 5 trades. The evidence density does not justify a 5‑star rating (tier inflation).  

- **COIN**:  
  - **R/R mismatch** – With entry ≈ 865, SL ≈ 847, TP ≈ 908 the R/R ≈ 2.39, again not disclosed.  
  - **SL placement** – Same “‑2 % below close” rule, lacking any support‑based justification.  
  - **TP placement** – “+5 % above close” is not linked to a concrete resistance level.  
  - **Conviction vs evidence** – Conviction is labeled **Untested** (i.e., no historical edge), yet the pick is still presented as a BUY with a full trade plan. This is a clear tier deflation/inflation mismatch.  

- **Overall**: Both picks are mathematically clean (no calculation errors) but suffer from **missing R/R disclosure**, **arbitrary stop‑loss/take‑profit rules**, and **conviction‑evidence mismatches**.  

## 2. Contradiction Hunter

1. **“High‑conviction edge” vs 40 % win‑rate** – The text states:  
   > “High‑conviction edge” for SDMU, but the win‑rate over the last 5 trades is only **40 %**. A high‑conviction label should be backed by a robust win‑rate or a statistically significant edge; the two statements contradict each other.  

2. **“Untested” yet “BUY”** – For COIN the author writes:  
   > “Conviction: Untested (included for confluence)”  
   Yet immediately provides a full entry zone, SL, and TP, effectively treating it as a **trade recommendation**. Declaring a pick “untested” while simultaneously recommending a position is contradictory.  

3. **Golden‑cross dominance vs selective focus** – The market read says:  
   > “Golden‑cross signals dominate today, with SDMU offering a proven high‑conviction edge and COIN presenting a speculative but potentially rewarding breakout.”  
   Yet the author only highlights SDMU for “higher probability” while still allocating capital to COIN, which shares the same signal. If the golden‑cross is truly dominant, the analysis should either filter out low‑confidence signals or explicitly justify why COIN is kept despite being untested.  

## 3. Hidden Risks

- **Sector concentration** – Both SDMU and COIN are driven solely by a **golden‑cross** on the same timeframe, likely placing the portfolio heavily in **momentum‑driven, low‑fundamental sectors** (e.g., mining for SDMU, crypto‑related for COIN). A 2‑stock concentration in a single technical signal inflates sector‑specific VaR; a sector reversal would wipe both positions.  

- **Liquidity risk** – COIN (a relatively obscure ticker) typically trades **< 500 k shares/day** on IDX. Position sizing is not disclosed, but a standard 5 % portfolio allocation could easily exceed 10 % of daily volume, leading to slippage and execution risk.  

- **Correlation risk** – Both picks rely on the same **golden‑cross** trigger, meaning they will likely move together. The portfolio’s exposure to a single signal type (price‑trend crossover) reduces true diversification.  

- **Timing / chase risk** – If either stock has already **gapped up > 10 %** today (common for golden‑cross breakouts), the entry zone (95 for SDMU, 865 for COIN) may already be **behind the market price**, turning the trade into a chase. The analysis does not confirm the current price relative to the entry band.  

- **Stale data / small‑sample bias** – The “historical edge” for SDMU is based on **5 past trades** only. Such a tiny sample is highly susceptible to overfitting and regime‑shift bias; the edge may be stale if market conditions (volatility, macro backdrop) have changed since those trades.  

- **Indicator overlap** – Both picks use **only one indicator** (golden‑cross). There is no secondary confirmation (e.g., volume surge, RSI divergence, MACD histogram). Relying on a single, highly correlated signal inflates false‑positive confidence.  

## 4. What the Author Got Right

The author correctly identified that a **golden‑cross** can act as a short‑term momentum catalyst on the IDX, and they appropriately flagged SDMU as having a **recorded positive edge** (13.42 % over the limited sample), which does suggest a potential short‑term upside if the signal holds.  

## 5. Critical Recommendations

1. **Re‑calibrate stop‑losses** – Replace the flat “‑2 % below close” rule with a **support‑based stop** (e.g., below the most recent swing low, ATR‑based multiple, or a broken trend‑line). This will align risk with market structure and avoid arbitrary stop placement.  

2. **Disclose and justify R/R** – Explicitly calculate and publish the **risk‑reward ratio** for each trade. If the R/R is below 2.0, either tighten the stop or raise the TP, or else downgrade the conviction tier to reflect the weaker risk‑reward profile.  

3. **Prune or re‑classify COIN** – Given the “untested” label, either **remove COIN from the actionable list** or downgrade it to a “watch‑only” status with a **smaller position size** (e.g., < 2 % of capital). This eliminates the contradiction of recommending a trade with no historical edge.
