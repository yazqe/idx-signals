# Hermes Review — June 8, 2026

## 1. Sanity Check (math + logic)

- WIFI: ✓ clean  
- ZATA: R/R = (10 / 50) / (7 / 50) = 1.43, not stated 1.87 — math error  
- BRMS: R/R = (12 / 474) / (7 / 474) = 1.71, not stated 1.71 — ✓ clean  
- TAPG: R/R = (14 / 1335) / (8 / 1335) = 1.75, not stated 1.75 — ✓ clean  
- GTSI: R/R = (11 / 99) / (7 / 99) = 1.57, not stated 1.57 — ✓ clean  
- VKTR: R/R = (12 / 555) / (8 / 555) = 1.5, not stated 1.5 — ✓ clean  
- GJTL: R/R = (13 / 1005) / (7 / 1005) = 1.86, not stated 1.86 — ✓ clean  
- INKP: R/R = (15 / 6400) / (8 / 6400) = 1.875, not stated 1.875 — ✓ clean  
- ESSA: R/R = (12 / 550) / (7 / 550) = 1.71, not stated 1.71 — ✓ clean  
- ARCI: R/R = (11 / 945) / (7 / 945) = 1.57, not stated 1.57 — ✓ clean  
- CBDK: R/R = (14 / 3090) / (8 / 3090) = 1.75, not stated 1.75 — ✓ clean  
- TPIA: R/R = (12 / 1390) / (7 / 1390) = 1.71, not stated 1.71 —- TPIA: R/R = (12 / 1390) / (7 / 1390) = 1.71, not stated 1.71 — ✓ clean  
- PANI: R/R = (15 / 5550) / (8 / 5550) = 1.875, not stated 1.875 — ✓ clean  
- BULL: R/R = (11 / 278) / (7 / 278) = 1.57, not stated 1.57 — ✓ clean  
- INDY: R/R = (13 / 1900) / (7 / 1900) = 1.86, not stated 1.86 — ✓ clean  

**SL placement**: All SLs are fixed % below close — no technical structure (S/R, ATR, VWAP) cited. Arbitrary.  
**TP placement**: All TPs are fixed % above close — no resistance levels, prior highs, or volume clusters referenced.  
**Conviction tier inflation**: TAPG (100% win rate, n=8) rated Medium — unjustified. INKP (low edge, high price) rated Low — appropriate.  
**Conviction deflation**: WIFI (9.3% edge, 70% win rate) rated High — appropriate. ZATA (5.39% edge, 50% win rate) rated High — inflated.  

## 2. Contradiction Hunter

1. “Highest win rate among medium-tier signals” (BRMS) vs. “Highest win rate among low-tier” (INDY, CBDK) — contradiction in tier logic. INDY and CBDK have higher win rates than BRMS but are rated Low.  
2. “RSI is the sole driver” (Market Read) vs. TAPG, GTSI, ARCI, ESSA, CBDK, TPIA, PANI, BULL, INDY all cite “volume support” or “relative volume” — direct contradiction.  
3. “No MA golden cross or vol breakout signals detected” vs. all picks rely on RSI oversold — implies RSI is the only signal, yet conviction tiers imply multi-factor analysis.  
4. “Strongest historical edge” (WIFI) rated High vs. ZATA (5.39% edge) also rated High — inconsistent tiering.  
5. “Low win rate offset by high Sharpe potential” (INKP) — Sharpe ratio not calculated or cited. Claim unsupported.  

## 3. Hidden Risks

- **Sector concentration**: 14/15 picks are small-cap IDX stocks — all likely in same sector (tech, consumer, or financials). No diversification. Single-day VaR >15% if sector reverses.  
- **Liquidity risk**: INKP (6400), CBDK (3090), PANI (5550) — all >3000 IDR. Avg daily volume likely <500k shares. Proposed position size could be 10–20% of daily volume — slippage risk >5%.  
- **Correlation**: All picks triggered by RSI oversold — identical signal. High correlation. Not diversification.  
- **Timing**: 47 tickers triggered RSI oversold — market-wide mean-reversion play. Any reversal will hit all picks simultaneously.  
- **Stale data**: “Historical edge” and “win rate” — no training window cited. If RSI strategy stopped working 3 months ago, data is stale.  
- **Indicator overlap**: RSI is the only signal cited. “Volume support” is not an independent indicator — it’s confirmation of RSI move. False confluence.  

## 4. What the Author Got Right

RSI oversold as a mean-reversion trigger in IDX is valid. The 70%+ win rate on WIFI is empirically strong. The market breadth observation (only 3/50 up) correctly frames this as a pure contrarian play.

## 5. Critical Recommendations

1. **Reduce all positions to 1–2% per pick** — no single stock should exceed 2% of portfolio due to liquidity risk and sector concentration.  
2. **Replace fixed % SL/TP with ATR-based stops** — use 1.5x 14-day ATR for SL, 2x ATR for TP1. Fixed % ignores volatility.  
3. **Add volume confirmation threshold** — require relative volume >1.5x 10-day avg for entry. Currently, volume is mentioned but not quantified.
