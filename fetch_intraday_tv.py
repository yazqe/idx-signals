#!/usr/bin/env python3
"""Fetch intraday IDX data via TradingView Scanner (public API, no key).

Used for pre-close signal generation: runs ~30-60 min before IDX close
(16:00 WIB), pulls current intraday OHLCV + technical indicators for the
70 tickers in watchlist.txt.

Output:
  data/intraday_today.json  — current snapshot (overwritten each run)
  data/snapshot_YYYY-MM-DD.json  — daily snapshot (persisted for MA-cross detection)

TradingView scanner: https://scanner.tradingview.com/indonesia/scan
"""
import json
import sys
from pathlib import Path
from datetime import date
import requests

ROOT = Path(__file__).parent
WATCHLIST = ROOT / "watchlist.txt"
DATA_DIR = ROOT / "data"

SCANNER_URL = "https://scanner.tradingview.com/indonesia/scan"
HEADERS = {
    "Content-Type": "application/json",
    "Origin": "https://id.tradingview.com",
    "Referer": "https://id.tradingview.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# Columns we need for signals
COLUMNS = [
    "name", "close", "change", "volume",
    "average_volume_10d_calc", "relative_volume_10d_calc",
    "RSI", "SMA20", "SMA50",
    "high", "low",  # for context / sanity
]

def fetch(tickers: list[str]) -> dict:
    """Post one request restricted to specific tickers via symbols.tickers."""
    payload = {
        "symbols": {
            "tickers": [f"IDX:{t}" for t in tickers],
            "query": {"types": []},
        },
        "columns": COLUMNS,
        "range": [0, len(tickers) + 10],
    }
    r = requests.post(SCANNER_URL, headers=HEADERS, json=payload, timeout=15)
    r.raise_for_status()
    return r.json()

def main():
    tickers = [t.strip() for t in WATCHLIST.read_text().splitlines() if t.strip()]
    print(f"Fetching intraday data for {len(tickers)} tickers via TradingView scanner...")
    raw = fetch(tickers)

    out = {}
    for item in raw.get("data", []):
        d = item.get("d", [])
        if len(d) < len(COLUMNS):
            continue
        record = dict(zip(COLUMNS, d))
        name = (record["name"] or "").replace("IDX:", "")
        out[name] = record

    DATA_DIR.mkdir(exist_ok=True)
    today = date.today().isoformat()
    (DATA_DIR / "intraday_today.json").write_text(json.dumps(out, indent=2))
    (DATA_DIR / f"snapshot_{today}.json").write_text(json.dumps(out, indent=2))

    missing = [t for t in tickers if t not in out]
    print(f"OK: {len(out)}  |  Missing: {len(missing)}")
    if missing:
        print(f"  Missing: {' '.join(missing)}")

if __name__ == "__main__":
    main()
