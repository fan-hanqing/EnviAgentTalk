# sec_bw — construction record

## Source

> Patel, S.K., Lee, B., Westerhoff, P. & Elimelech, M., "The potential of
> electrodialysis as a cost-effective alternative to reverse osmosis for
> brackish water desalination", *Water Research* **250** (2024) 121009.

**Fig. 3** (page 6): levelised cost of water as stacked bars for ED and RO at
feed salinities 1, 3, 5, 7 and 10 g/L, with the specific energy consumption of
each technology overlaid as lines against the right-hand axis. Fig. 6B plots
the same two SEC series again, plus a third "optimized ED" case.

## Why this source, and not Table S1 of the Desalination review

An earlier attempt fitted Table S1 of Shah et al., *Desalination* **538**
(2022) 115827 — 116 rows of published desalination energy figures. That fit
was abandoned. It has two problems in the inland brackish range:

1. its low-salinity end is carried almost entirely by laboratory stacks;
2. the review's table contains **no brackish reverse osmosis at all** — its 37
   RO rows are all 31,600–47,000 ppm seawater — and BWRO is the dominant
   inland technology.

Patel et al. model both technologies over exactly 1–10 g/L (1000–10000 ppm) with every
operating condition stated. That closes the BWRO gap and gives a fully
specified method, at the cost of being modelled rather than measured.

## Digitisation

Digitised from the printed figure with PlotDigitizer.

**The x axis needed correction.** Fig. 3 is a bar chart: its categories sit at
evenly spaced pixel positions (428, 543, 656, 769, 883 — spacings 115, 113,
113, 114) but carry the non-uniform values 1, 3, 5, 7, 10 g/L. Calibrating it
as a linear 1→10 axis therefore returned 1, 3.25, 5.5, 7.75, 10. The digitiser
x output was discarded and the known category values substituted.

**The y calibration is independent and exact.** Axis pixels 1836 → 0.0 and
1517 → 3.0 kWh/m³. Checked: point 0 at pixel y 1827 gives
(1836−1827)/319 × 3 = 0.08464, matching the digitiser output to five decimals.
Resolution 3.0/319 = 0.0094 kWh/m³ per pixel.

**Series identification.** Series A reads 0.085 at 1 g/L and 0.762 at 3 g/L;
series B reads 0.320 and 0.555. Section 3.2 of the paper states that at 1 g/L
"the energy consumption of ED is significantly lower than that of RO" and that
"at 3 g L⁻¹, RO actually provides a lower energy consumption than ED". Series A
is therefore ED and series B is RO. The values also match Fig. 6B's current-ED
and current-RO curves.

## Data

```
technology  feed_ppm  sec_kwh_per_m3
ED         1000      0.0846
ED         3000      0.7618
ED         5000      1.2508
ED         7000      1.7962
ED        10000      2.7743
RO         1000      0.3197
RO         3000      0.5549
RO         5000      0.7806
RO         7000      0.9969
RO        10000      1.4577
```

## The crossover

```
 1 g/L   ED 0.085   RO 0.320   diff -0.235
 3       ED 0.762   RO 0.555   diff +0.207
 5       ED 1.251   RO 0.781   diff +0.470
 7       ED 1.796   RO 0.997   diff +0.799
10       ED 2.774   RO 1.458   diff +1.317
```

Linear interpolation on the 1–3 g/L segment puts the crossover at **2.06 g/L = 2060 ppm**.
The paper states that a crossover exists in that interval; it does not locate
it. The 2.06 figure is ours.

Physically: ED energy is proportional to the salt actually transported, so at
1 g/L feed and a fixed 0.5 g/L product it moves very little salt and costs very
little. RO must pressurise the feed regardless. As salinity rises ED's energy
climbs 33× from 1 to 10 g/L while RO's climbs only 4.6×, and RO overtakes.

This is why `technology` has no default despite RO holding over 80% of
installed brackish capacity: the choice is worth up to a factor of two, and its
sign reverses inside the tool's own valid range.

## Cross-check against published practice

The abandoned fit is still useful as an independent yardstick. Ordinary least
squares on the 16 electrodialysis rows of that Table S1 gives

```
log10(SEC kWh/m3) = -2.692328 + 0.780635 * log10(feed ppm TDS)
n = 16   R2 = 0.746   residual geometric s.d. 1.87   valid 585-35000 ppm
```

Against the ED curve digitised here:

```
 1000 ppm   Fig3 ED 0.085   literature fit 0.446   ratio 0.19
 3000       0.762           1.052                  0.72
 5000       1.251           1.568                  0.80
 7000       1.796           2.038                  0.88
10000       2.774           2.693                  1.03
```

At 10000 ppm a mechanistic process model and an empirical regression over 16
unrelated published studies agree to 3%. That is strong mutual corroboration
and neither was tuned to the other.

At 1000 ppm they differ by a factor of 5, the model being lower. The
explanation is consistent: the literature fit's low-salinity end is
laboratory-scale work, and the
proportional penalty of non-optimal operation is largest where the
thermodynamic requirement is smallest. Over 2000–5000 ppm — where inland
brackish groundwater usually sits — the two differ by 25–80%.

This divergence is not an error in either source. It is the gap between
**modelled optimum** and **published practice**, it is quantified, and it must
travel with any number taken from `sec_bw`.

## Unit conversion

The source works in g/L. This tool takes **ppm**, because that is the unit
the desalination literature states feed salinity in and the unit a caller is
most likely to already have. The conversion
1 g/L = 1000 ppm assumes a solution density of 1 kg/L; over 1–10 g/L the true
density reaches about 1.007 kg/L, so ppm is understated by at most 0.7% — an
order of magnitude below the digitisation error, but an assumption, and stated
as one in `conditions`.

## Declared gaps

1. **Modelled, not measured.** Cost-optimal productivity is a design ideal; no
   operating plant is sized that way. These are lower bounds on real consumption.
2. **Three variables fixed, not exposed.** Product salinity 0.5 g/L, recovery
   80%, productivity cost-optimised. Changing any of them invalidates the
   numbers, and a caller cannot vary them through this tool.
3. **RO's energy recovery device is applied everywhere except 1 g/L**, so the
   RO curve's left endpoint rests on a different assumption from the rest of it.
4. **No ionic composition.** A single NaCl-equivalent TDS; real inland
   groundwater is hard and sulphate-rich, and ED energy depends on which ions
   move.
5. **Five computed points only.** Everything between them is our interpolation.
6. **Concentrate disposal is outside the boundary** — for inland desalination
   this is often the binding constraint, and no part of it is in these numbers.
