#!/usr/bin/env python3
"""Generate dashboard index.html from candidates.json + Hermes report.

Modeled visually after yazqe/idx-ai-hedge-fund — dark GitHub-style theme,
card-per-ticker layout, color-coded tier badges. Renders to repo root so
GitHub Pages serves it at yazqe.github.io/idx-signals/.
"""
import json
import re
from pathlib import Path
from datetime import date, datetime

ROOT = Path(__file__).parent

# --- Read inputs ----------------------------------------------------------
candidates = json.loads((ROOT / "candidates.json").read_text())
today_iso = date.today().isoformat()
hermes_md = (ROOT / "signals" / f"{today_iso}-hermes.md")
hermes_text = hermes_md.read_text() if hermes_md.exists() else ""

# IHSG live value (best-effort: parse from cached snapshot or skip)
ihsg_value, ihsg_change = "—", ""
intraday = ROOT / "data" / "intraday_today.json"
if intraday.exists():
    snap = json.loads(intraday.read_text())
    # No IHSG in our snapshot; placeholder for now (could add fetch later)

# Parse top picks from Hermes markdown (## TICKER — BUY (...) sections)
top_picks: list[dict] = []
current: dict | None = None
for line in hermes_text.splitlines():
    if line.startswith("## "):
        if current:
            top_picks.append(current)
        m = re.match(r"##\s+([A-Z]+)\s+—", line)
        current = {"ticker": m.group(1), "fields": {}} if m else None
    elif current and line.startswith("- **"):
        m = re.match(r"-\s+\*\*([^:]+):\*\*\s*(.+)", line)
        if m:
            current["fields"][m.group(1).strip()] = m.group(2).strip()
if current:
    top_picks.append(current)

# Market read paragraph
market_read = ""
m = re.search(r"###\s+Market\s+[Rr]ead\s*\n+(.+?)(?=\n###|\Z)",
              hermes_text, re.DOTALL)
if m:
    market_read = m.group(1).strip()

# Stats by tier
by_tier: dict[str, list[dict]] = {"high": [], "medium": [], "low": [],
                                   "untested": [], "negative": []}
for c in candidates:
    by_tier[c["history"]["tier"]].append(c)

# Hermes-picked tickers — these get the "EXECUTE" badge on the dashboard
hermes_tickers = {p["ticker"] for p in top_picks}

# --- HTML template --------------------------------------------------------
def fmt_pct(x):
    if x is None: return "—"
    return f"{x*100:+.1f}%" if x is not None else "—"

def fmt_int_pct(x):
    if x is None: return "—"
    return f"{int(round(x*100))}%"

def card(c: dict) -> str:
    """One ticker card."""
    t = c["history"]["tier"]
    badge_class = f"badge-{t}"
    is_pick = c["ticker"] in hermes_tickers
    action_badge = '<span class="action-execute">✅ EXECUTE</span>' if is_pick \
        else '<span class="action-monitor">👀 MONITOR</span>'

    strategy_label = {
        "vol_breakout_up": "Volume Breakout",
        "rsi_oversold": "RSI Oversold",
        "ma_golden_cross": "Golden Cross",
    }.get(c["strategy"], c["strategy"])

    rsi_html = ""
    if c.get("rsi") is not None:
        rsi_html = f'<span class="chip chip-blue">RSI {c["rsi"]:.0f}</span>'

    vol_html = ""
    if c.get("vol_ratio") is not None:
        vol_html = f'<span class="chip chip-orange">Vol {c["vol_ratio"]:.1f}×</span>'

    pct_html = ""
    if c.get("pct_chg") is not None:
        sign = "+" if c["pct_chg"] >= 0 else ""
        cls = "chip-green" if c["pct_chg"] >= 0 else "chip-red"
        pct_html = f'<span class="chip {cls}">{sign}{c["pct_chg"]:.2f}%</span>'

    edge = c["history"].get("edge_5d")
    win = c["history"].get("win_5d")
    n = c["history"].get("n", 0)

    return f"""
    <div class="card card-{t}">
      <div class="card-head">
        <div class="card-ticker">
          <span class="ticker">{c['ticker']}</span>
          {action_badge}
        </div>
        <div class="card-price">Rp{c['close']:,.0f}</div>
      </div>
      <div class="card-body">
        <span class="chip chip-strategy">{strategy_label}</span>
        <span class="chip {badge_class}">{t.upper()}</span>
        {rsi_html}
        {vol_html}
        {pct_html}
      </div>
      <div class="card-stats">
        <div class="stat">
          <div class="stat-label">Edge 5d</div>
          <div class="stat-value">{fmt_pct(edge)}</div>
        </div>
        <div class="stat">
          <div class="stat-label">Win rate</div>
          <div class="stat-value">{fmt_int_pct(win)}</div>
        </div>
        <div class="stat">
          <div class="stat-label">Trades</div>
          <div class="stat-value">{n}</div>
        </div>
      </div>
    </div>
    """

