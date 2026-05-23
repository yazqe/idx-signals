#!/usr/bin/env python3
"""Fetch IDX prices via yfinance for tickers in watchlist.txt.

Reads tickers (one per line), appends .JK suffix, downloads ~6 months
of daily OHLCV, writes to data/<TICKER>.csv. Skips tickers that fail.
"""
import sys
from pathlib import Path
import yfinance as yf
import pandas as pd

ROOT = Path(__file__).parent
WATCHLIST = ROOT / "watchlist.txt"
DATA_DIR = ROOT / "data"
PERIOD = "6mo"

def main():
    tickers = [t.strip() for t in WATCHLIST.read_text().splitlines() if t.strip()]
    yf_symbols = [f"{t}.JK" for t in tickers]
    print(f"Fetching {len(yf_symbols)} IDX tickers ({PERIOD})...")

    # yfinance batch download — fast, single HTTP burst
    df = yf.download(
        tickers=yf_symbols,
        period=PERIOD,
        interval="1d",
        group_by="ticker",
        auto_adjust=True,
        progress=False,
        threads=True,
    )

    ok, missing = [], []
    for t, sym in zip(tickers, yf_symbols):
        try:
            sub = df[sym].dropna(how="all")
            if len(sub) < 30:
                missing.append(t)
                continue
            sub.to_csv(DATA_DIR / f"{t}.csv")
            ok.append(t)
        except (KeyError, AttributeError):
            missing.append(t)

    print(f"OK: {len(ok)}  |  Missing/insufficient: {len(missing)}")
    if missing:
        print(f"  Missing: {' '.join(missing)}")

if __name__ == "__main__":
    main()
