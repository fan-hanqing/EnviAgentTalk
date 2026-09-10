# drought_ef — construction record

*Written so that the authors of the source can check every number in it.
Nothing below is fitted, tuned, or assumed. Every value is a sum, a ratio, or
a min/max over columns that already exist in their own published file.*

---

## 1. Source

> Qiu, M., et al., "Drought impacts on the electricity system, emissions, and
> air quality in the western United States", *PNAS* **120** (2023) e2300395120.

Replication repository: <https://github.com/mhqiu/drought-electricity-WUS>
(contact: mhqiu@stanford.edu)

**The one file used:**

```
Data/intermediate/unit_drought_emis_historical.rds
sha256  96be7b5b6cd7a377d152b2a8d776f7a21588e90d07f69cf981e91fb661c73537
rows    108,190 unit-months
years   2001 – 2021
states  AZ CA CO ID MT NM NV OR SD TX UT WA WY
```

Per the repository README, that file is *"the estimated drought-induced
emissions and observed emissions from each fossil fuel unit from 2001 to
2021, generated using 2_historical_damages.R"*.

No other file, and no data from outside the repository, is used.

---

## 2. Which of the authors' columns are used

Four, and only four:

| column | meaning in the source | used for |
|---|---|---|
| `gen_total` | drought-induced generation, MWh, = `gen_CA + gen_NW + gen_SW` | numerator of the scale, denominator of the intensity |
| `co2_total` | drought-induced CO₂, **short tons**, = `co2_CA + co2_NW + co2_SW` | numerator of the intensity |
| `grossload_mw` | observed generation of the unit in that month | denominator for the drought share; per-unit rate |
| `co2_mass_tons` | observed CO₂ of the unit in that month, short tons | per-unit rate |

plus `state`, `year`, `orispl`, `unitid` as keys.

Two unit facts, neither of which is stated in a variable name and both of
which were recovered from the source's own arithmetic:

- **`co2_mass_tons` is in SHORT tons.** `2_historical_damages.R` multiplies it
  by `us_to_metric_ton <- lb_to_kg*2` before applying the social cost of
  carbon. The same factor 0.907184 is used here.
- **`grossload_mw` is in MWh, not MW.** `4_future_damages.R` forms
  `ch4_used = gen_total * ton_gas_mwh`, which requires energy, not power.

---

## 3. Exactly what was computed

For calendar year 2021, grouped by `state`:

```
gen_total_MWh         = sum(gen_total)
co2_total_short_tons  = sum(co2_total)
grossload_MWh         = sum(grossload_mw)
ef_kg_co2_per_kwh     = co2_total_short_tons / gen_total_MWh * 0.907184
coherence             = |sum(pmax(gen_total,0)) - sum(pmax(-gen_total,0))|
                        / (sum(pmax(gen_total,0)) + sum(pmax(-gen_total,0)))
unit_rate_min/max     = min/max over units of  sum(co2_mass_tons)/sum(grossload_mw)*0.907184,
                        for units generating >= 1000 MWh in 2021
```

### R that reproduces `drought_ef_2021.csv`

```r
library(dplyr)
d <- readRDS("Data/intermediate/unit_drought_emis_historical.rds")
TT <- 0.453592 * 2                      # us_to_metric_ton, as in the source scripts
y  <- filter(d, year == 2021)

rates <- y %>%
  group_by(state, orispl, unitid) %>%
  summarise(L = sum(grossload_mw), C = sum(co2_mass_tons), .groups = "drop") %>%
  filter(L >= 1000) %>%
  mutate(rate = C / L * TT)

bounds <- rates %>%
  group_by(state) %>%
  summarise(n_units = n(), n_plants = n_distinct(orispl),
            unit_rate_min = min(rate), unit_rate_max = max(rate), .groups = "drop")

agg <- y %>%
  group_by(state) %>%
  summarise(unit_months          = n(),
            gen_total_MWh        = sum(gen_total,     na.rm = TRUE),
            co2_total_short_tons = sum(co2_total,     na.rm = TRUE),
            grossload_MWh        = sum(grossload_mw,  na.rm = TRUE),
            pos = sum(pmax( gen_total, 0), na.rm = TRUE),
            neg = sum(pmax(-gen_total, 0), na.rm = TRUE), .groups = "drop") %>%
  mutate(coherence         = abs(pos - neg) / (pos + neg),
         ef_kg_co2_per_kwh = ifelse(gen_total_MWh > 0,
                                    co2_total_short_tons / gen_total_MWh * TT, NA))

left_join(agg, bounds, by = "state")
```

