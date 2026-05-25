#!/usr/bin/env bash
# Weekly Hermes pipeline validation report → Telegram.
#
# Runs backtest_analyze.py + track_outcomes_hermes.py compare and sends a
# compact summary message. Fired by daily.sh only on Mondays around 9 WIB
# to avoid daily spam. Standalone usage: ./weekly_validation_report.sh

set -uo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

# Load secrets
if [ -f "$HOME/.idx-signals.env" ] && [ -z "${TELEGRAM_BOT_TOKEN:-}" ]; then
  set -a; . "$HOME/.idx-signals.env"; set +a
fi
if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ -z "${TELEGRAM_CHAT_ID:-}" ]; then
  echo "[telegram] env vars missing — aborting" >&2
  exit 1
fi

WIB_DATE=$(TZ=Asia/Jakarta date +%Y-%m-%d)

# Build report payload via Python (single-process, leverages json module)
REPORT=$("$ROOT/.venv/bin/python" - <<'PYEOF'
import json
import sys
from pathlib import Path

ROOT = Path("/Users/ultra/idx-signals")
sys.path.insert(0, str(ROOT))

from backtest_analyze import analyze
from track_outcomes_hermes import load_df, stats_for, STAGE_FILES

def fmt_diff(stage_val, baseline_val):
    if stage_val is None or baseline_val is None:
        return "—"
    diff = stage_val - baseline_val
    sign = "+" if diff > 0 else ""
    return f"{sign}{diff:.2f}"

# Backtest comparison
backtest = analyze()
lines = ["🔬 *Hermes Pipeline — Weekly Validation*", ""]

if backtest:
    s = backtest["sources"]
    n_dates = len(backtest["dates"])
    h5_s3 = s["Stage3 (Hermes final)"].get(5, {})
    h5_s1 = s["Stage1 (Hermes broad)"].get(5, {})
    h5_old = s["old_filter (H+M tier)"].get(5, {})

    lines.append(f"*Backtest ({n_dates} dates, 5d horizon):*")
    if h5_s3.get("n", 0) > 0:
        lines.append("```")
        lines.append(f"           n   mean%   win%  Sharpe")
        lines.append(f"Stage3    {h5_s3['n']:>2}  {h5_s3['mean_pct']:+5.2f}  "
                     f"{h5_s3['win_pct']:>4.1f}%   {h5_s3['sharpe']:>4.2f}")
        lines.append(f"Stage1    {h5_s1['n']:>2}  {h5_s1['mean_pct']:+5.2f}  "
                     f"{h5_s1['win_pct']:>4.1f}%   {h5_s1['sharpe']:>4.2f}")
        lines.append(f"OldFilter {h5_old['n']:>2}  {h5_old['mean_pct']:+5.2f}  "
                     f"{h5_old['win_pct']:>4.1f}%   {h5_old['sharpe']:>4.2f}")
        lines.append("```")

        diff_mean = h5_s3["mean_pct"] - h5_old["mean_pct"]
        diff_sharpe = h5_s3["sharpe"] - h5_old["sharpe"]
        verdict_sym = "✅" if (diff_mean > 1.0 and diff_sharpe > 0.3) else \
                      "⚠️" if (diff_mean < -1.0 or diff_sharpe < -0.3) else "🟡"
        lines.append(f"{verdict_sym} Stage3 vs OldFilter: "
                     f"{fmt_diff(h5_s3['mean_pct'], h5_old['mean_pct'])}% mean, "
                     f"{fmt_diff(h5_s3['sharpe'], h5_old['sharpe'])} Sharpe")
    else:
        lines.append("(no Stage3 picks yet)")
else:
    lines.append("*Backtest:* no data — run backtest_run_dates.sh")

# Live tracking
lines.append("")
lines.append("*Live (since daily.sh):*")
live = {
    "Stage1": load_df(STAGE_FILES["stage1"][1]),
    "Stage3": load_df(STAGE_FILES["stage3"][1]),
    "Mech":   load_df(ROOT / "outcomes.csv"),
}
any_data = False
lines.append("```")
lines.append(f"        n   mean%   win%")
for name, df in live.items():
    st = stats_for(df, 5)
    if st.get("n", 0) > 0:
        any_data = True
        lines.append(f"{name:<7}{st['n']:>2}  {st['mean_pct']:+5.2f}  {st['win_pct']:>4.1f}%")
    else:
        lines.append(f"{name:<7} —      —      —")
lines.append("```")
if not any_data:
    lines.append("_Need 5+ days of signal data to populate. Currently accumulating._")

lines.append("")
lines.append("[📊 Full dashboard](https://yazqe.github.io/idx-signals/validation.html)")

print("\n".join(lines))
PYEOF
)

if [ -z "$REPORT" ]; then
  echo "[error] empty report generated" >&2
  exit 1
fi

# Send to Telegram
RESP=$(curl -s -X POST \
  "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  -d "chat_id=${TELEGRAM_CHAT_ID}" \
  -d "parse_mode=Markdown" \
  -d "disable_web_page_preview=true" \
  --data-urlencode "text=${REPORT}")

if echo "$RESP" | jq -e '.ok' > /dev/null 2>&1; then
  echo "[telegram] weekly validation sent ($(echo "$REPORT" | wc -l) lines)"
else
  echo "[telegram] send failed:"
  echo "$RESP" | jq . 2>/dev/null || echo "$RESP"
  exit 1
fi
