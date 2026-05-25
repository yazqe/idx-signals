#!/usr/bin/env python3
"""Recompute R/R in hermes.md from Entry/SL/TP values.

LLMs are bad at arithmetic. Trust the structured price data, not the LLM's math.

Usage:
    python3 fix_rr_math.py signals/2026-05-25-hermes.md

Operates in-place. Writes "(auto-computed)" suffix so downstream readers know
the R/R was post-processed.
"""
import re
import sys
from pathlib import Path
from typing import Optional, Tuple


def parse_price(text: str) -> Optional[float]:
    """Extract first meaningful price from a markdown line.

    Handles:
      - "Entry zone: 700 ± 5%"        → 700
      - "Entry zone: 700-720"          → 710 (midpoint)
      - "Entry zone: 700 to 720"       → 710
      - "Stop loss: 670 (support)"     → 670
      - "Take profit: 770 (resistance)" → 770
    """
    # Strip parenthetical context first so we don't pick numbers from there
    cleaned = re.sub(r'\([^)]*\)', '', text)

    # Range like "700-720" or "700 - 720" or "700 to 720"
    range_match = re.search(
        r'(\d+(?:\.\d+)?)\s*(?:[-–—]|to)\s*(\d+(?:\.\d+)?)',
        cleaned
    )
    if range_match:
        a = float(range_match.group(1))
        b = float(range_match.group(2))
        # Sanity: midpoint only if 2nd value is within 2x of 1st (avoid -5%/+15% style)
        if 0.5 <= b / a <= 2.0:
            return (a + b) / 2

    # Tolerance like "700 ± 5%" → 700
    pm_match = re.search(r'(\d+(?:\.\d+)?)\s*[±]', cleaned)
    if pm_match:
        return float(pm_match.group(1))

    # First standalone number
    num_match = re.search(r'(\d+(?:\.\d+)?)', cleaned)
    return float(num_match.group(1)) if num_match else None


def fix_rr(content: str) -> Tuple[str, int, int]:
    """Find each pick block and overwrite its R/R line with computed value.

    Returns: (new_content, num_fixed, num_failed)
    """
    lines = content.split('\n')
    out = []
    entry = sl = tp = None
    pick_header = re.compile(r'^## \d')
    fixed = failed = 0

    for line in lines:
        # Reset on new pick header
        if pick_header.match(line):
            entry = sl = tp = None

        lower = line.lower()
        if '**entry zone:**' in lower or '**entry:**' in lower:
            entry = parse_price(line)
        elif '**stop loss:**' in lower or '**sl:**' in lower:
            sl = parse_price(line)
        elif '**take profit:**' in lower or '**tp:**' in lower or '**tp1:**' in lower:
            tp = parse_price(line)
        elif '**r/r:**' in lower or '**rr:**' in lower:
            if entry is not None and sl is not None and tp is not None:
                if entry > sl and tp > entry:
                    rr = (tp - entry) / (entry - sl)
                    line = f'- **R/R:** {rr:.2f} (auto-computed: TP {tp:g} − Entry {entry:g}) / (Entry − SL {sl:g})'
                    fixed += 1
                else:
                    line = f'- **R/R:** INVALID — Entry={entry:g}, SL={sl:g}, TP={tp:g} (SL must be < Entry < TP)'
                    failed += 1
            else:
                line = f'- **R/R:** N/A — missing data (Entry={entry}, SL={sl}, TP={tp})'
                failed += 1

        out.append(line)

    return '\n'.join(out), fixed, failed


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <hermes.md>', file=sys.stderr)
        sys.exit(2)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f'File not found: {path}', file=sys.stderr)
        sys.exit(1)

    original = path.read_text()
    new_content, fixed, failed = fix_rr(original)

    if new_content == original:
        print(f'[fix_rr] No R/R lines found in {path}')
        return

    path.write_text(new_content)
    print(f'[fix_rr] {path}: {fixed} R/R recomputed, {failed} invalid/missing')


if __name__ == '__main__':
    main()