def pick_card(p: dict) -> str:
    """Hermes top-pick card with entry/stop/TP."""
    f = p["fields"]
    return f"""
    <div class="pick-card">
      <div class="pick-head">
        <span class="ticker">{p['ticker']}</span>
        <span class="action-execute">✅ TOP PICK</span>
      </div>
      <div class="pick-grid">
        <div><div class="pick-label">Strategy</div><div>{f.get('Triggered', '—')}</div></div>
        <div><div class="pick-label">Conviction</div><div>{f.get('Conviction', '—')}</div></div>
        <div><div class="pick-label">Edge / Win</div><div>{f.get('Historical edge', '—')}</div></div>
        <div><div class="pick-label">Entry</div><div>{f.get('Entry zone', '—')}</div></div>
        <div><div class="pick-label">Stop</div><div>{f.get('Stop loss', '—')}</div></div>
        <div><div class="pick-label">Target</div><div>{f.get('Take profit', '—')}</div></div>
      </div>
      <div class="pick-why">{f.get('Why', '')}</div>
    </div>
    """

cards_html = "\n".join(card(c) for c in candidates if c["history"]["tier"] != "negative")
picks_html = "\n".join(pick_card(p) for p in top_picks)

n_high = len(by_tier["high"])
n_med = len(by_tier["medium"])
n_low = len(by_tier["low"])
n_neg = len(by_tier["negative"])
n_total = len(candidates)

import pytz
wib = datetime.now(pytz.timezone("Asia/Jakarta"))
wib_now = wib.strftime("%H:%M WIB")
h = wib.hour
session_label = "Sesi Pagi" if h < 12 else \
                "Sesi Siang" if h < 15 else \
                "Menjelang Tutup" if h < 16 else "After-hours"

html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0d1117">
<title>IDX Signals — {today_iso}</title>
<meta name="description" content="Daily IDX BUY signals — 3 strategies + Hermes Agent qualitative review">
<style>
:root {{
  --bg:#0d1117; --card:#161b22; --card-2:#1a1f27;
  --border:#30363d; --border-soft:#21262d;
  --text:#e6edf3; --muted:#8b949e; --dim:#6e7681;
  --green:#3fb950; --green-bg:#1a2d1e; --green-border:#2ea043;
  --red:#f85149; --red-bg:#2d1619; --red-border:#da3633;
  --gold:#d29922; --gold-bg:#272115; --gold-border:#9e6a03;
  --blue:#58a6ff; --blue-bg:#121d2f; --blue-border:#1f6feb;
  --purple:#bc8cff; --purple-bg:#1f1535; --purple-border:#6e40c9;
  --orange:#ffa657; --orange-bg:#27190c; --orange-border:#bd561d;
  --grey:#6e7681; --grey-bg:#1c2128;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{
  background:var(--bg); color:var(--text);
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  font-size:14px; line-height:1.55; min-height:100vh;
}}
.container{{max-width:1100px;margin:0 auto;padding:0 24px}}