The Python that actually produced the shipped CSV lives inside the tool
itself, as `drought_ef.py --rebuild <path to the .rds>`; the R above is the
same computation, written for checking in the authors' own environment. The
rebuild path imports `pandas`/`pyreadr` only inside that branch, so the tool
still runs on a machine that has neither.

Running `python drought_ef.py --rebuild Data/intermediate/unit_drought_emis_historical.rds`
against the repository file reproduces the shipped `drought_ef_2021.csv`
byte for byte.

### The table it produces

```
state plants units unit-mo   gen_total_MWh   co2_short_tons  coherence  unit rates      EF
 AZ     25     86     949       1,522,879         717,304      0.465    0.363-1.084   0.4273
 CA    101    227    2461      13,177,407       5,898,460      0.998    0.327-1.343   0.4061
 CO     22     66     734       1,171,288         507,239      0.756    0.388-1.022   0.3929
 ID      5      8      89         599,812         270,955      1.000    0.365-0.648   0.4098
 MT      2      3      35         177,833         179,775      1.000    0.889-1.202   0.9171
 NM     12     24     265        -208,482        -257,466      0.269    0.366-1.076      --
 NV     12     35     390         937,273         624,377      1.000    0.357-1.042   0.6043
 OR      7     14     163       3,203,467       1,359,758      1.000    0.365-0.499   0.3851
 SD      1      1      12           8,416           4,622      1.000    0.498-0.498   0.4982
 TX      2     11     124         507,542         291,376      1.000    0.446-0.648   0.5208
 UT     10     27     292       3,992,035       2,539,628      1.000    0.374-0.989   0.5771
 WA     11     17     190       1,885,454         910,429      1.000    0.365-1.011   0.4381
 WY     10     21     243         857,323         841,806      0.861    0.512-1.119   0.8908
```

WECC total 2021: **0.4527 kg CO₂/kWh**, drought share of fossil generation
**8.16%**.

---

## 4. What is the authors' and what is ours

**Theirs.** `gen_total` and `co2_total` — the whole attribution chain behind
them: the runoff anomaly construction, the 54 BA×fuel regressions, the 500
bootstrap replicates, the median coefficients, the `(exp(β·a) − 1)` scaling.
`drought_generation_MWh` is a plain sum of their own output and is the closer
of the two returns to what the paper reports.

**Ours.** The division. **The paper does not report an emission factor** — it
reports drought-induced generation and drought-induced damages, never their
ratio. The division is dimensionally sound and uses nothing but their columns,
but it is a derived quantity and is labelled as one in `provenance`.

**Also ours, and it matters:** the *use* of that ratio as the intensity a new
drought-driven load would carry. Their object is the response of the existing
fleet to low runoff. Applying its intensity to a new load assumes the new load
is served in the same proportion as the fleet already responds. That is stated
in `conditions` as an assumption, not presented as their result.

Related, and worth the authors' attention: the paper's causal mediation
analysis **tested electricity demand as a channel and found no empirical
relationship**. That null was obtained over 2001–2021, when inland
desalination in the region was negligible, so it is a null for a channel that
did not then exist. It is not treated here as licence, and it is not treated
as a prohibition either; it is quoted in the conditions so that a reader meets
it.

---

## 5. Why 2021, and why a single year

Recomputing the intensity for every state-year shows two things.

**Wet years have no margin.** In 2006, 2011, 2016 and 2017 the attributed
generation is negative across essentially the whole region; there is no
drought-induced generation to characterise.

**Low-coherence state-years produce nonsense.** When positive and negative
unit responses nearly cancel, the ratio of two small residuals explodes:

```
NV 2003   coherence 0.011   ->  EF  13.740      NM 2017  coherence 0.367  ->  1.215
NM 2009             0.036   ->     -1.831       CO 2001            0.237  ->  0.018
NV 2012             0.047   ->      1.459       CO 2004            0.297  ->  0.009
```

