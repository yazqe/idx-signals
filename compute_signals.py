#!/usr/bin/env python3
"""Compute BUY-side strategies across all tickers in data/.

Strategies kept (validated by 2y backtest with edge > 0 at 5-20d horizon):
  1. rsi_oversold     — 14d RSI crosses below 30
  2. ma_golden_cross  — 20-SMA crosses above 50-SMA
  3. vol_breakout_up  — volume > 2x 20d avg AND price up > 2%

SELL strategies (rsi_overbought, ma_death_cross, vol_breakout_down) DROPPED:
backtest showed they predict continuation, not reversal — they're actually
contrarian signals. See backtest.py output for evidence.

Each signal is annotated with historical edge for that (ticker, strategy)
from ticker_edge.json. Output: candidates.json + signals/YYYY-MM-DD.json.
"""
import json
from pathlib import Path
from datetime import date
import pandas as pd
import numpy as np

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
SIGNALS_DIR = ROOT / "signals"
EDGE_LOOKUP = ROOT / "ticker_edge.json"

# Load historical edge table (built by build_lookup.py from backtest)
EDGE = json.loads(EDGE_LOOKUP.read_text()) if EDGE_LOOKUP.exists() else {}

def confidence(ticker: str, strategy: str) -> dict:
    """Return historical context for this (ticker, strategy) from backtest."""
    hist = EDGE.get(ticker, {}).get(strategy)
    if not hist:
        return {"tier": "untested", "edge_5d": None, "n": 0}
    edge = hist["mean_5d"]
    n = hist["n"]
    if edge >= 0.05 and n >= 4:
        tier = "high"
    elif edge >= 0.02 and n >= 3:
        tier = "medium"
    elif edge > 0:
        tier = "low"
    else:
        tier = "negative"  # historically loses on this ticker — flag to skip
    return {"tier": tier, "edge_5d": edge, "win_5d": hist["win_5d"], "n": n}

def rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def analyze(ticker: str, df: pd.DataFrame) -> list[dict]:
    df = df.dropna().copy()
    if len(df) < 60:
        return []

    df["rsi14"] = rsi(df["Close"])
    df["sma20"] = df["Close"].rolling(20).mean()
    df["sma50"] = df["Close"].rolling(50).mean()
    df["vol_sma20"] = df["Volume"].rolling(20).mean()
    df["pct_chg"] = df["Close"].pct_change() * 100

    last = df.iloc[-1]
    prev = df.iloc[-2]
    signals = []

    def emit(strategy: str, extras: dict):
        sig = {
            "ticker": ticker, "strategy": strategy, "side": "BUY",
            "close": round(last["Close"], 2),
            **extras,
            "history": confidence(ticker, strategy),
        }
        signals.append(sig)

    # 1. RSI oversold (BUY only — overbought side dropped, backtest showed continuation)
    if last["rsi14"] < 30:
        emit("rsi_oversold", {
            "rsi": round(last["rsi14"], 1),
            "note": f"RSI {last['rsi14']:.1f} < 30 (oversold)"
        })

    # 2. MA golden cross (BUY only — death cross side dropped, lagging in IDX small-caps)
    if pd.notna(last["sma50"]) and pd.notna(prev["sma50"]):
        if last["sma20"] > last["sma50"] and prev["sma20"] <= prev["sma50"]:
            emit("ma_golden_cross", {
                "note": "20-SMA crossed above 50-SMA today (golden cross)"
            })

    # 3. Volume breakout up (BUY only — breakout-down side dropped, was selling climax)
    if pd.notna(last["vol_sma20"]) and last["vol_sma20"] > 0:
        vol_ratio = last["Volume"] / last["vol_sma20"]
        if vol_ratio > 2 and last["pct_chg"] > 2:
            emit("vol_breakout_up", {
                "vol_ratio": round(vol_ratio, 1),
                "pct_chg": round(last["pct_chg"], 2),
                "note": f"Volume {vol_ratio:.1f}x avg + price +{last['pct_chg']:.2f}%"
            })

    return signals

def main():
    all_signals = []
    for csv in sorted(DATA_DIR.glob("*.csv")):
        ticker = csv.stem
        df = pd.read_csv(csv, index_col=0, parse_dates=True)
        all_signals.extend(analyze(ticker, df))

    # Sort by confidence tier (high → medium → low → untested → negative)
    tier_rank = {"high": 0, "medium": 1, "low": 2, "untested": 3, "negative": 4}
    all_signals.sort(key=lambda s: (tier_rank[s["history"]["tier"]],
                                     -(s["history"]["edge_5d"] or 0)))

    today = date.today().isoformat()
    out_path = SIGNALS_DIR / f"{today}.json"
    out_path.write_text(json.dumps(all_signals, indent=2))
    (ROOT / "candidates.json").write_text(json.dumps(all_signals, indent=2))

    by_tier = {"high": [], "medium": [], "low": [], "untested": [], "negative": []}
    for s in all_signals:
        by_tier[s["history"]["tier"]].append(f"{s['ticker']}/{s['strategy']}")

    n_files = len(list(DATA_DIR.glob('*.csv')))
    print(f"Scanned {n_files} tickers as of {today}")
    print(f"Total BUY signals: {len(all_signals)}\n")
    for tier in ("high", "medium", "low", "untested", "negative"):
        items = by_tier[tier]
        if not items:
            continue
        print(f"  [{tier:<9}] ({len(items)}) {' '.join(items)}")
    print(f"\nWritten: {out_path}")

if __name__ == "__main__":
    main()
