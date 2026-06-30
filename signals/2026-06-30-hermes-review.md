# Hermes Review — 2026‑06‑30  

## 1. Sanity Check (math + logic)  

- **APLN**:  
  - ❌ **R/R not disclosed** – the analysis only gives “‑2 % SL, +4 % TP”. The implied risk‑reward is 2.0, but the author never states it, violating the R/R‑verification requirement.  
  - ❌ **SL placement** – a flat “‑2 % below close” is an arbitrary percentage, not anchored to a technical level (support, ATR‑based stop, or volatility‑adjusted point). This could place the stop inside the noise band.  
  - ❌ **TP placement** – “+4 % above close” is not tied to any identified resistance, pivot, or profit‑target zone. It appears to be a mirror of the SL distance rather than a market‑based target.  
  - ❌ **Tier consistency** – Conviction is marked *Low* yet the pick is still presented as a “BUY”. With a win‑rate barely above 50 % and a minuscule edge (0.49 %), the low tier should have been reflected by a *neutral* or *avoid* recommendation, not a buy.  

- **MEDC**:  
  - ❌ **R/R not disclosed** – same issue as APLN; implied R/R = (4 %)/(2 %) = 2.0 but not explicitly reported.  
  - ❌ **SL placement** – a flat “‑2 % below close” again ignores structural support levels or volatility‑adjusted buffers.  
  - ❌ **TP placement** – “+4 % above close” lacks justification from resistance, prior highs, or Fibonacci extensions.  
  - ❌ **Tier consistency** – Conviction is *Low* while the recommendation is a straight “BUY”. Given a win‑rate of 55.6 % and a tiny edge (0.41 %), a low‑confidence stance should have been accompanied by a *cautious* qualifier, not a plain buy.  

Both picks pass the basic arithmetic check (2 % vs 4 % yields a 2.0 R/R), but the omission of an explicit R/R figure and the reliance on arbitrary percentage stops/targets constitute **sanity failures**.  

## 2. Contradiction Hunter  

1. **“Low conviction” vs “BUY”** – In both APLN and MEDC the author tags the conviction as *Low* yet still issues a buy signal. This contradicts the internal logic that low conviction should translate to a neutral/avoid stance or at least a “watch” label.  
2. **Mean‑reversion claim vs limited upside** – The author states the trade is a “short‑term mean‑reversion potential” (implying a bounce) while simultaneously qualifying that “limited upside unless broader market momentum lifts these names.” If the broader market is bearish, the mean‑reversion premise collapses, yet the analysis does not reconcile this conflict.  

## 3. Hidden Risks  

- **Sector concentration** – Both APLN and MEDC belong to the *basic materials / consumer* segment (Astra Plastik Nusantara and Medco Energy, respectively). Concentrating two low‑conviction longs in the same sector inflates sector‑specific VaR; a sector‑wide shock would simultaneously impair both positions.  
- **Liquidity risk** – Neither ticker’s average daily volume is disclosed. If either security trades < 200 k shares/day, a 5‑20 day hold could encounter slippage, especially with a tight 2 % stop that may be breached by a single large order.  
- **Correlation risk** – Both picks are driven solely by RSI‑oversold alerts. RSI tends to move in tandem across correlated assets, so the two signals are not independent; the portfolio is effectively double‑counting the same momentum bias.  
- **Timing / chase risk** – If either stock has already rallied > 10 % today (common for oversold reversals), entering at the upper bound of the entry zone (≈105.5 for APLN, 1035 for MEDC) could be a “late‑entry” chase, increasing the probability of a pull‑back to the stop.  
- **Stale indicator risk** – RSI is a lagging oscillator; the analysis does not mention the look‑back period or whether the oversold condition is persistent or a fleeting dip. A single‑day RSI dip can be a false signal if the broader trend is still down.  
- **Indicator overlap** – The entire thesis rests on one indicator (RSI‑oversold). No secondary confirmation (e.g., volume surge, candlestick pattern, or higher‑timeframe trend) is provided, making the signal fragile to random noise.  

## 4. What the Author Got Right  

The author correctly identifies that the historical edge for both stocks is positive, albeit marginal, and transparently reports the win‑rate and edge magnitude. This honest quantification prevents over‑optimistic expectations and keeps the risk‑reward framing (2 :1) in view.  

## 5. Critical Recommendations  

1. **Replace arbitrary % stops with structure‑based levels** – Set the SL at the nearest technical support (e.g., prior swing low, ATR‑based buffer, or a key moving‑average) rather than a flat 2 % drop. This aligns risk with market‑defined price barriers.  
2. **Add a second‑layer filter** – Require a confirming signal (e.g., bullish candlestick, volume spike, or higher‑timeframe trend reversal) before issuing a BUY. This will filter out false RSI‑oversold triggers and improve conviction alignment.  
3. **Cap sector exposure and position size** – Limit the combined exposure to the *basic materials / consumer* sector to ≤ 10 % of the total portfolio and cap each individual position at ≤ 5 % of capital. This mitigates sector‑specific drawdowns and prevents over‑concentration from two low‑conviction longs.