/* Header */
header{{
  background:var(--card); border-bottom:1px solid var(--border);
  padding:16px 0; position:sticky; top:0; z-index:10;
  backdrop-filter:blur(8px); background:rgba(22,27,34,.92);
}}
.header-row{{display:flex;align-items:center;gap:16px;flex-wrap:wrap}}
.brand{{font-size:18px;font-weight:700;display:flex;align-items:center;gap:8px}}
.brand-mark{{color:var(--blue);font-size:18px}}
.meta{{margin-left:auto;text-align:right;font-size:11px;color:var(--muted)}}
.meta strong{{display:block;color:var(--text);font-weight:600}}

/* Hero stats */
.hero{{padding:36px 0 24px;text-align:center}}
.hero h1{{font-size:28px;font-weight:700;letter-spacing:-.02em}}
.hero p{{color:var(--muted);margin-top:6px;font-size:13px}}
.stats-row{{
  display:grid;grid-template-columns:repeat(5,1fr);gap:12px;
  margin:28px 0 32px;
}}
.stat-box{{
  background:var(--card);border:1px solid var(--border);
  border-radius:10px;padding:18px 12px;text-align:center;
}}
.stat-num{{font-size:30px;font-weight:700;line-height:1}}
.stat-name{{font-size:11px;color:var(--muted);margin-top:6px;
  text-transform:uppercase;letter-spacing:.06em;font-weight:500}}
.stat-box.high .stat-num{{color:var(--green)}}
.stat-box.medium .stat-num{{color:var(--gold)}}
.stat-box.low .stat-num{{color:var(--blue)}}
.stat-box.skip .stat-num{{color:var(--grey)}}
.stat-box.total .stat-num{{color:var(--text)}}

/* Section */
section{{margin:40px 0}}
section h2{{
  font-size:13px;font-weight:600;color:var(--muted);
  text-transform:uppercase;letter-spacing:.08em;
  margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid var(--border);
}}

/* Top pick cards */
.pick-card{{
  background:var(--card);border:1px solid var(--green-border);
  border-left:4px solid var(--green);
  border-radius:10px;padding:18px 20px;margin-bottom:14px;
  box-shadow:0 1px 3px rgba(0,0,0,.2);
}}
.pick-head{{display:flex;align-items:center;gap:12px;margin-bottom:14px}}
.pick-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:14px 24px;
  margin-bottom:14px;
}}
.pick-label{{font-size:10px;color:var(--muted);text-transform:uppercase;
  letter-spacing:.08em;margin-bottom:2px;font-weight:500}}
.pick-grid div div:last-child{{color:var(--text);font-size:13px;font-weight:500}}
.pick-why{{
  padding:10px 14px;background:var(--green-bg);border-radius:6px;
  color:var(--text);font-size:13px;font-style:italic;border-left:2px solid var(--green);
}}

/* Ticker cards */
.cards{{display:flex;flex-direction:column;gap:10px}}
.card{{
  background:var(--card);border:1px solid var(--border-soft);
  border-radius:10px;padding:14px 18px;
  transition:border-color .15s;
}}
.card:hover{{border-color:var(--border)}}
.card-high{{border-left:3px solid var(--green)}}
.card-medium{{border-left:3px solid var(--gold)}}
.card-low{{border-left:3px solid var(--blue)}}
.card-head{{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}}
.card-ticker{{display:flex;align-items:center;gap:10px}}
.ticker{{font-size:16px;font-weight:700;letter-spacing:.02em}}
.card-price{{font-size:15px;font-weight:600;color:var(--text);font-variant-numeric:tabular-nums}}
.card-body{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}}
.card-stats{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:12px;
  padding-top:10px;border-top:1px dashed var(--border-soft);
}}
.stat{{text-align:center}}
.stat-label{{font-size:10px;color:var(--muted);
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:2px}}
.stat-value{{font-size:13px;font-weight:600;font-variant-numeric:tabular-nums}}

