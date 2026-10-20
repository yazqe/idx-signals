# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **BNBR**: ✓ clean  
- **WIFI**: ✓ clean  
- **WMUU**: ✓ clean  
- **KAQI**: ✓ clean  
- **PACK**: ✓ clean  
- **DEWA**: ✓ clean  
- **RAJA**: ✗ R/R math error — stated combined edge “~10.5%” implies TP = 10.5% above entry, but TP is set at +14%. R/R = (14)/(7) = 2.0, not 10.5. 10.5% is the *expected return*, not R/R. Mislabeling risk-reward as expected return is dangerous.  
- **BUVA**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **GTSI**: ✓ clean  
- **BREN**: ✓ clean  
- **BUMI**: ✓ clean  
- **PTRO**: ✗ SL placement arbitrary — SL at -8% below close, but entry zone is 2980–3050 (2.3% range). SL is placed at 2784–2814, which is 6.5–7.8% below *entry*, not “below close.” If close is 3050, SL = 2806 (8% down). But if entry is 2980, SL = 2742 (8% down). SL is not anchored to a structural level (e.g., prior swing low, VWAP, volume node) — it’s a flat %, ignoring price context.  
- **All picks**: ✗ SL consistently set at -7% or -8% — no variation based on volatility, ATR, or support structure. This is a mechanical, arbitrary rule, not risk management.  
- **All picks**: ✗ TP set as fixed % above entry — no reference to resistance, prior highs, Fibonacci, or volume clusters. TP is arbitrary, not technical.  
- **All picks**: ✗ Conviction tier inflated — 5+ picks with conviction “High” based on RSI oversold alone, with n < 15 (KAQI: n=5, BUVA: n=10, PTRO: n=11). Conviction “High” requires robust statistical and structural evidence — this is data mining with small samples. Tier inflation is rampant.  
- **All picks**: ✗ Historical edge claims are misleading — “edge” is not defined. Is it mean return? Sharpe? Profit factor? No methodology disclosed. 12.67% “edge” over 36 trades? That’s an average return, not an edge. Edge implies statistical advantage over random. No baseline comparison (e.g., buy-and-hold) provided.  

## 2. Contradiction Hunter

1. **Location**: “Volume-driven RSI oversold confluences are dominating today’s buy signals... Vol_breakout_up remains the most reliable standalone signal for 20d holds.” — **Contradiction**: BNBR and WIFI are listed as top picks due to “dual trigger” (vol + RSI), yet the Market Read claims vol_breakout_up alone is “most reliable.” Why then include RSI in 12/14 picks? If vol alone is most reliable, why not pick 10 vol-only trades? Contradictory prioritization.  
2. **Location**: “Negative RSI signals remain dangerous — avoid them unless triple-triggered.” — **Contradiction**: 12 of 14 picks are triggered by RSI oversold alone (no volume, no other indicator). Yet author says RSI alone is dangerous unless triple-triggered. This is a direct contradiction — author is recommending the exact thing they warn against.  
3. **Location**: RAJA entry: “strongest confluence among medium-tier tickers” — **Contradiction**: RAJA has dual triggers (vol + RSI), same as BNBR and WIFI, yet RAJA is downgraded to “Medium confluence” while BNBR/WIFI are “High.” No justification given for differential treatment. Arbitrary tiering.  
4. **Location**: BUVA: “Exceptional 90% win rate on RSI oversold — highest in dataset” — **Contradiction**: PTRO has 63.6% win rate with RSI 15.5 (“extreme oversold”), yet BUVA’s 90% win rate is based on only 10 trades. PTRO’s RSI is more extreme, yet lower conviction. Inconsistent logic: extreme RSI should warrant higher conviction, not lower.  
5. **Location**: PTRO: “high price but strong reversal history justifies inclusion” — **Contradiction**: BREN (price 1930–1970) also has “high price” and “institutional interest,” yet is rated Medium. PTRO priced 3x higher than BREN, yet same conviction logic applied inconsistently.  

## 3. Hidden Risks

- **Sector concentration**: 11/14 picks (79%) are in non-financial sectors with high retail participation (mining, materials, consumer goods). No bank or utility exposure. If commodity prices (coal, metals) reverse — which drives BNBR, WIFI, PACK, BUMI — entire portfolio could drop 15–25% in one day. Single-day VaR >20% likely.  
- **Liquidity risk**: PTRO (2980–3050) has avg daily volume likely <500k shares (typical for IDX high-price stocks). Proposed position size not stated, but if >10k shares traded, slippage >3% likely on entry/exit.  
- **Correlation**: BNBR, WIFI, PACK, BUMI all exposed to coal/mining. KAQI and WMUU are in materials. BUVA and KOTA are consumer discretionary with overlapping retail buyer base. These are not diversified — they’re a single commodity/retail sentiment bet disguised as diversification.  
- **Timing**: BNBR closed at 54 (top of entry zone). WIFI closed at 1120 (top of entry). PTRO closed at 3050 (top of entry). All are trading at upper bounds of entry zones — high risk of gap-down if market pauses.  
- **Stale data**: “Historical edge” claims — no training window disclosed. If training data includes 2021–2022 (post-pandemic liquidity surge), and current regime is 2024 (tightening, lower volatility), the edge is stale. RSI oversold signals have lower win rates in low-vol regimes.  
- **Indicator overlap**: RSI oversold is the trigger for 12/14 picks. Vol_breakout_up is only in 5. “Confluence” is a lie — 85% of signals are the same indicator (RSI). False confluence. SMC, DA8, Markov not even mentioned in triggers — irrelevant to this analysis.  

## 4. What the Author Got Right

The author correctly identified that RSI oversold + volume surge can generate short-term mean-reversion edges in IDX mid-caps — and the historical win rates (where n>20) do show marginal statistical edge over random. The focus on volume as a filter is valid.

## 5. Critical Recommendations

1. **Reduce all RSI-only picks to Medium conviction** — KAQI (n=5), BUVA (n=10), PTRO (n=11), GTSI (n=15) — their “High” conviction is statistically indefensible. Downgrade to Medium or Low.  
2. **Replace flat % SL/TP with structural levels** — SL must be below nearest swing low or 20-day ATR. TP must align with prior resistance or 1.618 Fibonacci extension. Arbitrary 7–8% SL is gambling, not trading.  
3. **Cap sector exposure at 40%** — BNBR, WIFI, PACK, BUMI, KAQI, WMUU are all mining/materials. Reduce total allocation to these 6 to ≤40% of portfolio. Add at least 2 non-correlated picks (e.g., bank, telco) to reduce single-sector VaR.
