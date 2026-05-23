# idx-signals

Daily IDX (Indonesia Stock Exchange) BUY-signal pipeline. Three technical
strategies → tier-sorted by per-ticker historical edge → qualitative review
by a local LLM via [Hermes Agent](https://github.com/NousResearch/hermes-agent).

**Signal-only — user executes manually on Stockbit.** Retail IDX brokers
don't expose trading APIs, so this is a research/recommendation tool, not
direct automation.

## Strategies

| Strategy          | Trigger                                         |
| ----------------- | ----------------------------------------------- |
| `rsi_oversold`    | 14d RSI crosses below 30                        |
| `ma_golden_cross` | 20-SMA crosses above 50-SMA                     |
| `vol_breakout_up` | volume > 2× 20d avg AND price up > 2% same day  |

SELL-side strategies (`rsi_overbought`, `ma_death_cross`, `vol_breakout_down`)
were tested but dropped — 2y backtest showed they predict **continuation**, not
reversal, in IDX small/mid-caps.

## Pipeline

```
fetch_prices.py     → data/<TICKER>.csv          (yfinance batch download)
compute_signals.py  → signals/YYYY-MM-DD.json    (raw signals, tier-sorted)
ask_hermes.sh       → signals/YYYY-MM-DD-hermes.md  (LLM qualitative review)
track_outcomes.py   → outcomes.csv               (actual P/L at 1/5/20d after entry)
build_lookup.py     → ticker_edge.json           (per-ticker edge, refreshed from outcomes)
```

## Daily workflow

```bash
cd ~/idx-signals
.venv/bin/python fetch_prices.py     # ~30s
.venv/bin/python compute_signals.py  # instant — tier-sorted output
./ask_hermes.sh                       # ~5 min — Hermes (local 72B) picks top 5

# Weekly:
.venv/bin/python track_outcomes.py    # log realized returns
.venv/bin/python build_lookup.py      # refresh ticker_edge.json from accumulated data
```

## Setup

Requires Python 3.12, [uv](https://github.com/astral-sh/uv), and Hermes Agent
running against an OpenAI-compatible LLM endpoint (local MLX server, OpenRouter,
etc.). See `.hermes/config.yaml` for provider config.

```bash
uv venv --python 3.12
uv pip install yfinance pandas numpy
```

## Tier definitions

Each signal gets tagged with historical conviction based on past trades for
the same (ticker, strategy) pair:

| Tier         | Criteria                                       |
| ------------ | ---------------------------------------------- |
| `high`       | mean 5d edge ≥ +5%, n ≥ 4                      |
| `medium`     | mean 5d edge +2% to +5%, n ≥ 3                 |
| `low`        | mean 5d edge between 0 and +2%                 |
| `untested`   | < 2 historical occurrences                     |
| `negative`   | mean 5d edge ≤ 0 — auto-skipped                |

`ask_hermes.sh` feeds only **high + medium** tiers to the LLM.

## Caveats

- **Look-ahead bias** affects 1d returns (signal triggers at close; realistic
  entry is next-day open). 5d/10d/20d horizons are clean.
- **Survivorship bias** — tickers that delisted aren't in yfinance.
- **No transaction cost modeling** beyond a flat 0.4% round-trip assumption
  in backtest output. Real slippage on speculative IDX small-caps can be worse.
- **Not financial advice.** Picks are computer-generated suggestions for
  manual review.
