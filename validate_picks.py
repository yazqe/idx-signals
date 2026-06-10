#!/usr/bin/env python3
"""Strip hallucinated picks from a Hermes final report.

The finalize stage is allowed to "promote" picks, and the LLM abuses this by
inventing well-known tickers (and prices from training memory) that are NOT in
the day's candidate pool — e.g. PTBA entry 5885 when PTBA actually trades ~2690.

This deterministically removes any `## N. <TICKER>` pick whose ticker is not in
candidates.json, or whose entry deviates >35% from the candidate's real close.
Survivors are renumbered; a validator note records what was dropped. Same guard
philosophy as fix_rr_math.py — never trust the LLM for hard facts.

Usage: validate_picks.py <hermes.md> <candidates.json>
"""
import json
import re
import sys
from pathlib import Path

PRICE_TOL = 0.35

PICK_RE = re.compile(r'^##\s+(\d+)\.\s*([A-Z][A-Z0-9]*)')


def entry_of(block: str):
    for line in block.split('\n'):
        if 'entry zone' in line.lower():
            tail = line.split(':', 1)[1] if ':' in line else line
            nums = [float(n) for n in re.findall(r'\d+(?:\.\d+)?', tail)]
            if nums:
                return sum(nums) / len(nums)
    return None


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <hermes.md> <candidates.json>", file=sys.stderr)
        sys.exit(2)
    report = Path(sys.argv[1])
    closes = {c['ticker'].upper(): c.get('close')
              for c in json.loads(Path(sys.argv[2]).read_text())}

    lines = report.read_text().split('\n')
    starts = [i for i, l in enumerate(lines) if re.match(r'^#{2,3}\s', l)]
    if not starts:
        return
    starts.append(len(lines))
    preamble = lines[:starts[0]]

    kept, others, dropped = [], [], []
    for s, e in zip(starts, starts[1:]):
        block = lines[s:e]
        m = PICK_RE.match(block[0])
        if not m:
            others.append(block)
            continue
        ticker = m.group(2).upper()
        reason = None
        if ticker not in closes:
            reason = 'not in candidates'
        else:
            entry, close = entry_of('\n'.join(block)), closes[ticker]
            if entry and close and abs(entry - close) / close > PRICE_TOL:
                reason = f'entry {entry:g} vs close {close:g} ({abs(entry-close)/close*100:.0f}% off)'
        (dropped.append((ticker, reason)) if reason else kept.append(block))

    out = list(preamble)
    for idx, block in enumerate(kept, 1):
        block = list(block)
        block[0] = re.sub(r'^##\s+\d+\.', f'## {idx}.', block[0])
        out += block
    for block in others:
        # the LLM's "Changes from Initial Picks" narrative lists the invented
        # tickers as fact — drop it so the report doesn't contradict itself.
        if 'changes from initial picks' in block[0].lower():
            continue
        out += block
    if dropped:
        out += ['', '### ⚠️ Auto-validator',
                f"Removed {len(dropped)} pick(s) not backed by today's candidate data: "
                + ', '.join(f'{t} ({r})' for t, r in dropped) + '.',
                'Only tickers in candidates.json are tradeable; invented tickers/prices were stripped.']

    report.write_text('\n'.join(out))
    print(f"validate_picks: kept {len(kept)}, dropped {len(dropped)}"
          + (": " + ', '.join(t for t, _ in dropped) if dropped else ''), file=sys.stderr)


if __name__ == '__main__':
    main()
