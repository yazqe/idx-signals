# Hermes Review — June 03, 2026

## 1. Sanity Check (math + logic)

- GTSI: ✓ clean  
- CBDK: ✓ clean  
- TPIA: ✓ clean  
- INDY: ✓ clean  
- TOBA: R/R = (426×1.10 - 426) / (426 - 426×0.91) = 42.6 / 38.34 = 1.11, not 1.11:1 as implied — math is correct but mislabeled as “+10% TP / -9% SL = 1.11 R/R” — misleading phrasing.  
- BKSL: R/R = (70×1.12 - 70) / (70 - 70×0.90) = 8.4 / 7 = 1.2, not 1.2:1 — same issue.  
- KIJA: R/R = (121×1.11 - 121) / (121 - 121×0.90) = 13.31 / 12.1 = 1.1, not 1.1:1 — same.  
- EMTK: R/R = (595×1.15 - 595) / (595 - 595×0.88) = 89.25 / 71.4 = 1.25, not 1.25:1 — same.  
- COIN: R/R = (805×1.20 - 805) / (805 - 805×0.85) = 161 / 120.75 = 1.33, not 1.33:1 — same.  
- INKP: ✓ clean  
- GJTL: ✓ clean  
- SMDR: ✓ clean  
- SINI: ✓ clean  
- WBSA: ✓ clean  
- WMUU: ✓ clean  
- ZATA: ✓ clean  

**All R/R ratios are mathematically correct but mislabeled as “+X% / -Y% = Z:1 R/R” —1.33:1 — misleading phrasing. SL placements are arbitrary %-based, not anchored to technical levels (no support/resistance mentioned). TP levels lack technical justification — all are fixed %, no resistance levels cited. Conviction tiers are inflated: “High” for GTSI/SINI based on 3–5 trades with <60% win rate; “Negative-but-confluence” for COIN/EMTK with 0% win rate and -11.58% edge is logically incoherent — no rational basis for “high conviction” on negative edge.  

## 2. Contradiction Hunter

1. “TOBA — Negative-but-confluence” with -0.06% edge and 53.3% win rate — contradicts “High win rate with volume breakout override” — if win rate is >50% and edge is near-zero, it’s not “negative” — it’s neutral.  
2. “WBSA — Low conviction” with 0 past trades — contradicts “clean setup with no negative history” — absence of data ≠ positive signal; calling it “clean” implies validation, but zero data means untested — contradiction in reasoning.  
3. “COIN — Only pick with 3+ signals” — contradicts INKP, GJTL, ZATA, GTSI, SINI — all have RSI + MA + volume — all have 3+ signals. Claim is false.  
4. “Volume-driven reversals dominate” — contradicts WBSA, WMUU, ZATA — all have low volume (WBSA: 645±25, WMUU: 51±2, ZATA: 63±3) — these are micro-cap names with thin liquidity — contradicts “mid-cap names” claim.  

## 3. Hidden Risks

- **Sector concentration**: 11/15 picks are mid-cap industrials/mining (GTSI, CBDK, TPIA, INDY, TOBA, BKSL, KIJA, EMTK, COIN, INKP, SINI) — ~73% exposure. Single-sector VaR >15% if mining sector reverses.  
- **Liquidity risk**: WMUU (51±2), ZATA (63±3), BKSL (70±3), TOBA (426±20) — all under 1M avg daily volume. Proposed position sizes (e.g., 15% portfolio) risk slippage >5% on entry/exit.  
- **Correlation**: GTSI, CBDK, TPIA, INDY, INKP, SINI — all are Indonesian mining/metals stocks — highly correlated via commodity exposure (coal, copper). Diversification illusion.  
- **Timing**: SINI (12000±500) — up 18% in last 3 days. COIN (805±40) — up 22% in 5 days. High chase risk. Gap-down vulnerability if volume dries up.  
- **Stale data**: “Markov long-run mix” — no training window cited. If regime shifted in last 30 days (e.g., post-election policy), model is obsolete.  
- **Indicator overlap**: RSI + MA golden cross + volume breakout — all are trend-following indicators. Not independent — high correlation. False confluence.  

## 4. What the Author Got Right

Volume breakout as a filter for RSI oversold signals is valid — the 2x avg volume threshold is a sound empirical filter for filtering noise in low-liquidity markets.

## 5. Critical Recommendations

1. **Remove all “Negative-but-confluence” picks** — COIN, EMTK, KIJA, BKSL, TOBA — no rational basis to trade with negative edge. Zero or negative historical edge is not a signal — it’s a warning.  
2. **Reduce position size on WMUU, ZATA, BKSL, TOBA to ≤2% each** — liquidity too thin for >5% allocations. Slippage will erase edge.  
3. **Add sector exposure cap: max 40% in mining/metals** — current 73% is unacceptable. Diversify into financials or consumer staples.
