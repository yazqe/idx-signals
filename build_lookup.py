#!/usr/bin/env python3
"""Build per-ticker × strategy edge lookup, merging backtest + live outcomes.

Sources:
- backtest_signals.csv : 2y synthetic backtest (one-time baseline)
- outcomes.csv         : live signals + actual realized returns (growing)

Output: ticker_edge.json with merged stats. Re-run weekly/monthly to keep
the lookup learning from real trades.
"""
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent
BACKTEST_CSV = ROOT / "backtest_signals.csv"
OUTCOMES_CSV = ROOT / "outcomes.csv"
OUT = ROOT / "ticker_edge.json"

BUY_STRATS = ("rsi_oversold", "ma_golden_cross", "vol_breakout_up")

def load_combined() -> pd.DataFrame:
    """Concatenate backtest + outcomes, keeping only BUY strategies."""
    frames = []
    if BACKTEST_CSV.exists():
        bt = pd.read_csv(BACKTEST_CSV)
        bt["source"] = "backtest"
        frames.append(bt[["ticker", "strategy", "ret_5d", "ret_10d", "source"]])
    if OUTCOMES_CSV.exists():
        oc = pd.read_csv(OUTCOMES_CSV)
        if not oc.empty:
            oc["ret_10d"] = pd.NA  # outcomes.csv tracks 1/5/20d, not 10d
            oc["source"] = "live"
            frames.append(oc[["ticker", "strategy", "ret_5d", "ret_10d", "source"]])
    if not frames:
        return pd.DataFrame(columns=["ticker", "strategy", "ret_5d", "ret_10d", "source"])
    df = pd.concat(frames, ignore_index=True)
    return df[df["strategy"].isin(BUY_STRATS)]

def main():
    df = load_combined()
    print(f"Combined: {len(df)} signals "
          f"({(df['source']=='backtest').sum()} backtest + "
          f"{(df['source']=='live').sum()} live)")

    lookup = {}
    for (ticker, strat), g in df.groupby(["ticker", "strategy"]):
        ret5 = g["ret_5d"].dropna()
        ret10 = g["ret_10d"].dropna()
        if len(ret5) < 2:
            continue
        n_live = int((g["source"] == "live").sum())
        lookup.setdefault(ticker, {})[strat] = {
            "n": int(len(ret5)),
            "n_live": n_live,  # how many of the trades were real (not backtest)
            "mean_5d": round(float(ret5.mean()), 4),
            "mean_10d": round(float(ret10.mean()), 4) if len(ret10) else None,
            "win_5d": round(float((ret5 > 0).mean()), 3),
        }

    OUT.write_text(json.dumps(lookup, indent=2, sort_keys=True))
    print(f"Wrote {len(lookup)} ticker entries to {OUT}")

    # Sanity: show top 5 best (ticker, strategy) by mean_5d with n>=4
    rows = []
    for ticker, strats in lookup.items():
        for s, v in strats.items():
            if v["n"] >= 4:
                rows.append((v["mean_5d"], ticker, s, v["n"]))
    rows.sort(reverse=True)
    print("\nTop 10 by historical 5d edge (n>=4):")
    for r, t, s, n in rows[:10]:
        print(f"  {t:6s} {s:20s} mean_5d={r*100:+.2f}% n={n}")

if __name__ == "__main__":
    main()
