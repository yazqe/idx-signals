#!/usr/bin/env python3
"""Reconstruct candidates.json format for a historical date.

Used by backtest_run_one.sh to simulate "if Hermes pipeline had run on date X,
what would it have picked?"

CAVEAT: ticker_edge.json reflects CURRENT (today's) historical edges, not
walk-forward edges as they would have been on date X. This means Hermes sees
"look-ahead bias" — knows that BUVA's edge is 6.38% at win 90% based on full
2-year data including post-X period. True walk-forward would require recomputing
ticker_edge per backtest date. This shortcut is acknowledged; results are
directional, not perfectly clean backtest.

Usage:
    python3 backtest_reconstruct.py 2026-03-02 > candidates_2026-03-02.json
"""
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent
BACKTEST_CSV = ROOT / "backtest_signals.csv"
TICKER_EDGE = ROOT / "ticker_edge.json"


def classify_tier(stats):
    if not stats:
        return "untested"
    n = stats.get("n", 0)
    mean_5d = stats.get("mean_5d", 0)
    win_5d = stats.get("win_5d", 0)
    if n < 3:
        return "untested"
    if mean_5d < 0:
        return "negative"
    if mean_5d >= 0.05 and n >= 4 and win_5d >= 0.55:
        return "high"
    if mean_5d >= 0.02 and n >= 3:
        return "medium"
    return "low"


def reconstruct(target_date: str) -> list:
    """Build candidates.json structure matching production format."""
    df = pd.read_csv(BACKTEST_CSV)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    day = df[(df["date"] == target_date) & (df["side"] == "BUY")]
    if day.empty:
        return []

    with TICKER_EDGE.open() as f:
        ticker_edge = json.load(f)

    candidates = []
    for _, row in day.iterrows():
        ticker = row["ticker"]
        strategy = row["strategy"]
        stats = ticker_edge.get(ticker, {}).get(strategy, {})
        history = {
            "tier": classify_tier(stats),
            "edge_5d": stats.get("mean_5d"),
            "win_5d": stats.get("win_5d"),
            "n": stats.get("n", 0),
        }
        candidates.append({
            "ticker": ticker,
            "strategy": strategy,
            "side": "BUY",
            "close": float(row["entry"]),
            "history": history,
            "_backtest_date": target_date,
        })
    return candidates


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} YYYY-MM-DD", file=sys.stderr)
        sys.exit(2)
    target = sys.argv[1]
    candidates = reconstruct(target)
    print(json.dumps(candidates, indent=2))


if __name__ == "__main__":
    main()