**Pooling years makes it worse, not better,** because it mixes wet and dry
years whose responses have opposite sign. Pooling 2019–2021 drops Utah's
coherence from 1.000 to 0.383 and Montana's from 1.000 to 0.515.

2021 was a severe western drought year with a coherent response in almost
every state, so it is used, alone.

**The year is not interchangeable.** The fossil fleet turned over across the
study period, and the intensity fell with it:

```
        2001    2021    change
 AZ     0.686   0.427    -38%
 CA     0.539   0.406    -25%
 NV     0.787   0.604    -23%
 WA     0.764   0.438    -43%
 OR     0.664   0.385    -42%
```

A number from this tool describes the 2021 grid and no other.

---

## 6. The two guards, and why neither is a tuned threshold

Write the intensity out. Both increments carry the *same* bracket:

```
gen_total_u = grossload_u  * w_u
co2_total_u = co2_mass_u   * w_u          w_u = Σ_r (exp(β_r a_ru) − 1)
```

so at unit level the bracket cancels exactly, and

```
EF = Σ_u co2_mass_u · w_u  /  Σ_u grossload_u · w_u
```

**The intensity is a weighted mean of the units' own observed emission rates.
The regression only sets the weights; it never touches the rates.** Two
consequences, and both are the guards:

1. **If every `w_u` is positive, EF must lie between the state's cleanest and
   dirtiest unit.** So the test `unit_rate_min ≤ EF ≤ unit_rate_max` is a
   physical bound, not a threshold anyone chose. It catches every pathological
   state-year listed in §5 and passes every sound one.
2. **`w_u` can be negative** — a unit that generates *less* during drought. If
   negative weights dominate, the mean escapes the bound or the denominator
   collapses. `gen_total ≤ 0` is refused outright; `coherence` is reported
   alongside so the degree of cancellation is visible even when the bound
   passes (Arizona at 0.465 is the weakest state that is accepted).

A third, softer rule: states with fewer than three sampled plants are refused
(SD 1, MT 2, TX 2). One or two plants is an operator's emission rate, not a
grid margin.

**Texas is a real edge case, not an error.** Its two plants are ORISPL 3456
and 58562 at 31.98°N/−106.43°E and 31.82°N/−106.21°E — both in El Paso, which
is in WECC rather than ERCOT, and both are assigned to the source's SW region.
So "TX" in this table means El Paso Electric, not Texas. It is refused on the
plant count, and the refusal message says why, because silently returning an
El Paso number under the label "TX" would be the worse failure.

---

## 7. What this tool does not carry

1. **CH₄ is omitted by choice.** The repository has
   `Data/input/fuel_gas_consumption_2001_2021.rds` with plant-level
   `ton_gas_mwh`, and the source applies a 2.3% life-cycle leakage rate, so
   this channel is computable. It is left out because including it forces a
   20- vs 100-year GWP decision that would have to be defended separately.
2. **PM₂.₅ mortality cannot be computed.** `3_reg_air_quality.R` gives the
   monitor-level concentration response, but the step from concentration to
   deaths lives in `historical_pm25_mortality.rds`, and the repository README
   states plainly that *"the derivation process is not shown in this repo"*.
   This is a boundary of the published method, not an omission on our part.
3. Consequently **any total built on this tool is a lower bound**, and
   gas-heavy fleets understate by the most.
4. **No uncertainty interval.** The 500 bootstrap draws survive in
   `BA_fuel_reg_results.rds`, but `2_historical_damages.R` takes their median
   before applying them, so nothing downstream carries a distribution.
   Propagating it would mean re-running the attribution 500 times — feasible,
   not done.
5. **Fossil only.** CEMS covers no hydro, wind, solar or nuclear. The fleet
   quantities here are fossil quantities and must never be read as grid
   averages.
6. **Eleven of 681 units** carry pooled rather than BA-fuel coefficients
   because the BA-fuel estimates would have exceeded their total generation.
   The affected pairs are `nevada power company_RFO` and
   `puget sound energy_NG`, so Nevada and Washington are touched by that
   correction.
