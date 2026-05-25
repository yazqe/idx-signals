#!/usr/bin/env python3
"""Generate validation.html — Hermes pipeline empirical validation dashboard.

Three sections:
  1. Backtest comparison (Hermes vs baselines on identical sample dates)
  2. Full-history baselines (2-year reference — what wins overall?)
  3. Live tracking accumulation (will populate as daily.sh runs)

Output: validation.html in repo root, served at yazqe.github.io/idx-signals/validation
"""
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# Lazy import (these are expensive) — wrap in try in case backtest results not yet ready
try:
    from backtest_analyze import analyze as backtest_analyze
except Exception:
    backtest_analyze = None
try:
    from backtest_compare import run_comparison as full_history_compare
except Exception:
    full_history_compare = None
try:
    from track_outcomes_hermes import (
        load_df, stats_for as live_stats_for, STAGE_FILES
    )
except Exception:
    load_df = None


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #0d1117; color: #c9d1d9;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  line-height: 1.5; padding: 24px;
}
h1 { color: #58a6ff; font-size: 24px; margin-bottom: 8px; }
h2 { color: #79c0ff; font-size: 18px; margin: 32px 0 12px; border-bottom: 1px solid #30363d; padding-bottom: 6px; }
h3 { color: #d2a8ff; font-size: 14px; margin: 16px 0 8px; }
.subtitle { color: #8b949e; font-size: 13px; margin-bottom: 4px; }
.timestamp { color: #6e7681; font-size: 11px; font-family: ui-monospace, monospace; }
.section { margin: 24px 0; padding: 16px; background: #161b22; border: 1px solid #30363d; border-radius: 6px; }
table { width: 100%; border-collapse: collapse; font-family: ui-monospace, monospace; font-size: 12px; margin-top: 12px; }
th { background: #1c2128; color: #79c0ff; text-align: right; padding: 8px; border-bottom: 1px solid #30363d; font-weight: 600; }
th:first-child { text-align: left; }
td { padding: 8px; border-bottom: 1px solid #21262d; text-align: right; }
td:first-child { text-align: left; color: #c9d1d9; font-weight: 500; }
tr:hover td { background: #1c2128; }
.tag { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 600; }
.tag-best { background: #033a16; color: #56d364; }
.tag-good { background: #1f6feb33; color: #79c0ff; }
.tag-bad { background: #67060c; color: #f85149; }
.tag-neutral { background: #21262d; color: #8b949e; }
.pos { color: #56d364; }
.neg { color: #f85149; }
.muted { color: #6e7681; }
.callout { padding: 12px; margin: 12px 0; background: #1c2128; border-left: 3px solid #58a6ff; border-radius: 0 6px 6px 0; font-size: 13px; }
.callout-warn { border-left-color: #d29922; }
.callout-good { border-left-color: #56d364; }
.empty { padding: 24px; text-align: center; color: #6e7681; font-style: italic; }
.legend { font-size: 11px; color: #8b949e; margin-top: 8px; font-family: ui-monospace, monospace; }
.nav { font-size: 13px; margin-bottom: 16px; }
.nav a { color: #58a6ff; text-decoration: none; margin-right: 12px; }
.nav a:hover { text-decoration: underline; }
"""


def cell_pct(value, best=False, worst=False):
    """Format a percent value with color + best/worst tag."""
    if value is None:
        return '<td class="muted">—</td>'
    color = "pos" if value > 0 else ("neg" if value < 0 else "")
    tag = ""
    if best:
        tag = ' <span class="tag tag-best">BEST</span>'
    elif worst:
        tag = ' <span class="tag tag-bad">WORST</span>'
    return f'<td class="{color}">{value:+.2f}%{tag}</td>'


def cell_num(value, fmt="{:.2f}", best=False, worst=False):
    if value is None:
        return '<td class="muted">—</td>'
    tag = ""
    if best:
        tag = ' <span class="tag tag-best">BEST</span>'
    elif worst:
        tag = ' <span class="tag tag-bad">WORST</span>'
    return f'<td>{fmt.format(value)}{tag}</td>'


def render_stats_table(sources_data: dict, horizon: int) -> str:
    """Render side-by-side comparison for one horizon, marking best/worst per column."""
    rows = []
    for name, by_h in sources_data.items():
        s = by_h.get(horizon, {})
        if s.get("n", 0) == 0:
            rows.append((name, None))
        else:
            rows.append((name, s))

    valid = [(n, s) for n, s in rows if s is not None]
    if not valid:
        return '<div class="empty">No data for this horizon yet</div>'

    # Find best/worst for each numeric column
    def best_idx(col, higher_is_better=True):
        vals = [s.get(col) for _, s in valid if s.get(col) is not None]
        if not vals:
            return None
        return max(vals) if higher_is_better else min(vals)

    best_mean = best_idx("mean_pct")
    worst_mean = best_idx("mean_pct", False)
    best_sharpe = best_idx("sharpe")
    worst_sharpe = best_idx("sharpe", False)
    best_win = best_idx("win_pct")
    best_cum = best_idx("cum_pct")

    html = ['<table>',
            '<thead><tr><th>Source</th><th>n</th><th>Mean%</th><th>Win%</th>'
            '<th>Med%</th><th>Best%</th><th>Worst%</th><th>Cum%</th>'
            '<th>Sharpe</th></tr></thead><tbody>']
    for name, s in rows:
        if s is None:
            html.append(f'<tr><td>{name}</td><td colspan="8" class="muted">no picks</td></tr>')
            continue
        html.append('<tr>')
        html.append(f'<td>{name}</td>')
        html.append(f'<td>{s["n"]}</td>')
        html.append(cell_pct(s["mean_pct"],
                            best=s["mean_pct"] == best_mean,
                            worst=s["mean_pct"] == worst_mean and len(valid) > 1))
        html.append(f'<td>{s["win_pct"]:.1f}%' +
                    (' <span class="tag tag-best">BEST</span>' if s["win_pct"] == best_win else '')
                    + '</td>')
        html.append(cell_pct(s.get("median_pct")))
        html.append(cell_pct(s.get("best_pct")))
        html.append(cell_pct(s.get("worst_pct")))
        if "cum_pct" in s:
            html.append(cell_pct(s.get("cum_pct"),
                                best=s.get("cum_pct") == best_cum))
        else:
            html.append('<td class="muted">—</td>')
        html.append(cell_num(s.get("sharpe"),
                            best=s.get("sharpe") == best_sharpe,
                            worst=s.get("sharpe") == worst_sharpe and len(valid) > 1))
        html.append('</tr>')
    html.append('</tbody></table>')
    return '\n'.join(html)


def render_backtest_section() -> str:
    if backtest_analyze is None:
        return '<div class="empty">backtest_analyze module not importable</div>'
    try:
        result = backtest_analyze()
    except Exception as e:
        return f'<div class="empty">Error: {e}</div>'
    if result is None:
        return '''<div class="empty">No backtest results yet.<br>
        Run <code>./backtest_run_dates.sh DATE1 DATE2 ...</code> to populate.</div>'''

    out = [
        f'<p class="subtitle">Dates tested: <code>{", ".join(result["dates"])}</code></p>',
        f'<p class="subtitle">Pick counts: '
        f'Stage1={result["counts"]["stage1_picks"]}, '
        f'Stage3={result["counts"]["stage3_picks"]}, '
        f'old_filter={result["counts"]["old_filter"]}, '
        f'mechanical_all={result["counts"]["mechanical_all"]}</p>',
    ]
    for h in (1, 5, 20):
        out.append(f'<h3>Horizon: {h}d forward return (fees applied)</h3>')
        out.append(render_stats_table(result["sources"], h))

    out.append('''<div class="callout">
        <strong>Decision logic:</strong><br>
        • Stage3 ≥ old_filter → Hermes adds value, keep full pipeline<br>
        • Stage1 ≥ old_filter but Stage3 &lt; Stage1 → drop Stages 2+3<br>
        • old_filter ≥ both Hermes → simplify to mechanical tier filter
    </div>''')
    out.append('<p class="legend">Caveat: ticker_edge uses current-day view (look-ahead bias). '
               'Small sample (~5 dates) — directional only.</p>')
    return ''.join(out)


def render_full_history_section() -> str:
    if full_history_compare is None:
        return '<div class="empty">backtest_compare module not importable</div>'
    try:
        result = full_history_compare()
    except Exception as e:
        return f'<div class="empty">Error: {e}</div>'

    sources = {
        "mechanical_all":     result.get("mechanical_all", {}),
        "old_filter (H+M)":   result.get("old_filter (H+M)", {}),
        "stage1_broader":     result.get("stage1_broader", {}),
        "vol_breakout_only":  result.get("vol_breakout_only", {}),
        "top5_per_day":       result.get("top5_per_day", {}),
    }
    out = ['<p class="subtitle">2-year backtest reference (Jun 2024 → May 2026), '
           'all 5300+ signals.</p>']
    for h in (1, 5, 20):
        out.append(f'<h3>Horizon: {h}d forward return (fees applied)</h3>')
        out.append(render_stats_table(sources, h))
    out.append('<p class="legend">Reference benchmark — what filtering wins on full history. '
               'Compare with backtest section above.</p>')
    return ''.join(out)


def render_live_section() -> str:
    if load_df is None:
        return '<div class="empty">live tracking module not importable</div>'
    sources = {
        "Stage1 (Hermes picks)":  load_df(STAGE_FILES["stage1"][1]),
        "Stage3 (Hermes final)":  load_df(STAGE_FILES["stage3"][1]),
        "Mechanical (all)":       load_df(ROOT / "outcomes.csv"),
    }
    summary = {name: {h: live_stats_for(df, h) for h in (1, 5, 20)}
               for name, df in sources.items()}
    out = ['<p class="subtitle">Live picks tracked since daily.sh integration. '
           'Accumulates over time — at least 30 days needed for meaningful comparison.</p>']

    nonempty = sum(1 for src in summary.values() for h in (1, 5, 20) if src[h].get("n", 0) > 0)
    if nonempty == 0:
        out.append('''<div class="empty">
            No live outcomes yet (need ≥ 1 day since signal date for 1d horizon).<br>
            Will populate automatically as <code>daily.sh</code> runs.
        </div>''')
    else:
        for h in (1, 5, 20):
            out.append(f'<h3>Horizon: {h}d</h3>')
            out.append(render_stats_table(summary, h))
    return ''.join(out)


def render_verdict() -> str:
    """Auto-generate a 1-paragraph verdict by reading backtest results."""
    if backtest_analyze is None:
        return ''
    try:
        result = backtest_analyze()
    except Exception:
        return ''
    if result is None:
        return ''
    s = result["sources"]
    h5_stage3 = s["Stage3 (Hermes final)"].get(5, {})
    h5_old = s["old_filter (H+M tier)"].get(5, {})
    if h5_stage3.get("n", 0) == 0 or h5_old.get("n", 0) == 0:
        return ''
    diff_mean = h5_stage3["mean_pct"] - h5_old["mean_pct"]
    diff_sharpe = (h5_stage3.get("sharpe") or 0) - (h5_old.get("sharpe") or 0)

    if diff_mean > 1.0 and diff_sharpe > 0.3:
        verdict = ('<strong class="pos">VERDICT: Hermes adds value.</strong> Stage 3 picks beat '
                   f'the HIGH+MED tier filter by {diff_mean:+.2f}% mean and {diff_sharpe:+.2f} Sharpe '
                   '(5d horizon) on backtested dates. Keep the full pipeline.')
        klass = 'callout-good'
    elif diff_mean < -1.0 or diff_sharpe < -0.3:
        verdict = ('<strong class="neg">VERDICT: Hermes hurts performance.</strong> Stage 3 picks '
                   f'underperform old_filter by {diff_mean:+.2f}% mean and {diff_sharpe:+.2f} Sharpe '
                   '(5d horizon). Recommend reverting to mechanical tier filter, drop Stages 2-3.')
        klass = 'callout-warn'
    else:
        verdict = ('<strong>VERDICT: Inconclusive.</strong> Stage 3 ≈ old_filter '
                   f'(diff: {diff_mean:+.2f}% mean, {diff_sharpe:+.2f} Sharpe). Sample too small '
                   'or effect too marginal to justify Hermes pipeline complexity. '
                   'Default to simpler (drop Stages 2-3).')
        klass = 'callout-warn'

    return f'<div class="callout {klass}">{verdict}</div>'


def render_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IDX Signals — Hermes Pipeline Validation</title>
<style>{CSS}</style>
</head>
<body>
<h1>🔬 Hermes Pipeline Validation</h1>
<p class="subtitle">Empirical analysis: does the 3-stage Hermes pipeline beat
a simple mechanical tier filter?</p>
<p class="timestamp">Generated: {datetime.now().isoformat(timespec='seconds')}</p>

<div class="nav">
  <a href="./">← Dashboard</a>
  <a href="./signals/">Signals archive</a>
</div>

{render_verdict()}

<div class="section">
<h2>1. Backtest Comparison (sampled dates)</h2>
{render_backtest_section()}
</div>

<div class="section">
<h2>2. Full-History Reference (2 years, all 5300+ signals)</h2>
{render_full_history_section()}
</div>

<div class="section">
<h2>3. Live Outcomes Tracking</h2>
{render_live_section()}
</div>

</body>
</html>
"""


def main():
    out_path = ROOT / "validation.html"
    html = render_html()
    out_path.write_text(html)
    print(f"Wrote {out_path} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
