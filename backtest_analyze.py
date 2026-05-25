#!/usr/bin/env python3
"""Analyze Hermes backtest results vs baselines.

For each historical date that was backtested, parse the Hermes pick files in
signals/backtest/ and look up actual forward returns from backtest_signals.csv
(no yfinance re-fetch needed — returns are precomputed for all 5300+ signals).

Compares for the SAME backtest dates:
  - Stage1 picks  (Hermes initial broader)
  - Stage3 picks  (Hermes final consolidated, post-critique)
  - old_filter   (HIGH+MEDIUM tier — what we'd have picked without Hermes)
  - mechanical_all (every BUY signal on those dates)

Output: side-by-side stats. Tells us empirically whether Hermes adds alpha
over simple tier filter for the same date range.

Usage:
    python3 backtest_analyze.py
    python3 backtest_analyze.py --json
"""
import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).parent
BACKTEST_CSV = ROOT / "backtest_signals.csv"
TICKER_EDGE = ROOT / "ticker_edge.json"
BACKTEST_DIR = ROOT / "signals" / "backtest"
ROUND_TRIP_COST = 0.004

sys.path.insert(0, str(ROOT))
from extract_trade_table import parse_picks  # noqa: E402
from backtest_compare import classify_tier, add_tier_column  # noqa: E402


def discover_backtest_dates() -> list:
    """Scan signals/backtest/ for all dates that have any Hermes output."""
    if not BACKTEST_DIR.exists():
        return []
    dates = set()
    for fp in BACKTEST_DIR.glob("*-hermes*.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", fp.stem)
        if m:
            dates.add(m.group(1))
    return sorted(dates)


def parse_picks_for(date: str, stage: str) -> list:
    """Return list of (date, ticker) tuples for a stage's picks file."""
    if stage == "stage1":
        fp = BACKTEST_DIR / f"{date}-hermes-picks.md"
    elif stage == "stage3":
        fp = BACKTEST_DIR / f"{date}-hermes.md"
    else:
        raise ValueError(stage)
    if not fp.exists():
        return []
    picks = parse_picks(fp.read_text())
    return [(date, p["ticker"]) for p in picks if p.get("ticker")]


def lookup_returns(picks_keyed: list, all_signals: pd.DataFrame) -> pd.DataFrame:
    """Inner join Hermes picks (date, ticker) to backtest_signals.csv rows."""
    if not picks_keyed:
        return pd.DataFrame()
    picks_df = pd.DataFrame(picks_keyed, columns=["date", "ticker"])
    picks_df["date"] = pd.to_datetime(picks_df["date"]).dt.strftime("%Y-%m-%d")
    sig = all_signals.copy()
    sig["date"] = pd.to_datetime(sig["date"]).dt.strftime("%Y-%m-%d")
    # For same (date, ticker), multiple strategy rows may exist with identical
    # forward returns (returns depend on date+ticker only). Dedupe keeping first.
    sig_dedup = sig.sort_values("strategy").drop_duplicates(["date", "ticker"], keep="first")
    return picks_df.merge(sig_dedup, on=["date", "ticker"], how="inner")


def stats_for(df: pd.DataFrame, horizon: int) -> dict:
    col = f"ret_{horizon}d"
    if col not in df.columns or df.empty:
        return {"n": 0}
    valid = df[col].dropna() - ROUND_TRIP_COST
    if len(valid) == 0:
        return {"n": 0}
    mean = valid.mean()
    median = valid.median()
    win = (valid > 0).mean()
    std = valid.std() if len(valid) > 1 else 0
    sharpe = (mean / std) * np.sqrt(252 / horizon) if std > 0 else None
    # Sum equity curve to estimate cumulative outcome
    cum = (1 + valid).prod() - 1
    return {
        "n": int(len(valid)),
        "mean_pct": round(float(mean) * 100, 2),
        "median_pct": round(float(median) * 100, 2),
        "win_pct": round(float(win) * 100, 1),
        "best_pct": round(float(valid.max()) * 100, 2),
        "worst_pct": round(float(valid.min()) * 100, 2),
        "cum_pct": round(float(cum) * 100, 2),
        "sharpe": round(float(sharpe), 2) if sharpe is not None else None,
    }


