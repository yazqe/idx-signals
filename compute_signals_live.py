#!/usr/bin/env python3
"""Compute BUY signals from TradingView intraday snapshot.

Runs against current (intraday) data so signals can be generated BEFORE
IDX close. Reads:
  data/intraday_today.json    — today's snapshot (from fetch_intraday_tv.py)
  data/snapshot_*.json        — previous days for MA-cross detection

Strategies (BUY-only, same as compute_signals.py):
  1. rsi_oversold     — current RSI < 30
  2. ma_golden_cross  — today's SMA20 > SMA50 AND yesterday's SMA20 <= SMA50
  3. vol_breakout_up  — relative_volume_10d_calc > 2 AND change > 2%

Each signal annotated with historical edge from ticker_edge.json.
Output: candidates.json + signals/YYYY-MM-DD.json (same format as the
post-close pipeline so ask_hermes.sh and track_outcomes.py work unchanged).
"""
import json
from pathlib import Path
from datetime import date, datetime

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
SIGNALS_DIR = ROOT / "signals"
TODAY_JSON = DATA_DIR / "intraday_today.json"
EDGE_LOOKUP = ROOT / "ticker_edge.json"

EDGE = json.loads(EDGE_LOOKUP.read_text()) if EDGE_LOOKUP.exists() else {}

def confidence(ticker: str, strategy: str) -> dict:
    hist = EDGE.get(ticker, {}).get(strategy)
    if not hist:
        return {"tier": "untested", "edge_5d": None, "n": 0}
    edge, n = hist["mean_5d"], hist["n"]
    if edge >= 0.05 and n >= 4:
        tier = "high"
    elif edge >= 0.02 and n >= 3:
        tier = "medium"
    elif edge > 0:
        tier = "low"
    else:
        tier = "negative"
    return {"tier": tier, "edge_5d": edge, "win_5d": hist["win_5d"], "n": n}

def find_yesterday_snapshot() -> dict:
    """Return the most recent prior daily snapshot, or {} if none."""
    today = date.today().isoformat()
    candidates = sorted(DATA_DIR.glob("snapshot_*.json"),
                        key=lambda p: p.stem, reverse=True)
    for p in candidates:
        snap_date = p.stem.replace("snapshot_", "")
        if snap_date < today:
            return json.loads(p.read_text())
    return {}

def analyze(ticker: str, today: dict, prev: dict) -> list[dict]:
    signals = []
    close = today.get("close")
    if not close:
        return signals

    def emit(strategy: str, extras: dict):
        signals.append({
            "ticker": ticker, "strategy": strategy, "side": "BUY",
            "close": round(close, 2),
            **extras,
            "history": confidence(ticker, strategy),
        })

    rsi = today.get("RSI")
    if rsi is not None and rsi < 30:
        emit("rsi_oversold", {"rsi": round(rsi, 1),
                              "note": f"RSI {rsi:.1f} < 30 (oversold)"})

    sma20, sma50 = today.get("SMA20"), today.get("SMA50")
    p_sma20, p_sma50 = prev.get("SMA20"), prev.get("SMA50")
    if all(v is not None for v in (sma20, sma50, p_sma20, p_sma50)):
        if sma20 > sma50 and p_sma20 <= p_sma50:
            emit("ma_golden_cross",
                 {"note": "20-SMA crossed above 50-SMA today (golden cross)"})

    rel_vol = today.get("relative_volume_10d_calc")
    change = today.get("change")
    if rel_vol is not None and change is not None:
        if rel_vol > 2 and change > 2:
            emit("vol_breakout_up", {
                "vol_ratio": round(rel_vol, 1),
                "pct_chg": round(change, 2),
                "note": f"Volume {rel_vol:.1f}x avg + price +{change:.2f}%"
            })
    return signals

def main():
    if not TODAY_JSON.exists():
        print(f"Missing {TODAY_JSON}. Run fetch_intraday_tv.py first.")
        return 1
    today_data = json.loads(TODAY_JSON.read_text())
    prev_data = find_yesterday_snapshot()
    print(f"Today: {len(today_data)} tickers  |  Prev snapshot: "
          f"{len(prev_data)} tickers" if prev_data
          else f"Today: {len(today_data)} tickers  |  No prev snapshot — "
               "MA-cross strategy will be skipped this run")

    all_signals = []
    for ticker, today in today_data.items():
        prev = prev_data.get(ticker, {})
        all_signals.extend(analyze(ticker, today, prev))

    tier_rank = {"high": 0, "medium": 1, "low": 2, "untested": 3, "negative": 4}
    all_signals.sort(key=lambda s: (tier_rank[s["history"]["tier"]],
                                     -(s["history"]["edge_5d"] or 0)))

    today_str = date.today().isoformat()
    timestamp = datetime.now().strftime("%H:%M")
    out_path = SIGNALS_DIR / f"{today_str}.json"
    out_path.write_text(json.dumps(all_signals, indent=2))
    (ROOT / "candidates.json").write_text(json.dumps(all_signals, indent=2))

    by_tier = {"high": [], "medium": [], "low": [], "untested": [], "negative": []}
    for s in all_signals:
        by_tier[s["history"]["tier"]].append(f"{s['ticker']}/{s['strategy']}")

    print(f"\n[{today_str} {timestamp}] BUY signals: {len(all_signals)}\n")
    for tier in ("high", "medium", "low", "untested", "negative"):
        items = by_tier[tier]
        if items:
            print(f"  [{tier:<9}] ({len(items)}) {' '.join(items)}")
    print(f"\nWritten: {out_path}")
    return 0

if __name__ == "__main__":
    import sys; sys.exit(main())
