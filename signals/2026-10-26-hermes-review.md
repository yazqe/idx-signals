# Hermes Review — 2024-06-15

## 1. Sanity Check (math + logic)

- **WIFI**: ✓ clean  
- **BUVA**: ✓ clean  
- **BRMS**: ✓ clean  
- **GTSI**: ✓ clean  
- **BIPP**: ✓ clean  
- **PTRO**: ✓ clean  
- **MDKA**: ✓ clean  
- **CUAN**: ✓ clean  
- **MBMA**: ✓ clean  
- **GOTO**: ✓ clean  
- **NICL**: R/R math error. TP = +7%, SL = -8%. R/R = 7/8 = 0.875, but implied R/R is >1 (stated as “confluence” implies positive expectation). Mismatched narrative.  
- **IMPC**: R/R math error. TP = +8%, SL = -8%. R/R = 1.0, but historical edge is -0.94%. Contradiction: positive R/R claimed via confluence, but backtest shows net loss.  
- **INET**: R/R math error. TP = +7%, SL = -8%. R/R = 0.875. Historical edge = -3.13%. Stated as “oversold exhaustion” — but R/R <1 and negative edge make this a negative expectancy trade disguised as “confluence.”  
- **All picks**: SL placement is arbitrary -8% or -7% across all stocks. No reference to ATR, prior swing lows, volume clusters, or support zones. SL is a fixed %, not a structural level — violates risk management best practices.  
- **All picks**: TP is fixed % (7–15%) with no mention of resistance levels, prior highs, or volume profile targets. TP is arbitrary, not technical.  
- **Conviction tiers inflated**:  
  - WIFI: 5⭐ for 9.3% edge over 10 trades — sample size too small to claim “high conviction.” Statistical noise likely dominates.  
  - BUVA: 5⭐ for 8.67% edge over 37 trades with 45.9% win rate — negative expectancy? Win rate <50% with positive edge? Math inconsistency. (See Contradiction Hunter #2)  
  - NICL, IMPC, INET: “Negative-but-confluence” conviction is a contradiction in terms. Conviction cannot be “negative” and still be a “BUY.” Tier mislabeling.  
- **Tier deflation**: PTRO, MDKA, CUAN, MBMA, GOTO — all have win rates >50% and positive edge (except GOTO), yet rated “Low.” Inconsistent with historical performance. GOTO has 36.4% win rate but low edge — should be “Low,” but others with better stats are also Low — tier system is incoherent.

## 2. Contradiction Hunter

1. **BUVA**: “Historical edge: 8.67% over 37 past trades (win rate 45.9%)” — if win rate is <50%, how is edge positive? Edge = (win rate × avg win) - (loss rate × avg loss). For edge to be +8.67% with 45.9% win rate, avg win must be ~15.8% and avg loss ~10.2% — but TP is only 14% and SL is 7%. Mathematically impossible under given TP/SL. Contradiction: stated edge cannot be achieved with stated TP/SL.  
2. **NICL/IMPC/INET**: “Negative-but-confluence” conviction rating contradicts “BUY” recommendation. You cannot “BUY” a stock with negative historical edge and call it “conviction.” This is not confluence — it’s gambling with a negative expectation.  
3. **Market Read**: Claims “broad-based technical bounce is underway” due to RSI oversold + volume stabilization — yet INET has -3.13% edge, IMPC -0.94%, NICL -0.65%. How can a “broad-based bounce” occur if 3 of 13 picks have negative historical returns? Contradiction: narrative ignores data.  
4. **Conviction vs. Edge**: BUVA has higher edge than WIFI (8.67% vs 9.3%) but lower conviction? No justification. GOTO has 0.62% edge and low conviction — but PTRO has 1.8% edge and also low conviction. No logic in tier assignment.  
5. **RSI oversold as universal trigger**: All 13 picks triggered on RSI oversold — yet RSI levels vary wildly (18.1 to 29.1). No threshold defined. How is “oversold” operationalized? Arbitrary. Contradiction: if RSI <30 = oversold, why is INET at 29.1 called “extreme” while GTSI at 24.4 is “just below 30”? Inconsistent definition.

## 3. Hidden Risks

- **Sector concentration**: 10 of 13 picks are small/mid-cap Indonesian stocks with no sector disclosure — but 7 are RSI-oversold with low liquidity (GOTO, MBMA, INET, NICL, IMPC, CUAN, GTSI). Likely concentrated in retail/investor sentiment-driven sectors (tech, consumer, mining services). No sector breakdown = unknown single-sector exposure. If mining or consumer discretionary reverses, 60%+ of portfolio could drop 10–15% in one day.  
- **Liquidity risk**: GOTO (23–25) — avg daily volume likely <500k shares (micro-cap). Proposed position size? Not stated, but if >100k shares traded, slippage will crush entry/exit. Same for MBMA, NICL, INET.  
- **Correlation**: All 11 RSI-oversold picks are likely correlated via “market-wide sentiment exhaustion” — not true diversification. If retail traders exit en masse (e.g., due to BCA rate hike), all 11 could gap down together.  
- **Timing**: No data on today’s price action. If any of these stocks (e.g., BUVA, BIPP) already rallied >15% today on volume spike, entering now = chasing. High gap-down risk at next open.  
- **Stale data**: “Historical edge” claims — no training window stated. If backtest used 2020–2022 data, and 2023–2024 saw regime shift to higher volatility and central bank intervention (e.g., BI rate hikes), edge is invalid.  
- **Indicator overlap**: All 11 RSI-oversold picks use the *same* trigger. RSI is not independent of volume or price action — it’s derived from price. Claiming “confluence” of RSI + volume is false — volume spike *causes* RSI oversold. Not confluence. Redundant signals = false confidence.

## 4. What the Author Got Right

The recognition that volume stabilization + extreme RSI can precede mean-reversion in low-volatility environments is empirically valid — and the inclusion of negative-edge stocks to test confluence shows methodological awareness, even if poorly executed.

## 5. Critical Recommendations

1. **Remove all fixed % SL/TP** — replace with ATR-based stops (e.g., 1.5x 14-day ATR) and resistance-based TPs. Current SL/TP are random and violate risk management.  
2. **Rebuild conviction tiers using win rate × edge × sample size** — BUVA’s 45.9% win rate with 8.67% edge is mathematically impossible under given TP/SL. Recalculate or remove.  
3. **Disclose sector exposure and avg daily volume for every pick** — especially GOTO, NICL, INET. If any has avg volume <200k shares and proposed position >50k shares, delete it. No micro-cap trades without liquidity analysis.