/* Chips & badges */
.chip{{
  display:inline-flex;align-items:center;font-size:11px;font-weight:600;
  padding:3px 9px;border-radius:16px;border:1px solid;
  letter-spacing:.02em;
}}
.chip-strategy{{background:var(--purple-bg);color:var(--purple);border-color:var(--purple-border)}}
.chip-green{{background:var(--green-bg);color:var(--green);border-color:var(--green-border)}}
.chip-red{{background:var(--red-bg);color:var(--red);border-color:var(--red-border)}}
.chip-blue{{background:var(--blue-bg);color:var(--blue);border-color:var(--blue-border)}}
.chip-orange{{background:var(--orange-bg);color:var(--orange);border-color:var(--orange-border)}}
.badge-high{{background:var(--green-bg);color:var(--green);border-color:var(--green-border)}}
.badge-medium{{background:var(--gold-bg);color:var(--gold);border-color:var(--gold-border)}}
.badge-low{{background:var(--blue-bg);color:var(--blue);border-color:var(--blue-border)}}
.action-execute{{
  font-size:10px;font-weight:700;padding:3px 9px;border-radius:14px;
  background:var(--green-bg);color:var(--green);border:1px solid var(--green-border);
  letter-spacing:.04em;
}}
.action-monitor{{
  font-size:10px;font-weight:700;padding:3px 9px;border-radius:14px;
  background:var(--gold-bg);color:var(--gold);border:1px solid var(--gold-border);
  letter-spacing:.04em;
}}

/* Market read */
.market-read{{
  background:var(--card);border:1px solid var(--border);
  border-left:3px solid var(--blue);
  border-radius:10px;padding:18px 22px;color:var(--text);
  font-size:14px;line-height:1.65;
}}

/* Footer */
footer{{
  border-top:1px solid var(--border);margin-top:60px;
  padding:28px 0 36px;text-align:center;color:var(--muted);font-size:12px;
}}
.disclaimer{{margin-top:6px;color:var(--dim);font-size:11px}}

/* Responsive */
@media(max-width:720px){{
  .stats-row{{grid-template-columns:repeat(3,1fr)}}
  .pick-grid{{grid-template-columns:repeat(2,1fr)}}
  .card-stats{{grid-template-columns:repeat(3,1fr)}}
  .hero h1{{font-size:22px}}
}}
@media(max-width:480px){{
  .stats-row{{grid-template-columns:repeat(2,1fr)}}
  .pick-grid{{grid-template-columns:1fr 1fr}}
}}
</style>
</head>
<body>

<header>
  <div class="container header-row">
    <div class="brand">
      <span class="brand-mark">▲</span>
      <span>IDX Signals</span>
    </div>
    <div class="meta">
      <strong>{today_iso}</strong>
      <span>{session_label} · {wib_now}</span>
    </div>
  </div>
</header>

<div class="container">

  <div class="hero">
    <h1>Daily BUY Signal Dashboard</h1>
    <p>3 technical strategies · per-ticker historical edge · Hermes Agent qualitative review</p>
  </div>

  <div class="stats-row">
    <div class="stat-box high"><div class="stat-num">{n_high}</div><div class="stat-name">High</div></div>
    <div class="stat-box medium"><div class="stat-num">{n_med}</div><div class="stat-name">Medium</div></div>
    <div class="stat-box low"><div class="stat-num">{n_low}</div><div class="stat-name">Low</div></div>
    <div class="stat-box skip"><div class="stat-num">{n_neg}</div><div class="stat-name">Skip</div></div>
    <div class="stat-box total"><div class="stat-num">{n_total}</div><div class="stat-name">Total</div></div>
  </div>

  {f'''<section>
    <h2>Hermes Top Picks · 5–20 day hold</h2>
    {picks_html}
  </section>''' if picks_html else ''}

  {f'''<section>
    <h2>Market Read</h2>
    <div class="market-read">{market_read}</div>
  </section>''' if market_read else ''}

  <section>
    <h2>All Candidates · {len(candidates) - n_neg} actionable ({n_neg} historically negative skipped)</h2>
    <div class="cards">
      {cards_html}
    </div>
  </section>

</div>

<footer>
  <div class="container">
    <div>Generated automatically by <code>idx-signals</code> · 3× daily during IDX trading sessions</div>
    <div class="disclaimer">Not financial advice. Past performance does not guarantee future results.</div>
  </div>
</footer>

</body>
</html>
"""

(ROOT / "index.html").write_text(html)
print(f"Wrote index.html ({len(html):,} bytes)")
