#!/usr/bin/env python3
"""Track outcomes of Hermes-picked stocks per pipeline stage + compare.

Goal: empirically validate whether the 3-stage Hermes pipeline (picks → critic
→ finalize) actually outperforms the mechanical signals or Stage 1 alone.

Tracks:
  - outcomes_stage1.csv  ← parsed from signals/{date}-hermes-picks.md
  - outcomes_stage3.csv  ← parsed from signals/{date}-hermes.md (FINAL)
  - outcomes.csv         ← existing, all mechanical signals (track_outcomes.py)

Subcommands:
  python3 track_outcomes_hermes.py update            Refresh both stage CSVs
  python3 track_outcomes_hermes.py compare           Print Stage1 vs Stage3 vs Mechanical
  python3 track_outcomes_hermes.py compare --json    Same but JSON for dashboard

Idempotent: skips (signal_date, ticker, stage) already recorded.
"""
import argparse
import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

import pandas as pd
import yfinance as yf

# Reuse parser from extract_trade_table.py
sys.path.insert(0, str(Path(__file__).parent))
from extract_trade_table import parse_picks  # noqa: E402

ROOT = Path(__file__).parent
SIGNALS_DIR = ROOT / "signals"
HORIZONS = [1, 5, 20]

STAGE_FILES = {
    "stage1": ("*-hermes-picks.md", ROOT / "outcomes_stage1.csv"),
    "stage3": ("*-hermes.md",       ROOT / "outcomes_stage3.csv"),
}

FIELDS = ["signal_date", "ticker", "stage", "entry_price",
          "ret_1d", "ret_5d", "ret_20d", "computed_at"]


def load_existing(csv_path: Path) -> set:
    if not csv_path.exists():
        return set()
    df = pd.read_csv(csv_path)
    return set(zip(df["signal_date"], df["ticker"]))


def md_files_for(pattern: str) -> list:
    """Find date-prefixed md files matching pattern, exclude review files."""
    files = []
    for fp in sorted(SIGNALS_DIR.glob(pattern)):
        # Skip review files when pattern is hermes.md (would also match hermes-review.md)
        if "review" in fp.stem:
            continue
        # Extract date from filename like '2026-05-25-hermes.md'
        try:
            dt = date.fromisoformat(fp.stem[:10])
        except ValueError:
            continue
        files.append((dt, fp))
    return files


def collect_picks(stage: str) -> list:
    """Walk MD files for this stage, parse picks, return list of pending records."""
    pattern, csv_path = STAGE_FILES[stage]
    existing = load_existing(csv_path)
    today = date.today()
    pending = []

    for signal_date, fp in md_files_for(pattern):
        age_days = (today - signal_date).days
        if age_days < 1:
            continue
        picks = parse_picks(fp.read_text())
        for p in picks:
            ticker = p.get("ticker")
            if not ticker:
                continue
            key = (signal_date.isoformat(), ticker)
            if key in existing:
                continue
            entry = p.get("entry")
            if entry is None:
                continue
            pending.append({
                "signal_date": signal_date.isoformat(),
                "ticker": ticker,
                "stage": stage,
                "entry_price": entry,
            })
    return pending


def fetch_outcomes(pending: list) -> list:
    """For each pick, fetch yfinance, compute forward returns."""
    if not pending:
        return []

    tickers = sorted({p["ticker"] for p in pending})
    earliest = min(date.fromisoformat(p["signal_date"]) for p in pending)
    print(f"  fetching {len(tickers)} tickers from {earliest}")

    raw = yf.download(
        [f"{t}.JK" for t in tickers],
        start=earliest.isoformat(),
        interval="1d", group_by="ticker",
        auto_adjust=True, progress=False, threads=True,
    )

    rows = []
    for p in pending:
        try:
            df = raw[f"{p['ticker']}.JK"].dropna(how="all")
        except (KeyError, AttributeError):
            continue
        sd = pd.Timestamp(p["signal_date"])
        future = df[df.index >= sd]
        if future.empty:
            continue
        entry_idx = future.index[0]
        i = df.index.get_loc(entry_idx)

        ret = {f"ret_{h}d": None for h in HORIZONS}
        for h in HORIZONS:
            if i + h < len(df):
                exit_close = df.iloc[i + h]["Close"]
                ret[f"ret_{h}d"] = round(exit_close / p["entry_price"] - 1, 4)

        if all(v is None for v in ret.values()):
            continue
        rows.append({
            "signal_date": p["signal_date"],
            "ticker": p["ticker"],
            "stage": p["stage"],
            "entry_price": p["entry_price"],
            **ret,
            "computed_at": datetime.now().isoformat(timespec="seconds"),
        })
    return rows


