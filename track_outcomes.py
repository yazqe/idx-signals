#!/usr/bin/env python3
"""Track actual outcomes of past signals.

For every signal in signals/*.json that's old enough to have a measurable
forward return at horizon h (1d, 5d, 20d), refetch price at that point and
record actual P/L in outcomes.csv.

Idempotent: skips (signal_date, ticker, strategy) rows already in outcomes.csv.
"""
import json
import csv
from pathlib import Path
from datetime import date, datetime
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).parent
SIGNALS_DIR = ROOT / "signals"
OUTCOMES_CSV = ROOT / "outcomes.csv"
HORIZONS = [1, 5, 20]

FIELDS = ["signal_date", "ticker", "strategy", "side", "entry_price",
          "ret_1d", "ret_5d", "ret_20d", "computed_at"]

def load_existing() -> set[tuple]:
    """Return set of (signal_date, ticker, strategy) already recorded."""
    if not OUTCOMES_CSV.exists():
        return set()
    df = pd.read_csv(OUTCOMES_CSV)
    return set(zip(df["signal_date"], df["ticker"], df["strategy"]))

def collect_pending() -> list[dict]:
    """Walk signals/*.json (excluding *-hermes.md), return signals that are
    old enough for at least the 1d horizon."""
    today = date.today()
    pending = []
    for fp in sorted(SIGNALS_DIR.glob("*.json")):
        signal_date = date.fromisoformat(fp.stem)
        age_days = (today - signal_date).days
        if age_days < 1:
            continue
        signals = json.loads(fp.read_text())
        for s in signals:
            # only BUY-side (post-refactor); skip if SELL still present from old logs
            if s.get("side") != "BUY":
                continue
            pending.append({
                "signal_date": signal_date.isoformat(),
                "ticker": s["ticker"],
                "strategy": s["strategy"],
                "side": s["side"],
                "entry_price": s["close"],
                "age_days": age_days,
            })
    return pending

def fetch_outcomes(pending: list[dict]) -> list[dict]:
    """For each pending signal, fetch yfinance and compute returns at
    each horizon that's now in the past."""
    if not pending:
        return []

    tickers = sorted({p["ticker"] for p in pending})
    earliest = min(date.fromisoformat(p["signal_date"]) for p in pending)
    print(f"Fetching {len(tickers)} tickers from {earliest}...")
    raw = yf.download([f"{t}.JK" for t in tickers],
                      start=earliest.isoformat(),
                      interval="1d", group_by="ticker",
                      auto_adjust=True, progress=False, threads=True)

    rows = []
    for p in pending:
        try:
            df = raw[f"{p['ticker']}.JK"].dropna(how="all")
        except (KeyError, AttributeError):
            continue
        # Find the entry day index (first day on/after signal_date)
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

        # Only record if at least one horizon resolved
        if all(v is None for v in ret.values()):
            continue
        rows.append({
            "signal_date": p["signal_date"],
            "ticker": p["ticker"],
            "strategy": p["strategy"],
            "side": p["side"],
            "entry_price": p["entry_price"],
            **ret,
            "computed_at": datetime.now().isoformat(timespec="seconds"),
        })
    return rows

def main():
    existing = load_existing()
    pending = [p for p in collect_pending()
               if (p["signal_date"], p["ticker"], p["strategy"]) not in existing]
    print(f"Pending: {len(pending)} (already recorded: {len(existing)})")

    new_rows = fetch_outcomes(pending)
    print(f"New outcomes: {len(new_rows)}")

    if not new_rows:
        return

    write_header = not OUTCOMES_CSV.exists()
    with OUTCOMES_CSV.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            w.writeheader()
        for r in new_rows:
            w.writerow(r)
    print(f"Appended to {OUTCOMES_CSV}")

    # Quick summary
    df = pd.DataFrame(new_rows)
    for h in HORIZONS:
        col = f"ret_{h}d"
        valid = df[col].dropna()
        if len(valid):
            print(f"  {h}d: n={len(valid)}, mean={valid.mean()*100:+.2f}%, "
                  f"win={(valid > 0).mean()*100:.0f}%")

if __name__ == "__main__":
    main()
