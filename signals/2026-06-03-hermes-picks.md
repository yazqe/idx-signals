I already have both datasets. Let me analyze them to select the top 10-15 ideas:

Today's RSI oversold signals (from 2026-06-03.json):
- ZATA (high tier, edge_5d: 5.39%, win_5d: 50%, n: 14)
- BRMS (medium tier, edge_5d: 4.12%, win_5d: 71.4%, n: 14)
- GTSI (medium tier, edge_5d: 3.52%, win_5d: 46.7%, n: 15)
- INKP (low tier, edge_5d: 1.81%, win_5d: 44.4%, n: 18)
- ARCI (low tier, edge_5d: 1.64%, win_5d: 44.4%, n: 9)
- CBDK (low tier, edge_5d: 1.55%, win_5d: 61.5%, n: 13)
- TPIA (low tier, edge_5d: 1.53%, win_5d: 52.6%, n: 19)
- PANI (low tier, edge_5d: 1.41%, win_5d: 55.6%, n: 18)
- INDY (low tier, edge_5d: 1.21%, win_5d: 64.3%, n: 14)
- MBMA (low tier, edge_5d: 0.96%, win_5d: 52.4%, n: 21)
- ADMR (low tier, edge_5d: 0.77%, win_5d: 53.3%, n: 15)
- TOBA (negative tier, edge_5d: -0.06%, win_5d: 53.3%, n: 15)
- BKSL (negative tier, edge_5d: -0.16%, win_5d: 38.5%, n: 13)
- ANTM (negative tier, edge_5d: -0- ANTM (negative tier, edge_5d: -0.0054, win_5d: 42.9%, n: 7)
- NICL (negative tier, edge_5d: -0.0065, win_5d: 47.1%, n: 17)
- DEWA (negative tier, edge_5d: -0.0072, win_5d: 50%, n: 10)
- KIJA (negative tier, edge_5d: -0.0081, win_5d: 42.9%, n: 14)
- BUMI (negative tier, edge_5d: -0.0082, win_5d: 50%, n: 14)
- HUMI (negative tier, edge_5d: -0.0189, win_5d: 29.2%, n: 24)
- INET (negative tier, edge_5d: -0.0313, win_5d: 29.4%, n: 17)
- EMTK (negative tier, edge_5d: -0.0367, win_5d: 20%, n: 10)
- COIN (negative tier, edge_5d: -0.1158, win_5d: 0%, n: 7)

Now cross-referencing with ticker_edge.json for multi-strategy confluence:

1. ZATA: RSI oversold (high) + ma_golden_cross (mean_5d: 3.68%, win_5d: 50%, n: 4) + vol_breakout_up (mean_5d: 0.52%, win_5d: 38.7%, n: 31) → Triple confluence!
2. BRMS: RSI oversold (medium) + vol_breakout_up (mean_5d: 3.32%, win_5d: 50%, n: 26) → Double confluence
3. GTSI: RSI oversold (medium) + ma_golden_cross (mean_5d: 1.45%, win_5d: 50%, n: 4) + vol_breakout_up (mean_5d: 9.77%, win_5d: 48.6%, n: 37) → Triple confluence!
4. INKP: RSI oversold (low) + ma_golden_cross (mean_5d: 2.81%, win_5d: 60%, n: 5) + vol_breakout_up (mean_5d: 3.47%, win_5d: 64.3%, n: 14) → Triple confluence!
5. ARCI: RSI oversold (low) + vol_breakout_up (mean_5d: 4.53%, win_5d: 54.1%, n: 37) → Double confluence
6. CBDK: RSI oversold (low) + ma_golden_cross (mean_5d: 4.27%, win_5d: 33.3%, n: 3) → Double confluence
7. TPIA: RSI oversold (low) + ma_golden_cross (mean_5d: -8.55%, win_5d: 20%, n: 5) → Negative confluence, but RSI is strong
8. PANI: RSI oversold (low) + vol_breakout_up (mean_5d: -0.73%, win_5d: 48%, n: 25) → Mixed signals
9. INDY: RSI oversold (low) + ma_golden_cross (mean_5d: 2.24%, win_5d: 60%, n: 5) + vol_breakout_up (mean_5d: 2.52%, win_5d: 43.8%, n: 32) → Triple confluence!
10. MBMA: RSI oversold (low) + vol_breakout_up (mean_5d: -0.19%, win_5d: 54.2%, n: 24) → Double confluence
11. ADMR: RSI oversold (low) + ma_golden_cross (mean_5d: 6.77%, win_5d: 75%, n: 4) + vol_breakout_up (mean_5d: 2.23%, win_5d: 50%, n: 20) → Triple confluence!
12. TOBA: RSI oversold (negative) + ma_golden_cross (mean_5d: -3.92%, win_5d: 20%, n: 5) + vol_breakout_up (mean_5d: 4.73%, win_5d: 50%, n: 34) → Triple confluence with mixed signals
13. BKSL: RSI oversold (negative) + ma_golden_cross (mean_5d: 9.52%, win_5d: 60%, n: 5) + vol_breakout_up (mean_5d: 5.63%, win_5d: 54.3%, n: 46) → Triple confluence with mixed signals
14. ANTM: RSI oversold (negative) + vol_breakout_up (mean_5d: 5.64%, win_5d: 62.5%, n: 24) → Double confluence
15. NICL: RSI oversold (negative) + vol_breakout_up (mean_5d: 7.14%, win_5d: 57.1%, n: 42) → Double confluence

Now selecting the top 15 based on rules:
1. ZATA - Triple confluence, high tier
2. GTSI - Triple confluence, medium tier, best vol_breakout_up performance
3. INKP - Triple confluence, low tier but strong vol_breakout_up and ma_golden_cross
4. INDY - Triple confluence, low tier, highest win rate among low tier
5. ADMR - Triple confluence, low tier, best ma_golden_cross performance
6. BRMS - Double confluence, medium tier, highest RSI win rate
7. ARCI - Double confluence, low tier, strong vol_breakout_up
8. CBDK - Double confluence, low tier, strong RSI win rate
9. MBMA - Double confluence, low tier, strong vol_breakout_up win rate
10. NICL - Double confluence, negative tier, best vol_breakout_up among negatives
11. ANTM - Double confluence, negative tier, strong vol_breakout_up
12. TOBA - Triple confluence, negative tier, but strong vol_breakout_up
13. BKSL - Triple confluence, negative tier, strong ma_golden_cross and vol_breakout_up
14. PANI - RSI oversold with mixed vol_breakout_up performance
15. HUMI - RSI oversold with strong ma_golden_cross (mean_5d: 17.02%, win_5d: 50%, n: 4)

### Market Read
RSI oversold signals are dominating today's landscape with strong multi-strategy confluence emerging from ma_golden_cross and vol_breakout_up patterns. The most compelling opportunities combine RSI with historically high-performing volume breakouts, particularly in GTSI, ZATA, and INDY. Negative-tier stocks with exceptional confluence (BKSL, ANTM, NICL) show surprising resilience, suggesting potential mean-reversion opportunities in oversold conditions.
