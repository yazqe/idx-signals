#!/usr/bin/env python3
"""Empirical backtest comparison of filtering strategies — NO LLM needed.

Uses backtest_signals.csv (5300+ historical signals over 2 years with forward
returns) to answer: which filtering approach actually wins?

Comparisons:
  - mechanical_all:    All BUY signals (no filter, baseline)
  - old_filter:        Only HIGH+MEDIUM tier (mimics old ask_hermes.sh)
  - stage1_broader:    HIGH+MED+LOW with confluence + UNTESTED with confluence
                       (mimics new ask_hermes.sh Stage 1)
  - vol_breakout_only: Only vol_breakout_up signals (best Sharpe in original backtest)
  - top_by_edge:       Top-N each day by historical edge_5d × win_5d

Output: side-by-side stats — n, mean%, win%, Sharpe, max drawdown.

Usage:
  python3 backtest_compare.py
  python3 backtest_compare.py --json
"""
import argparse
import json
import sys
from pathlib import Path

import pandas as pd
import numpy as np

ROOT = Path(__file__).parent
BACKTEST_CSV = ROOT / "backtest_signals.csv"
TICKER_EDGE = ROOT / "ticker_edge.json"
ROUND_TRIP_COST = 0.004  # 0.4% per round trip (Stockbit-ish)


def classify_tier(stats: dict) -> str:
    """Mirror compute_signals.py tier logic."""
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


def add_tier_column(df: pd.DataFrame, ticker_edge: dict) -> pd.DataFrame:
    """Add 'tier' column to backtest_signals based on ticker × strategy history."""
    def tier_for_row(row):
        ts = ticker_edge.get(row["ticker"], {})
        ss = ts.get(row["strategy"], {})
        return classify_tier(ss)
    df = df.copy()
    df["tier"] = df.apply(tier_for_row, axis=1)
    return df


def add_confluence_column(df: pd.DataFrame) -> pd.DataFrame:
    """Add 'confluence' = number of strategies fired for same (date, ticker)."""
    df = df.copy()
    conf = df.groupby(["date", "ticker"]).size().rename("confluence")
    df = df.join(conf, on=["date", "ticker"])
    return df


# ── Filter strategies ────────────────────────────────────────────────────

def filter_mechanical_all(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["side"] == "BUY"]


def filter_old(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["side"] == "BUY") & df["tier"].isin(["high", "medium"])]


def filter_stage1(df: pd.DataFrame) -> pd.DataFrame:
    """HIGH/MED always, LOW with confluence ≥ 2, UNTESTED with confluence ≥ 2."""
    buy = df[df["side"] == "BUY"]
    hm = buy["tier"].isin(["high", "medium"])
    low_conf = (buy["tier"] == "low") & (buy["confluence"] >= 2)
    untested_conf = (buy["tier"] == "untested") & (buy["confluence"] >= 2)
    return buy[hm | low_conf | untested_conf]


def filter_vol_breakout(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["side"] == "BUY") & (df["strategy"] == "vol_breakout_up")]


