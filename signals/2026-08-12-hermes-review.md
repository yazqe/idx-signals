# Hermes Review — 2026‑08‑12  

## 1. Sanity Check (math + logic)

- **PTRO**: ✓ clean (R/R = (10 %)/(5 %) = 2.0, matches implied 2:1).  
- **HRTA**: ✓ clean (R/R = 2.0).  
- **CUAN**: ✓ clean (R/R = 2.0).  
- **PACK**: ✓ clean (R/R = 2.0).  
- **BREN**: ✓ clean (R/R = 2.0).  
- **CDIA**: ✓ clean (R/R = 2.0).  
- **COIN**: ✓ clean (R/R = 2.0).  
- **EMAS**: ✓ clean (R/R = 2.0).  

**SL placement issues**  
- All eight picks use a flat “‑5 % below close” stop.  No reference to recent support, swing‑low, ATR‑based volatility, or sector‑specific risk. This is an arbitrary percentage stop, not a structural level.  
- PTRO, HRTA, CUAN, BREN, CDIA: the last swing low sits **≈ 2‑3 %** below the current close, meaning the SL is *looser* than a true technical stop and could allow a larger loss than intended.  

**TP placement issues**  
- All picks set TP at **+10 %** regardless of visible resistance, Fibonacci extensions, or earnings‑date catalysts. No price‑level justification is provided, turning every TP into a guess rather than a resistance‑based target.  

**Conviction‑evidence mismatch**  
- **COIN** and **EMAS** are labelled “Untested (confluence present)” yet are given the same 5‑20 d hold horizon and identical R/R as high‑conviction stocks.  No historical edge exists, so the conviction rating is **inflated**.  
- **BREN** and **CDIA** carry *Low* conviction but are still placed in the top‑8 list with the same R/R as high‑conviction picks, creating a **tier deflation** (low conviction but identical risk‑reward).  

**Overall tier consistency**  
- The list treats every ticker as a “BUY” with identical R/R, ignoring the wide spread in historical edge (0.79 % vs 8.33 %). This uniformity masks the true risk‑adjusted attractiveness of each pick.  

---

## 2. Contradiction Hunter

1. **COIN & EMAS – “Untested” vs “Buy”**  
   > *Quote*: “Conviction: Untested (confluence present)”  
   > *Why contradictory*: A “Buy” recommendation implies a positive conviction, yet “Untested” signals no proven edge. The author simultaneously treats them as viable entries while admitting no track record.  

2. **BREN – Low conviction but placed alongside high‑conviction volume breakouts**  
   > *Quote*: “Conviction: Low (but confluence via volume)”  
   > *Why contradictory*: The author still allocates the same position size (implicit) as PTRO/HRTA, despite a win‑rate of **47.6 %** and a meager edge of **1.23 %**. This conflicts with the risk‑adjusted approach implied elsewhere.  

3. **Uniform R/R vs divergent historical edges**  
   > *Quote*: All picks use a 2:1 R/R while historical edges range from **0.79 %** to **8.33 %**.  
   > *Why contradictory*: A rational R/R should scale with edge; a low‑edge trade (CDIA) deserves a tighter R/R or tighter SL, not the same generous 2:1 as a high‑edge trade (PTRO).  

---

## 3. Hidden Risks

- **Sector concentration**:  
  - PTRO, HRTA, CUAN, PACK, BREN, CDIA, COIN, EMAS are all **momentum‑driven** and likely belong to **materials / commodities** (e.g., mining, cement, packaging, metals).  If a macro‑shift hits the commodities sector, the entire portfolio could suffer a >30 % drawdown.  

- **Liquidity risk**:  
  - Several tickers (e.g., COIN at ~IDR 710, EMAS at ~IDR 7,500) are low‑priced, thin‑float stocks.  Without concrete average‑daily‑volume data, a 5‑20 d position could easily exceed 10 % of daily turnover, inviting slippage and market impact.  

- **Correlation risk**:  
  - All eight picks are triggered by **volume breakouts** or **golden‑crosses** on the same day, meaning they are likely to move together on the same market‑wide momentum surge.  The portfolio is effectively a single‑factor bet, not diversified.  

- **Timing / chase risk**:  
  - PTRO, CUAN, BREN, CDIA have already **price jumps of 9‑13 %** on the breakout day.  Entering after such a move raises the probability of a short‑term pull‑back or “buy‑the‑dip” reversal.  

- **Stale data / small sample bias**:  
  - Historical edges are derived from **4‑29 past trades**.  Such small samples are statistically fragile; a 65 % win‑rate on 23 trades (PTRO) has a 95 % confidence interval of roughly **45‑85 %**.  The edge could be a statistical artifact.  

- **Indicator overlap**:  
  - The “vol_breakout_up” signal and “ma_golden_cross” are not independent; a strong volume surge often pushes the short‑term moving average above the longer‑term average, creating **double‑counted** confluence.  The author may be over‑weighting the same underlying price action.  

---

## 4. What the Author Got Right

The analysis correctly spotlights **short‑term momentum** as a repeatable edge in the current market environment, and it quantifies historical performance (edge and win‑rate) for each signal, providing a transparent baseline for back‑tested profitability.  

---

## 5. Critical Recommendations

1. **Re‑calibrate stop‑losses to structural support** – replace the flat ‑5 % rule with a support‑based stop (e.g., recent swing low, ATR‑based multiple, or a key moving‑average).  This will align risk with the actual price‑action landscape and prevent oversized losses on volatile breakouts.  

2. **Scale R/R to historical edge** – for low‑edge picks (CDIA, BREN, COIN, EMAS) tighten the target profit or widen the stop to achieve a **risk‑adjusted R/R ≥ 1.5**.  Conversely, high‑edge picks (PTRO, HRTA, CUAN) can keep the 2:1 ratio.  Uniform R/R inflates risk on marginal trades.  

3. **Cap sector exposure and position sizing** – limit the total allocation to any single commodity‑related sector to **≤ 20 %** of the portfolio.  For the thin‑float tickers, cap individual position size to **≤ 5 %** of daily volume (or use a smaller dollar amount) to avoid market‑impact slippage and concentration risk.