def write_rows(csv_path: Path, rows: list):
    if not rows:
        return
    write_header = not csv_path.exists()
    with csv_path.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            w.writeheader()
        for r in rows:
            w.writerow(r)


def cmd_update():
    """Refresh both Hermes stage CSVs."""
    for stage in ("stage1", "stage3"):
        print(f"\n[{stage}]")
        pending = collect_picks(stage)
        print(f"  pending: {len(pending)}")
        rows = fetch_outcomes(pending)
        print(f"  new outcomes: {len(rows)}")
        write_rows(STAGE_FILES[stage][1], rows)


def stats_for(df: pd.DataFrame, horizon: int) -> dict:
    """Return stats dict for given horizon column."""
    col = f"ret_{horizon}d"
    if col not in df.columns:
        return {"n": 0}
    valid = df[col].dropna()
    if len(valid) == 0:
        return {"n": 0}
    mean = valid.mean()
    win = (valid > 0).mean()
    std = valid.std() if len(valid) > 1 else 0
    # Annualized Sharpe: assumes 252 trading days, horizon-relative
    sharpe = (mean / std) * (252 / horizon) ** 0.5 if std > 0 else None
    return {
        "n": len(valid),
        "mean_pct": round(mean * 100, 2),
        "win_pct": round(win * 100, 1),
        "median_pct": round(valid.median() * 100, 2),
        "best_pct": round(valid.max() * 100, 2),
        "worst_pct": round(valid.min() * 100, 2),
        "sharpe": round(sharpe, 2) if sharpe is not None else None,
    }


def load_df(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def cmd_compare(as_json: bool = False):
    """Print Stage1 vs Stage3 vs Mechanical comparison."""
    sources = {
        "Stage1 (Hermes picks)":   load_df(STAGE_FILES["stage1"][1]),
        "Stage3 (Hermes final)":   load_df(STAGE_FILES["stage3"][1]),
        "Mechanical (all signals)": load_df(ROOT / "outcomes.csv"),
    }

    summary = {}
    for name, df in sources.items():
        summary[name] = {h: stats_for(df, h) for h in HORIZONS}

    if as_json:
        print(json.dumps(summary, indent=2))
        return

    # Pretty print
    print()
    print("=" * 80)
    print("HERMES STAGE OUTCOME COMPARISON")
    print(f"Generated: {datetime.now().isoformat(timespec='seconds')}")
    print("=" * 80)

    for h in HORIZONS:
        print(f"\n── Horizon: {h}d forward return ──")
        print(f"{'Source':<28} {'n':>4} {'Mean%':>7} {'Win%':>6} {'Med%':>7} "
              f"{'Best%':>7} {'Worst%':>7} {'Sharpe':>7}")
        for name in sources:
            s = summary[name][h]
            if s["n"] == 0:
                print(f"{name:<28} {'—':>4} {'—':>7} {'—':>6} {'—':>7} "
                      f"{'—':>7} {'—':>7} {'—':>7}")
            else:
                print(
                    f"{name:<28} {s['n']:>4} "
                    f"{s['mean_pct']:>+7.2f} {s['win_pct']:>5.1f}% "
                    f"{s['median_pct']:>+7.2f} {s['best_pct']:>+7.2f} "
                    f"{s['worst_pct']:>+7.2f} "
                    f"{s['sharpe'] if s['sharpe'] is not None else '—':>7}"
                )

    print()
    print("READING GUIDE:")
    print("  - Mean%/Win%/Med%/Sharpe higher = better (alpha discovery)")
    print("  - Worst% closer to 0 = better (risk control)")
    print("  - Stage3 should beat Stage1 to justify Stages 2+3 complexity")
    print("  - Both Hermes stages should beat Mechanical to justify the LLM cost")
    print()


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("update", help="Refresh stage CSVs from MD files")
    cmp = sub.add_parser("compare", help="Print stage comparison")
    cmp.add_argument("--json", action="store_true", help="Output JSON instead of table")
    args = p.parse_args()

    if args.cmd == "update":
        cmd_update()
    elif args.cmd == "compare":
        cmd_compare(as_json=args.json)


if __name__ == "__main__":
    main()
