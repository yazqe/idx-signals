#!/usr/bin/env python3
"""Extract trade plan table from final hermes.md for Telegram monospace block.

Parses each `## N. TICKER` block, pulls Entry/SL/TP/R/R/Tier/Strategy,
and outputs a fixed-width table optimized for Telegram code block rendering
on phones (~36-40 chars wide).

Usage:
    python3 extract_trade_table.py signals/2026-05-25-hermes.md
"""
import json
import re
import sys
from pathlib import Path


def parse_price(text):
    """Extract first meaningful price. Mirrors logic in fix_rr_math.py."""
    cleaned = re.sub(r'\([^)]*\)', '', text)

    range_match = re.search(
        r'(\d+(?:\.\d+)?)\s*(?:[-–—]|to)\s*(\d+(?:\.\d+)?)',
        cleaned
    )
    if range_match:
        a = float(range_match.group(1))
        b = float(range_match.group(2))
        if 0.5 <= b / a <= 2.0:
            return (a + b) / 2

    pm_match = re.search(r'(\d+(?:\.\d+)?)\s*[±]', cleaned)
    if pm_match:
        return float(pm_match.group(1))

    num_match = re.search(r'(\d+(?:\.\d+)?)', cleaned)
    return float(num_match.group(1)) if num_match else None


def parse_rr(text):
    """Extract R/R numeric value (handles 'R/R: 2.33 (auto-computed: ...)')."""
    m = re.search(r'(\d+\.\d+|\d+)', text)
    return float(m.group(1)) if m else None


def parse_strat(text):
    """Compact strategy name."""
    s = text.lower()
    if 'vol_breakout_up' in s or 'vol breakout' in s or 'volbo' in s:
        return 'volBO'
    if 'rsi_oversold' in s or 'rsi oversold' in s or 'rsi<30' in s or 'rsi <' in s:
        return 'RSI<30'
    if 'ma_golden_cross' in s or 'golden cross' in s or 'ma cross' in s:
        return 'MAx'
    return text.strip()[:8]


def strat_emoji(strat):
    """Map strategy to emoji for compact display."""
    if not strat:
        return ' '
    s = strat.lower()
    if 'vol' in s or 'bo' in s:
        return '📊'
    if 'rsi' in s:
        return '📉'
    if 'ma' in s:
        return '✗'
    return '·'


def parse_edge_win(text):
    """From 'Historical edge: 6.38% over 10 past trades (win rate 90%)'
    extract (edge_pct, win_pct, n). Handles 'N/A' gracefully.

    Returns (None, None, None) if no useful data.
    """
    # Bail early on 'N/A' or literal zero count (word boundary so '10 past trades' doesn't match)
    if 'n/a' in text.lower() or re.search(r'\b0\s+past\s+trades\b', text, re.IGNORECASE):
        return None, None, 0

    edge = win = n = None
    edge_m = re.search(r'(-?\d+(?:\.\d+)?)\s*%', text)
    if edge_m:
        edge = float(edge_m.group(1))

    n_m = re.search(r'(\d+)\s+past\s+trades', text, re.IGNORECASE)
    if n_m:
        n = int(n_m.group(1))

    win_m = re.search(r'win\s+rate\s+(\d+(?:\.\d+)?)\s*%', text, re.IGNORECASE)
    if win_m:
        win = float(win_m.group(1))

    return edge, win, n


def parse_tier(text):
    """Compact tier name from Conviction line."""
    s = text.lower()
    if 'high' in s:
        return 'HIGH'
    if 'medium' in s or 'med' in s:
        return 'MED'
    if 'low' in s:
        return 'LOW'
    if 'untested' in s:
        return 'UNT'
    if 'negative' in s:
        return 'NEG'
    return '?'


def parse_picks(content):
    """Return list of dicts with ticker, strat, tier, entry, sl, tp, rr."""
    picks = []
    cur = None
    pick_header = re.compile(r'^##\s+(\d+\.\s+)?([A-Z]{3,5})\s+[—-]')

    for line in content.split('\n'):
        m = pick_header.match(line)
        if m:
            if cur and cur.get('ticker'):
                picks.append(cur)
            cur = {'ticker': m.group(2)}
            continue
        if cur is None:
            continue

        lower = line.lower()
        if '**triggered:**' in lower:
            cur['strat'] = parse_strat(line.split('**Triggered:**', 1)[-1])
        elif '**conviction:**' in lower:
            cur['tier'] = parse_tier(line.split('**Conviction:**', 1)[-1])
        elif '**historical edge:**' in lower:
            edge, win, n = parse_edge_win(line.split('**Historical edge:**', 1)[-1])
            cur['edge'] = edge
            cur['win'] = win
            cur['n'] = n
        elif '**entry zone:**' in lower or '**entry:**' in lower:
            cur['entry'] = parse_price(line)
        elif '**stop loss:**' in lower or '**sl:**' in lower:
            cur['sl'] = parse_price(line)
        elif '**take profit:**' in lower or '**tp:**' in lower:
            cur['tp'] = parse_price(line)
        elif '**r/r:**' in lower or '**rr:**' in lower:
            cur['rr'] = parse_rr(line)

    if cur and cur.get('ticker'):
        picks.append(cur)
    return picks


def format_table(picks):
    """Render fixed-width table fitting Telegram monospace block on phone."""
    if not picks:
        return '(no picks parsed)'

    def fmt_price(v):
        if v is None:
            return '—'
        if v >= 1000:
            return str(int(round(v)))
        if v >= 10:
            return str(int(round(v)))
        return f'{v:g}'

    def fmt_rr(v):
        if v is None:
            return '—'
        return f'{v:.2f}'

    def fmt_pct(v):
        """Format percentage compact: +6%, -2%, —."""
        if v is None:
            return '—'
        sign = '+' if v > 0 else ''
        return f'{sign}{int(round(v))}%'

    def fmt_win(v):
        """Win rate as bare integer + %, fits 4 chars."""
        if v is None:
            return '—'
        return f'{int(round(v))}%'

    # Sort by R/R desc (best setups first)
    sorted_picks = sorted(picks, key=lambda p: p.get('rr') or 0, reverse=True)

    # Header — width tuned for Telegram code block on phone (~40-44 chars)
    rows = [
        f'{"SYM":<5}{"S":<2} {"ENT":>5} {"SL":>5} {"TP":>5} {"R/R":>4} {"EDG":>4} {"WIN":>4}'
    ]
    for p in sorted_picks:
        rr = p.get('rr')
        marker = '⭐' if rr and rr >= 2.0 else ' '
        rows.append(
            f'{p["ticker"]:<5}{strat_emoji(p.get("strat"))} '
            f'{fmt_price(p.get("entry")):>5} '
            f'{fmt_price(p.get("sl")):>5} '
            f'{fmt_price(p.get("tp")):>5} '
            f'{fmt_rr(rr):>4} '
            f'{fmt_pct(p.get("edge")):>4} '
            f'{fmt_win(p.get("win")):>4} '
            f'{p.get("tier","?")[:1]}{marker}'
        )

    return '\n'.join(rows)


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <hermes.md> [--json]', file=sys.stderr)
        sys.exit(2)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f'File not found: {path}', file=sys.stderr)
        sys.exit(1)

    picks = parse_picks(path.read_text())

    if '--json' in sys.argv:
        print(json.dumps(picks, indent=2))
    else:
        print(format_table(picks))


if __name__ == '__main__':
    main()