def analyze():
    dates = discover_backtest_dates()
    if not dates:
        print("No backtest results in signals/backtest/. Run backtest_run_dates.sh first.",
              file=sys.stderr)
        return None

    # Load full backtest signals
    all_signals = pd.read_csv(BACKTEST_CSV)
    all_signals["date"] = pd.to_datetime(all_signals["date"]).dt.strftime("%Y-%m-%d")
    buy = all_signals[all_signals["side"] == "BUY"]

    # Tier classification
    with TICKER_EDGE.open() as f:
        ticker_edge = json.load(f)
    buy_tiered = add_tier_column(buy, ticker_edge)

    # Limit baselines to SAME dates as backtest
    same_date_buy = buy_tiered[buy_tiered["date"].isin(dates)]

    # Collect picks for each stage across all backtest dates
    stage1_keys = []
    stage3_keys = []
    for d in dates:
        stage1_keys.extend(parse_picks_for(d, "stage1"))
        stage3_keys.extend(parse_picks_for(d, "stage3"))

    stage1_df = lookup_returns(stage1_keys, all_signals)
    stage3_df = lookup_returns(stage3_keys, all_signals)
    old_filter_df = same_date_buy[same_date_buy["tier"].isin(["high", "medium"])]
    mech_all_df = same_date_buy

    return {
        "dates": dates,
        "counts": {
            "stage1_picks": len(stage1_df),
            "stage3_picks": len(stage3_df),
            "old_filter": len(old_filter_df),
            "mechanical_all": len(mech_all_df),
        },
        "sources": {
            "Stage1 (Hermes broad)":   {h: stats_for(stage1_df, h)   for h in (1, 5, 20)},
            "Stage3 (Hermes final)":   {h: stats_for(stage3_df, h)   for h in (1, 5, 20)},
            "old_filter (H+M tier)":   {h: stats_for(old_filter_df, h) for h in (1, 5, 20)},
            "mechanical_all":          {h: stats_for(mech_all_df, h)   for h in (1, 5, 20)},
        },
    }


def print_table(result: dict):
    print()
    print("=" * 96)
    print("HERMES BACKTEST ANALYSIS — head-to-head on identical date range")
    print(f"Dates tested: {', '.join(result['dates'])}")
    print(f"Pick counts: stage1={result['counts']['stage1_picks']}, "
          f"stage3={result['counts']['stage3_picks']}, "
          f"old_filter={result['counts']['old_filter']}, "
          f"all={result['counts']['mechanical_all']}")
    print("=" * 96)

    for h in (1, 5, 20):
        print(f"\n── Horizon: {h}d forward return (fees applied) ──")
        print(f"{'Source':<26} {'n':>4} {'Mean%':>7} {'Win%':>6} {'Med%':>7} "
              f"{'Best%':>7} {'Worst%':>7} {'Cum%':>8} {'Sharpe':>7}")
        for name, by_h in result["sources"].items():
            s = by_h[h]
            if s["n"] == 0:
                print(f"{name:<26} {'—':>4} {'—':>7} {'—':>6} {'—':>7} "
                      f"{'—':>7} {'—':>7} {'—':>8} {'—':>7}")
                continue
            sh = f"{s['sharpe']:>+6.2f}" if s.get("sharpe") is not None else "     —"
            print(
                f"{name:<26} {s['n']:>4} "
                f"{s['mean_pct']:>+7.2f} {s['win_pct']:>5.1f}% "
                f"{s['median_pct']:>+7.2f} {s['best_pct']:>+7.2f} "
                f"{s['worst_pct']:>+7.2f} {s['cum_pct']:>+7.2f}% "
                f"{sh:>7}"
            )

    print()
    print("DECISION FRAMEWORK:")
    print("  If Stage3 ≥ old_filter (mean% and Sharpe) → Hermes adds value, keep pipeline")
    print("  If Stage1 ≥ old_filter, Stage3 < old_filter → only Stage 1 helps, drop 2+3")
    print("  If old_filter ≥ both Hermes → simplify to mechanical tier filter, drop Hermes")
    print()
    print("CAVEATS:")
    print("  - ticker_edge.json is current-day view (look-ahead bias)")
    print("  - Small sample (5 dates) — directional, not statistically conclusive")
    print("  - 'Cum%' is naive product return assuming equal sizing per trade")
    print()


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    result = analyze()
    if result is None:
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_table(result)


if __name__ == "__main__":
    main()
