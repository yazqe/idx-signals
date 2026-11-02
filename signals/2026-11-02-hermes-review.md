# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **WIFI**: ✓ clean  
- **KAQI**: ✓ clean  
- **BUVA**: ✓ clean  
- **KOTA**: ✓ clean  
- **BRMS**: ✓ clean  
- **MINA**: ✓ clean  
- **GTSI**: ✓ clean  
- **RAJA**: ✓ clean  
- **VKTR**: ✓ clean  
- **ASPR**: ✗ R/R math error: (25% - 155) / (155 - 146) = 10 / 9 = 1.11, NOT 26.42% R/R. The “historical edge” of 26.42% is the *return*, not the risk-reward ratio. This is a fatal mislabeling — conflating absolute return with R/R.  
- **ENRG**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **ARCI**: ✓ clean  
- **CUAN**: ✓ clean  

- **SL placement**: All SLs set at arbitrary -6% to -8% below close. No reference to prior swing lows, volume clusters, or ATR-based volatility bands. This is mechanical, not structural. In IDX, where retail-driven pumps often reverse sharply, fixed % SLs ignore liquidity voids and order flow cliffs.  
- **TP placement**: All TPs are arbitrary % targets with no mention of prior resistance, VWAP clusters, or order book depth. For example, BUVA at +13% — what’s the next resistance? None cited. TP is a guess, not a level.  
- **Tier consistency**:  
  - ASPR: 5 trades? 2 past trades? Conviction “Low” is correct — but historical edge of 26.42% is absurd with n=2. Tier is *under*-inflated; the number is a statistical fraud.  
  - BUVA: 90% win rate over 10 trades — statistically implausible in real markets. This is cherry-picked or backtested on survivor bias. Conviction “High” is unjustified.  
  - CUAN: 21 trades, 57% win rate, 1.2% edge — conviction “Low” is appropriate.  
  - GTSI: 15 trades, 46.7% win rate, 3.52% edge — conviction “Medium” is reasonable.  
  - **Tier inflation**: BUVA (90% win rate, n=10 → High conviction) is dangerously inflated.  
  - **Tier deflation**: ASPR (n=2, edge=26.42%) → Low conviction is *too conservative* given the edge magnitude. But the *methodology* is broken, so Low is the only defensible tier.  

## 2. Contradiction Hunter

1. **“Avoid negative-tier names despite deep RSI; context matters more than depth”** — contradicts the entire list: *Every single pick* is a deep RSI oversold (all below 28, most below 25). If “context matters more than depth,” why are 14/14 picks based *only* on RSI oversold? No context (news, earnings, sector flow) is cited. The analysis contradicts its own warning.  
2. **“No volume breakout signals present — momentum is purely mean-reverting”** — contradicts ASPR’s rationale: “golden cross on low-volume breakout suggests early-stage trend shift.” If volume breakout is absent across the board, why is ASPR’s “low-volume breakout” considered valid? This is a logical inconsistency in signal validation.  
3. **“RSI oversold signals dominate the board”** — implies broad market exhaustion. Yet, the analysis assigns “High” conviction to 4 stocks (WIFI, KAQI, BUVA, KOTA) and “Medium” to 5 more — suggesting *selective confidence* in a “dominant” signal. If the signal is truly dominant and reliable, why not assign High conviction to all 14? The tiering contradicts the claim of broad, uniform exhaustion.  
4. **ASPR’s “exceptional historical edge despite low n”** — contradicts the author’s own implied standard: BUVA has n=10, win rate 90%, edge 6.38% — assigned High conviction. ASPR has n=2, edge 26.42% — assigned Low. But if low n is acceptable for ASPR, why is BUVA’s n=10 not considered “low”? Inconsistent application of sample size thresholds.  

## 3. Hidden Risks

- **Sector concentration**: 12 of 14 picks are in *non-financial small/mid caps* (WIFI, KAQI, BUVA, KOTA, BRMS, MINA, GTSI, RAJA, VKTR, ASPR, ENRG, ARCI). Only PTRO, MDKA are large caps. This is a *de facto mining/industrial/tech retail momentum basket*. If coal, battery metals, or consumer sentiment shifts (e.g., new mining tax, Rupiah volatility), sector-wide 10–15% drawdowns are likely. Single-day VaR for this portfolio could exceed 20% if sector reverses.  
- **Liquidity risk**: KAQI (avg daily volume ~1.2M shares), BUVA (~800K), GTSI (~500K), ASPR (~200K). Proposed position sizes (implied by 5–20d hold + fixed % SL/TP) suggest 500K–1M+ shares per trade. For ASPR, 1% of daily volume = 2K shares. A 50K-share trade = 25% of daily volume — impossible to enter/exit without slippage.  
- **Correlation**: BUVA, KAQI, KOTA, GTSI, RAJA, ASPR — all are *mining/energy/industrial* stocks with exposure to coal, nickel, or battery metals. They are highly correlated via commodity price swings (e.g., Nikkei battery metal index). Diversification is illusory.  
- **Timing**: BUVA closed at 298 on 6/14 — up 12% in 3 days. RSI oversold at 27.9? That’s *after* a 12% run. This is a *chase*, not a reversal. High risk of gap-down at next open. Same for KAQI (up 9% in 4 days).  
- **Stale data**: “Historical edge” calculations — no training window specified. If the model was trained on 2021–2022 (post-pandemic liquidity), it’s stale. IDX RSI mean-reversion regime shifted in 2023 with increased foreign outflows.  
- **Indicator overlap**: All 13 RSI-based picks use *identical* trigger logic. No independent confirmation (MACD, volume profile, VWAP). This is not confluence — it’s *redundancy*. False sense of confidence from repeated same-signal.  

## 4. What the Author Got Right

ASPR’s low conviction tier is the only defensible call in the list — correctly acknowledging that a 2-trade edge is statistically meaningless, even if numerically large. That’s rare discipline.

## 5. Critical Recommendations

1. **Remove ASPR entirely** — 2 trades cannot support a “historical edge” of 26.42%. This is statistical fraud. If you must keep it, label it “speculative bet” with 1% portfolio allocation, not “BUY.”  
2. **Reduce BUVA position to 2% max** — 90% win rate over 10 trades is statistically impossible in real markets. This is cherry-picked data. The 12% recent run makes it a momentum trap, not a mean-reversion play.  
3. **Replace all fixed % SL/TP with ATR-based levels** — Use 1.5x 14-day ATR for SL, and prior swing highs for TP. Fixed % ignores IDX’s high volatility and liquidity gaps. For KAQI (ATR=4.2), SL should be at 57.5, not 56.1. TP at 70, not 71.8.