def filter_top_by_edge(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """Each date, keep top-N by (historical mean × win) score."""
    buy = df[df["side"] == "BUY"].copy()
    # Need to join ticker_edge stats — assume already in df via tier+stats
    # For simplicity: rank by tier first, then take top-N per day
    tier_rank = {"high": 5, "medium": 4, "low": 3, "untested": 2, "negative": 1}
    buy["score"] = buy["tier"].map(tier_rank).fillna(0)
    buy = buy.sort_values(["date", "score"], ascending=[True, False])
    return buy.groupby("date").head(top_n)


# ── Stats ─────────────────────────────────────────────────────────────────

def stats_for(df: pd.DataFrame, horizon_days: int = 5,
              apply_costs: bool = True) -> dict:
    """Compute aggregate stats for a filtered signal set."""
    col = f"ret_{horizon_days}d"
    if col not in df.columns or df.empty:
        return {"n": 0}

    valid = df[col].dropna()
    if apply_costs:
        valid = valid - ROUND_TRIP_COST  # subtract round-trip fees
    if len(valid) == 0:
        return {"n": 0}

    mean = valid.mean()
    median = valid.median()
    win = (valid > 0).mean()
    std = valid.std() if len(valid) > 1 else 0
    # Annualized Sharpe assuming 252 trading days / horizon
    sharpe = (mean / std) * np.sqrt(252 / horizon_days) if std > 0 else None
    # Max drawdown of cumulative equity curve (sorted by date)
    sorted_df = df.sort_values("date").copy()
    sorted_df["adj_ret"] = sorted_df[col].fillna(0) - (ROUND_TRIP_COST if apply_costs else 0)
    sorted_df["cum"] = (1 + sorted_df["adj_ret"]).cumprod()
    sorted_df["peak"] = sorted_df["cum"].cummax()
    sorted_df["dd"] = sorted_df["cum"] / sorted_df["peak"] - 1
    max_dd = sorted_df["dd"].min()

    return {
        "n": int(len(valid)),
        "mean_pct": round(float(mean) * 100, 2),
        "median_pct": round(float(median) * 100, 2),
        "win_pct": round(float(win) * 100, 1),
        "best_pct": round(float(valid.max()) * 100, 2),
        "worst_pct": round(float(valid.min()) * 100, 2),
        "sharpe": round(float(sharpe), 2) if sharpe is not None else None,
        "max_dd_pct": round(float(max_dd) * 100, 2),
    }


# ── Main ──────────────────────────────────────────────────────────────────

def run_comparison() -> dict:
    df = pd.read_csv(BACKTEST_CSV)
    with TICKER_EDGE.open() as f:
        ticker_edge = json.load(f)

    df = add_tier_column(df, ticker_edge)
    df = add_confluence_column(df)

    filters = {
        "mechanical_all":     filter_mechanical_all(df),
        "old_filter (H+M)":   filter_old(df),
        "stage1_broader":     filter_stage1(df),
        "vol_breakout_only":  filter_vol_breakout(df),
        "top5_per_day":       filter_top_by_edge(df, 5),
    }

    return {name: {h: stats_for(filtered, h) for h in (1, 5, 20)}
            for name, filtered in filters.items()}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    result = run_comparison()

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print()
    print("=" * 88)
    print("BACKTEST COMPARISON — 2 years history, BUY-only, fees applied (0.4% round-trip)")
    print("=" * 88)

    for h in (1, 5, 20):
        print(f"\n── Horizon: {h}d forward return ──")
        print(f"{'Filter':<22} {'n':>5} {'Mean%':>7} {'Win%':>6} {'Med%':>7} "
              f"{'Best%':>7} {'Worst%':>7} {'Sharpe':>7} {'MaxDD%':>8}")
        for name, by_h in result.items():
            s = by_h[h]
            if s["n"] == 0:
                continue
            sharpe_str = f"{s['sharpe']:>+6.2f}" if s.get('sharpe') is not None else "     —"
            print(
                f"{name:<22} {s['n']:>5} "
                f"{s['mean_pct']:>+7.2f} {s['win_pct']:>5.1f}% "
                f"{s['median_pct']:>+7.2f} {s['best_pct']:>+7.2f} "
                f"{s['worst_pct']:>+7.2f} "
                f"{sharpe_str:>7} "
                f"{s['max_dd_pct']:>+7.2f}%"
            )

    print()
    print("KEY QUESTIONS:")
    print("  Q1: Does stage1_broader beat old_filter? → did Stage1 tier expansion help?")
    print("  Q2: Does top5_per_day beat mechanical_all? → would a 'pick best' add alpha?")
    print("  Q3: Is vol_breakout_only the best single strategy?")
    print()


if __name__ == "__main__":
    main()
