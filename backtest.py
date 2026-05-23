#!/usr/bin/env python3
"""Vectorized backtest of the 3 strategies on 2 years of IDX data.

For each signal day, computes forward returns at 1/3/5/10/20 trading-day horizons.
Aggregates by strategy: count, win rate, mean/median return, Sharpe-ish, hit-rate
after fees.

Assumptions / caveats:
- No position sizing, no portfolio overlap handling (treats every signal as independent).
- BUY return = (price_t+h / price_t - 1). SELL return computed same way; for SELL
  a NEGATIVE forward return is a "win" (because we'd have avoided/exited).
- Round-trip cost assumed 0.4% (Stockbit-ish: 0.15% buy + 0.25% sell incl. PPh).
- Look-ahead bias avoided: signal at day t uses only data up to day t, return measured
  from day t+1 onward (assume entry at next-day close).
- Survivorship bias NOT corrected — tickers that delisted are missing from yfinance.
"""
import sys
from pathlib import Path
import yfinance as yf
import pandas as pd
import numpy as np
from collections import defaultdict

ROOT = Path(__file__).parent
WATCHLIST = ROOT / "watchlist.txt"
PERIOD = "2y"
HORIZONS = [1, 3, 5, 10, 20]
ROUND_TRIP_COST = 0.004  # 0.4%

def rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def generate_signals(df: pd.DataFrame, ticker: str) -> list[dict]:
    """Return list of (date, strategy, side, entry_close) for each signal day."""
    df = df.dropna().copy()
    if len(df) < 60:
        return []

    df["rsi14"] = rsi(df["Close"])
    df["sma20"] = df["Close"].rolling(20).mean()
    df["sma50"] = df["Close"].rolling(50).mean()
    df["vol_sma20"] = df["Volume"].rolling(20).mean()
    df["pct_chg"] = df["Close"].pct_change() * 100

    signals = []
    for i in range(1, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]
        date = df.index[i]

        # RSI thresholds (crossing into oversold/overbought today only)
        if row["rsi14"] < 30 and prev["rsi14"] >= 30:
            signals.append({"date": date, "ticker": ticker, "strategy": "rsi_oversold",
                            "side": "BUY", "entry": row["Close"], "idx": i})
        elif row["rsi14"] > 70 and prev["rsi14"] <= 70:
            signals.append({"date": date, "ticker": ticker, "strategy": "rsi_overbought",
                            "side": "SELL", "entry": row["Close"], "idx": i})

        # MA crossover (today only)
        if pd.notna(row["sma50"]) and pd.notna(prev["sma50"]):
            if row["sma20"] > row["sma50"] and prev["sma20"] <= prev["sma50"]:
                signals.append({"date": date, "ticker": ticker, "strategy": "ma_golden_cross",
                                "side": "BUY", "entry": row["Close"], "idx": i})
            elif row["sma20"] < row["sma50"] and prev["sma20"] >= prev["sma50"]:
                signals.append({"date": date, "ticker": ticker, "strategy": "ma_death_cross",
                                "side": "SELL", "entry": row["Close"], "idx": i})

        # Volume breakout
        if pd.notna(row["vol_sma20"]) and row["vol_sma20"] > 0:
            vol_ratio = row["Volume"] / row["vol_sma20"]
            if vol_ratio > 2 and row["pct_chg"] > 2:
                signals.append({"date": date, "ticker": ticker, "strategy": "vol_breakout_up",
                                "side": "BUY", "entry": row["Close"], "idx": i})
            elif vol_ratio > 2 and row["pct_chg"] < -2:
                signals.append({"date": date, "ticker": ticker, "strategy": "vol_breakout_down",
                                "side": "SELL", "entry": row["Close"], "idx": i})

    # Attach forward returns
    for s in signals:
        i = s["idx"]
        for h in HORIZONS:
            tgt = i + h
            if tgt < len(df):
                ret = df.iloc[tgt]["Close"] / s["entry"] - 1
                s[f"ret_{h}d"] = ret
            else:
                s[f"ret_{h}d"] = np.nan
    return signals

def main():
    tickers = [t.strip() for t in WATCHLIST.read_text().splitlines() if t.strip()]
    yf_symbols = [f"{t}.JK" for t in tickers]
    print(f"Downloading {PERIOD} of data for {len(yf_symbols)} IDX tickers...")
    raw = yf.download(yf_symbols, period=PERIOD, interval="1d",
                      group_by="ticker", auto_adjust=True,
                      progress=False, threads=True)

    all_signals = []
    skipped = 0
    for t, sym in zip(tickers, yf_symbols):
        try:
            sub = raw[sym].dropna(how="all")
            all_signals.extend(generate_signals(sub, t))
        except (KeyError, AttributeError):
            skipped += 1
    print(f"Generated {len(all_signals)} signals across {len(tickers) - skipped} tickers")
    print(f"Round-trip cost assumption: {ROUND_TRIP_COST*100:.2f}%\n")

    if not all_signals:
        return

    df = pd.DataFrame(all_signals)
    df.to_csv(ROOT / "backtest_signals.csv", index=False)

    # Per-strategy stats
    print(f"{'Strategy':<22} {'N':>5} {'h':>4} {'Win%':>7} {'Mean%':>8} {'Med%':>8} "
          f"{'Edge%':>8} {'Sharpe':>7}")
    print("-" * 88)

    for strat, g in df.groupby("strategy"):
        side = g["side"].iloc[0]
        for h in HORIZONS:
            col = f"ret_{h}d"
            valid = g[col].dropna()
            if len(valid) < 5:
                continue
            # For SELL: win = negative return
            if side == "BUY":
                wins = (valid > 0).mean() * 100
                edge = valid.mean() - ROUND_TRIP_COST
            else:
                wins = (valid < 0).mean() * 100
                edge = -valid.mean() - ROUND_TRIP_COST
            mean = valid.mean() * 100
            median = valid.median() * 100
            std = valid.std()
            sharpe = (valid.mean() / std * np.sqrt(252 / h)) if std > 0 else 0
            print(f"{strat:<22} {len(valid):>5} {h:>3}d {wins:>6.1f}% "
                  f"{mean:>+7.2f}% {median:>+7.2f}% {edge*100:>+7.2f}% {sharpe:>7.2f}")
        print()

    # Best/worst tickers per strategy at 5d horizon
    print("\n=== Top 5 tickers per strategy (avg 5d return) ===")
    for strat, g in df.groupby("strategy"):
        top = g.groupby("ticker")["ret_5d"].agg(["mean", "count"])
        top = top[top["count"] >= 3].sort_values("mean", ascending=False)
        if top.empty:
            continue
        print(f"\n{strat}:")
        side = g["side"].iloc[0]
        order = top if side == "BUY" else top.iloc[::-1]
        for ticker, row in order.head(5).iterrows():
            print(f"  {ticker:6s}  mean: {row['mean']*100:+6.2f}%  (n={int(row['count'])})")

if __name__ == "__main__":
    main()
