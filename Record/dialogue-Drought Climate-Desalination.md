# Dialogue: Can you discuss drought, climate, and desalination? Find possible opportunities for collaboration and potential gaps. Make reasonable assumptions for in-depth discussion.

- Date: 9/9/2026, 5:24:21 PM
- Scientist 1: Scientist 1 (desalination) · qwen3.8-max
- Scientist 2: Scientist 2 (climate change) · qwen3.8-max
- Rounds completed: 18 (paused every 6)

---

### Scientist 1

My frame is brackish-water desalination cost, not drought hydrology. [GROUNDED] In my technoeconomic model, ED is cheaper than RO at ≤3 g/L NaCl, RO is cheaper at ≥5 g/L, with product 0.5 g/L, 80% recovery, and 10,000 m³/d. [EXTENDED] If drought pushes sources to higher TDS, technology choice shifts toward RO; this assumes NaCl-equivalent feed and unchanged pretreatment/brine costs, and stops if scaling, silica, or brine disposal dominate.

[ASSUMED][EXTENDED] For discussion, assume drought moves a basin’s usable feed from 3,000 to 5,000 ppm TDS; I invented those values, and they may not transfer because drought can change ion mix, not just salinity. Under that assumption, my SEC tool can compare kWh/m³ for RO and ED, and Scientist 2’s drought-generation emission factors can convert kWh to CO₂.

Gaps [GROUNDED]: my LCOW excludes pretreatment, brine handling, permitting, and reliability; the SEC figures are model lower bounds, and reported ED energy is often higher, especially at 2,000–5,000 ppm.

> ⚙ **R1** · Scientist 2 ran the tool: {"state":{"v":"CA","src":"assumed"}}

> ```
> {
>  "ef_kg_co2_per_kwh": 0.4061,
>  "drought_generation_MWh": 13177407
> }
> 
> (ran in 0.06s)
> ```

> ⚙ **R2** · Scientist 2 ran the tool: {"state":{"v":"AZ","src":"assumed"}}

> ```
> {
>  "ef_kg_co2_per_kwh": 0.4273,
>  "drought_generation_MWh": 1522879
> }
> 
> (ran in 0.06s)
> ```

### Scientist 2

Scientist 1, your kWh-to-CO₂ link is useful, but the margin matters. My work shows drought displaces hydro and makes fossil plants the marginal supply during shortages [GROUNDED]. For drought-induced fossil generation, I computed CA 0.406 kg CO₂/kWh [ASSUMED][COMPUTED from R1] and AZ 0.427 [ASSUMED][COMPUTED from R2]; I chose CA/AZ as illustrative states, and they may not transfer to a desalination basin because the EF is where emitting units sit, is 2021 Western Interconnection, combustion CO₂ only, lower bound, no uncertainty, and attribution—not new-load prediction. CA vs AZ changes EF by ~5%, so a planning placeholder of ~0.4 kg CO₂/kWh is robust across these choices [ASSUMED][COMPUTED from R1 and R2].

Send SEC kWh/m³ for RO/ED at 3,000 and 5,000 ppm; I’ll convert to CO₂/m³ and flag methane/PM₂.₅ caveats. My knowledge base offers no evidence on drought→TDS; that remains your assumption. Gap: applying EFs assumes desalination load is served by the same drought-called fossil margin; stops if dedicated renewables/storage serve it [EXTENDED]. Historical no-demand effect predates major desalination [GROUNDED].

> ⚙ **R3** · Scientist 1 ran the tool: {"feed_ppm":{"v":3000,"src":"source"},"technology":{"v":"RO","src":"source"}}

> ```
> {
>  "sec_kwh_per_m3": 0.5549
> }
> 
> (ran in 0.06s)
> ```

> ⚙ **R4** · Scientist 1 ran the tool: {"feed_ppm":{"v":3000,"src":"source"},"technology":{"v":"ED","src":"source"}}

> ```
> {
>  "sec_kwh_per_m3": 0.7618
> }
> 
> (ran in 0.06s)
> ```

> ⚙ **R5** · Scientist 1 ran the tool: {"feed_ppm":{"v":5000,"src":"source"},"technology":{"v":"RO","src":"source"}}

> ```
> {
>  "sec_kwh_per_m3": 0.7806
> }
> 
> (ran in 0.06s)
> ```

> ⚙ **R6** · Scientist 1 ran the tool: {"feed_ppm":{"v":5000,"src":"source"},"technology":{"v":"ED","src":"source"}}

> ```
> {
>  "sec_kwh_per_m3": 1.2508
> }
> 
> (ran in 0.06s)
> ```

### Scientist 1

Scientist 2, here are cost-optimal SECs — product water 0.5 g/L, 80% recovery, NaCl-equivalent feed — [COMPUTED from R3–R6]:

- 3,000 ppm: RO 0.555, ED 0.762 kWh/m³.  
- 5,000 ppm: RO 0.781, ED 1.251 kWh/m³.  

These are model lower bounds, not plant data; reported ED energy is 25–80% higher over 2,000–5,000 ppm [GROUNDED]. At 3,000 ppm RO has lower SEC, but ED still wins LCOW because RO’s high-pressure pump cost dominates [GROUNDED]. At 5,000 ppm RO wins LCOW [GROUNDED].

Using your ~0.4 kg CO₂/kWh placeholder [ASSUMED][COMPUTED from R1 and R2] — assumed because state choice and 2021 drought-marginal EF may not represent a desalination basin’s load — gives roughly 0.22 RO vs 0.30 ED kg CO₂/m³ at 3,000 ppm, and 0.31 vs 0.50 at 5,000 ppm [ASSUMED][EXTENDED].

The climate link remains conditional on drought actually raising TDS and on desalination load being served by the drought-called fossil margin. My gap: no drought→TDS evidence, and my model cannot test ion composition.

> ⚙ **R7** · Scientist 2 ran the tool: {"state":{"v":"NM","src":"assumed"}}

> ```
> THE TOOL FAILED: the script exited with code 1
> 
> stderr:
> NM had NEGATIVE drought-induced fossil generation in 2021 (-208482 MWh, response coherence 0.27): across its units the runoff response cancelled out rather than adding up. There is no drought margin to report. This is a property of that state-year, not a missing number.
> 
> Check the parameter names and units on your tool card. You may try once more, or carry on without the number and say that the calculation did not run.
> ```

### Scientist 2

Scientist 1, those conversions are the right first-order coupling. Using your SECs [COMPUTED from R3–R6] and my ~0.4 kg CO₂/kWh placeholder [ASSUMED][COMPUTED from R1 and R2], I get ~0.22/0.31 kg CO₂/m³ for RO and 0.30/0.50 for ED at 3,000/5,000 ppm [ASSUMED][EXTENDED]; assumption: new desalination load is served by the same drought-called fossil margin, and it stops if dedicated renewables/storage or a non-fossil margin serves it. CA vs AZ changes the placeholder by ~5% [ASSUMED][COMPUTED from R1 and R2].

I tried NM as a sensitivity [ASSUMED][COMPUTED from R7]: state=NM, chosen by me; it returned no EF because drought-attributed generation was negative (−208,482 MWh), so the margin does not transfer there. This shows the drought margin is spatially uneven.

My historical no-demand result predates major desalination, so it is not evidence against this load [GROUNDED]. Collaboration: pair your TDS scenarios with my balancing-authority generation response, but we need a marginal-load experiment, not fleet attribution. Gaps: drought→TDS, ion mix, and CO₂-only/methane/PM₂.₅ lower bounds.

### Scientist 1

Scientist 2, agreed: your NM result shows we should not apply a single drought EF to a desalination basin without locating both load and margin [EXTENDED]. Assumption: the basin’s desalination load is served by the same drought-displaced fossil margin; it stops if dedicated renewables/storage or imports set the margin.

I can supply TDS scenarios, not drought hydrology. [GROUNDED] My model covers fixed cases at 1,000–10,000 ppm; values between are interpolation. [GROUNDED] LCOW crossover is 3–5 g/L: ED cheaper ≤3,000 ppm, RO cheaper ≥5,000 ppm. [ASSUMED][EXTENDED] If drought shifts feed from 3,000 to 5,000 ppm—a scenario I invented, and it may not transfer if ion mix or scaling changes—RO’s SEC advantage widens from 0.207 to 0.470 kWh/m³ [COMPUTED from R3–R6].

Collaboration: I provide feed TDS, product spec, recovery, SEC/LCOW; you provide balancing-authority marginal EFs and test whether desalination load is incremental. Needed experiment: baseline vs drought TDS × grid mix vs drought-fossil margin. My gaps: drought→TDS, ion mix, brine. Your gaps: CO₂-only lower bound.

### Scientist 2

Scientist 1, agreed. A coupled test should be: your TDS/recovery cases → SEC kWh/m³ → my state drought-fossil EF → kg CO₂/m³, with balancing-authority/fuel generation checks, then compare against grid-average and dedicated-clean cases [EXTENDED]. Assumption: desalination load is served by the drought-called fossil margin; it stops if renewables, storage, or imports set the margin.

My side can provide state EFs and drought-attributed generation where positive, but the EF is an attribution for 2021 western drought, combustion CO₂ only, no uncertainty, and not a prediction for new load [GROUNDED]. My historical demand null predates large desalination, so it cannot reject an incremental-load effect [GROUNDED].

The CO₂-only figure is a lower bound: historical drought-induced fossil generation produced $20B damages 2001–21, including CO₂, PM₂.₅ mortality, and methane leakage; the 2012–16 California drought caused $5.1B [GROUNDED]. So siting desalination where drought calls up fossil generation may add health/climate damages beyond electricity cost [EXTENDED].

Collaboration: choose basins/balancing authorities, define TDS scenarios, and test the marginal source. Gaps: drought→TDS/ion mix, brine, and local PM₂.₅.

### Scientist 1

Scientist 2, Moderator: I accept the coupled test as conditional, not settled. I can supply the desalination side: [GROUNDED] fixed NaCl-equivalent cases 1,000–10,000 ppm, 500 ppm product, 80% recovery, 10,000 m³/d; ED cheaper ≤3 g/L, RO cheaper ≥5 g/L. [COMPUTED from R3–R6] SECs: 3,000 ppm RO 0.555 / ED 0.762; 5,000 ppm RO 0.781 / ED 1.251 kWh/m³. [GROUNDED] These are model lower bounds; reported ED energy is 25–80% higher over 2,000–5,000 ppm.

[ASSUMED][EXTENDED] A drought-driven TDS shift from 3,000 to 5,000 ppm is my invented scenario; it stops if ion mix, scaling, or brine dominate. [ASSUMED][EXTENDED] With your 0.4 kg CO₂/kWh placeholder from R1/R2, emissions are ~0.22/0.31 RO and ~0.30/0.50 ED kg/m³; assumed because basin/margin may not transfer.

[GROUNDED] My LCOW excludes environmental damages, so your damage-cost point matters but is outside my boundary; I cannot validate it. Next: choose basin; I provide TDS/recovery cases, you provide marginal, grid-average, and clean-power counterfactuals.

> ⚙ **R8** · Scientist 2 ran the tool: {"state":{"v":"NM","src":"assumed"}}

> ```
> THE TOOL FAILED: the script exited with code 1
> 
> stderr:
> NM had NEGATIVE drought-induced fossil generation in 2021 (-208482 MWh, response coherence 0.27): across its units the runoff response cancelled out rather than adding up. There is no drought margin to report. This is a property of that state-year, not a missing number.
> 
> Check the parameter names and units on your tool card. You may try once more, or carry on without the number and say that the calculation did not run.
> ```

> ⚙ **R9** · Scientist 2 ran the tool: {"state":{"v":"NV","src":"assumed"}}

> ```
> {
>  "ef_kg_co2_per_kwh": 0.6043,
>  "drought_generation_MWh": 937273
> }
> 
> (ran in 0.05s)
> ```

### Scientist 2

Scientist 1, Moderator: I can provide drought-marginal EFs; grid-average/clean counterfactuals require extra assumptions [EXTENDED]. [ASSUMED][EXTENDED] Assumption: desalination load is served by drought-called fossil margin; it stops if dedicated renewables/storage/imports set the margin.

NM sensitivity failed: negative 2021 drought-attributed generation (−208,482 MWh), so no drought margin [ASSUMED][COMPUTED from R8]; I chose NM, and it may not transfer because emitting-unit location ≠ load location. NV alternative gives EF 0.604 kg CO₂/kWh and 937,273 MWh [ASSUMED][COMPUTED from R9]; I chose NV, 2021-only, combustion CO₂-only, attribution not new load.

With your SECs [COMPUTED from R3–R6], NV gives RO 0.34/0.47 and ED 0.46/0.76 kg CO₂/m³ at 3,000/5,000 ppm [ASSUMED][EXTENDED]. This is ~50% above the 0.4 placeholder, so basin/balancing-authority selection dominates.

Next [EXTENDED]: choose states/BAs with positive drought generation; I test the drought-marginal case, you supply TDS/SEC. Grid-average/clean cases remain assumptions. Gaps: drought→TDS/ion mix, brine, and methane/PM₂.₅ damages outside the CO₂-only lower bound [GROUNDED].

### Scientist 1

Scientist 2, Moderator: I accept the coupled test as conditional, not settled. My model is generic: NaCl-equivalent feed, 0.5 g/L product, 80% recovery, 10,000 m³/d [GROUNDED]. LCOW crossover: ED ≤3 g/L, RO ≥5 g/L [GROUNDED]. SECs: 3k ppm RO 0.555/ED 0.762; 5k ppm RO 0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm [GROUNDED].

[ASSUMED][EXTENDED] Drought shifting feed from 3k to 5k ppm is my invented scenario; it stops if ion mix, scaling, or brine dominate. Using NV EF 0.604 kg/kWh [ASSUMED][COMPUTED from R9], emissions are RO 0.34/0.47 and ED 0.46/0.76 kg/m³; assumed because EF is attribution and basin margin may differ. At 5k ppm RO wins cost and fossil-margin CO₂; at 3k ED wins LCOW but emits more under fossil margin [ASSUMED][EXTENDED].

Next: Scientist 2, list states/BAs with positive drought generation; I’ll match them to my 1–10k ppm cases. My knowledge base offers no evidence on drought→TDS, ion mix, brine, or damages.

### Scientist 2

Scientist 1, Moderator: from computed tests, positive drought-attributed fossil generation is currently:

- CA: 13,177,407 MWh, EF 0.406 kg CO₂/kWh [ASSUMED][COMPUTED from R1]  
- AZ: 1,522,879 MWh, EF 0.427 [ASSUMED][COMPUTED from R2]  
- NV: 937,273 MWh, EF 0.604 [ASSUMED][COMPUTED from R9]  

State choices were my assumed illustrative selections; they may not transfer because the EF locates emitting units, is 2021-only, combustion-CO₂-only, and is attribution, not new-load prediction [GROUNDED]. I cannot yet list BAs; my instrument is state-level, though the underlying study estimates balancing-authority × fuel effects [GROUNDED].

Candidate basins: CA/AZ/NV [ASSUMED][EXTENDED]. Assumption: desalination load is served by the drought-called fossil margin; it stops if dedicated renewables, storage, or imports set the margin.

Next: Scientist 1, map your 1–10k ppm cases to CA/AZ/NV; I’ll provide EF sensitivity and identify negative-margin states. Grid-average and clean-power counterfactuals remain explicit assumptions [EXTENDED]. Gaps: drought→TDS/ion mix, brine, and methane/PM₂.₅ damages beyond CO₂ [GROUNDED].

### Scientist 1

Moderator: I cannot map CA/AZ/NV to actual basin TDS; my knowledge base offers no evidence on state-specific TDS. [GROUNDED] My cases are generic fixed feeds: 1, 3, 5, 7, 10k ppm, 0.5 g/L product, 80% recovery. CA/AZ/NV therefore enter only as EF multipliers, not desalination physics.

Screening map: for any candidate basin, if TDS ≤3k ppm ED wins LCOW; if ≥5k RO wins [GROUNDED]. SECs: 3k RO 0.555 / ED 0.762; 5k RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm [GROUNDED]. With CA/AZ/NV EFs [ASSUMED][COMPUTED from R1,R2,R9], CO₂/m³ at 3k is RO 0.225/0.237/0.335, ED 0.309/0.325/0.460; at 5k RO 0.317/0.333/0.471, ED 0.508/0.534/0.756 [ASSUMED][EXTENDED]. Assumptions: EFs apply to new load, NaCl feed, no brine/ion mix; stops if renewables/storage/imports set margin or local TDS differs.

Next: Scientist 2, flag negative-margin states; I can supply 1/7/10k SECs to complete the matrix.

> ⚙ **R10** · Scientist 2 ran the tool: {"state":{"v":"NM","src":"assumed"}}

> ```
> THE TOOL FAILED: the script exited with code 1
> 
> stderr:
> NM had NEGATIVE drought-induced fossil generation in 2021 (-208482 MWh, response coherence 0.27): across its units the runoff response cancelled out rather than adding up. There is no drought margin to report. This is a property of that state-year, not a missing number.
> 
> Check the parameter names and units on your tool card. You may try once more, or carry on without the number and say that the calculation did not run.
> ```

> ⚙ **R11** · Scientist 2 ran the tool: {"state":{"v":"OR","src":"assumed"}}

> ```
> {
>  "ef_kg_co2_per_kwh": 0.3851,
>  "drought_generation_MWh": 3203467
> }
> 
> (ran in 0.06s)
> ```

### Scientist 2

Scientist 1, Moderator: tested subset, not full map. Positive 2021 margins: CA 13.18M MWh, EF 0.406 [ASSUMED][COMPUTED from R1]; AZ 1.52M, 0.427 [ASSUMED][COMPUTED from R2]; NV 0.94M, 0.604 [ASSUMED][COMPUTED from R9]; OR 3.20M, 0.385 [ASSUMED][COMPUTED from R11]—I chose OR; may not transfer: 2021 state attribution at emitting units, combustion CO₂ only, not new load. Negative: NM no EF; −208,482 MWh [ASSUMED][COMPUTED from R10]—I chose NM; cancellation means no margin.

State choice moves result: EF 0.385–0.604 (~57% spread), so basin/BA selection dominates. With OR EF and your SECs [R3–R6]: 3k ppm RO/ED ≈0.21/0.29 kg CO₂/m³; 5k ≈0.30/0.48 [ASSUMED][EXTENDED]; assumption: new load served by drought-called fossil margin; stops if renewables/storage/imports set margin.

Next: Moderator, choose basins/BAs. My study estimates BA×fuel effects, but my instrument is state-level [GROUNDED]. Grid-average/clean counterfactuals remain assumptions [EXTENDED]. Gaps: drought→TDS/ion mix, brine, methane/PM₂.₅ lower bound [GROUNDED].

### MODERATOR

You have both listed what is missing for research. Which one would you do first, how, and what result would settle it? You can discuss the research plan, and assume values or scenarios where you need them to continue the discussion.

### Scientist 1

Moderator: I would do first: basin-specific drought→TDS/ion-composition mapping, because my technology choice is feed-salinity-driven. [GROUNDED] My model uses NaCl-equivalent feed, 0.5 g/L product, 80% recovery; LCOW crossover is 3–5 g/L, ED cheaper ≤3, RO cheaper ≥5. [GROUNDED] It cannot test ion mix, though ED energy depends on which ions are moved.

Method: choose one positive-margin state, e.g. CA or AZ [ASSUMED][COMPUTED from R1/R2]—state choices are illustrative and may not transfer—compile monthly groundwater TDS/major ions and drought index, fit TDS response, then rerun SEC/LCOW. [ASSUMED][EXTENDED] Working scenario: drought shifts feed across 3,000 or 5,000 ppm; invented, and it stops if scaling, brine, or ion mix dominate.

Settling result: a robust drought-season TDS/ion shift crossing the 3–5 g/L LCOW crossover or invalidating the NaCl-equivalent assumption. If no crossing occurs, the cost/climate link remains weak [EXTENDED]. Scientist 2’s marginal-BA EF and grid/clean counterfactuals come second.

### Scientist 2

Scientist 1, Moderator: I would do the marginal-load test first, because TDS mapping only matters climatically if desalination load is incremental and served by drought-called fossil plants. [EXTENDED] Plan: pick a CA/AZ balancing authority [ASSUMED]—illustrative, may not transfer—use your 10,000 m³/d plant and 5,000 ppm RO SEC 0.781 kWh/m³ [COMPUTED from R5], add a 7.8 MWh/d (2.85 GWh/yr) load shock [ASSUMED], and compare dispatch against 2021 drought-attributed generation and EFs: CA 0.406 [COMPUTED from R1], AZ 0.427 [COMPUTED from R2], plus grid-average/clean counterfactuals.

Settling result: positive incremental fossil generation with an EF inside the observed state range validates the coupling; zero/negative response, or a clean/storage/import margin, kills it. Scale check: 2.85 GWh/yr is ~0.02% of CA’s 13.18 TWh 2021 drought generation [ASSUMED][EXTENDED]; one plant is negligible, so a basin portfolio is needed.

My study has BA×fuel estimates, but my instrument is state-level [GROUNDED]. TDS/ion mapping should follow; if marginal-load proof fails, the crossover is economically relevant but climate-irrelevant. CO₂-only remains a lower bound [GROUNDED].

### Scientist 1

Scientist 2, Moderator: I accept the marginal-load test as the first climate gate. If new desalination load is not served by drought-called fossil generation, my LCOW crossover has no drought-margin CO₂ consequence.

Stage 1, Scientist 2 leads: test a 10,000 m³/d load shock. At 5,000 ppm RO, SEC is 0.781 kWh/m³ [COMPUTED from R5], giving 7.81 MWh/d or 2.85 GWh/yr [COMPUTED from R5]. Settling result: positive incremental fossil generation with EF inside the observed 0.385–0.604 kg CO₂/kWh range [ASSUMED][COMPUTED from R1,R2,R9,R11]; CA/AZ/NV/OR state choices are illustrative and may not transfer because EFs are 2021 state-level attribution at emitting units, not new-load prediction. Zero/negative response or clean/storage/import margin kills the coupling.

Stage 2, I lead: basin TDS/ion mapping. Settling result: drought shifts feed across the 3–5 g/L LCOW crossover or invalidates NaCl equivalence [GROUNDED]. If Stage 1 fails, stop; if Stage 2 shows no shift, technology choice is economically but not climate-differentially affected.

### Scientist 2

Moderator: I would do the marginal-load proof first. My `drought_ef` instrument gives 2021 drought-attributed fossil EFs, not a dispatch model for a new load [GROUNDED].

Test: put Scientist 1’s assumed 10,000 m³/d, 5,000-ppm RO load—7.8 MWh/d, 2.85 GWh/yr using R5 SEC [ASSUMED][EXTENDED]—into a California/Arizona balancing authority [ASSUMED]. Compare incremental fossil EF with observed drought-marginal EFs: 0.385–0.604 kg CO₂/kWh across OR/AZ/CA/NV [COMPUTED from R1,R2,R9,R11]. Assumption: the load is served by drought-called fossil generation; stops if renewables, storage, or imports set the margin.

Settling result: positive incremental fossil generation with EF in that range validates the climate gate; zero/negative or clean margin kills it. If it fails, Scientist 1’s TDS work remains important for water cost but not drought-climate coupling. If it passes, Stage 2 TDS/ion mapping sets technology and SEC magnitude.

Single-plant scale is ~0.02% of CA’s 13.18 TWh 2021 drought generation [ASSUMED][EXTENDED]; use a portfolio. CO₂-only is a lower bound [GROUNDED].

### Scientist 1

Moderator: I would implement Stage 1 first, but as a portfolio screen rather than one plant. [ASSUMED][EXTENDED] Assume ten 10,000 m³/d plants at 5,000 ppm RO; I invented this portfolio scale, and it may not transfer to real basin permitting or siting. Load is 28.5 GWh/yr, from 0.781 kWh/m³ [COMPUTED from R5].

Scientist 2 can test whether incremental fossil EF falls inside 0.385–0.604 kg CO₂/kWh and whether drought-attributed generation is positive [ASSUMED][COMPUTED from R1,R2,R9,R11]; state choices are illustrative. I supply salinity-specific SEC/LCOW: ED wins ≤3,000 ppm, RO wins ≥5,000 ppm [GROUNDED]; 3k/5k SECs [COMPUTED from R3–R6].

I cannot provide BA dispatch. Without BA-level marginal data, Stage 1 remains an attribution screen, not proof [EXTENDED]. Settling result: positive fossil response with EF in range and enough drought generation to cover the portfolio; otherwise climate coupling fails. If it passes, Stage 2 is drought→TDS/ion mapping; it settles if feed crosses the 3–5 g/L LCOW crossover or invalidates NaCl equivalence [GROUNDED].

> ⚙ **R12** · Scientist 2 ran the tool: {"state":{"v":"NM","src":"assumed"}}

> ```
> THE TOOL FAILED: the script exited with code 1
> 
> stderr:
> NM had NEGATIVE drought-induced fossil generation in 2021 (-208482 MWh, response coherence 0.27): across its units the runoff response cancelled out rather than adding up. There is no drought margin to report. This is a property of that state-year, not a missing number.
> 
> Check the parameter names and units on your tool card. You may try once more, or carry on without the number and say that the calculation did not run.
> ```

> ⚙ **R13** · Scientist 2 ran the tool: {"state":{"v":"CO","src":"assumed"}}

> ```
> {
>  "ef_kg_co2_per_kwh": 0.3929,
>  "drought_generation_MWh": 1171288
> }
> 
> (ran in 0.06s)
> ```

### Scientist 2

Scientist 1, Moderator: I accept the portfolio screen. NM returned no EF because 2021 drought-attributed generation was negative (−208,482 MWh) [ASSUMED][COMPUTED from R12]; I chose NM, a sensitivity that may not transfer because it is state-level attribution at emitting units, not basin/load dispatch. CO gives EF 0.393 kg CO₂/kWh and 1.17M MWh [ASSUMED][COMPUTED from R13]; I chose CO, with same 2021, combustion-only, attribution-not-new-load caveats. Conclusion unchanged: positive margins exist, EFs stay 0.385–0.604 across OR/CA/AZ/CO/NV [COMPUTED from R1,R2,R9,R11,R13], but some states fail.

Use the ten-plant portfolio, 28.5 GWh/yr [ASSUMED][EXTENDED]; it is small vs positive-state drought generation—~0.2% of CA, ~2.4% of CO [ASSUMED][EXTENDED]. Settling result: BA-level incremental fossil response positive with EF in range; clean/storage/import margin or negative response kills coupling. My study estimates BA×fuel responses, but current tool is state-level [GROUNDED]. Moderator: choose 2–3 positive BAs; we need BA hourly fuel generation plus AMPD emissions to upgrade this from attribution screen to dispatch test.

### Scientist 1

Moderator: I support selecting BAs from Scientist 2’s positive-margin list, but my knowledge base offers no evidence on basin salinity or dispatch, so I cannot name BAs from my side [GROUNDED]. Choose BAs where both positive drought generation and TDS records exist.

I can supply water-side cases: fixed 1–10 g/L NaCl, 0.5 g/L product, 80% recovery; LCOW crossover ED ≤3 g/L, RO ≥5 g/L [GROUNDED]. SECs at 3/5k ppm are on the table [COMPUTED from R3–R6]; I can add 7/10k if drought scenarios require them.

For Stage 1, define the ten-plant portfolio as constant load: 100,000 m³/d × 0.781 kWh/m³ = 78.1 MWh/d = 28.5 GWh/yr ≈ 3.25 MW average [ASSUMED][EXTENDED]; ten plants and constant operation are my assumptions, and may not transfer to real cycling or permitting. Settling result: BA-level incremental fossil response positive, EF within 0.385–0.604 kg/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; clean/storage/import margin kills it. If it passes, Stage 2 settles if drought TDS/ion shift crosses 3–5 g/L or breaks NaCl equivalence [GROUNDED].

> 🔍 Scientist 2 looked up: balancing authority / California ISO Southwest Northwest

### Scientist 2

Scientist 1, Moderator: I agree Stage 1 first, but as a screen, not proof [EXTENDED]. My study estimates balancing-authority × fuel drought responses, but my callable EF is state-level, 2021, combustion-CO₂-only, attribution—not dispatch [GROUNDED].

Choose BAs inside positive states; I propose CA and AZ [ASSUMED][COMPUTED from R1,R2]. I chose them because CA/AZ have positive EFs and CA has the largest drought-attributed generation; they may not transfer to actual basin TDS or BA boundaries.

Data plan: combine my monthly AMPD plant generation/emissions with external hourly BA fuel-generation data—outside my knowledge base—and regress incremental fossil output against runoff anomalies and the 28.5 GWh/yr portfolio load [ASSUMED][EXTENDED]. Counterfactuals: grid-average, high-renewables/storage, and import margins [EXTENDED].

Settling result: positive incremental fossil generation with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; clean/storage/import margin or negative response kills the coupling. NM’s negative margin shows selection matters [ASSUMED][COMPUTED from R12]. If Stage 1 fails, Stage 2 remains water-cost relevant but not climate-coupled.

### Scientist 1

Moderator: first, Scientist 2’s marginal-load screen, because without incremental fossil dispatch my LCOW crossover has no drought-climate consequence [EXTENDED]. Assumption: desalination load is incremental; stops if it is not.

I cannot choose BAs from my knowledge base; it has no basin TDS or dispatch evidence [GROUNDED]. If a choice is required now, use CA and AZ only as Scientist 2’s assumed positive-margin candidates [ASSUMED][COMPUTED from R1,R2]; they may not transfer to actual basins.

Water-side input: ten-plant portfolio, 100,000 m³/d at 5,000 ppm RO, 28.5 GWh/yr ≈3.25 MW average, using 0.781 kWh/m³ [ASSUMED][EXTENDED]; ten plants and constant load are invented and may not transfer. SECs: 3k RO 0.555/ED 0.762; 5k RO 0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds [GROUNDED].

My method cannot supply hourly BA generation or AMPD [GROUNDED]. Settling result: BA-level positive fossil response with EF inside 0.385–0.604 kg/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; otherwise Stage 2 remains water-cost only. Stage 2 settles if drought TDS/ion shift crosses the 3–5 g/L LCOW crossover or breaks NaCl equivalence [GROUNDED].

### Scientist 2

Moderator: I would run Stage 1 first, as a screen then a dispatch upgrade. [EXTENDED] Assumption: desalination load is incremental and served by drought-called fossil margin; stops if storage/renewables/imports set margin.

Use CA and AZ as candidate BAs [ASSUMED][COMPUTED from R1,R2]; I chose them because positive 2021 drought generation and EFs 0.406/0.427 kg CO₂/kWh; may not transfer to actual basins. Compare the ten-plant 28.5 GWh/yr load [ASSUMED][EXTENDED] with state drought generation: 13.18 TWh CA, 1.52 TWh AZ [ASSUMED][COMPUTED from R1,R2]; capacity is not proof of marginal dispatch.

Upgrade: combine my monthly AMPD plant generation/emissions and BA×fuel runoff responses [GROUNDED] with hourly BA fuel-generation/trade data—needed but outside my instrument—to estimate incremental fossil MWh from the load shock [EXTENDED]. Counterfactuals: grid-average, high renewables/storage, imports [ASSUMED][EXTENDED].

Settling result: positive incremental fossil generation with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]. If clean/storage/import margin or negative response, climate coupling fails; Stage 2 remains water-cost only. CO₂-only is lower bound [GROUNDED].

### Scientist 1

Moderator: I agree Stage 1 comes first, but only as an attribution screen until dispatch data exist. My knowledge base offers no basin TDS, BA boundaries, or hourly generation evidence [GROUNDED].

For the chosen BAs, I supply the water-side load and technology cases. Candidate portfolio: ten 10,000 m³/d RO plants at 5,000 ppm, 100,000 m³/d, 28.5 GWh/yr ≈3.25 MW average, using 0.781 kWh/m³ [ASSUMED][EXTENDED] — invented portfolio size and constant load; may not transfer to real cycling, permitting, or siting.

Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L; SECs at 3k/5k ppm from R3–R6 [GROUNDED][COMPUTED from R3–R6].

Settling Stage 1: BA-level incremental fossil generation positive, with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; zero/negative response or clean/storage/import margin kills the climate coupling. If hourly BA fuel-generation/trade and AMPD data cannot be obtained, we should report only that state EFs bracket possible emissions, not that desalination causes fossil dispatch.

Stage 2, if Stage 1 passes: drought→TDS/ion mapping; it settles if feed crosses the 3–5 g/L LCOW crossover or invalidates NaCl equivalence [GROUNDED].

> 🔍 Scientist 2 looked up: balancing authority fuel type / California Arizona Southwest balancing authority / hourly generation trade data

### Scientist 2

Moderator: first, run Stage 1 as a BA-level attribution screen, then upgrade to dispatch. My study estimates 54 BA×fuel drought responses from monthly EPA AMPD generation/emissions and runoff anomalies [GROUNDED]. Use California/Arizona placeholder BAs [ASSUMED][COMPUTED from R1,R2]; may not transfer. Apply Scientist 1’s 28.5 GWh/yr portfolio [ASSUMED][EXTENDED]; compare with EF bracket 0.385–0.604 kg CO₂/kWh [COMPUTED from R1,R2,R9,R11,R13]. Because 63% of California’s drought-generation increase is transboundary [GROUNDED], include neighboring BAs/imports.

Upgrade [EXTENDED] needs hourly BA fuel-generation/trade matched to AMPD; my tool is state-level attribution, not dispatch [GROUNDED]. Counterfactuals—grid-average, storage/renewables, imports—are assumed scenarios [ASSUMED][EXTENDED]. If hourly data cannot be obtained, report only bracket, not causal dispatch [EXTENDED].

Settling criterion [EXTENDED]: positive incremental fossil generation with EF inside bracket; zero/negative or clean/storage/import margin kills coupling. Fossil remains marginal 71% of CA hours in 2050 despite 8.6% generation [GROUNDED]; CO₂-only lower bound [GROUNDED].

### MODERATOR

Can you two converge to a research plan, aiming for good impact? Please also explain the research to people knowing nothing about your previous studies. Focus on big picture and outline this time.

### Scientist 1

Moderator: yes. Plain-language plan: the hypothesis is drought may raise feed salinity [EXTENDED]; stops if dilution/operations dominate. Desalination uses electricity [GROUNDED]; if new load is served by drought-called fossil margin, it can add emissions [ASSUMED][EXTENDED]; stops if clean/storage/imports serve it. We test two stages.

Stage 1 (Scientist 2 leads): does desalination load cause extra fossil generation? Placeholder portfolio: ten 10,000 m³/d RO plants, 28.5 GWh/yr ≈3.25 MW [ASSUMED][EXTENDED]; invented scale/constant load, may not transfer. Pass: positive fossil response, EF inside 0.385–0.604 kg/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; fail: clean/storage/import margin.

Stage 2 (I lead): does drought shift feed salinity/ions enough to change cheapest technology? ED cheaper ≤3 g/L, RO ≥5 g/L [GROUNDED]. Pass if feed crosses 3–5 g/L or breaks NaCl equivalence [GROUNDED]. Without BA dispatch, report bracket only, assuming state EFs bound BA EFs; stops if BA EF outside [EXTENDED]. Impact: find basins needing clean power or different technology. My LCOW excludes brine/damages [GROUNDED].

### Scientist 2

Moderator: plain-language plan: drought reduces hydropower, so fossil plants often fill the gap [GROUNDED]. Desalination needs electricity; if that electricity comes from drought-called fossil plants, it can add emissions [EXTENDED]. Assumption: load is incremental and served by the drought margin; stops if clean power, storage, or imports serve it.

Converged plan: Stage 1, attribution screen then dispatch test. State EFs cannot prove dispatch [GROUNDED]. Choose CA/AZ placeholder BAs—CAISO/Arizona BA if names needed [ASSUMED][COMPUTED from R1,R2]; include imports because much CA effect is transboundary [GROUNDED]. Apply the 28.5 GWh/yr portfolio [ASSUMED][EXTENDED]. Pass: positive fossil response with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]. Without hourly BA generation/trade plus AMPD, report bracket only [EXTENDED]. Stage 2: drought→TDS/ion mapping; pass if feed crosses 3–5 g/L or breaks NaCl equivalence [GROUNDED].

Data: my monthly AMPD/runoff/trade framework; external hourly BA generation/interchange and counterfactuals needed [ASSUMED]. Impact: identify basins where desalination is climate-safe and where it needs dedicated clean power.

### Scientist 1

Moderator: I confirm the converged plan. Big picture: drought may raise source salinity, and desalination may add electricity demand; the climate consequence exists only if that demand is met by drought-called fossil generation. The drought→salinity premise is an assumed working scenario; it stops if dilution, operations, or ion mix dominate [ASSUMED][EXTENDED].

My contribution is the water-cost/technology side: fixed NaCl cases, 0.5 g/L product, 80% recovery; ED cheaper ≤3 g/L, RO cheaper ≥5 g/L [GROUNDED]. SECs at 3k/5k ppm are on the table [COMPUTED from R3–R6]; they are model lower bounds [GROUNDED]. The ten-plant portfolio is an assumed screening case: 100,000 m³/d, 28.5 GWh/yr, ~3.25 MW; invented and may not transfer [ASSUMED][EXTENDED].

I accept CA/AZ only as placeholders. Without BA-level dispatch and import accounting, we should report an emissions bracket, not causal fossil dispatch [EXTENDED]. Stage 2 settles if drought TDS/ion shift crosses the 3–5 g/L LCOW crossover or breaks NaCl equivalence [GROUNDED]. Needed external data: hourly BA generation/trade, AMPD emissions, and clean/storage/import counterfactuals.

### Scientist 2

Moderator: I confirm. Big picture: drought cuts hydropower and fossil plants often fill the gap [GROUNDED]. Desalination uses electricity; if its new load is served by that drought-called fossil margin, it can add CO₂ and air-quality damages [EXTENDED]. Assumption: load is incremental and not served by dedicated clean/storage/imports; stops otherwise.

Stage 1: I choose CA/AZ balancing authorities, with NV optional, as placeholders from positive state EFs R1/R2/R9; they may not transfer to actual basins/dispatch [ASSUMED]. Apply Scientist 1’s assumed 28.5 GWh/yr portfolio; invented ten-plant constant load may not transfer [ASSUMED][EXTENDED]. Use my monthly AMPD/runoff BA×fuel attribution [GROUNDED]; upgrade with external hourly BA generation/trade and counterfactuals [EXTENDED]. Until then report only bracket 0.385–0.604 kg CO₂/kWh, not causal dispatch [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]. Pass: positive fossil response with EF in bracket; fail: clean/storage/import margin. Include imports because much CA effect is transboundary [GROUNDED]. CO₂-only is lower bound [GROUNDED].

### Scientist 1

Moderator: I confirm. Scientist 2, I accept the bracket-only framing.

My deliverables:  
1. Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L under fixed NaCl feed, 0.5 g/L product, 80% recovery [GROUNDED].  
2. SEC inputs: 3k ppm RO 0.555 / ED 0.762; 5k ppm RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; these are cost-optimal model outputs, not plant measurements [GROUNDED].  
3. Stage-2 pass/fail: drought TDS/ion shift must cross the 3–5 g/L LCOW crossover or invalidate NaCl equivalence [GROUNDED].

My knowledge base offers no evidence on basin TDS, BA dispatch, brine, or damages [GROUNDED]. The ten-plant portfolio—100,000 m³/d, 28.5 GWh/yr, ~3.25 MW—is an assumed screening construct; invented scale/constant load, may not transfer [ASSUMED][EXTENDED]. CA/AZ remain placeholders only [ASSUMED].

Next: Moderator, confirm placeholder BAs and the path to hourly BA generation/trade, AMPD emissions, and counterfactuals. Until then, report an emissions bracket, not causal dispatch [EXTENDED].

### Scientist 2

Moderator: I confirm. Plain language: drought reduces hydropower, so fossil plants may run more; if new desalination electricity is served by that fossil margin, it adds emissions.

Stage 1: use California and Arizona placeholder BAs [ASSUMED][COMPUTED from R1,R2]; I chose them from positive 2021 state EFs, and they may not transfer to actual basins or dispatch. Apply the 28.5 GWh/yr portfolio [ASSUMED][EXTENDED]—invented ten-plant constant load, may not transfer. Report only the bracket 0.385–0.604 kg CO₂/kWh, not causal dispatch; assumption is state EFs bound BA EFs, stops if BA EF lies outside [ASSUMED][COMPUTED from R1,R2,R9,R11,R13].

My side supplies monthly AMPD plant generation/emissions and the BA×fuel drought-response framework [GROUNDED]; my tool is state-level attribution, not hourly dispatch [GROUNDED]. Needed: external hourly BA generation/interchange and counterfactuals; my knowledge base cannot supply them. Include imports because California effects are transboundary [GROUNDED]. Pass: positive incremental fossil response within bracket [EXTENDED]; fail: clean/storage/import margin. Impact: identify basins where desalination needs dedicated clean firm power rather than drought-called fossil generation.

### Scientist 1

Moderator: I confirm the summary and accept Stage 2 leadership, with an honest limit: my knowledge base contains no drought→TDS observations, so I can define the test and run the desalination model, but the basin water-quality data must come from outside both of us [GROUNDED].

My commitments:
1. Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L; fixed NaCl feed, 0.5 g/L product, 80% recovery [GROUNDED].
2. SEC inputs: 3k ppm RO 0.555 / ED 0.762; 5k ppm RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, not plants [GROUNDED].
3. Stage-2 pass/fail: drought-season TDS/ion shift must cross the 3–5 g/L LCOW crossover or invalidate NaCl equivalence; otherwise no technology change [GROUNDED].

If no basin records are obtainable, fallback: report the assumed 3k→5k ppm scenario as sensitivity, not finding [ASSUMED][EXTENDED]—invented shift, may not transfer.

Request: confirm placeholder CA/AZ BAs and the external data path—hourly BA generation/trade, AMPD emissions, and basin TDS/ion records with drought index. Until then, bracket only, no causal dispatch [EXTENDED].

### Scientist 2

Scientist 1, your fallback is right. Moderator: I confirm CA/AZ only as placeholder screening regions, not confirmed BAs [ASSUMED][COMPUTED from R1,R2]; chosen for positive 2021 drought-attributed generation and EFs 0.406/0.427 kg CO₂/kWh; may not transfer because EFs are state-level at emitting units, not load dispatch. Include neighboring BAs/imports because 63% of California’s drought-induced fossil increase is transboundary [GROUNDED].

Data path: my side supplies monthly AMPD generation/emissions, runoff anomalies, and BA×fuel attribution [GROUNDED]. To test dispatch, we need external hourly BA generation/interchange/fuel mix and basin TDS/ion records; my knowledge base offers no basin water-quality evidence [GROUNDED]. Until then, report only EF bracket 0.385–0.604 kg CO₂/kWh, assuming state EFs bound BA EFs; stops if BA EF lies outside [ASSUMED][COMPUTED from R1,R2,R9,R11,R13].

Pass: positive incremental fossil generation within bracket; fail: clean/storage/import margin [EXTENDED]. CO₂-only is lower bound; methane/PM₂.₅ damages excluded [GROUNDED].

### Scientist 1

Moderator: I confirm the summary and the plan. Stage 1 remains Scientist 2’s attribution screen: CA/AZ are placeholder BAs only [ASSUMED][COMPUTED from R1,R2]; the ten-plant portfolio—100,000 m³/d, 28.5 GWh/yr, ~3.25 MW—is an assumed screening construct and may not transfer [ASSUMED][EXTENDED]. Until hourly BA generation/trade, AMPD, imports, and counterfactuals exist, report only the EF bracket, not causal dispatch [EXTENDED].

Stage 2: I can run the desalination side for any drought-season TDS/ion scenario supplied externally. My model’s fixed boundary is NaCl-equivalent feed, 0.5 g/L product, 80% recovery; LCOW crossover is ED cheaper ≤3 g/L and RO cheaper ≥5 g/L [GROUNDED]. SEC inputs remain 3k ppm RO 0.555 / ED 0.762 and 5k ppm RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; these are model lower bounds [GROUNDED].

My knowledge base offers no basin TDS/ion records [GROUNDED]. Fallback if none are obtained: test an assumed 3k→5k ppm shift [ASSUMED][EXTENDED]; invented and may not transfer. Settling result: crossing 3–5 g/L or invalidating NaCl equivalence; otherwise Stage 2 is water-cost relevant only.

### Scientist 2

Moderator: I confirm. Stage 1 is an attribution screen, not dispatch proof.

Use CA/AZ as placeholder screening regions [ASSUMED][COMPUTED from R1,R2]: the value is “CA/AZ,” chosen from positive 2021 state EFs/generation; it may not transfer to actual basin dispatch. Apply Scientist 1’s assumed ten-plant load of 28.5 GWh/yr [ASSUMED][EXTENDED]: invented constant-load portfolio, may not transfer to real siting/cycling.

Until hourly BA generation/trade, fuel mix, AMPD emissions, and counterfactuals are obtained, report only the EF bracket 0.385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; assumption: state EFs bound BA EFs, and the bracket stops if a BA-specific EF lies outside. Include imports because much of California’s drought-induced fossil increase is transboundary [GROUNDED].

Pass: positive incremental fossil generation within the bracket. Fail: clean/storage/import margin [EXTENDED]. CO₂-only is a lower bound; methane and PM₂.₅ damages are excluded [GROUNDED].

Request: confirm CA/AZ placeholders and the external data path.

### Scientist 1

Moderator: I confirm the converged plan from the water side. CA/AZ are acceptable only as placeholder screening regions, not validated basins [ASSUMED][COMPUTED from R1,R2]; they may not transfer to actual dispatch or water quality.

Stage 2, which I lead, needs external basin TDS/ion records paired with a drought index. My model can test those scenarios but cannot supply them [GROUNDED]. Pass/fail: drought shifts feed across the 3–5 g/L LCOW crossover—ED cheaper ≤3 g/L, RO cheaper ≥5 g/L—or invalidates NaCl equivalence [GROUNDED].

If no records are obtainable, fallback is an assumed 3,000→5,000 ppm drought shift [ASSUMED][EXTENDED]; I invented it, and it may not transfer if ion mix, scaling, or brine dominate. SEC inputs remain 3k RO 0.555 / ED 0.762 and 5k RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds [GROUNDED].

External data path: hourly BA generation/trade, AMPD emissions, counterfactuals, and basin TDS/ion records. Until then, bracket only, not causal dispatch [EXTENDED].

### Scientist 2

Moderator: confirmed. Plain language: drought cuts hydro; fossil plants often compensate [GROUNDED]. Desalination uses power; climate harm occurs only if new load is served by drought-called fossil plants [EXTENDED]. Assumption: load is incremental and not served by dedicated clean/storage/imports; stops otherwise.

Stage 1: screen using placeholder CA/AZ—chosen from positive R1/R2 state EFs, may not transfer to actual basins/dispatch [ASSUMED][COMPUTED from R1,R2]—and Scientist 1’s assumed 28.5 GWh/yr ten-plant portfolio, invented constant load, may not transfer [ASSUMED][EXTENDED]. Until hourly BA generation/trade, AMPD, imports, counterfactuals, and basin TDS/ion records exist, report only EF bracket 0.385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]; assumption: state EFs bound BA EFs, stops if BA EF outside. Include imports because much CA drought-fossil response is transboundary [GROUNDED]. Pass: positive incremental fossil generation within bracket; fail: clean/storage/import margin [EXTENDED].

Stage 2: Scientist 1 tests drought→TDS/ion scenarios; fallback assumed salinity shift is sensitivity, not finding [ASSUMED][EXTENDED]. CO₂-only is lower bound; methane/PM₂.₅ excluded [GROUNDED].

---

## Appendix: moderator running summary

Discussion stands at a converged two-stage plan with no live technical disagreement; Scientist 1 and Scientist 2 have confirmed it and are waiting on Moderator. Stage 1, led by Scientist 2, is an attribution screen, not dispatch proof: test Scientist 1’s assumed ten-plant portfolio—100,000 m³/d, 5,000 ppm RO, 28.5 GWh/yr, ≈3.25 MW—in placeholder CA/AZ screening regions, including imports because CA effects are transboundary. Until hourly BA generation/trade, AMPD, fuel mix, and counterfactuals are available, report only an EF bracket, 0.385–0.604 kg CO₂/kWh, not causal dispatch. Scientist 1 commits generic NaCl cases: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L; SECs 3k RO 0.555/ED 0.762, 5k RO 0.781/ED 1.251 kWh/m³; no basin TDS data. Scientist 2 commits drought EFs for OR/CA/AZ/CO/NV; tool state-level, not hourly dispatch. Unresolved: Moderator must confirm CA/AZ placeholders and external data path for hourly BA data, AMPD, basin TDS/ion records, and counterfactuals. Stage 2, led by Scientist 1, remains open: drought→TDS/ion mapping crossing 3–5 g/L or invalidating NaCl equivalence; brine, methane/PM₂.₅ damages unresolved.

## Appendix: scientist profiles

### Scientist 1

## Core claims
Electrodialysis is currently cheaper than reverse osmosis only at low brackish salinities, winning at ≤3 g L⁻¹ but losing at ≥5 g L⁻¹.  
Lower ion-exchange membrane price alone can make ED competitive through about 5 g L⁻¹, but not reliably beyond that.  
At higher salinities, ED needs membranes with higher charge density and low enough diffusion coefficient to preserve current efficiency.  
Only simultaneous membrane-price reduction and membrane-performance improvement makes ED preferable to RO across the whole brackish range.

## Method framework
Model-based technoeconomic comparison using levelized cost of water. Fixed cases: 1, 3, 5, 7, and 10 g L⁻¹ NaCl feed; 0.5 g L⁻¹ product water; 80% recovery; 10,000 m³ d⁻¹ production. ED uses a 2-D Nernst-Planck model across spacer channels and ion-exchange membranes, so current efficiency and membrane resistance are emergent outputs; feed-and-bleed recycle achieves system recovery. RO uses a 1-D pressure-driven model with complete salt rejection and feed bypass to meet product salinity. Productivity is optimized independently for each technology from 10–100 L m⁻² h⁻¹. LCOW includes annualized CAPEX and OPEX for the desalination step only; baseline membrane prices are 100 USD m⁻² for ED ion-exchange membranes and 30 USD m⁻² for RO membranes. The study scans membrane prices and membrane properties, especially charge density and diffusion coefficient.

## Key evidence
- RO holds >80% of brackish desalination capacity; ED is <10% (§1).  
- Baseline comparison: ED is cheaper ≤3 g L⁻¹, RO is cheaper ≥5 g L⁻¹; ED’s largest margin is 0.04 USD m⁻³ at 1 g L⁻¹, RO’s is 0.21 USD m⁻³ at 10 g L⁻¹ (§3.2).  
- ED optimum productivity falls from 100 to 54 L m⁻² h⁻¹ from 1 to 3 g L⁻¹, then another 63% by 10 g L⁻¹; RO’s lowest optimum is 60 L m⁻² h⁻¹ at 7 g L⁻¹ (§3.1).  
- At 3 g L⁻¹, RO has lower specific energy consumption, but ED still wins LCOW because RO’s high-pressure pump costs more (§3.2).  
- Electricity is 33% of ED LCOW at 10 g L⁻¹; removing carbon tax does not flip the winner (§3.2).  
- Membrane-price breakevens: at 5 g L⁻¹, ion-exchange membranes must be <57.18 USD m⁻² versus RO at 30 USD m⁻², and <28.42 USD m⁻² versus RO at 10 USD m⁻²; at 7 g L⁻¹, thresholds are <36.64 and <18.57 USD m⁻², respectively (§3.3).  
- At 7 g L⁻¹, maximizing diffusion coefficient at low charge density cuts resistance from 29 to 3.4 Ω cm² but collapses current efficiency to 0.19 and raises LCOW from 0.84 to 2.19 USD m⁻³ (§3.4).  
- Optimized membrane properties shift target charge density to 7.75 mol L⁻¹ at 10 g L⁻¹, raising current efficiency from 0.90 to 0.95; property improvement alone cuts LCOW by 3% at 3 g L⁻¹ and 17% at 10 g L⁻¹ (§3.4).  
- With ion-exchange membrane price at 30 USD m⁻² and optimized properties, ED LCOW falls >2× at 10 g L⁻¹ and 1.4× at 1 g L⁻¹, becoming cheaper across all brackish salinities even though ED SEC remains slightly above RO at ≥5 g L⁻¹ (§3.5).

## Explicit boundaries
Pretreatment and post-treatment are excluded; ED’s fouling/scaling/chlorine tolerance and RO’s removal of uncharged contaminants are assumed to cancel, though this may determine real technology choice (§2). Feedwater is ideal NaCl, so silica, scaling ions, organics, viruses, and micropollutants are not modeled. This is a modeling study, not pilot validation; ED curves terminate near limiting current density (§3.1). Charge density and diffusion coefficient are scanned as independent variables despite real material coupling; high-charge polymer limitations are idealized (§3.4). Membrane thickness is fixed at 130 µm and spacer thickness at 0.3 mm, so stack geometry is not treated as a major cost lever (§3.4). LCOW covers only the desalination step, excluding brine handling, full project finance, environmental effects, permitting, and operational reliability.

## Voice
Quantitative and mechanistic: the author translates membrane transport physics into LCOW rather than treating energy as sufficient. The tone is cautious: excluded treatment costs are flagged, proxies like specific energy consumption are limited, and future claims are conditional on explicit price and property targets. Characteristic terms include LCOW, productivity, current efficiency, membrane resistance, charge density, diffusion coefficient, permselectivity, concentration polarization, feed-and-bleed, and structure-property-performance. The author extrapolates, but only through threshold values, sensitivity scans, and cost-optimized comparisons.

### Scientist 2

## Core claims
Drought in the western United States reduces hydropower and forces fossil-fuel plants to generate more, with individual plants sometimes increasing output by up to 65% and large effects transmitted across electricity regions.  
This drought-induced fossil generation raises CO2, NOx, SO2, and nearby PM2.5, creating health and climate damages that exceed direct electricity-sector economic costs.  
Historical damages from 2001–2021 are large but declined as emission factors fell, especially for NOx and SO2.  
Future drought risk will keep these damages large even with aggressive renewables because fossil plants remain the marginal source during supply shortfalls.

## Method framework
The study links monthly plant-level generation and emissions from EPA Air Markets Program Data (2001–2021; 681 fossil units >25 MW) to regional drought measured as 9-month running-average runoff anomalies from NLDAS-2/VIC, benchmarked to 1980–2021. It estimates log-generation responses to runoff anomalies in California, Northwest, and Southwest using fixed-effect weighted regressions, then disaggregates impacts by balancing-authority × fuel type. Mechanisms are tested with causal mediation, interregional trade data, and a placebo test in Texas/Florida. Air-quality impacts relate predicted drought-induced SO2+NOx emissions to monitor-based non-wildfire PM2.5 using distance bins, meteorology controls, and upwind tests. Health and climate damages are monetized using a short-term PM2.5 mortality concentration-response function, EPA value of statistical life, social cost of carbon/methane, and methane leakage assumptions. Future impacts combine CMIP6 runoff projections (2030–2059) with stylized electricity-sector scenarios.

## Key evidence
- Under extreme drought, fossil generation increased on average by 35% in California, 11% in Northwest, and 9.5% in Southwest relative to average conditions; cross-region effects accounted for 63% of California’s increase, 44% in Northwest, and almost all in Southwest (Results).  
- A dry Northwest (5th percentile runoff) versus wet (95th) raised net exports from California to Northwest by 23% and Southwest to Northwest by 7.2%; matching estimated generation increases of 26.4% in California and 11.2% in Southwest from Northwest drought (Results/SI).  
- Mediation shows hydro displacement is the dominant channel, not electricity demand; Texas/Florida placebo shows no runoff effect where hydro is small (Results/SI).  
- During extreme drought, drought-induced emissions were ~12% of regional power-sector CO2, ~6% of NOx, and ~8% of SO2; in 2001 about 20% of plants increased SO2/NOx by ≥30% (Results).  
- Drought-induced SO2/NOx emissions raised PM2.5 near plants, especially within 50 km, with effects decaying with distance and stronger for upwind plants; InMAP gave smaller magnitudes (Results/Discussion).  
- Total 2001–2021 monetized damage was $20 billion: $14B CO2, $5.1B PM2.5 mortality, $1.0B methane leakage; 2012–2016 California drought caused $5.1B damage, 1.2–1.9× direct hydro-loss cost and 2.5× demand-cost (Results).  
- Under SSP3-7.0, future annual damage averages $293 million; lower-forcing scenarios reduce damages by up to $214 million; coal-to-gas cuts damage only 11%, high renewables only 5.4% by 2050; California fossil plants remain marginal 71% of hours while providing 8.6% of generation in 2050, and extreme-drought emissions could be 41% of state electricity GHG in 2050 (Results/Discussion).

## Explicit boundaries
The study does not directly isolate heat-wave demand effects because runoff-based drought only partially captures temperature-driven demand. It excludes wildfire-smoke PM2.5 days, backup generators, non-grid units, blackouts, fuel-price shocks, and non-electricity energy responses. Air-quality analysis is limited to 2006–2020 and monitor locations; PM2.5 effects beyond ~200 km are not empirically detected. The main sample covers grid-connected fossil units >25 MW, missing smaller/non-AMPD plants estimated at 7.3% of main generation response. Future sector scenarios are stylized, not policy forecasts, and rely on fixed 2021 plant fleet and specified marginal-source assumptions. Health impacts use a short-term mortality CRF rather than long-term exposure estimates, and the authors note uncertainty in runoff projections, InMAP comparison, and global extrapolation.

## Voice
The author argues empirically and quantitatively, using fixed effects, heterogeneity, mediation, placebo tests, and monetized damages to make a causal and policy-relevant case. The tone is cautious about mechanisms and uncertainties but willing to extrapolate to future climate and decarbonization policy. Characteristic terms include runoff anomalies, drought-induced generation, transboundary effects, marginal energy source, hydro displacement, PM2.5 damages, social cost, and lower-bound damages.

## Appendix: result ledger

Every tool run in the dialogue. This is what a `[COMPUTED from R…]` reference points at.

| id | round | who | tool | arguments | where each value came from | assumed? | returned |
|----|-------|-----|------|-----------|-----------------------------|----------|----------|
| R1 | 0 | Scientist 2 | drought_ef.py | `{"state":"CA"}` | state←assumed | **yes** | `{"ef_kg_co2_per_kwh":0.4061,"drought_generation_MWh":13177407}` |
| R2 | 0 | Scientist 2 | drought_ef.py | `{"state":"AZ"}` | state←assumed | **yes** | `{"ef_kg_co2_per_kwh":0.4273,"drought_generation_MWh":1522879}` |
| R3 | 1 | Scientist 1 | sec_bw.py | `{"feed_ppm":3000,"technology":"RO"}` | feed_ppm←source, technology←source | no | `{"sec_kwh_per_m3":0.5549}` |
| R4 | 1 | Scientist 1 | sec_bw.py | `{"feed_ppm":3000,"technology":"ED"}` | feed_ppm←source, technology←source | no | `{"sec_kwh_per_m3":0.7618}` |
| R5 | 1 | Scientist 1 | sec_bw.py | `{"feed_ppm":5000,"technology":"RO"}` | feed_ppm←source, technology←source | no | `{"sec_kwh_per_m3":0.7806}` |
| R6 | 1 | Scientist 1 | sec_bw.py | `{"feed_ppm":5000,"technology":"ED"}` | feed_ppm←source, technology←source | no | `{"sec_kwh_per_m3":1.2508}` |
| R7 | 1 | Scientist 2 | drought_ef.py | `{"state":"NM"}` | state←assumed | **yes** | **failed** — the script exited with code 1 |
| R8 | 3 | Scientist 2 | drought_ef.py | `{"state":"NM"}` | state←assumed | **yes** | **failed** — the script exited with code 1 |
| R9 | 3 | Scientist 2 | drought_ef.py | `{"state":"NV"}` | state←assumed | **yes** | `{"ef_kg_co2_per_kwh":0.6043,"drought_generation_MWh":937273}` |
| R10 | 5 | Scientist 2 | drought_ef.py | `{"state":"NM"}` | state←assumed | **yes** | **failed** — the script exited with code 1 |
| R11 | 5 | Scientist 2 | drought_ef.py | `{"state":"OR"}` | state←assumed | **yes** | `{"ef_kg_co2_per_kwh":0.3851,"drought_generation_MWh":3203467}` |
| R12 | 8 | Scientist 2 | drought_ef.py | `{"state":"NM"}` | state←assumed | **yes** | **failed** — the script exited with code 1 |
| R13 | 8 | Scientist 2 | drought_ef.py | `{"state":"CO"}` | state←assumed | **yes** | `{"ef_kg_co2_per_kwh":0.3929,"drought_generation_MWh":1171288}` |

Runs resting on a value nobody established, and why:

- **R1** — state: declared assumed by the caller
- **R2** — state: declared assumed by the caller
- **R9** — state: declared assumed by the caller
- **R11** — state: declared assumed by the caller
- **R13** — state: declared assumed by the caller

## Appendix: mechanical checks

Turns where what was claimed and what was recorded disagree. These are data, not
defects: they say whether the tagging discipline actually bound.

| round | who | check | what failed |
|-------|-----|-------|--------------|
| 0 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 1 | Scientist 2 | C2 | tagged [ASSUMED] after 1 tool run — the assumed value was never varied |
| 2 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 3 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 4 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 4 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 5 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 6 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 6 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 7 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 7 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 8 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 9 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 9 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 10 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 10 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 11 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 11 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 12 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 12 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 13 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 13 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 14 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 14 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 15 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 15 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 16 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 16 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 17 | Scientist 1 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |
| 17 | Scientist 2 | C2 | tagged [ASSUMED] after 0 tool runs — the assumed value was never varied |

## Appendix: adjudication — to be filled in by hand

One row per substantive claim. The tag is what the agent asserted; the last two columns
are the judgement no model can make for you.

| # | round | speaker | tag | claim | basis shown | tag correct? | note |
|---|-------|---------|-----|-------|-------------|--------------|------|
| 1 | 0 | Scientist 1 | GROUNDED | …My frame is brackish-water desalination cost, not drought hydrology. | | | |
| 2 | 0 | Scientist 1 | EXTENDED | …onomic model, ED is cheaper than RO at ≤3 g/L NaCl, RO is cheaper at ≥5 g/L, with product 0.5 g/L, 80% recovery, and 10,000 m³/d. | | | |
| 3 | 0 | Scientist 1 | ASSUMED | …s assumes NaCl-equivalent feed and unchanged pretreatment/brine costs, and stops if scaling, silica, or brine disposal dominate. | | | |
| 4 | 0 | Scientist 1 | EXTENDED | …NaCl-equivalent feed and unchanged pretreatment/brine costs, and stops if scaling, silica, or brine disposal dominate. [ASSUMED] | | | |
| 5 | 0 | Scientist 1 | GROUNDED | …my SEC tool can compare kWh/m³ for RO and ED, and Scientist 2’s drought-generation emission factors can convert kWh to CO₂. Gaps | | | |
| 6 | 0 | Scientist 2 | GROUNDED | …seful, but the margin matters. My work shows drought displaces hydro and makes fossil plants the marginal supply during shortages | | | |
| 7 | 0 | Scientist 2 | ASSUMED | …sil plants the marginal supply during shortages [GROUNDED]. For drought-induced fossil generation, I computed CA 0.406 kg CO₂/kWh | | | |
| 8 | 0 | Scientist 2 | COMPUTED FROM R1 | …s the marginal supply during shortages [GROUNDED]. For drought-induced fossil generation, I computed CA 0.406 kg CO₂/kWh [ASSUMED] | | | |
| 9 | 0 | Scientist 2 | ASSUMED | …rtages [GROUNDED]. For drought-induced fossil generation, I computed CA 0.406 kg CO₂/kWh [ASSUMED][COMPUTED from R1] and AZ 0.427 | | | |
| 10 | 0 | Scientist 2 | COMPUTED FROM R2 | …ROUNDED]. For drought-induced fossil generation, I computed CA 0.406 kg CO₂/kWh [ASSUMED][COMPUTED from R1] and AZ 0.427 [ASSUMED] | | | |
| 11 | 0 | Scientist 2 | ASSUMED | …—not new-load prediction. CA vs AZ changes EF by ~5%, so a planning placeholder of ~0.4 kg CO₂/kWh is robust across these choices | | | |
| 12 | 0 | Scientist 2 | COMPUTED FROM R1 AND R2 | …load prediction. CA vs AZ changes EF by ~5%, so a planning placeholder of ~0.4 kg CO₂/kWh is robust across these choices [ASSUMED] | | | |
| 13 | 0 | Scientist 2 | EXTENDED | …EFs assumes desalination load is served by the same drought-called fossil margin; stops if dedicated renewables/storage serve it | | | |
| 14 | 0 | Scientist 2 | GROUNDED | …fossil margin; stops if dedicated renewables/storage serve it [EXTENDED]. Historical no-demand effect predates major desalination | | | |
| 15 | 1 | Scientist 1 | COMPUTED FROM R3–R6 | …Scientist 2, here are cost-optimal SECs — product water 0.5 g/L, 80% recovery, NaCl-equivalent feed — | | | |
| 16 | 1 | Scientist 1 | GROUNDED | …0.781, ED 1.251 kWh/m³. These are model lower bounds, not plant data; reported ED energy is 25–80% higher over 2,000–5,000 ppm | | | |
| 17 | 1 | Scientist 1 | GROUNDED | …2,000–5,000 ppm [GROUNDED]. At 3,000 ppm RO has lower SEC, but ED still wins LCOW because RO’s high-pressure pump cost dominates | | | |
| 18 | 1 | Scientist 1 | GROUNDED | …ppm RO has lower SEC, but ED still wins LCOW because RO’s high-pressure pump cost dominates [GROUNDED]. At 5,000 ppm RO wins LCOW | | | |
| 19 | 1 | Scientist 1 | ASSUMED | …RO’s high-pressure pump cost dominates [GROUNDED]. At 5,000 ppm RO wins LCOW [GROUNDED]. Using your ~0.4 kg CO₂/kWh placeholder | | | |
| 20 | 1 | Scientist 1 | COMPUTED FROM R1 AND R2 | …h-pressure pump cost dominates [GROUNDED]. At 5,000 ppm RO wins LCOW [GROUNDED]. Using your ~0.4 kg CO₂/kWh placeholder [ASSUMED] | | | |
| 21 | 1 | Scientist 1 | ASSUMED | …ot represent a desalination basin’s load — gives roughly 0.22 RO vs 0.30 ED kg CO₂/m³ at 3,000 ppm, and 0.31 vs 0.50 at 5,000 ppm | | | |
| 22 | 1 | Scientist 1 | EXTENDED | …ent a desalination basin’s load — gives roughly 0.22 RO vs 0.30 ED kg CO₂/m³ at 3,000 ppm, and 0.31 vs 0.50 at 5,000 ppm [ASSUMED] | | | |
| 23 | 1 | Scientist 2 | COMPUTED FROM R3–R6 | …Scientist 1, those conversions are the right first-order coupling. Using your SECs | | | |
| 24 | 1 | Scientist 2 | ASSUMED | …1, those conversions are the right first-order coupling. Using your SECs [COMPUTED from R3–R6] and my ~0.4 kg CO₂/kWh placeholder | | | |
| 25 | 1 | Scientist 2 | COMPUTED FROM R1 AND R2 | …conversions are the right first-order coupling. Using your SECs [COMPUTED from R3–R6] and my ~0.4 kg CO₂/kWh placeholder [ASSUMED] | | | |
| 26 | 1 | Scientist 2 | ASSUMED | …CO₂/kWh placeholder [ASSUMED][COMPUTED from R1 and R2], I get ~0.22/0.31 kg CO₂/m³ for RO and 0.30/0.50 for ED at 3,000/5,000 ppm | | | |
| 27 | 1 | Scientist 2 | EXTENDED | …laceholder [ASSUMED][COMPUTED from R1 and R2], I get ~0.22/0.31 kg CO₂/m³ for RO and 0.30/0.50 for ED at 3,000/5,000 ppm [ASSUMED] | | | |
| 28 | 1 | Scientist 2 | ASSUMED | …il margin, and it stops if dedicated renewables/storage or a non-fossil margin serves it. CA vs AZ changes the placeholder by ~5% | | | |
| 29 | 1 | Scientist 2 | COMPUTED FROM R1 AND R2 | …, and it stops if dedicated renewables/storage or a non-fossil margin serves it. CA vs AZ changes the placeholder by ~5% [ASSUMED] | | | |
| 30 | 1 | Scientist 2 | ASSUMED | …fossil margin serves it. CA vs AZ changes the placeholder by ~5% [ASSUMED][COMPUTED from R1 and R2]. I tried NM as a sensitivity | | | |
| 31 | 1 | Scientist 2 | COMPUTED FROM R7 | …rgin serves it. CA vs AZ changes the placeholder by ~5% [ASSUMED][COMPUTED from R1 and R2]. I tried NM as a sensitivity [ASSUMED] | | | |
| 32 | 1 | Scientist 2 | GROUNDED | …margin is spatially uneven. My historical no-demand result predates major desalination, so it is not evidence against this load | | | |
| 33 | 2 | Scientist 1 | EXTENDED | …greed: your NM result shows we should not apply a single drought EF to a desalination basin without locating both load and margin | | | |
| 34 | 2 | Scientist 1 | GROUNDED | …l margin; it stops if dedicated renewables/storage or imports set the margin. I can supply TDS scenarios, not drought hydrology. | | | |
| 35 | 2 | Scientist 1 | GROUNDED | …S scenarios, not drought hydrology. [GROUNDED] My model covers fixed cases at 1,000–10,000 ppm; values between are interpolation. | | | |
| 36 | 2 | Scientist 1 | ASSUMED | …10,000 ppm; values between are interpolation. [GROUNDED] LCOW crossover is 3–5 g/L: ED cheaper ≤3,000 ppm, RO cheaper ≥5,000 ppm. | | | |
| 37 | 2 | Scientist 1 | EXTENDED | …m; values between are interpolation. [GROUNDED] LCOW crossover is 3–5 g/L: ED cheaper ≤3,000 ppm, RO cheaper ≥5,000 ppm. [ASSUMED] | | | |
| 38 | 2 | Scientist 1 | COMPUTED FROM R3–R6 | …a scenario I invented, and it may not transfer if ion mix or scaling changes—RO’s SEC advantage widens from 0.207 to 0.470 kWh/m³ | | | |
| 39 | 2 | Scientist 2 | EXTENDED | …ssil EF → kg CO₂/m³, with balancing-authority/fuel generation checks, then compare against grid-average and dedicated-clean cases | | | |
| 40 | 2 | Scientist 2 | GROUNDED | …ve, but the EF is an attribution for 2021 western drought, combustion CO₂ only, no uncertainty, and not a prediction for new load | | | |
| 41 | 2 | Scientist 2 | GROUNDED | …on for new load [GROUNDED]. My historical demand null predates large desalination, so it cannot reject an incremental-load effect | | | |
| 42 | 2 | Scientist 2 | GROUNDED | …n produced $20B damages 2001–21, including CO₂, PM₂.₅ mortality, and methane leakage; the 2012–16 California drought caused $5.1B | | | |
| 43 | 2 | Scientist 2 | EXTENDED | …GROUNDED]. So siting desalination where drought calls up fossil generation may add health/climate damages beyond electricity cost | | | |
| 44 | 3 | Scientist 1 | GROUNDED | …Scientist 2, Moderator: I accept the coupled test as conditional, not settled. I can supply the desalination side: | | | |
| 45 | 3 | Scientist 1 | COMPUTED FROM R3–R6 | …] fixed NaCl-equivalent cases 1,000–10,000 ppm, 500 ppm product, 80% recovery, 10,000 m³/d; ED cheaper ≤3 g/L, RO cheaper ≥5 g/L. | | | |
| 46 | 3 | Scientist 1 | GROUNDED | …eaper ≤3 g/L, RO cheaper ≥5 g/L. [COMPUTED from R3–R6] SECs: 3,000 ppm RO 0.555 / ED 0.762; 5,000 ppm RO 0.781 / ED 1.251 kWh/m³. | | | |
| 47 | 3 | Scientist 1 | ASSUMED | …m RO 0.781 / ED 1.251 kWh/m³. [GROUNDED] These are model lower bounds; reported ED energy is 25–80% higher over 2,000–5,000 ppm. | | | |
| 48 | 3 | Scientist 1 | EXTENDED | …1 / ED 1.251 kWh/m³. [GROUNDED] These are model lower bounds; reported ED energy is 25–80% higher over 2,000–5,000 ppm. [ASSUMED] | | | |
| 49 | 3 | Scientist 1 | ASSUMED | …DED] A drought-driven TDS shift from 3,000 to 5,000 ppm is my invented scenario; it stops if ion mix, scaling, or brine dominate. | | | |
| 50 | 3 | Scientist 1 | EXTENDED | …ought-driven TDS shift from 3,000 to 5,000 ppm is my invented scenario; it stops if ion mix, scaling, or brine dominate. [ASSUMED] | | | |
| 51 | 3 | Scientist 1 | GROUNDED | …/kWh placeholder from R1/R2, emissions are ~0.22/0.31 RO and ~0.30/0.50 ED kg/m³; assumed because basin/margin may not transfer. | | | |
| 52 | 3 | Scientist 2 | EXTENDED | …Scientist 1, Moderator: I can provide drought-marginal EFs; grid-average/clean counterfactuals require extra assumptions | | | |
| 53 | 3 | Scientist 2 | ASSUMED | …entist 1, Moderator: I can provide drought-marginal EFs; grid-average/clean counterfactuals require extra assumptions [EXTENDED]. | | | |
| 54 | 3 | Scientist 2 | EXTENDED | …Moderator: I can provide drought-marginal EFs; grid-average/clean counterfactuals require extra assumptions [EXTENDED]. [ASSUMED] | | | |
| 55 | 3 | Scientist 2 | ASSUMED | …/imports set the margin. NM sensitivity failed: negative 2021 drought-attributed generation (−208,482 MWh), so no drought margin | | | |
| 56 | 3 | Scientist 2 | COMPUTED FROM R8 | …set the margin. NM sensitivity failed: negative 2021 drought-attributed generation (−208,482 MWh), so no drought margin [ASSUMED] | | | |
| 57 | 3 | Scientist 2 | ASSUMED | …and it may not transfer because emitting-unit location ≠ load location. NV alternative gives EF 0.604 kg CO₂/kWh and 937,273 MWh | | | |
| 58 | 3 | Scientist 2 | COMPUTED FROM R9 | …ay not transfer because emitting-unit location ≠ load location. NV alternative gives EF 0.604 kg CO₂/kWh and 937,273 MWh [ASSUMED] | | | |
| 59 | 3 | Scientist 2 | COMPUTED FROM R3–R6 | …nd 937,273 MWh [ASSUMED][COMPUTED from R9]; I chose NV, 2021-only, combustion CO₂-only, attribution not new load. With your SECs | | | |
| 60 | 3 | Scientist 2 | ASSUMED | …ribution not new load. With your SECs [COMPUTED from R3–R6], NV gives RO 0.34/0.47 and ED 0.46/0.76 kg CO₂/m³ at 3,000/5,000 ppm | | | |
| 61 | 3 | Scientist 2 | EXTENDED | …not new load. With your SECs [COMPUTED from R3–R6], NV gives RO 0.34/0.47 and ED 0.46/0.76 kg CO₂/m³ at 3,000/5,000 ppm [ASSUMED] | | | |
| 62 | 3 | Scientist 2 | EXTENDED | …00/5,000 ppm [ASSUMED][EXTENDED]. This is ~50% above the 0.4 placeholder, so basin/balancing-authority selection dominates. Next | | | |
| 63 | 3 | Scientist 2 | GROUNDED | …rage/clean cases remain assumptions. Gaps: drought→TDS/ion mix, brine, and methane/PM₂.₅ damages outside the CO₂-only lower bound | | | |
| 64 | 4 | Scientist 1 | GROUNDED | …e coupled test as conditional, not settled. My model is generic: NaCl-equivalent feed, 0.5 g/L product, 80% recovery, 10,000 m³/d | | | |
| 65 | 4 | Scientist 1 | GROUNDED | …del is generic: NaCl-equivalent feed, 0.5 g/L product, 80% recovery, 10,000 m³/d [GROUNDED]. LCOW crossover: ED ≤3 g/L, RO ≥5 g/L | | | |
| 66 | 4 | Scientist 1 | COMPUTED FROM R3–R6 | …m³/d [GROUNDED]. LCOW crossover: ED ≤3 g/L, RO ≥5 g/L [GROUNDED]. SECs: 3k ppm RO 0.555/ED 0.762; 5k ppm RO 0.781/ED 1.251 kWh/m³ | | | |
| 67 | 4 | Scientist 1 | GROUNDED | …0.555/ED 0.762; 5k ppm RO 0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm | | | |
| 68 | 4 | Scientist 1 | ASSUMED | …62; 5k ppm RO 0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm [GROUNDED]. | | | |
| 69 | 4 | Scientist 1 | EXTENDED | …m RO 0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm [GROUNDED]. [ASSUMED] | | | |
| 70 | 4 | Scientist 1 | ASSUMED | …hifting feed from 3k to 5k ppm is my invented scenario; it stops if ion mix, scaling, or brine dominate. Using NV EF 0.604 kg/kWh | | | |
| 71 | 4 | Scientist 1 | COMPUTED FROM R9 | …eed from 3k to 5k ppm is my invented scenario; it stops if ion mix, scaling, or brine dominate. Using NV EF 0.604 kg/kWh [ASSUMED] | | | |
| 72 | 4 | Scientist 1 | ASSUMED | …and basin margin may differ. At 5k ppm RO wins cost and fossil-margin CO₂; at 3k ED wins LCOW but emits more under fossil margin | | | |
| 73 | 4 | Scientist 1 | EXTENDED | …n margin may differ. At 5k ppm RO wins cost and fossil-margin CO₂; at 3k ED wins LCOW but emits more under fossil margin [ASSUMED] | | | |
| 74 | 4 | Scientist 2 | ASSUMED | …ator: from computed tests, positive drought-attributed fossil generation is currently: - CA: 13,177,407 MWh, EF 0.406 kg CO₂/kWh | | | |
| 75 | 4 | Scientist 2 | COMPUTED FROM R1 | …m computed tests, positive drought-attributed fossil generation is currently: - CA: 13,177,407 MWh, EF 0.406 kg CO₂/kWh [ASSUMED] | | | |
| 76 | 4 | Scientist 2 | ASSUMED | …l generation is currently: - CA: 13,177,407 MWh, EF 0.406 kg CO₂/kWh [ASSUMED][COMPUTED from R1] - AZ: 1,522,879 MWh, EF 0.427 | | | |
| 77 | 4 | Scientist 2 | COMPUTED FROM R2 | …ion is currently: - CA: 13,177,407 MWh, EF 0.406 kg CO₂/kWh [ASSUMED][COMPUTED from R1] - AZ: 1,522,879 MWh, EF 0.427 [ASSUMED] | | | |
| 78 | 4 | Scientist 2 | ASSUMED | …kg CO₂/kWh [ASSUMED][COMPUTED from R1] - AZ: 1,522,879 MWh, EF 0.427 [ASSUMED][COMPUTED from R2] - NV: 937,273 MWh, EF 0.604 | | | |
| 79 | 4 | Scientist 2 | COMPUTED FROM R9 | …Wh [ASSUMED][COMPUTED from R1] - AZ: 1,522,879 MWh, EF 0.427 [ASSUMED][COMPUTED from R2] - NV: 937,273 MWh, EF 0.604 [ASSUMED] | | | |
| 80 | 4 | Scientist 2 | GROUNDED | …ot transfer because the EF locates emitting units, is 2021-only, combustion-CO₂-only, and is attribution, not new-load prediction | | | |
| 81 | 4 | Scientist 2 | GROUNDED | …D]. I cannot yet list BAs; my instrument is state-level, though the underlying study estimates balancing-authority × fuel effects | | | |
| 82 | 4 | Scientist 2 | ASSUMED | …is state-level, though the underlying study estimates balancing-authority × fuel effects [GROUNDED]. Candidate basins: CA/AZ/NV | | | |
| 83 | 4 | Scientist 2 | EXTENDED | …-level, though the underlying study estimates balancing-authority × fuel effects [GROUNDED]. Candidate basins: CA/AZ/NV [ASSUMED] | | | |
| 84 | 4 | Scientist 2 | EXTENDED | …vide EF sensitivity and identify negative-margin states. Grid-average and clean-power counterfactuals remain explicit assumptions | | | |
| 85 | 4 | Scientist 2 | GROUNDED | …er counterfactuals remain explicit assumptions [EXTENDED]. Gaps: drought→TDS/ion mix, brine, and methane/PM₂.₅ damages beyond CO₂ | | | |
| 86 | 5 | Scientist 1 | GROUNDED | …Moderator: I cannot map CA/AZ/NV to actual basin TDS; my knowledge base offers no evidence on state-specific TDS. | | | |
| 87 | 5 | Scientist 1 | GROUNDED | …as EF multipliers, not desalination physics. Screening map: for any candidate basin, if TDS ≤3k ppm ED wins LCOW; if ≥5k RO wins | | | |
| 88 | 5 | Scientist 1 | COMPUTED FROM R3–R6 | …didate basin, if TDS ≤3k ppm ED wins LCOW; if ≥5k RO wins [GROUNDED]. SECs: 3k RO 0.555 / ED 0.762; 5k RO 0.781 / ED 1.251 kWh/m³ | | | |
| 89 | 5 | Scientist 1 | GROUNDED | …0.555 / ED 0.762; 5k RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm | | | |
| 90 | 5 | Scientist 1 | ASSUMED | …/ ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm [GROUNDED]. With CA/AZ/NV EFs | | | |
| 91 | 5 | Scientist 1 | COMPUTED FROM R1,R2,R9 | …51 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, ED reported 25–80% higher at 2–5k ppm [GROUNDED]. With CA/AZ/NV EFs [ASSUMED] | | | |
| 92 | 5 | Scientist 1 | ASSUMED | …UTED from R1,R2,R9], CO₂/m³ at 3k is RO 0.225/0.237/0.335, ED 0.309/0.325/0.460; at 5k RO 0.317/0.333/0.471, ED 0.508/0.534/0.756 | | | |
| 93 | 5 | Scientist 1 | EXTENDED | …R1,R2,R9], CO₂/m³ at 3k is RO 0.225/0.237/0.335, ED 0.309/0.325/0.460; at 5k RO 0.317/0.333/0.471, ED 0.508/0.534/0.756 [ASSUMED] | | | |
| 94 | 5 | Scientist 2 | ASSUMED | …Scientist 1, Moderator: tested subset, not full map. Positive 2021 margins: CA 13.18M MWh, EF 0.406 | | | |
| 95 | 5 | Scientist 2 | COMPUTED FROM R1 | …Scientist 1, Moderator: tested subset, not full map. Positive 2021 margins: CA 13.18M MWh, EF 0.406 [ASSUMED] | | | |
| 96 | 5 | Scientist 2 | ASSUMED | …derator: tested subset, not full map. Positive 2021 margins: CA 13.18M MWh, EF 0.406 [ASSUMED][COMPUTED from R1]; AZ 1.52M, 0.427 | | | |
| 97 | 5 | Scientist 2 | COMPUTED FROM R2 | …tested subset, not full map. Positive 2021 margins: CA 13.18M MWh, EF 0.406 [ASSUMED][COMPUTED from R1]; AZ 1.52M, 0.427 [ASSUMED] | | | |
| 98 | 5 | Scientist 2 | ASSUMED | …e 2021 margins: CA 13.18M MWh, EF 0.406 [ASSUMED][COMPUTED from R1]; AZ 1.52M, 0.427 [ASSUMED][COMPUTED from R2]; NV 0.94M, 0.604 | | | |
| 99 | 5 | Scientist 2 | COMPUTED FROM R9 | …rgins: CA 13.18M MWh, EF 0.406 [ASSUMED][COMPUTED from R1]; AZ 1.52M, 0.427 [ASSUMED][COMPUTED from R2]; NV 0.94M, 0.604 [ASSUMED] | | | |
| 100 | 5 | Scientist 2 | ASSUMED | …MED][COMPUTED from R1]; AZ 1.52M, 0.427 [ASSUMED][COMPUTED from R2]; NV 0.94M, 0.604 [ASSUMED][COMPUTED from R9]; OR 3.20M, 0.385 | | | |
| 101 | 5 | Scientist 2 | COMPUTED FROM R11 | …UTED from R1]; AZ 1.52M, 0.427 [ASSUMED][COMPUTED from R2]; NV 0.94M, 0.604 [ASSUMED][COMPUTED from R9]; OR 3.20M, 0.385 [ASSUMED] | | | |
| 102 | 5 | Scientist 2 | ASSUMED | …; may not transfer: 2021 state attribution at emitting units, combustion CO₂ only, not new load. Negative: NM no EF; −208,482 MWh | | | |
| 103 | 5 | Scientist 2 | COMPUTED FROM R10 | …transfer: 2021 state attribution at emitting units, combustion CO₂ only, not new load. Negative: NM no EF; −208,482 MWh [ASSUMED] | | | |
| 104 | 5 | Scientist 2 | ASSUMED | …~57% spread), so basin/BA selection dominates. With OR EF and your SECs [R3–R6]: 3k ppm RO/ED ≈0.21/0.29 kg CO₂/m³; 5k ≈0.30/0.48 | | | |
| 105 | 5 | Scientist 2 | EXTENDED | …ad), so basin/BA selection dominates. With OR EF and your SECs [R3–R6]: 3k ppm RO/ED ≈0.21/0.29 kg CO₂/m³; 5k ≈0.30/0.48 [ASSUMED] | | | |
| 106 | 5 | Scientist 2 | GROUNDED | …age/imports set margin. Next: Moderator, choose basins/BAs. My study estimates BA×fuel effects, but my instrument is state-level | | | |
| 107 | 5 | Scientist 2 | EXTENDED | …udy estimates BA×fuel effects, but my instrument is state-level [GROUNDED]. Grid-average/clean counterfactuals remain assumptions | | | |
| 108 | 5 | Scientist 2 | GROUNDED | …D]. Grid-average/clean counterfactuals remain assumptions [EXTENDED]. Gaps: drought→TDS/ion mix, brine, methane/PM₂.₅ lower bound | | | |
| 109 | 6 | Scientist 1 | GROUNDED | …ator: I would do first: basin-specific drought→TDS/ion-composition mapping, because my technology choice is feed-salinity-driven. | | | |
| 110 | 6 | Scientist 1 | GROUNDED | …NDED] My model uses NaCl-equivalent feed, 0.5 g/L product, 80% recovery; LCOW crossover is 3–5 g/L, ED cheaper ≤3, RO cheaper ≥5. | | | |
| 111 | 6 | Scientist 1 | ASSUMED | …t cannot test ion mix, though ED energy depends on which ions are moved. Method: choose one positive-margin state, e.g. CA or AZ | | | |
| 112 | 6 | Scientist 1 | COMPUTED FROM R1/R2 | …test ion mix, though ED energy depends on which ions are moved. Method: choose one positive-margin state, e.g. CA or AZ [ASSUMED] | | | |
| 113 | 6 | Scientist 1 | ASSUMED | …trative and may not transfer—compile monthly groundwater TDS/major ions and drought index, fit TDS response, then rerun SEC/LCOW. | | | |
| 114 | 6 | Scientist 1 | EXTENDED | …nd may not transfer—compile monthly groundwater TDS/major ions and drought index, fit TDS response, then rerun SEC/LCOW. [ASSUMED] | | | |
| 115 | 6 | Scientist 1 | EXTENDED | …3–5 g/L LCOW crossover or invalidating the NaCl-equivalent assumption. If no crossing occurs, the cost/climate link remains weak | | | |
| 116 | 6 | Scientist 2 | EXTENDED | …st, because TDS mapping only matters climatically if desalination load is incremental and served by drought-called fossil plants. | | | |
| 117 | 6 | Scientist 2 | ASSUMED | …if desalination load is incremental and served by drought-called fossil plants. [EXTENDED] Plan: pick a CA/AZ balancing authority | | | |
| 118 | 6 | Scientist 2 | COMPUTED FROM R5 | …a CA/AZ balancing authority [ASSUMED]—illustrative, may not transfer—use your 10,000 m³/d plant and 5,000 ppm RO SEC 0.781 kWh/m³ | | | |
| 119 | 6 | Scientist 2 | ASSUMED | …ransfer—use your 10,000 m³/d plant and 5,000 ppm RO SEC 0.781 kWh/m³ [COMPUTED from R5], add a 7.8 MWh/d (2.85 GWh/yr) load shock | | | |
| 120 | 6 | Scientist 2 | COMPUTED FROM R1 | …a 7.8 MWh/d (2.85 GWh/yr) load shock [ASSUMED], and compare dispatch against 2021 drought-attributed generation and EFs: CA 0.406 | | | |
| 121 | 6 | Scientist 2 | COMPUTED FROM R2 | …d shock [ASSUMED], and compare dispatch against 2021 drought-attributed generation and EFs: CA 0.406 [COMPUTED from R1], AZ 0.427 | | | |
| 122 | 6 | Scientist 2 | ASSUMED | …esponse, or a clean/storage/import margin, kills it. Scale check: 2.85 GWh/yr is ~0.02% of CA’s 13.18 TWh 2021 drought generation | | | |
| 123 | 6 | Scientist 2 | EXTENDED | …or a clean/storage/import margin, kills it. Scale check: 2.85 GWh/yr is ~0.02% of CA’s 13.18 TWh 2021 drought generation [ASSUMED] | | | |
| 124 | 6 | Scientist 2 | GROUNDED | …NDED]; one plant is negligible, so a basin portfolio is needed. My study has BA×fuel estimates, but my instrument is state-level | | | |
| 125 | 6 | Scientist 2 | GROUNDED | …llow; if marginal-load proof fails, the crossover is economically relevant but climate-irrelevant. CO₂-only remains a lower bound | | | |
| 126 | 7 | Scientist 1 | COMPUTED FROM R5 | …drought-margin CO₂ consequence. Stage 1, Scientist 2 leads: test a 10,000 m³/d load shock. At 5,000 ppm RO, SEC is 0.781 kWh/m³ | | | |
| 127 | 7 | Scientist 1 | COMPUTED FROM R5 | …2 leads: test a 10,000 m³/d load shock. At 5,000 ppm RO, SEC is 0.781 kWh/m³ [COMPUTED from R5], giving 7.81 MWh/d or 2.85 GWh/yr | | | |
| 128 | 7 | Scientist 1 | ASSUMED | …MPUTED from R5]. Settling result: positive incremental fossil generation with EF inside the observed 0.385–0.604 kg CO₂/kWh range | | | |
| 129 | 7 | Scientist 1 | COMPUTED FROM R1,R2,R9,R11 | …om R5]. Settling result: positive incremental fossil generation with EF inside the observed 0.385–0.604 kg CO₂/kWh range [ASSUMED] | | | |
| 130 | 7 | Scientist 1 | GROUNDED | …ad: basin TDS/ion mapping. Settling result: drought shifts feed across the 3–5 g/L LCOW crossover or invalidates NaCl equivalence | | | |
| 131 | 7 | Scientist 2 | GROUNDED | …rginal-load proof first. My `drought_ef` instrument gives 2021 drought-attributed fossil EFs, not a dispatch model for a new load | | | |
| 132 | 7 | Scientist 2 | ASSUMED | …el for a new load [GROUNDED]. Test: put Scientist 1’s assumed 10,000 m³/d, 5,000-ppm RO load—7.8 MWh/d, 2.85 GWh/yr using R5 SEC | | | |
| 133 | 7 | Scientist 2 | EXTENDED | …new load [GROUNDED]. Test: put Scientist 1’s assumed 10,000 m³/d, 5,000-ppm RO load—7.8 MWh/d, 2.85 GWh/yr using R5 SEC [ASSUMED] | | | |
| 134 | 7 | Scientist 2 | ASSUMED | …000 m³/d, 5,000-ppm RO load—7.8 MWh/d, 2.85 GWh/yr using R5 SEC [ASSUMED][EXTENDED]—into a California/Arizona balancing authority | | | |
| 135 | 7 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11 | …authority [ASSUMED]. Compare incremental fossil EF with observed drought-marginal EFs: 0.385–0.604 kg CO₂/kWh across OR/AZ/CA/NV | | | |
| 136 | 7 | Scientist 2 | ASSUMED | …tage 2 TDS/ion mapping sets technology and SEC magnitude. Single-plant scale is ~0.02% of CA’s 13.18 TWh 2021 drought generation | | | |
| 137 | 7 | Scientist 2 | EXTENDED | …S/ion mapping sets technology and SEC magnitude. Single-plant scale is ~0.02% of CA’s 13.18 TWh 2021 drought generation [ASSUMED] | | | |
| 138 | 7 | Scientist 2 | GROUNDED | …e-plant scale is ~0.02% of CA’s 13.18 TWh 2021 drought generation [ASSUMED][EXTENDED]; use a portfolio. CO₂-only is a lower bound | | | |
| 139 | 8 | Scientist 1 | ASSUMED | …Moderator: I would implement Stage 1 first, but as a portfolio screen rather than one plant. | | | |
| 140 | 8 | Scientist 1 | EXTENDED | …Moderator: I would implement Stage 1 first, but as a portfolio screen rather than one plant. [ASSUMED] | | | |
| 141 | 8 | Scientist 1 | COMPUTED FROM R5 | …invented this portfolio scale, and it may not transfer to real basin permitting or siting. Load is 28.5 GWh/yr, from 0.781 kWh/m³ | | | |
| 142 | 8 | Scientist 1 | ASSUMED | …can test whether incremental fossil EF falls inside 0.385–0.604 kg CO₂/kWh and whether drought-attributed generation is positive | | | |
| 143 | 8 | Scientist 1 | COMPUTED FROM R1,R2,R9,R11 | …whether incremental fossil EF falls inside 0.385–0.604 kg CO₂/kWh and whether drought-attributed generation is positive [ASSUMED] | | | |
| 144 | 8 | Scientist 1 | GROUNDED | …D from R1,R2,R9,R11]; state choices are illustrative. I supply salinity-specific SEC/LCOW: ED wins ≤3,000 ppm, RO wins ≥5,000 ppm | | | |
| 145 | 8 | Scientist 1 | COMPUTED FROM R3–R6 | …tate choices are illustrative. I supply salinity-specific SEC/LCOW: ED wins ≤3,000 ppm, RO wins ≥5,000 ppm [GROUNDED]; 3k/5k SECs | | | |
| 146 | 8 | Scientist 1 | EXTENDED | …UTED from R3–R6]. I cannot provide BA dispatch. Without BA-level marginal data, Stage 1 remains an attribution screen, not proof | | | |
| 147 | 8 | Scientist 1 | GROUNDED | …passes, Stage 2 is drought→TDS/ion mapping; it settles if feed crosses the 3–5 g/L LCOW crossover or invalidates NaCl equivalence | | | |
| 148 | 8 | Scientist 2 | ASSUMED | …oderator: I accept the portfolio screen. NM returned no EF because 2021 drought-attributed generation was negative (−208,482 MWh) | | | |
| 149 | 8 | Scientist 2 | COMPUTED FROM R12 | …I accept the portfolio screen. NM returned no EF because 2021 drought-attributed generation was negative (−208,482 MWh) [ASSUMED] | | | |
| 150 | 8 | Scientist 2 | ASSUMED | …sfer because it is state-level attribution at emitting units, not basin/load dispatch. CO gives EF 0.393 kg CO₂/kWh and 1.17M MWh | | | |
| 151 | 8 | Scientist 2 | COMPUTED FROM R13 | …use it is state-level attribution at emitting units, not basin/load dispatch. CO gives EF 0.393 kg CO₂/kWh and 1.17M MWh [ASSUMED] | | | |
| 152 | 8 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …-only, attribution-not-new-load caveats. Conclusion unchanged: positive margins exist, EFs stay 0.385–0.604 across OR/CA/AZ/CO/NV | | | |
| 153 | 8 | Scientist 2 | ASSUMED | …385–0.604 across OR/CA/AZ/CO/NV [COMPUTED from R1,R2,R9,R11,R13], but some states fail. Use the ten-plant portfolio, 28.5 GWh/yr | | | |
| 154 | 8 | Scientist 2 | EXTENDED | …across OR/CA/AZ/CO/NV [COMPUTED from R1,R2,R9,R11,R13], but some states fail. Use the ten-plant portfolio, 28.5 GWh/yr [ASSUMED] | | | |
| 155 | 8 | Scientist 2 | ASSUMED | …e ten-plant portfolio, 28.5 GWh/yr [ASSUMED][EXTENDED]; it is small vs positive-state drought generation—~0.2% of CA, ~2.4% of CO | | | |
| 156 | 8 | Scientist 2 | EXTENDED | …nt portfolio, 28.5 GWh/yr [ASSUMED][EXTENDED]; it is small vs positive-state drought generation—~0.2% of CA, ~2.4% of CO [ASSUMED] | | | |
| 157 | 8 | Scientist 2 | GROUNDED | …/storage/import margin or negative response kills coupling. My study estimates BA×fuel responses, but current tool is state-level | | | |
| 158 | 9 | Scientist 1 | GROUNDED | …s positive-margin list, but my knowledge base offers no evidence on basin salinity or dispatch, so I cannot name BAs from my side | | | |
| 159 | 9 | Scientist 1 | GROUNDED | …ds exist. I can supply water-side cases: fixed 1–10 g/L NaCl, 0.5 g/L product, 80% recovery; LCOW crossover ED ≤3 g/L, RO ≥5 g/L | | | |
| 160 | 9 | Scientist 1 | COMPUTED FROM R3–R6 | …d 1–10 g/L NaCl, 0.5 g/L product, 80% recovery; LCOW crossover ED ≤3 g/L, RO ≥5 g/L [GROUNDED]. SECs at 3/5k ppm are on the table | | | |
| 161 | 9 | Scientist 1 | ASSUMED | …tage 1, define the ten-plant portfolio as constant load: 100,000 m³/d × 0.781 kWh/m³ = 78.1 MWh/d = 28.5 GWh/yr ≈ 3.25 MW average | | | |
| 162 | 9 | Scientist 1 | EXTENDED | …efine the ten-plant portfolio as constant load: 100,000 m³/d × 0.781 kWh/m³ = 78.1 MWh/d = 28.5 GWh/yr ≈ 3.25 MW average [ASSUMED] | | | |
| 163 | 9 | Scientist 1 | ASSUMED | …nsfer to real cycling or permitting. Settling result: BA-level incremental fossil response positive, EF within 0.385–0.604 kg/kWh | | | |
| 164 | 9 | Scientist 1 | COMPUTED FROM R1,R2,R9,R11,R13 | …real cycling or permitting. Settling result: BA-level incremental fossil response positive, EF within 0.385–0.604 kg/kWh [ASSUMED] | | | |
| 165 | 9 | Scientist 1 | GROUNDED | …storage/import margin kills it. If it passes, Stage 2 settles if drought TDS/ion shift crosses 3–5 g/L or breaks NaCl equivalence | | | |
| 166 | 9 | Scientist 2 | EXTENDED | …Scientist 1, Moderator: I agree Stage 1 first, but as a screen, not proof | | | |
| 167 | 9 | Scientist 2 | GROUNDED | …ancing-authority × fuel drought responses, but my callable EF is state-level, 2021, combustion-CO₂-only, attribution—not dispatch | | | |
| 168 | 9 | Scientist 2 | ASSUMED | …te-level, 2021, combustion-CO₂-only, attribution—not dispatch [GROUNDED]. Choose BAs inside positive states; I propose CA and AZ | | | |
| 169 | 9 | Scientist 2 | COMPUTED FROM R1,R2 | …2021, combustion-CO₂-only, attribution—not dispatch [GROUNDED]. Choose BAs inside positive states; I propose CA and AZ [ASSUMED] | | | |
| 170 | 9 | Scientist 2 | ASSUMED | …data—outside my knowledge base—and regress incremental fossil output against runoff anomalies and the 28.5 GWh/yr portfolio load | | | |
| 171 | 9 | Scientist 2 | EXTENDED | …side my knowledge base—and regress incremental fossil output against runoff anomalies and the 28.5 GWh/yr portfolio load [ASSUMED] | | | |
| 172 | 9 | Scientist 2 | EXTENDED | …nd the 28.5 GWh/yr portfolio load [ASSUMED][EXTENDED]. Counterfactuals: grid-average, high-renewables/storage, and import margins | | | |
| 173 | 9 | Scientist 2 | ASSUMED | …ge, and import margins [EXTENDED]. Settling result: positive incremental fossil generation with EF inside 0.385–0.604 kg CO₂/kWh | | | |
| 174 | 9 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …mport margins [EXTENDED]. Settling result: positive incremental fossil generation with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED] | | | |
| 175 | 9 | Scientist 2 | ASSUMED | …R2,R9,R11,R13]; clean/storage/import margin or negative response kills the coupling. NM’s negative margin shows selection matters | | | |
| 176 | 9 | Scientist 2 | COMPUTED FROM R12 | …,R13]; clean/storage/import margin or negative response kills the coupling. NM’s negative margin shows selection matters [ASSUMED] | | | |
| 177 | 10 | Scientist 1 | EXTENDED | …entist 2’s marginal-load screen, because without incremental fossil dispatch my LCOW crossover has no drought-climate consequence | | | |
| 178 | 10 | Scientist 1 | GROUNDED | …on load is incremental; stops if it is not. I cannot choose BAs from my knowledge base; it has no basin TDS or dispatch evidence | | | |
| 179 | 10 | Scientist 1 | ASSUMED | …dispatch evidence [GROUNDED]. If a choice is required now, use CA and AZ only as Scientist 2’s assumed positive-margin candidates | | | |
| 180 | 10 | Scientist 1 | COMPUTED FROM R1,R2 | …evidence [GROUNDED]. If a choice is required now, use CA and AZ only as Scientist 2’s assumed positive-margin candidates [ASSUMED] | | | |
| 181 | 10 | Scientist 1 | ASSUMED | …al basins. Water-side input: ten-plant portfolio, 100,000 m³/d at 5,000 ppm RO, 28.5 GWh/yr ≈3.25 MW average, using 0.781 kWh/m³ | | | |
| 182 | 10 | Scientist 1 | EXTENDED | …. Water-side input: ten-plant portfolio, 100,000 m³/d at 5,000 ppm RO, 28.5 GWh/yr ≈3.25 MW average, using 0.781 kWh/m³ [ASSUMED] | | | |
| 183 | 10 | Scientist 1 | COMPUTED FROM R3–R6 | …XTENDED]; ten plants and constant load are invented and may not transfer. SECs: 3k RO 0.555/ED 0.762; 5k RO 0.781/ED 1.251 kWh/m³ | | | |
| 184 | 10 | Scientist 1 | GROUNDED | …invented and may not transfer. SECs: 3k RO 0.555/ED 0.762; 5k RO 0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds | | | |
| 185 | 10 | Scientist 1 | GROUNDED | …0.781/ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds [GROUNDED]. My method cannot supply hourly BA generation or AMPD | | | |
| 186 | 10 | Scientist 1 | ASSUMED | …ply hourly BA generation or AMPD [GROUNDED]. Settling result: BA-level positive fossil response with EF inside 0.385–0.604 kg/kWh | | | |
| 187 | 10 | Scientist 1 | COMPUTED FROM R1,R2,R9,R11,R13 | …y BA generation or AMPD [GROUNDED]. Settling result: BA-level positive fossil response with EF inside 0.385–0.604 kg/kWh [ASSUMED] | | | |
| 188 | 10 | Scientist 1 | GROUNDED | …2 remains water-cost only. Stage 2 settles if drought TDS/ion shift crosses the 3–5 g/L LCOW crossover or breaks NaCl equivalence | | | |
| 189 | 10 | Scientist 2 | EXTENDED | …Moderator: I would run Stage 1 first, as a screen then a dispatch upgrade. | | | |
| 190 | 10 | Scientist 2 | ASSUMED | …ental and served by drought-called fossil margin; stops if storage/renewables/imports set margin. Use CA and AZ as candidate BAs | | | |
| 191 | 10 | Scientist 2 | COMPUTED FROM R1,R2 | …served by drought-called fossil margin; stops if storage/renewables/imports set margin. Use CA and AZ as candidate BAs [ASSUMED] | | | |
| 192 | 10 | Scientist 2 | ASSUMED | …2021 drought generation and EFs 0.406/0.427 kg CO₂/kWh; may not transfer to actual basins. Compare the ten-plant 28.5 GWh/yr load | | | |
| 193 | 10 | Scientist 2 | EXTENDED | …ght generation and EFs 0.406/0.427 kg CO₂/kWh; may not transfer to actual basins. Compare the ten-plant 28.5 GWh/yr load [ASSUMED] | | | |
| 194 | 10 | Scientist 2 | ASSUMED | …ctual basins. Compare the ten-plant 28.5 GWh/yr load [ASSUMED][EXTENDED] with state drought generation: 13.18 TWh CA, 1.52 TWh AZ | | | |
| 195 | 10 | Scientist 2 | COMPUTED FROM R1,R2 | …ins. Compare the ten-plant 28.5 GWh/yr load [ASSUMED][EXTENDED] with state drought generation: 13.18 TWh CA, 1.52 TWh AZ [ASSUMED] | | | |
| 196 | 10 | Scientist 2 | GROUNDED | …city is not proof of marginal dispatch. Upgrade: combine my monthly AMPD plant generation/emissions and BA×fuel runoff responses | | | |
| 197 | 10 | Scientist 2 | EXTENDED | …with hourly BA fuel-generation/trade data—needed but outside my instrument—to estimate incremental fossil MWh from the load shock | | | |
| 198 | 10 | Scientist 2 | ASSUMED | …o estimate incremental fossil MWh from the load shock [EXTENDED]. Counterfactuals: grid-average, high renewables/storage, imports | | | |
| 199 | 10 | Scientist 2 | EXTENDED | …e incremental fossil MWh from the load shock [EXTENDED]. Counterfactuals: grid-average, high renewables/storage, imports [ASSUMED] | | | |
| 200 | 10 | Scientist 2 | ASSUMED | …rage, imports [ASSUMED][EXTENDED]. Settling result: positive incremental fossil generation with EF inside 0.385–0.604 kg CO₂/kWh | | | |
| 201 | 10 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …orts [ASSUMED][EXTENDED]. Settling result: positive incremental fossil generation with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED] | | | |
| 202 | 10 | Scientist 2 | GROUNDED | …lean/storage/import margin or negative response, climate coupling fails; Stage 2 remains water-cost only. CO₂-only is lower bound | | | |
| 203 | 11 | Scientist 1 | GROUNDED | …attribution screen until dispatch data exist. My knowledge base offers no basin TDS, BA boundaries, or hourly generation evidence | | | |
| 204 | 11 | Scientist 1 | ASSUMED | …ases. Candidate portfolio: ten 10,000 m³/d RO plants at 5,000 ppm, 100,000 m³/d, 28.5 GWh/yr ≈3.25 MW average, using 0.781 kWh/m³ | | | |
| 205 | 11 | Scientist 1 | EXTENDED | …didate portfolio: ten 10,000 m³/d RO plants at 5,000 ppm, 100,000 m³/d, 28.5 GWh/yr ≈3.25 MW average, using 0.781 kWh/m³ [ASSUMED] | | | |
| 206 | 11 | Scientist 1 | GROUNDED | …er to real cycling, permitting, or siting. Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L; SECs at 3k/5k ppm from R3–R6 | | | |
| 207 | 11 | Scientist 1 | COMPUTED FROM R3–R6 | …cycling, permitting, or siting. Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L; SECs at 3k/5k ppm from R3–R6 [GROUNDED] | | | |
| 208 | 11 | Scientist 1 | ASSUMED | …][COMPUTED from R3–R6]. Settling Stage 1: BA-level incremental fossil generation positive, with EF inside 0.385–0.604 kg CO₂/kWh | | | |
| 209 | 11 | Scientist 1 | COMPUTED FROM R1,R2,R9,R11,R13 | …D from R3–R6]. Settling Stage 1: BA-level incremental fossil generation positive, with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED] | | | |
| 210 | 11 | Scientist 1 | GROUNDED | …if Stage 1 passes: drought→TDS/ion mapping; it settles if feed crosses the 3–5 g/L LCOW crossover or invalidates NaCl equivalence | | | |
| 211 | 11 | Scientist 2 | GROUNDED | …rade to dispatch. My study estimates 54 BA×fuel drought responses from monthly EPA AMPD generation/emissions and runoff anomalies | | | |
| 212 | 11 | Scientist 2 | ASSUMED | …ught responses from monthly EPA AMPD generation/emissions and runoff anomalies [GROUNDED]. Use California/Arizona placeholder BAs | | | |
| 213 | 11 | Scientist 2 | COMPUTED FROM R1,R2 | …onses from monthly EPA AMPD generation/emissions and runoff anomalies [GROUNDED]. Use California/Arizona placeholder BAs [ASSUMED] | | | |
| 214 | 11 | Scientist 2 | ASSUMED | …se California/Arizona placeholder BAs [ASSUMED][COMPUTED from R1,R2]; may not transfer. Apply Scientist 1’s 28.5 GWh/yr portfolio | | | |
| 215 | 11 | Scientist 2 | EXTENDED | …rnia/Arizona placeholder BAs [ASSUMED][COMPUTED from R1,R2]; may not transfer. Apply Scientist 1’s 28.5 GWh/yr portfolio [ASSUMED] | | | |
| 216 | 11 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …; may not transfer. Apply Scientist 1’s 28.5 GWh/yr portfolio [ASSUMED][EXTENDED]; compare with EF bracket 0.385–0.604 kg CO₂/kWh | | | |
| 217 | 11 | Scientist 2 | GROUNDED | …0.385–0.604 kg CO₂/kWh [COMPUTED from R1,R2,R9,R11,R13]. Because 63% of California’s drought-generation increase is transboundary | | | |
| 218 | 11 | Scientist 2 | EXTENDED | …]. Because 63% of California’s drought-generation increase is transboundary [GROUNDED], include neighboring BAs/imports. Upgrade | | | |
| 219 | 11 | Scientist 2 | GROUNDED | …orts. Upgrade [EXTENDED] needs hourly BA fuel-generation/trade matched to AMPD; my tool is state-level attribution, not dispatch | | | |
| 220 | 11 | Scientist 2 | ASSUMED | …state-level attribution, not dispatch [GROUNDED]. Counterfactuals—grid-average, storage/renewables, imports—are assumed scenarios | | | |
| 221 | 11 | Scientist 2 | EXTENDED | …el attribution, not dispatch [GROUNDED]. Counterfactuals—grid-average, storage/renewables, imports—are assumed scenarios [ASSUMED] | | | |
| 222 | 11 | Scientist 2 | EXTENDED | …s, imports—are assumed scenarios [ASSUMED][EXTENDED]. If hourly data cannot be obtained, report only bracket, not causal dispatch | | | |
| 223 | 11 | Scientist 2 | EXTENDED | …[ASSUMED][EXTENDED]. If hourly data cannot be obtained, report only bracket, not causal dispatch [EXTENDED]. Settling criterion | | | |
| 224 | 11 | Scientist 2 | GROUNDED | …o/negative or clean/storage/import margin kills coupling. Fossil remains marginal 71% of CA hours in 2050 despite 8.6% generation | | | |
| 225 | 11 | Scientist 2 | GROUNDED | …t margin kills coupling. Fossil remains marginal 71% of CA hours in 2050 despite 8.6% generation [GROUNDED]; CO₂-only lower bound | | | |
| 226 | 12 | Scientist 1 | EXTENDED | …Moderator: yes. Plain-language plan: the hypothesis is drought may raise feed salinity | | | |
| 227 | 12 | Scientist 1 | GROUNDED | …he hypothesis is drought may raise feed salinity [EXTENDED]; stops if dilution/operations dominate. Desalination uses electricity | | | |
| 228 | 12 | Scientist 1 | ASSUMED | …s dominate. Desalination uses electricity [GROUNDED]; if new load is served by drought-called fossil margin, it can add emissions | | | |
| 229 | 12 | Scientist 1 | EXTENDED | …e. Desalination uses electricity [GROUNDED]; if new load is served by drought-called fossil margin, it can add emissions [ASSUMED] | | | |
| 230 | 12 | Scientist 1 | ASSUMED | …ds): does desalination load cause extra fossil generation? Placeholder portfolio: ten 10,000 m³/d RO plants, 28.5 GWh/yr ≈3.25 MW | | | |
| 231 | 12 | Scientist 1 | EXTENDED | …desalination load cause extra fossil generation? Placeholder portfolio: ten 10,000 m³/d RO plants, 28.5 GWh/yr ≈3.25 MW [ASSUMED] | | | |
| 232 | 12 | Scientist 1 | ASSUMED | …[ASSUMED][EXTENDED]; invented scale/constant load, may not transfer. Pass: positive fossil response, EF inside 0.385–0.604 kg/kWh | | | |
| 233 | 12 | Scientist 1 | COMPUTED FROM R1,R2,R9,R11,R13 | …[EXTENDED]; invented scale/constant load, may not transfer. Pass: positive fossil response, EF inside 0.385–0.604 kg/kWh [ASSUMED] | | | |
| 234 | 12 | Scientist 1 | GROUNDED | …rgin. Stage 2 (I lead): does drought shift feed salinity/ions enough to change cheapest technology? ED cheaper ≤3 g/L, RO ≥5 g/L | | | |
| 235 | 12 | Scientist 1 | GROUNDED | …h to change cheapest technology? ED cheaper ≤3 g/L, RO ≥5 g/L [GROUNDED]. Pass if feed crosses 3–5 g/L or breaks NaCl equivalence | | | |
| 236 | 12 | Scientist 1 | EXTENDED | …ks NaCl equivalence [GROUNDED]. Without BA dispatch, report bracket only, assuming state EFs bound BA EFs; stops if BA EF outside | | | |
| 237 | 12 | Scientist 1 | GROUNDED | …tops if BA EF outside [EXTENDED]. Impact: find basins needing clean power or different technology. My LCOW excludes brine/damages | | | |
| 238 | 12 | Scientist 2 | GROUNDED | …Moderator: plain-language plan: drought reduces hydropower, so fossil plants often fill the gap | | | |
| 239 | 12 | Scientist 2 | EXTENDED | …gap [GROUNDED]. Desalination needs electricity; if that electricity comes from drought-called fossil plants, it can add emissions | | | |
| 240 | 12 | Scientist 2 | GROUNDED | …r, storage, or imports serve it. Converged plan: Stage 1, attribution screen then dispatch test. State EFs cannot prove dispatch | | | |
| 241 | 12 | Scientist 2 | ASSUMED | …een then dispatch test. State EFs cannot prove dispatch [GROUNDED]. Choose CA/AZ placeholder BAs—CAISO/Arizona BA if names needed | | | |
| 242 | 12 | Scientist 2 | COMPUTED FROM R1,R2 | …dispatch test. State EFs cannot prove dispatch [GROUNDED]. Choose CA/AZ placeholder BAs—CAISO/Arizona BA if names needed [ASSUMED] | | | |
| 243 | 12 | Scientist 2 | GROUNDED | …lder BAs—CAISO/Arizona BA if names needed [ASSUMED][COMPUTED from R1,R2]; include imports because much CA effect is transboundary | | | |
| 244 | 12 | Scientist 2 | ASSUMED | …SSUMED][COMPUTED from R1,R2]; include imports because much CA effect is transboundary [GROUNDED]. Apply the 28.5 GWh/yr portfolio | | | |
| 245 | 12 | Scientist 2 | EXTENDED | …OMPUTED from R1,R2]; include imports because much CA effect is transboundary [GROUNDED]. Apply the 28.5 GWh/yr portfolio [ASSUMED] | | | |
| 246 | 12 | Scientist 2 | ASSUMED | …UNDED]. Apply the 28.5 GWh/yr portfolio [ASSUMED][EXTENDED]. Pass: positive fossil response with EF inside 0.385–0.604 kg CO₂/kWh | | | |
| 247 | 12 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …pply the 28.5 GWh/yr portfolio [ASSUMED][EXTENDED]. Pass: positive fossil response with EF inside 0.385–0.604 kg CO₂/kWh [ASSUMED] | | | |
| 248 | 12 | Scientist 2 | EXTENDED | …385–0.604 kg CO₂/kWh [ASSUMED][COMPUTED from R1,R2,R9,R11,R13]. Without hourly BA generation/trade plus AMPD, report bracket only | | | |
| 249 | 12 | Scientist 2 | GROUNDED | …s AMPD, report bracket only [EXTENDED]. Stage 2: drought→TDS/ion mapping; pass if feed crosses 3–5 g/L or breaks NaCl equivalence | | | |
| 250 | 12 | Scientist 2 | ASSUMED | …e [GROUNDED]. Data: my monthly AMPD/runoff/trade framework; external hourly BA generation/interchange and counterfactuals needed | | | |
| 251 | 13 | Scientist 1 | ASSUMED | …il generation. The drought→salinity premise is an assumed working scenario; it stops if dilution, operations, or ion mix dominate | | | |
| 252 | 13 | Scientist 1 | EXTENDED | …tion. The drought→salinity premise is an assumed working scenario; it stops if dilution, operations, or ion mix dominate [ASSUMED] | | | |
| 253 | 13 | Scientist 1 | GROUNDED | …ribution is the water-cost/technology side: fixed NaCl cases, 0.5 g/L product, 80% recovery; ED cheaper ≤3 g/L, RO cheaper ≥5 g/L | | | |
| 254 | 13 | Scientist 1 | COMPUTED FROM R3–R6 | …ed NaCl cases, 0.5 g/L product, 80% recovery; ED cheaper ≤3 g/L, RO cheaper ≥5 g/L [GROUNDED]. SECs at 3k/5k ppm are on the table | | | |
| 255 | 13 | Scientist 1 | GROUNDED | …eaper ≤3 g/L, RO cheaper ≥5 g/L [GROUNDED]. SECs at 3k/5k ppm are on the table [COMPUTED from R3–R6]; they are model lower bounds | | | |
| 256 | 13 | Scientist 1 | ASSUMED | …OUNDED]. The ten-plant portfolio is an assumed screening case: 100,000 m³/d, 28.5 GWh/yr, ~3.25 MW; invented and may not transfer | | | |
| 257 | 13 | Scientist 1 | EXTENDED | …The ten-plant portfolio is an assumed screening case: 100,000 m³/d, 28.5 GWh/yr, ~3.25 MW; invented and may not transfer [ASSUMED] | | | |
| 258 | 13 | Scientist 1 | EXTENDED | …placeholders. Without BA-level dispatch and import accounting, we should report an emissions bracket, not causal fossil dispatch | | | |
| 259 | 13 | Scientist 1 | GROUNDED | …ossil dispatch [EXTENDED]. Stage 2 settles if drought TDS/ion shift crosses the 3–5 g/L LCOW crossover or breaks NaCl equivalence | | | |
| 260 | 13 | Scientist 2 | GROUNDED | …Moderator: I confirm. Big picture: drought cuts hydropower and fossil plants often fill the gap | | | |
| 261 | 13 | Scientist 2 | EXTENDED | …lination uses electricity; if its new load is served by that drought-called fossil margin, it can add CO₂ and air-quality damages | | | |
| 262 | 13 | Scientist 2 | ASSUMED | …authorities, with NV optional, as placeholders from positive state EFs R1/R2/R9; they may not transfer to actual basins/dispatch | | | |
| 263 | 13 | Scientist 2 | ASSUMED | …l basins/dispatch [ASSUMED]. Apply Scientist 1’s assumed 28.5 GWh/yr portfolio; invented ten-plant constant load may not transfer | | | |
| 264 | 13 | Scientist 2 | EXTENDED | …dispatch [ASSUMED]. Apply Scientist 1’s assumed 28.5 GWh/yr portfolio; invented ten-plant constant load may not transfer [ASSUMED] | | | |
| 265 | 13 | Scientist 2 | GROUNDED | …portfolio; invented ten-plant constant load may not transfer [ASSUMED][EXTENDED]. Use my monthly AMPD/runoff BA×fuel attribution | | | |
| 266 | 13 | Scientist 2 | EXTENDED | …. Use my monthly AMPD/runoff BA×fuel attribution [GROUNDED]; upgrade with external hourly BA generation/trade and counterfactuals | | | |
| 267 | 13 | Scientist 2 | ASSUMED | …ly BA generation/trade and counterfactuals [EXTENDED]. Until then report only bracket 0.385–0.604 kg CO₂/kWh, not causal dispatch | | | |
| 268 | 13 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …eration/trade and counterfactuals [EXTENDED]. Until then report only bracket 0.385–0.604 kg CO₂/kWh, not causal dispatch [ASSUMED] | | | |
| 269 | 13 | Scientist 2 | GROUNDED | …ve fossil response with EF in bracket; fail: clean/storage/import margin. Include imports because much CA effect is transboundary | | | |
| 270 | 13 | Scientist 2 | GROUNDED | …t; fail: clean/storage/import margin. Include imports because much CA effect is transboundary [GROUNDED]. CO₂-only is lower bound | | | |
| 271 | 14 | Scientist 1 | GROUNDED | …y deliverables: 1. Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L under fixed NaCl feed, 0.5 g/L product, 80% recovery | | | |
| 272 | 14 | Scientist 1 | COMPUTED FROM R3–R6 | …Cl feed, 0.5 g/L product, 80% recovery [GROUNDED]. 2. SEC inputs: 3k ppm RO 0.555 / ED 0.762; 5k ppm RO 0.781 / ED 1.251 kWh/m³ | | | |
| 273 | 14 | Scientist 1 | GROUNDED | …/ ED 0.762; 5k ppm RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; these are cost-optimal model outputs, not plant measurements | | | |
| 274 | 14 | Scientist 1 | GROUNDED | …ts [GROUNDED]. 3. Stage-2 pass/fail: drought TDS/ion shift must cross the 3–5 g/L LCOW crossover or invalidate NaCl equivalence | | | |
| 275 | 14 | Scientist 1 | GROUNDED | …ver or invalidate NaCl equivalence [GROUNDED]. My knowledge base offers no evidence on basin TDS, BA dispatch, brine, or damages | | | |
| 276 | 14 | Scientist 1 | ASSUMED | …t portfolio—100,000 m³/d, 28.5 GWh/yr, ~3.25 MW—is an assumed screening construct; invented scale/constant load, may not transfer | | | |
| 277 | 14 | Scientist 1 | EXTENDED | …io—100,000 m³/d, 28.5 GWh/yr, ~3.25 MW—is an assumed screening construct; invented scale/constant load, may not transfer [ASSUMED] | | | |
| 278 | 14 | Scientist 1 | ASSUMED | …n assumed screening construct; invented scale/constant load, may not transfer [ASSUMED][EXTENDED]. CA/AZ remain placeholders only | | | |
| 279 | 14 | Scientist 1 | EXTENDED | …to hourly BA generation/trade, AMPD emissions, and counterfactuals. Until then, report an emissions bracket, not causal dispatch | | | |
| 280 | 14 | Scientist 2 | ASSUMED | …desalination electricity is served by that fossil margin, it adds emissions. Stage 1: use California and Arizona placeholder BAs | | | |
| 281 | 14 | Scientist 2 | COMPUTED FROM R1,R2 | …ion electricity is served by that fossil margin, it adds emissions. Stage 1: use California and Arizona placeholder BAs [ASSUMED] | | | |
| 282 | 14 | Scientist 2 | ASSUMED | …chose them from positive 2021 state EFs, and they may not transfer to actual basins or dispatch. Apply the 28.5 GWh/yr portfolio | | | |
| 283 | 14 | Scientist 2 | EXTENDED | …em from positive 2021 state EFs, and they may not transfer to actual basins or dispatch. Apply the 28.5 GWh/yr portfolio [ASSUMED] | | | |
| 284 | 14 | Scientist 2 | ASSUMED | …t only the bracket 0.385–0.604 kg CO₂/kWh, not causal dispatch; assumption is state EFs bound BA EFs, stops if BA EF lies outside | | | |
| 285 | 14 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …e bracket 0.385–0.604 kg CO₂/kWh, not causal dispatch; assumption is state EFs bound BA EFs, stops if BA EF lies outside [ASSUMED] | | | |
| 286 | 14 | Scientist 2 | GROUNDED | …UTED from R1,R2,R9,R11,R13]. My side supplies monthly AMPD plant generation/emissions and the BA×fuel drought-response framework | | | |
| 287 | 14 | Scientist 2 | GROUNDED | …neration/emissions and the BA×fuel drought-response framework [GROUNDED]; my tool is state-level attribution, not hourly dispatch | | | |
| 288 | 14 | Scientist 2 | GROUNDED | …terchange and counterfactuals; my knowledge base cannot supply them. Include imports because California effects are transboundary | | | |
| 289 | 14 | Scientist 2 | EXTENDED | …nclude imports because California effects are transboundary [GROUNDED]. Pass: positive incremental fossil response within bracket | | | |
| 290 | 15 | Scientist 1 | GROUNDED | …ions, so I can define the test and run the desalination model, but the basin water-quality data must come from outside both of us | | | |
| 291 | 15 | Scientist 1 | GROUNDED | …DED]. My commitments: 1. Technology screen: ED cheaper ≤3 g/L, RO cheaper ≥5 g/L; fixed NaCl feed, 0.5 g/L product, 80% recovery | | | |
| 292 | 15 | Scientist 1 | COMPUTED FROM R3–R6 | …NaCl feed, 0.5 g/L product, 80% recovery [GROUNDED]. 2. SEC inputs: 3k ppm RO 0.555 / ED 0.762; 5k ppm RO 0.781 / ED 1.251 kWh/m³ | | | |
| 293 | 15 | Scientist 1 | GROUNDED | …. SEC inputs: 3k ppm RO 0.555 / ED 0.762; 5k ppm RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds, not plants | | | |
| 294 | 15 | Scientist 1 | GROUNDED | …drought-season TDS/ion shift must cross the 3–5 g/L LCOW crossover or invalidate NaCl equivalence; otherwise no technology change | | | |
| 295 | 15 | Scientist 1 | ASSUMED | …ange [GROUNDED]. If no basin records are obtainable, fallback: report the assumed 3k→5k ppm scenario as sensitivity, not finding | | | |
| 296 | 15 | Scientist 1 | EXTENDED | …UNDED]. If no basin records are obtainable, fallback: report the assumed 3k→5k ppm scenario as sensitivity, not finding [ASSUMED] | | | |
| 297 | 15 | Scientist 1 | EXTENDED | …y BA generation/trade, AMPD emissions, and basin TDS/ion records with drought index. Until then, bracket only, no causal dispatch | | | |
| 298 | 15 | Scientist 2 | ASSUMED | …Scientist 1, your fallback is right. Moderator: I confirm CA/AZ only as placeholder screening regions, not confirmed BAs | | | |
| 299 | 15 | Scientist 2 | COMPUTED FROM R1,R2 | …Scientist 1, your fallback is right. Moderator: I confirm CA/AZ only as placeholder screening regions, not confirmed BAs [ASSUMED] | | | |
| 300 | 15 | Scientist 2 | GROUNDED | …, not load dispatch. Include neighboring BAs/imports because 63% of California’s drought-induced fossil increase is transboundary | | | |
| 301 | 15 | Scientist 2 | GROUNDED | …ansboundary [GROUNDED]. Data path: my side supplies monthly AMPD generation/emissions, runoff anomalies, and BA×fuel attribution | | | |
| 302 | 15 | Scientist 2 | GROUNDED | …nal hourly BA generation/interchange/fuel mix and basin TDS/ion records; my knowledge base offers no basin water-quality evidence | | | |
| 303 | 15 | Scientist 2 | ASSUMED | …ROUNDED]. Until then, report only EF bracket 0.385–0.604 kg CO₂/kWh, assuming state EFs bound BA EFs; stops if BA EF lies outside | | | |
| 304 | 15 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …Until then, report only EF bracket 0.385–0.604 kg CO₂/kWh, assuming state EFs bound BA EFs; stops if BA EF lies outside [ASSUMED] | | | |
| 305 | 15 | Scientist 2 | EXTENDED | …[COMPUTED from R1,R2,R9,R11,R13]. Pass: positive incremental fossil generation within bracket; fail: clean/storage/import margin | | | |
| 306 | 15 | Scientist 2 | GROUNDED | …generation within bracket; fail: clean/storage/import margin [EXTENDED]. CO₂-only is lower bound; methane/PM₂.₅ damages excluded | | | |
| 307 | 16 | Scientist 1 | ASSUMED | …Moderator: I confirm the summary and the plan. Stage 1 remains Scientist 2’s attribution screen: CA/AZ are placeholder BAs only | | | |
| 308 | 16 | Scientist 1 | COMPUTED FROM R1,R2 | …or: I confirm the summary and the plan. Stage 1 remains Scientist 2’s attribution screen: CA/AZ are placeholder BAs only [ASSUMED] | | | |
| 309 | 16 | Scientist 1 | ASSUMED | …D from R1,R2]; the ten-plant portfolio—100,000 m³/d, 28.5 GWh/yr, ~3.25 MW—is an assumed screening construct and may not transfer | | | |
| 310 | 16 | Scientist 1 | EXTENDED | …,R2]; the ten-plant portfolio—100,000 m³/d, 28.5 GWh/yr, ~3.25 MW—is an assumed screening construct and may not transfer [ASSUMED] | | | |
| 311 | 16 | Scientist 1 | EXTENDED | …DED]. Until hourly BA generation/trade, AMPD, imports, and counterfactuals exist, report only the EF bracket, not causal dispatch | | | |
| 312 | 16 | Scientist 1 | GROUNDED | …fixed boundary is NaCl-equivalent feed, 0.5 g/L product, 80% recovery; LCOW crossover is ED cheaper ≤3 g/L and RO cheaper ≥5 g/L | | | |
| 313 | 16 | Scientist 1 | COMPUTED FROM R3–R6 | …eaper ≤3 g/L and RO cheaper ≥5 g/L [GROUNDED]. SEC inputs remain 3k ppm RO 0.555 / ED 0.762 and 5k ppm RO 0.781 / ED 1.251 kWh/m³ | | | |
| 314 | 16 | Scientist 1 | GROUNDED | …nputs remain 3k ppm RO 0.555 / ED 0.762 and 5k ppm RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; these are model lower bounds | | | |
| 315 | 16 | Scientist 1 | GROUNDED | …D 1.251 kWh/m³ [COMPUTED from R3–R6]; these are model lower bounds [GROUNDED]. My knowledge base offers no basin TDS/ion records | | | |
| 316 | 16 | Scientist 1 | ASSUMED | …D]. My knowledge base offers no basin TDS/ion records [GROUNDED]. Fallback if none are obtained: test an assumed 3k→5k ppm shift | | | |
| 317 | 16 | Scientist 1 | EXTENDED | …nowledge base offers no basin TDS/ion records [GROUNDED]. Fallback if none are obtained: test an assumed 3k→5k ppm shift [ASSUMED] | | | |
| 318 | 16 | Scientist 2 | ASSUMED | …Moderator: I confirm. Stage 1 is an attribution screen, not dispatch proof. Use CA/AZ as placeholder screening regions | | | |
| 319 | 16 | Scientist 2 | COMPUTED FROM R1,R2 | …Moderator: I confirm. Stage 1 is an attribution screen, not dispatch proof. Use CA/AZ as placeholder screening regions [ASSUMED] | | | |
| 320 | 16 | Scientist 2 | ASSUMED | …021 state EFs/generation; it may not transfer to actual basin dispatch. Apply Scientist 1’s assumed ten-plant load of 28.5 GWh/yr | | | |
| 321 | 16 | Scientist 2 | EXTENDED | …EFs/generation; it may not transfer to actual basin dispatch. Apply Scientist 1’s assumed ten-plant load of 28.5 GWh/yr [ASSUMED] | | | |
| 322 | 16 | Scientist 2 | ASSUMED | …A generation/trade, fuel mix, AMPD emissions, and counterfactuals are obtained, report only the EF bracket 0.385–0.604 kg CO₂/kWh | | | |
| 323 | 16 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …ion/trade, fuel mix, AMPD emissions, and counterfactuals are obtained, report only the EF bracket 0.385–0.604 kg CO₂/kWh [ASSUMED] | | | |
| 324 | 16 | Scientist 2 | GROUNDED | …s if a BA-specific EF lies outside. Include imports because much of California’s drought-induced fossil increase is transboundary | | | |
| 325 | 16 | Scientist 2 | EXTENDED | …is transboundary [GROUNDED]. Pass: positive incremental fossil generation within the bracket. Fail: clean/storage/import margin | | | |
| 326 | 16 | Scientist 2 | GROUNDED | …thin the bracket. Fail: clean/storage/import margin [EXTENDED]. CO₂-only is a lower bound; methane and PM₂.₅ damages are excluded | | | |
| 327 | 17 | Scientist 1 | ASSUMED | …confirm the converged plan from the water side. CA/AZ are acceptable only as placeholder screening regions, not validated basins | | | |
| 328 | 17 | Scientist 1 | COMPUTED FROM R1,R2 | …the converged plan from the water side. CA/AZ are acceptable only as placeholder screening regions, not validated basins [ASSUMED] | | | |
| 329 | 17 | Scientist 1 | GROUNDED | …lead, needs external basin TDS/ion records paired with a drought index. My model can test those scenarios but cannot supply them | | | |
| 330 | 17 | Scientist 1 | GROUNDED | …/fail: drought shifts feed across the 3–5 g/L LCOW crossover—ED cheaper ≤3 g/L, RO cheaper ≥5 g/L—or invalidates NaCl equivalence | | | |
| 331 | 17 | Scientist 1 | ASSUMED | …L—or invalidates NaCl equivalence [GROUNDED]. If no records are obtainable, fallback is an assumed 3,000→5,000 ppm drought shift | | | |
| 332 | 17 | Scientist 1 | EXTENDED | …lidates NaCl equivalence [GROUNDED]. If no records are obtainable, fallback is an assumed 3,000→5,000 ppm drought shift [ASSUMED] | | | |
| 333 | 17 | Scientist 1 | COMPUTED FROM R3–R6 | …y not transfer if ion mix, scaling, or brine dominate. SEC inputs remain 3k RO 0.555 / ED 0.762 and 5k RO 0.781 / ED 1.251 kWh/m³ | | | |
| 334 | 17 | Scientist 1 | GROUNDED | …ne dominate. SEC inputs remain 3k RO 0.555 / ED 0.762 and 5k RO 0.781 / ED 1.251 kWh/m³ [COMPUTED from R3–R6]; model lower bounds | | | |
| 335 | 17 | Scientist 1 | EXTENDED | …ly BA generation/trade, AMPD emissions, counterfactuals, and basin TDS/ion records. Until then, bracket only, not causal dispatch | | | |
| 336 | 17 | Scientist 2 | GROUNDED | …Moderator: confirmed. Plain language: drought cuts hydro; fossil plants often compensate | | | |
| 337 | 17 | Scientist 2 | EXTENDED | …en compensate [GROUNDED]. Desalination uses power; climate harm occurs only if new load is served by drought-called fossil plants | | | |
| 338 | 17 | Scientist 2 | ASSUMED | …erwise. Stage 1: screen using placeholder CA/AZ—chosen from positive R1/R2 state EFs, may not transfer to actual basins/dispatch | | | |
| 339 | 17 | Scientist 2 | COMPUTED FROM R1,R2 | …Stage 1: screen using placeholder CA/AZ—chosen from positive R1/R2 state EFs, may not transfer to actual basins/dispatch [ASSUMED] | | | |
| 340 | 17 | Scientist 2 | ASSUMED | …ASSUMED][COMPUTED from R1,R2]—and Scientist 1’s assumed 28.5 GWh/yr ten-plant portfolio, invented constant load, may not transfer | | | |
| 341 | 17 | Scientist 2 | EXTENDED | …COMPUTED from R1,R2]—and Scientist 1’s assumed 28.5 GWh/yr ten-plant portfolio, invented constant load, may not transfer [ASSUMED] | | | |
| 342 | 17 | Scientist 2 | ASSUMED | …generation/trade, AMPD, imports, counterfactuals, and basin TDS/ion records exist, report only EF bracket 0.385–0.604 kg CO₂/kWh | | | |
| 343 | 17 | Scientist 2 | COMPUTED FROM R1,R2,R9,R11,R13 | …on/trade, AMPD, imports, counterfactuals, and basin TDS/ion records exist, report only EF bracket 0.385–0.604 kg CO₂/kWh [ASSUMED] | | | |
| 344 | 17 | Scientist 2 | GROUNDED | …umption: state EFs bound BA EFs, stops if BA EF outside. Include imports because much CA drought-fossil response is transboundary | | | |
| 345 | 17 | Scientist 2 | EXTENDED | …ponse is transboundary [GROUNDED]. Pass: positive incremental fossil generation within bracket; fail: clean/storage/import margin | | | |
| 346 | 17 | Scientist 2 | ASSUMED | …in [EXTENDED]. Stage 2: Scientist 1 tests drought→TDS/ion scenarios; fallback assumed salinity shift is sensitivity, not finding | | | |
| 347 | 17 | Scientist 2 | EXTENDED | …DED]. Stage 2: Scientist 1 tests drought→TDS/ion scenarios; fallback assumed salinity shift is sensitivity, not finding [ASSUMED] | | | |
| 348 | 17 | Scientist 2 | GROUNDED | …fallback assumed salinity shift is sensitivity, not finding [ASSUMED][EXTENDED]. CO₂-only is lower bound; methane/PM₂.₅ excluded | | | |

## Appendix: tool cards

### Scientist 1

```
NAME: sec_bw
PURPOSE: Specific energy consumption of brackish water desalination, RO vs ED
PARAMETERS:
  - feed_ppm (number, required) — feed total dissolved solids as a single NaCl-equivalent number; the source models a binary salt solution and carries no ionic composition, so it cannot distinguish soft NaCl groundwater from hard, sulphate-rich groundwater of the same TDS, although ED energy in particular depends on which ions are moved [ppm TDS]
  - technology (string, required) — technology class, at the source's 'current state-of-the-art' cost and performance assumptions (ion-exchange membranes 100 USD/m2 for ED, RO membranes 30 USD/m2); not a specific plant or vendor [-]
RETURNS:
  - sec_kwh_per_m3 [kWh/m3] — whole-process electrical energy for the modelled system at its cost-optimal productivity, per cubic metre of PRODUCT water (not feed); a technology-class figure, not a plant measurement
CONDITIONS: Brackish water only, 1000-10000 ppm feed TDS (the source's 1-10 g/L), and the tool refuses outside that range. THREE OPERATING VARIABLES ARE FIXED AND ARE NOT PARAMETERS: product water salinity 0.5 g/L (500 ppm), water recovery 80%, and productivity set to the value that MINIMISES THE LEVELISED COST OF WATER at each feed salinity -- cost-optimal, not energy-optimal, so this is not the lowest energy the technology could reach. Because the product spec is fixed at 500 ppm, the energy scales with the salt actually removed, which is why ED at 1000 ppm is so small: only 500 ppm of salt is being moved. Changing the product specification invalidates every number here. For RO an energy recovery device is applied at every feed salinity EXCEPT 1000 ppm, so the RO curve has a discontinuity in its assumptions at its own left endpoint. THESE ARE PROCESS-MODEL OUTPUTS, NOT OPERATING PLANTS. Real plants are not sized at cost-optimal productivity and do not achieve modelled performance, so treat these as a lower bound on what an actual installation consumes. COMPARED WITH PUBLISHED PRACTICE THESE NUMBERS RUN LOW. An empirical trend fitted to the 16 electrodialysis entries of Table S1 of Shah et al., Desalination 538 (2022) 115827 -- real and laboratory studies rather than a model -- agrees with the ED curve here to within 3% at 10000 ppm, but is 5 times higher at 1000 ppm and 25-80% higher over 2000-5000 ppm, the range in which inland brackish groundwater usually sits. That is the gap between a modelled optimum and what has actually been reported, and it must be carried alongside any number taken from here. The five feed salinities 1000, 3000, 5000, 7000 and 10000 ppm are the only ones the source computed; everything between them is linear interpolation performed by this tool. Values were read off a printed figure: the vertical axis resolves to 0.0094 kWh/m3 per pixel, so roughly +/-0.02 kWh/m3, which is negligible except at the ED 1000 ppm point where it is about +/-22%. The source's third curve, 'optimized ED', assumes ion-exchange membranes fall to 30 USD/m2 with improved charge density and diffusion coefficient; it is a hypothetical future case and is deliberately not served by this tool. Concentrate disposal, pretreatment and inland brine handling are outside the modelled boundary. THE SOURCE STATES SALINITY IN g/L AND THIS TOOL TAKES ppm: the conversion 1 g/L = 1000 ppm assumes a solution density of 1 kg/L. Over this range the true density reaches about 1.007 kg/L, so ppm is understated by at most 0.7% -- negligible against the digitisation error, but an assumption rather than an identity.
SOURCE: not stated
EXAMPLE: @tool: {"feed_ppm":{"v":5000,"src":"source"},"technology":{"v":"RO","src":"source"}}
```
(script: sec_bw.py)

### Scientist 2

```
NAME: drought_ef
PURPOSE: Carbon intensity of drought-induced fossil generation, by western US state, 2021
PARAMETERS:
  - state (string, required) — US state postal code, and it is the state where the GENERATING UNIT sits, not where the drought occurred. The source finds that over half of drought-induced generation is transboundary -- 63% of California's increase is caused by drought in neighbouring regions -- so this is the location of the emissions, not of the shortage. [-]
RETURNS:
  - ef_kg_co2_per_kwh [kg CO2/kWh] — state aggregate for calendar 2021, combustion CO2 only, over the fossil units that respond to runoff anomalies; a weighted mean of those units' own observed emission rates, weighted by how strongly each responds
  - drought_generation_MWh [MWh] — state aggregate for calendar 2021; the fossil generation attributable to runoff anomalies in all three electricity regions, summed over unit-months
CONDITIONS: WESTERN INTERCONNECTION ONLY (the source's CA, NW and SW regions), CALENDAR 2021 ONLY, and the tool refuses outside both. 2021 was a severe western drought year, which is why it was chosen: in wet years the attributed generation is negative and no intensity exists. THE YEAR IS NOT INTERCHANGEABLE -- recomputing the same quantity for 2001 gives 0.69 in AZ against 0.43 in 2021, a 25-43% decline across states over two decades as the fossil fleet turned over, so a number from here is about the 2021 grid and no other. COMBUSTION CO2 ONLY. Upstream methane is omitted by choice, although the source's data would support it, because including it forces a 20-vs-100-year GWP decision; PM2.5 mortality cannot be computed at all, because the step from concentration to deaths is not in the source's public code. Any total built on this is therefore a LOWER BOUND, and gas-heavy fleets understate most. THE RATIO IS OUR DERIVATION. Qiu et al. report drought-induced generation and drought-induced emissions; they do not divide one by the other, and no emission factor appears in that paper. The division is dimensionally sound and uses only their own outputs, but it is ours. THE INTENSITY IS AN ATTRIBUTION, NOT A PREDICTION FOR NEW LOAD. It answers 'the fossil generation that drought called up carried this much CO2 per kWh'. Using it for a new drought-driven load -- desalination, for instance -- assumes that load is served in the same proportion as the fleet already responds to drought, which is a stateable assumption and is not something the source tested. The source did test whether drought raises electricity DEMAND and found no empirical relationship, in a period when inland desalination was negligible; that is a null for a channel that did not then exist, not a refutation of one that might. NO UNCERTAINTY INTERVAL. The source's regressions are bootstrapped 500 times, but its attribution script collapses those draws to their median before applying them, so the number here is a point estimate and no interval is propagated. TWO GUARDS ARE ENFORCED. A state whose drought-attributed generation is negative is refused, and a state whose computed intensity falls outside the range of its own units' observed emission rates is refused: the intensity is a weighted mean of those rates, so a coherent response must land between the cleanest and dirtiest unit, and landing outside means opposing responses dominated the sum. Both are physical tests, not tuned thresholds. States with fewer than three sampled plants are refused as too thin to be a grid margin. SAMPLE. EPA Air Markets units above 25 MW nameplate with at least four non-missing values in a month, 90% of fossil generation and 49% of total generation in the eleven western states; hydro, wind, solar and nuclear are not in it, so the fleet totals here are FOSSIL totals and must never be read as grid averages. Eleven of 681 units in the source carry pooled rather than BA-fuel coefficients because the BA-fuel estimates would have exceeded their total generation; two of those pairs are in Nevada and Washington.
SOURCE: not stated
EXAMPLE: @tool: {"state":{"v":"AZ","src":"source"}}
```
(script: drought_ef.py)

## Appendix: seat configuration

Everything needed to rebuild these seats on a blank page, except the API slots,
which live in `api.json` and are never written into an export.

### Scientist 1

- field: desalination
- model: qwen3.8-max
- tool: sec_bw (from tools/)
- runtime: python
- knowledge base: 18158 chars

<!--kb:start-->
# The Potential of Electrodialysis as a Cost-Effective Alternative to Reverse Osmosis for Brackish Water Desalination (Condensed)

**Source:** Sohum K. Patel, Boreum Lee, Paul Westerhoff, Menachem Elimelech. *Water Research* 250 (2024) 121009. DOI: [10.1016/j.watres.2023.121009](https://doi.org/10.1016/j.watres.2023.121009)
S.K. Patel and B. Lee contributed equally. Corresponding author: menachem.elimelech@yale.edu

> **What was cut from this version**
> - **§2.2–2.3 model mechanics:** the 2-D Nernst-Planck / Sonin-Probstein formulation, the stack symmetry argument, feed-and-bleed derivation, and the RO 1-D pressure-driven model. Only the modeling assumptions needed to read the numbers are kept (§2 below).
> - **Pre/post-treatment discussion** compressed to the caveat that matters.
> - Figure captions, appendix figures/tables (A1–A9), and the reference list. Author-year citations in the original are dropped.
>
> Every quantitative result from the Results section is retained.

---

## Abstract

While electrodialysis (ED) demonstrates lower energy consumption than reverse osmosis (RO) in the desalination of low salinity waters, RO continues to be the predominant technology for brackish water desalination. This study probes this skewed market share and projects the potential for future disruption by ED through systematic assessment of the levelized cost of water (LCOW). Using rigorous process- and economic-models, the LCOW of RO and ED systems is minimized, highlighting tradeoffs between capital and operating expenditure for each technology. With optimized current state-of-the-art systems, ED is more economical than RO for feed salinities ≤ 3 g L⁻¹, albeit to a minor extent. Reduction in the price of ion-exchange membranes (< 60 USD m⁻²) can ensure competitiveness with RO for feed salinities up to 5 g L⁻¹. For higher feed salinities (≥ 5 g L⁻¹) the LCOW of ED may effectively be reduced by decreasing ion-exchange membrane resistance while preserving high current efficiency. Through assessment of structure-property-performance relationships, target membrane charge densities and diffusion coefficients that optimize the LCOW of ED are identified, providing guidance for future membrane material development. With a unified approach — whereby ion-exchange membrane price is reduced *and* performance is enhanced — ED can become the economically preferable technology compared to RO across the entire brackish water salinity range.

**Keywords:** Desalination; Brackish water; Levelized cost of water; Ion-exchange membrane; Charge density

---

## 1. Framing

Brackish water (≈1–10 g L⁻¹) is less energy-intensive to desalinate than seawater (~35 g L⁻¹), permits higher water recovery and therefore less brine, and enables inland desalination. **RO commands over 80% of brackish water desalination capacity; ED accounts for under 10%** — despite ED being a commercially mature technology and despite the authors' earlier work showing ED to be more *energetically* favorable at low brackish salinities and high water recovery.

The gap between that thermodynamic result and actual market share is the paper's subject. Prior technoeconomic ED–RO comparisons either did not emphasize the brackish range, or used semi-empirical ED models that prescribe fixed current efficiency and membrane resistance — thereby overlooking concentration polarization and co-ion leakage, and making it impossible to trace how membrane physicochemical properties propagate into cost. This study combines mechanistic process modeling with process economics to (i) benchmark current LCOW of cost-optimized ED and RO systems, (ii) evaluate membrane price reduction and membrane property improvement as separate cost-reduction routes, and (iii) test whether combining them lets ED beat RO across the whole brackish range.

---

## 2. Model setup — what is held fixed

**Separation parameters** (identical for both technologies, so the thermodynamic minimum energy is the same):

| Parameter | Value |
|---|---|
| Feed salinity | 1, 3, 5, 7, 10 g L⁻¹ |
| Product water salinity | 0.5 g L⁻¹ (US EPA drinking water standard) |
| Water recovery | 80% |
| Water production rate, *Q*_P | 10,000 m³ d⁻¹ (moderate-scale plant) |
| Feedwater composition | pure NaCl solution (both models) |

**Productivity, Γ** (water production rate per projected membrane area, L m⁻² h⁻¹) is *not* held equal — it sets the effective system size and is optimized independently for each technology at each salinity, so that cost-minimized systems are compared. Range scanned: 10–100 L m⁻² h⁻¹.

**ED model:** 2-D Nernst-Planck applied to both spacer channels and ion-exchange membranes, so **current efficiency and membrane resistance are model outputs, not prescribed inputs**. This is what enables the structure-property-performance analysis. Inputs: number of cell pairs, spacer thickness (0.3 mm baseline, already at the low end of commercial stacks), membrane charge density, membrane thickness (130 µm baseline), ion diffusion coefficients. Equal flowrates in adjacent channels fix module-scale recovery at 50%; a **feed-and-bleed** scheme recycles part of the concentrate into the concentrate-channel feed to reach 80% system-scale recovery.

**RO model:** 1-D, pressure-driven, *J*_w = *A*(Δ*P* − σΔπ), with complete salt rejection assumed (σ = 1). Because RO salt removal is not tunable by pressure, a **bypass system** blends part of the raw feed with the permeate to hit the 0.5 g L⁻¹ target — which is why complete rejection is a safe assumption here. *A* = 5 L m⁻² h⁻¹ bar⁻¹, mass transfer coefficient 150 L m⁻² h⁻¹, pump efficiency 0.8, energy recovery device (ERD) efficiency 0.9.

**Economics:** LCOW = annualized CAPEX + OPEX, over the desalination step only.

- **OPEX (common to both):** electricity, membrane replacement, labor, O&M, CO₂ tax.
- **CAPEX (technology-specific):** ED = ion-exchange membranes + electrodes; RO = membrane + high-pressure pump + ERD. Membrane price refers to an assembled module (gaskets, spacers, housing included).
- Baseline membrane prices: **ED 100 USD m⁻², RO 30 USD m⁻²**.

> **Caveat the authors flag explicitly:** pre- and post-treatment are excluded. ED (with polarity reversal) handles fouling/scaling-prone feeds better — notably dissolved silica, which is uncharged and so is a non-issue for ED but plagues RO — and ion-exchange membranes tolerate free chlorine, so ED needs less pretreatment. RO, conversely, removes uncharged micropollutants, viruses, and micro-organisms, whereas ED removes only ionic species and would need downstream polishing. These advantages are *assumed to cancel*. In practice, the extent and complexity of pre/post-treatment may be the determining factor for technology choice, **outweighing the LCOW difference computed here.**

---

## 3. Results

### 3.1 Optimal productivity: ED is far more salinity-sensitive than RO

Productivity drives both cost buckets in opposite directions: higher Γ means a larger driving force (higher OPEX) but less membrane area (lower CAPEX).

- At **1 g L⁻¹**, LCOW for *both* technologies is minimized at the maximum Γ (100 L m⁻² h⁻¹) — energy is cheap at this salinity, so LCOW is CAPEX-dominated and the smallest system wins.
- Above 1 g L⁻¹, energy cost grows and Γ_opt falls. **ED falls much faster:** Γ_opt drops from 100 to 54 L m⁻² h⁻¹ going from 1 to 3 g L⁻¹, then a further **63% drop** from 3 to 10 g L⁻¹. RO's lowest Γ_opt is 60 L m⁻² h⁻¹ (at 7 g L⁻¹).

Three mechanisms explain ED's sensitivity, all absent or milder in RO:

1. **More salt to move.** ED energy scales with ions transported, so higher feed salinity at fixed product quality directly means larger currents and potentials.
2. **Selectivity collapse under gradient.** Larger transmembrane concentration gradients magnify back-diffusion and co-ion flux; overcoming this parasitic transport needs still higher applied potential. RO's salt rejection, by contrast, is essentially unaffected.
3. **Concentration polarization hurts ED more.** In ED it depletes salt at the diluate-side membrane surface, raising the diluate channel's solution resistance and the Donnan potential drop — rising steeply as the limiting current density is approached (the model fails to converge at that point, which is why ED LCOW curves terminate). In RO, polarization only raises the osmotic pressure at the surface, requiring more hydraulic pressure but incurring no analogous loss.

An asymptotic gain in current efficiency with increasing Γ exists (electromigration outrunning back-diffusion) but is too small to offset the extra voltage; cell pair voltage and SEC rise monotonically with Γ at all salinities.

**Energy recovery in brackish RO is a minor effect** — unlike in seawater RO. ERD reduces LCOW only for feeds ≥ 3 g L⁻¹, and becomes notable only at ≥ 7 g L⁻¹. At 1 g L⁻¹ the ERD's capital cost exceeds its energy savings, so ERD is applied only at ≥ 3 g L⁻¹ thereafter.

### 3.2 Current benchmark: the crossover sits at 3–5 g L⁻¹

**ED is cheaper up to 3 g L⁻¹; RO is cheaper at ≥ 5 g L⁻¹**, and the gap widens sharply above 5 g L⁻¹.

| | ED advantage | RO advantage |
|---|---|---|
| Largest margin | **0.04 USD m⁻³** at 1 g L⁻¹ | **0.21 USD m⁻³** at 10 g L⁻¹ |

The asymmetry matters: because ED's edge at low salinity is small, technology choice there may reasonably be driven by non-cost factors (ease of operation, environmental impact), whereas at high salinity cost decides, and it decides for RO.

**Cost breakdown:**

- **At low salinity**, LCOW is dominated by labor (fixed by plant capacity) and membrane-related costs. ED membranes cost more up front, but RO membranes are replaced more often due to shorter lifespan — so **total membrane-related cost is nearly equal at ≤ 3 g L⁻¹**. The difference therefore comes from elsewhere: at 1 g L⁻¹ ED simply uses less energy (lower electricity + carbon tax); at 3 g L⁻¹ **RO actually has the lower energy consumption, yet ED still wins on LCOW** because the RO high-pressure pump costs far more than the ED electrodes.
- **At ≥ 5 g L⁻¹**, electricity takes over — **33% of ED's LCOW at 10 g L⁻¹**. Membrane capital cost grows for both (falling Γ_opt = more area), more steeply for ED. RO's resulting advantage is partly offset by pump cost, since higher feed salinity means a larger fraction of feed must pass through the RO module rather than bypass it. ED electrode cost stays negligible throughout.
- **Carbon tax** becomes sizeable at high salinity and hits ED harder (it scales with electricity use). But removing it entirely does not flip the winner at any salinity. Likewise, ±50% variation in the RO pump cost correlation does not change which technology wins — except at 3 g L⁻¹, where the two are nearly tied anyway.

**SEC is a poor proxy for LCOW at low salinity.** Going 1 → 3 g L⁻¹, ED's SEC rises 672% but its LCOW rises only 105%. At 3 g L⁻¹ the two metrics disagree outright: RO has lower SEC, ED has lower LCOW. At ≥ 5 g L⁻¹, where electricity is the dominant differentiator, SEC becomes an acceptable substitute.

### 3.3 Route 1 — cheaper ion-exchange membranes

RO polyamide TFC membrane pricing is mature (assessed range 5–30 USD m⁻²; 30 is the high end of current prices, 10 the low end). Ion-exchange membranes are immature — few large-scale manufacturers, little competition — so prices should fall; the study scans down to 10 USD m⁻², an order of magnitude below typical reported values.

Breakeven ion-exchange membrane price, as a function of RO membrane price:

| Feed salinity | vs. RO at 30 USD m⁻² | vs. RO at 10 USD m⁻² |
|---|---|---|
| 1 g L⁻¹ | ED wins across nearly the whole map | ED wins (RO's edge, where it exists, is < 0.01 USD m⁻³) |
| 3 g L⁻¹ | ED wins; RO takes over only if RO membranes fall below 24.31 USD m⁻² | IEM must be < 57 USD m⁻² |
| 5 g L⁻¹ | IEM < 57.18 USD m⁻² | IEM < 28.42 USD m⁻² |
| 7 g L⁻¹ | IEM < 36.64 USD m⁻² | IEM < 18.57 USD m⁻² |

Notable magnitudes:
- **1 g L⁻¹:** cutting IEM price 100 → 10 USD m⁻² (RO fixed at 30) widens ED's LCOW advantage from 31.6% to 72.4%, a total difference of 0.07 USD m⁻³.
- **3 g L⁻¹:** ED's baseline benefit is only 0.01 USD m⁻³, but becomes 0.11 USD m⁻³ at IEM = 10 USD m⁻². Even with both at their floor prices (ED 10, RO 5 USD m⁻²), ED retains a 0.04 USD m⁻³ advantage.
- The < 57 USD m⁻² figure at 3 g L⁻¹ may, per industry discussions, already sit at the low end of commercial IEM pricing.

**Conclusion for this route:** price reduction alone secures ED up to ~5 g L⁻¹. At 7 g L⁻¹ the required IEM prices (< 18.57 USD m⁻² against cheap RO membranes) are not plausible in the near term. **At ≥ 5 g L⁻¹, something other than price is needed.**

### 3.4 Route 2 — better ion-exchange membranes

Why membrane properties, not stack geometry: thinner spacers would cut the diluate solution potential drop, but 0.3 mm is already at the low end commercially, and any gain would be offset by the higher pressure drop needed to hold flow velocity. Ion-exchange resin packing or profiled membranes work but raise CAPEX and suit ultrapure applications rather than drinking water.

**Membrane thickness is ruled out as a design lever.** Thinner membranes lower resistance but shorten the diffusion path, worsening co-ion leakage; current efficiency decreases monotonically as thickness falls below 130 µm, with the decay rate growing with feed salinity. Net effect on LCOW is negligible, so thickness is held at 130 µm.

That leaves two parameters, scanned as surfaces:

- **Charge density:** 1–10 mol L⁻¹ (commercial membranes are typically < 5 mol L⁻¹; baseline 3 mol L⁻¹). Higher charge density improves permselectivity *and* lowers resistance — it is unambiguously good, which is why the absolute LCOW minimum always sits at the 10 mol L⁻¹ ceiling. But pushing conventional polymers beyond current values runs into increased water uptake and incomplete ionization of fixed charge groups; the study idealizes these away.
- **Membrane diffusion coefficient:** 1 × 10⁻¹¹ to 2.5 × 10⁻¹⁰ m² s⁻¹ (baseline 2 × 10⁻¹¹). Higher *D* lowers resistance but sacrifices permselectivity. Note these two parameters are not truly independent in real materials — more fixed charge raises hydrophilicity, hence water uptake, hence *D* — but they are decoupled here to locate the optimum.

**The governing tradeoff flips with salinity:**

- At **3 g L⁻¹**, current efficiency stays > 80% across most of the *D* range, so LCOW is more sensitive to *resistance* than to efficiency loss. The practical optimum actually **lowers** charge density from 3 to 1.9 mol L⁻¹ while raising *D* from 2 × 10⁻¹¹ to 8 × 10⁻¹¹ m² s⁻¹ — values already common in commercial membranes. **For ≤ 3 g L⁻¹, current state-of-the-art membranes are already essentially optimal.**
- At **≥ 5 g L⁻¹**, permeable membranes start destroying current efficiency, and LCOW rises more sharply with *D* than with resistance. The 7 g L⁻¹ case makes this vivid: minimizing both parameters gives a punishing 29 Ω cm² resistance and LCOW 0.84 USD m⁻³ — but "fixing" it by maximizing *D* at charge density 1 mol L⁻¹ cuts resistance nearly an order of magnitude (to 3.4 Ω cm²) while collapsing current efficiency to **0.19**, and LCOW rises exponentially to **2.19 USD m⁻³**. **Current efficiency must be prioritized over resistance reduction at high salinity.**

Hence the design target: *keep D low to preserve permselectivity, and buy back the resulting resistance penalty by raising charge density.* The practical optimum (defined as within 0.01 USD m⁻³ of the absolute minimum while minimizing charge density) therefore has *D* falling and charge density rising with feed salinity, reaching **7.75 mol L⁻¹ at 10 g L⁻¹ — more than double most commercial membranes**, and lifting current efficiency from 0.90 to 0.95.

**Impact of this route alone:** 3% LCOW reduction at 3 g L⁻¹, 17% at 10 g L⁻¹. **Not sufficient to beat RO even at 5 g L⁻¹.**

### 3.5 Both routes together

Assuming IEM price falls to parity with RO membranes (30 USD m⁻²), applying the practically-optimized charge density and diffusion coefficient at each salinity, and re-optimizing Γ:

- LCOW of ED falls by **more than a factor of 2 at 10 g L⁻¹**, and by **1.4× even at 1 g L⁻¹** (there almost entirely from membrane price, since properties don't matter at that salinity).
- **ED becomes the cheaper technology across the entire brackish range.**
- Importantly, **ED's SEC remains slightly above RO's even with optimized membranes** at ≥ 5 g L⁻¹. ED wins on LCOW anyway because its capital cost is markedly lower once membrane prices equalize — the RO high-pressure pump has no ED counterpart of comparable cost. Energy efficiency is not the deciding variable.

---

## 4. Conclusion

Benchmarking cost-optimized systems shows **ED is economically advantageous up to 3 g L⁻¹**; above that, ED's process inefficiencies surface as rising membrane and electricity costs, driving LCOW up rapidly and handing RO a large advantage — consistent with the two technologies' actual market positions.

- **Membrane price reduction** solidifies ED at low salinity and extends it to ~5 g L⁻¹, but at ≥ 5 g L⁻¹ the price cuts needed merely to break even are implausible. Price reduction is nonetheless expected as water-energy-nexus applications multiply and more manufacturers enter.
- **Membrane property optimization** — above all charge density, with *D* held relatively low — is the most impactful lever against ED's high-salinity inefficiency, and the study delivers explicit target values as guidance for material development. But it too is insufficient alone.
- **Both are needed simultaneously** for ED to beat RO across the whole brackish range. If achieved, it could displace RO's dominance in brackish water desalination.

---

## Acknowledgments

Supported by the NSF Nanosystems Engineering Research Center for Nanotechnology-Enabled Water Treatment (EEC-1449500) and NSF award CBET-2001219. AMTA and Bureau of Reclamation fellowship for Membrane Technology awarded to S.K.P.

**Competing interests:** none declared.
**Data availability:** available on request.
**Supplementary material:** doi:10.1016/j.watres.2023.121009
<!--kb:end-->

### Scientist 2

- field: climate change
- model: qwen3.8-max
- tool: drought_ef (from tools/)
- runtime: python
- knowledge base: 74174 chars

<!--kb:start-->
# Drought impacts on the electricity system, emissions, and air quality in the western United States

**Authors:** Minghao Qiu, Nathan Ratledge, Inés M. L. Azevedo, Noah S. Diffenbaugh, Marshall Burke

**Affiliations:**
- a. Doerr School of Sustainability, Stanford University, Stanford, CA 94305
- b. Center for Innovation in Global Health, Stanford University, Stanford, CA 94305
- c. Emmett Interdisciplinary Program in Environment and Resources, Stanford University, Stanford, CA 94305
- d. Department of Energy Science and Engineering, Stanford University, Stanford, CA 94305
- e. Center on Food Security and the Environment, Stanford University, Stanford, CA 94305
- f. National Bureau of Economic Research, Cambridge, MA 02138

**Corresponding author:** Minghao Qiu (mhqiu@stanford.edu)

**Journal:** PNAS, 2023, Vol. 120, No. 28, e2300395120
**DOI:** https://doi.org/10.1073/pnas.2300395120
**Published:** July 6, 2023
**Editor:** Peter Gleick, Pacific Institute for Studies in Development, Environment, and Security
**License:** CC BY-NC-ND 4.0
**Keywords:** drought | electricity system | air quality | climate change

---

## Abstract

The western United States has experienced severe drought in recent decades, and climate models project increased drought risk in the future. This increased drying could have important implications for the region's interconnected, hydropower-dependent electricity systems. Using power-plant level generation and emissions data from 2001 to 2021, we quantify the impacts of drought on the operation of fossil fuel plants and the associated impacts on greenhouse gas (GHG) emissions, air quality, and human health. We find that under extreme drought, electricity generation from individual fossil fuel plants can increase up to 65% relative to average conditions, mainly due to the need to substitute for reduced hydropower. Over 54% of this drought-induced generation is transboundary, with drought in one electricity region leading to net imports of electricity and thus increased pollutant emissions from power plants in other regions. These drought-induced emission increases have detectable impacts on local air quality, as measured by proximate pollution monitors. We estimate that the monetized costs of excess mortality and GHG emissions from drought-induced fossil generation are 1.2 to 2.5x the reported direct economic costs from lost hydro production and increased demand. Combining climate model estimates of future drying with stylized energy-transition scenarios suggests that these drought-induced impacts are likely to remain large even under aggressive renewables expansion, suggesting that more ambitious and targeted measures are needed to mitigate the emissions and health burden from the electricity sector during drought.

## Significance

Climate-driven changes in drought could disrupt electricity systems that depend heavily on hydropower, potentially increasing generation from fossil fuel sources. Impacts from the associated emissions and air pollution could represent a large and unaccounted-for social cost of climate change. We empirically quantify the impacts of drought on fossil fuel power plants in the western United States and the consequent effects on emissions and air quality. Damages through these channels are estimated to be 1.2 to 2.5x the increase in direct economic cost of drought-induced fossil fuel electricity generation. Under future climate, these drought-induced impacts likely remain large due to increasing drought risks, and we find that even rapid expansion of renewable energy has limited ability to curb these impacts.

---

## Introduction

Climate change can influence energy systems by altering energy supply, demand, and transmission, leading to significant economic and environmental impacts (1–5). For instance, existing work highlights how a changing climate will affect electricity demand and energy expenditure (6, 7), how it can influence how much of a given energy source (e.g., hydropower) can be utilized (8–10), and how it can influence the operations of thermal power plants (11). Many of these insights are then incorporated into energy system models to estimate the overall impacts of climate change on the energy supply, demand, and system cost (12).

Yet the overall societal costs of climate-related disruptions to the energy system could extend beyond the channels explored in existing work. In particular, climate disruptions could result in increases in electricity generation from fossil fuel sources if a changing climate induces large changes in energy demand and/or supply, as existing work suggests, and if marginal electricity generation source used to cover short-run increases in demand or decreases in supply remains reliant on fossil fuels. Increased fossil generation could then result in increased greenhouse gas (GHG) and air pollutant emissions, with emissions increases perhaps occurring far from the location of the climate shock, given the spatially interconnected nature of many energy systems. The associated economic and health impacts of these climate-induced emissions are often unaccounted for in existing analyses.

In this paper, we study the impacts of drought on the electricity system and the consequent effects on GHG emissions, air quality, and human health in the western United States. Drought could influence the electricity generation and emissions of fossil fuel power plants through a variety of compounding pathways. Drought reduces runoff and electricity generation from hydropower (12, 13), while accompanying heat waves can influence electricity demand (14, 15). Accompanied weather patterns during drought can also influence electricity supply from nonhydro renewable energy sources, e.g., drought-induced wildfire smoke could reduce solar generation (16), which can then influence generation and emissions from fossil fuel plants. As many fossil fuel plants require extensive amounts of cooling water, a scarcity of cooling water can also decrease the operating efficiency and electricity supply from those impacted plants (11, 14, 17).

More importantly, when multiple regions are connected through the electricity transmission networks, drought conditions in one region can lead to changes in generation from fossil fuel plants in another region (18, 19). These multiple pathways between drought and operation of fossil fuel plants make it difficult to understand the emission and air quality impacts of drought on the electricity system ex ante.

In this paper, we focus on the 11 US states which are connected to the Western Interconnection. The western United States has experienced record-breaking drought conditions since 2000 and a declining trend in total runoff (Fig. 1A), influenced by anthropogenic climate change (20, 21). Reduced runoff has substantial implications for the electricity system in the western United States, given that hydro accounts for 23% of the electricity generation in this region (22) and that there is a very close coupling between runoff anomalies and hydro generation (Fig. 1B). The western United States faces significant challenges under a changing climate as climate models project significant increases in drought risks due to increased co-occurrence of high-temperature and low-precipitation conditions (20, 23). Despite having lower air pollutant and GHG emissions per unit of electricity generation compared to the rest of the United States, 60% of the regional electricity supply still comes from over 800 fossil fuel power plants, including 108 coal or oil-based power plants with high CO2, SO2, and NOx emissions (Fig. 1C).

Recent droughts in this region have attracted wide attention (18, 24–28), but much less is understood about the potential impacts on emissions, air quality, and human health. Using energy system models or state-level data analysis, a few studies have found significant increases in CO2 emissions from the power sector during drought (25, 26, 29, 30). Very few studies have quantified the impacts of drought on air pollutant emissions from fossil fuel plants, and these estimates are often aggregated at the regional or state level (30, 31). Accurate accounting for the emissions and health impacts of drought-induced fossil fuel generation is challenging as it needs to account for both the heterogeneous responses across different power plants as well as transboundary impacts through the interregional exchange of electricity. Future policy and investment would also benefit from projections of the emissions impacts under future climate and transitions in the electricity sector (e.g., expansion of renewable energy); however, there exist no studies conducting such projections using empirically grounded relationships.

Here, we estimate the impacts of drought on electricity generation and emissions from fossil fuel plants in the western United States and the associated air quality and health effects, using empirical data on plant-level generation and emissions, runoff, and observational air quality measured by surface monitors from 2001 to 2021. Our analysis directly accounts for the transboundary impacts of drought on fossil fuel generation and pollutant emissions, due to the import/export of electricity across three electricity regions (Fig. 1C, following definitions of the Energy Information Agency). We first develop a statistical model between plant-level electricity generation and runoff anomalies in each of the three electricity regions. As drought impacts on individual fossil fuel plants vary as a result of their operational status, locations, and fuel type, we estimate drought impacts at a disaggregated level—specifically on each set of power plants that are located in the same electricity balancing–authority area and use the same fuel type. For each plant, we then calculate the drought-induced generation, defined as the changes in generation as a result of the runoff anomalies (relative to the 1980 to 2021 average).

To estimate the impacts on air quality and related health damages, we quantify the changes in measured surface PM2.5 that are attributable to drought-induced changes in SO2 and NOx emissions from fossil fuel plants. We specifically focus on surface PM2.5 that is not related to wildfire smoke, as wildfire is more prevalent during drought periods and it contributes substantially to surface PM2.5 (*Materials and Methods*). We quantify whether predicted drought-induced emissions affect surface PM2.5 concentration measured at nearby air pollution monitors. We then calculate the monetized damages from excess mortality due to observed PM2.5 changes using an empirically derived concentration–response function (CRF) that relates short-term changes in air pollution to mortality (32) and a value of statistical life of $10.95 million (year 2019 dollars) recommended by the US EPA (33). We further quantify the monetized damages of drought-induced GHG emissions by accounting for increased CO2 emissions using the social cost of carbon ($117 per ton, year 2020 dollars) (34) and methane (CH4) leakage using a 2.3% leakage rate across the life cycle of the gas production and usage (35) and the social cost of methane ($1257 per ton, year 2020 dollars) (34).

Finally, to assess potential impacts under future climate and energy production scenarios, we combine our empirical estimates of plant-level emission changes with climate projections and stylized electricity sector scenarios. We use the average 2030 to 2059 projected runoffs from The Coupled Model Intercomparison Project Phase 6 (CMIP6) climate model ensemble. We consider three potential scenarios in the electricity sectors using results from existing energy system model projections (36, 37): replacing coal power plants with natural gas plants, increased penetration of carbon capture and storage (CCS), and increased penetration of renewable energy and battery technology. For the renewable energy scenario, we use the "Low Renewable Cost" scenario from the National Renewable Energy Lab's projections of the US electric sector through 2050 (36), which projects the average and marginal energy source in the electricity sector.

---

## Results

### Drought Increases Electricity Generation from Fossil Fuel Plants

Compared to the average conditions in 1980 to 2021, the electricity generation from the fossil fuel plants on average increased by 35%, 11%, and 9.5%, in California (CA), Northwest (NW), and Southwest (SW), respectively, in the driest months during the study period (Fig. 2). Importantly, we find that the combined effect of drought on fossil generation across the three regions ("total effect") is substantially larger than the effect of drought on the fossil generation in the same region alone ("local effect"). Increases in fossil generation due to drought conditions occurring in the neighboring electricity regions account for 63% of the total generation increases in CA during the drought periods, along with 44% of the total generation increases in NW, and almost all of the generation increase in SW. As shown in Fig. 2D–F, drought occurring in the NW can lead to increases in fossil fuel generation in all three electricity regions, while CA drought leads to increases in fossil fuel generation from power plants in CA and NW. Our estimation results are consistent across alternative specifications of the regression models and models using alternative drought indices, choices of data inclusion criterion, and region definitions (SI Appendix, Figs. S2–S5 and Table S1).

The transboundary effects of drought on fossil fuel generation are largely driven by changes in the import/export of electricity due to drought-induced supply or demand shocks. Neighboring regions that are connected to the drought regions increase fossil fuel generation from their own plants to make up for shortfall in the drought region. We corroborate these findings using a separate dataset on the import and export of electricity between these three regions (38). For example, when comparing a dry period (with the 5th percentile of runoff anomalies) relative to a wet period (with the 95th percentile of runoff anomalies) in NW, we find a 23% increase of net export of electricity from CA to NW, and a 7.2% increase of net export from the SW to NW (SI Appendix, Fig. S6). Magnitudes of the import/export changes are consistent with the transboundary effects of drought-fossil generation quantified above (a 26.4% increase in CA fossil generation due to NW drought and an 11.2% increase in SW fossil generation due to NW drought). These results suggest that when hydropower production is reduced in NW under drought, less power is available for export to either CA or SW, and therefore, fossil fuel plants in CA or SW would need to increase their electricity generation to fill this gap.

To further understand the mechanisms between runoff and fossil fuel generation, we use causal mediation analysis in CA and NW where the "local effects" of drought on fossil generation are significant and substantial (SI Appendix, Fig. S7). We find that the need to substitute for changes in hydropower is the leading mechanism that explains the runoff—fossil generation relationship. We find that increases in fossil generation during low runoff periods are not empirically related to the changes in the electricity demand. In the *Discussion*, we briefly discuss the potential reasons and its implications. We further find that a small fraction of the increases in fossil generation could be due to reductions in renewable generation, consistent with the evidence of reduction in solar generation due to wildfire smoke (which often coincides with drought) and the reduction in wind power due to lower wind speed during drought episodes (see SI Appendix for more discussions) (39–41). We also find some evidence that the drought-induced emissions from the fossil fuel plants are possibly offset by increases in ambient temperature at the plant locations, suggesting potential generation curtailment due to high-temperature conditions (SI Appendix, Fig. S7). To further test whether the hydro displacement is the dominant channel between runoff and fossil fuel generation, we perform a placebo test that applies the same model to Texas and Florida, two electricity regions that are largely isolated from the rest of the country and have little hydroelectricity capacity. There, we find no effects of runoff changes on generation from fossil fuel plants (SI Appendix, Table S2).

### Drought-Induced Emissions Increase Surface PM2.5 Near Fossil Fuel Plants

When accounting for the plant-level heterogeneity, we find that drought-induced emissions account for ~12% of the total regional CO2 emissions from the electricity sector, ~6% of the total NOx emissions, and ~8% of the SO2 emissions during extreme drought periods (e.g., spring and summer during 2001). Relative changes in SO2 and NOx emissions are smaller than CO2 emissions due to the relatively small impacts of drought on the large high-emitting coal power plants. However, some individual power plants experience larger changes in SO2 and NOx (Fig. 3A). For example, in an extremely dry year like 2001, we predict that roughly 20% of plants would increase their SO2 and NOx emissions by at least 30%; this increase is more than triple the regional average increase for all plants. These results highlight the substantial local heterogeneity in emissions impacts from a common regional drought shock.

Drought-induced emissions of SO2 and NOx from fossil fuel plants increase surface PM2.5 near the power plants (in particular, within a 50-km radius), while, as expected, the effects gradually decay as the distance between the monitor and power plant increases (Fig. 3C; also see *Materials and Methods* and Fig. 3B for method illustrations). We also find evidence that suggests that increases in surface PM2.5 are more likely to be associated with drought-induced emissions from plants at the upwind location of the monitor, further strengthening our causal claims (SI Appendix, Fig. S8). Our estimation results are largely robust to alternative specifications of fixed effects, specification of regional air quality trends, and meteorology controls (SI Appendix, Fig. S9). We also calculate the PM2.5 impacts using the reduced-complexity air quality model, the Intervention Model for Air Pollution (InMAP) (42). Using the same set of drought-induced emission, InMAP also estimates an increase in surface PM2.5, although with a substantially smaller magnitude than our empirically derived estimates (SI Appendix, Fig. S10 and *Discussion*).

### Monetized Economic and Health Impacts of Historical Droughts

We value the total health and economic damages of drought-induced fossil electricity generation by monetizing the impact of predicted changes in air pollution, CH4 leakage, and CO2 emissions when drought strikes, applying our estimates backward over the observed drought time series (Fig. 4A). As most of the recent 20-y period is drier than the 1980 to 2021 long-term average, we calculate that the western United States has experienced a total net damage of $20 billion during this period. Drought-induced CO2 emissions account for $14 billion, or 70% of the total damage. PM2.5-associated mortality accounts for $5.1 billion (25% of the total damage) and CH4 leakage accounts for $1.0 billion (5% of the total damage).

Despite the consequential total damage from recent historical droughts, annual damages declined markedly after 2001. This is largely driven by the declining emission factor of fossil fuel electricity generation (i.e., emissions of NOx, SO2, and CO2 per unit of electricity generation) over the last 20 y (Fig. 4B). NOx and SO2 emission factors in the western United States have declined by eight- to ten-fold primarily due to the transition from coal to natural gas and the installation of scrubbers (44, 45). The CO2 emission factor also declined by 40%—a magnitude smaller than SO2 or NOx since natural gas plants are still significant carbon emitters and policies rarely target the stack-level emissions of CO2 within the fossil fuel plants.

We find that installation of scrubbers at high-emitting plants near the population centers leads to marked reduction in the PM2.5-related health damages. For example, one power plant (which includes two coal-fired units) in Washington state was responsible for 26% of the total drought-induced PM2.5 damage in 2001 in the western United States (SI Appendix, Fig. S11). However, drought-induced PM2.5 damages associated with this plant decreased by 90% after the installation of scrubbers in 2002, contributing to a large part of the decline in total PM2.5 damage. In the more recent years (e.g., 2018 to 2021), most of the monetized damages of the drought-induced fossil generation come from CO2 emissions (84% of total damage), while PM2.5-related health damage and the CH4 leakage each accounted for 10% and 6% of the total damage.

These monetized damages exceed estimates of the economic impacts of drought on the electricity system reported by previous studies (27, 28). As a point of comparison, we focus on the 2012 to 2016 drought in California, a period which has been extensively studied (Fig. 4C). Both Kern et al. and Gleick quantified the increase in total cost of electricity generation due to the switch from low-cost hydro generation to more expensive fossil fuel generation. Kern et al. also examined the extra cost due to increased electricity demand and the potential influence of higher natural gas prices on generation costs. We account for drought-induced damages associated with emissions from power plants in CA as well as damages in the other two regions as a result of the CA drought. We estimate that the drought-induced CO2 emissions account for 19% of the total electric CO2 emissions in CA during this period (11% from CA plants and 8% from the other two regions). The drought-induced fossil generation led to a total monetized damage of $5.1 billion (using SCC value of $117)—1.2–1.9x of the reported direct economic cost due to the reduction in hydropower and 2.5x of the direct economic cost due to the drought-induced increase of electricity demand (27, 28).

### Projecting Future Damages

Despite the variability in projected runoffs across climate models, most models project increasing or sustaining drought risks over the western United States during 2030 to 2059 relative to 1980 to 2014 (SI Appendix, Fig. S12). Averaged across climate model projections under the reference scenario [assuming no changes in the electricity sector under a high climate-forcing scenario (SSP3-7.0)], drought-induced fossil fuel generation could result in annual damages of $293 million (relative to 1980 to 2014 averages of each model, discounted back to 2020). Damages due to extra CO2 emissions account for 81% of the total damages, while CH4 leakage and PM2.5 damages account for 8% and 11%, respectively (Fig. 5A).

These drought-induced economic and health damages, however, could be substantially lower under the alternative climate scenarios with lower GHG emissions (SSP1-2.6 and SSP2-4.5). Compared to SSP3-7.0, we estimate a reduction in annual damages by $214 million under SSP2-4.5 or 73% of the damages under SSP3-7.0 (Fig. 5B). This reduction is primarily driven by the higher projected runoff in California and Northwest projected by models under the two lower GHG scenarios. We find that the damages under the SSP2-4.5 scenario are lower than the SSP1-2.6 scenario, likely due to the nonlinear relationship between runoffs and the GHG forcings and model uncertainties. Runoff generally decreases under higher air temperature due to the increased evapotranspiration (23, 46), but the substantial uncertainty in precipitation and the role of vegetation further complicates the runoff responses across different climate scenarios (47, 48).

Surprisingly, the projected transitions in the electricity sector have modest effects in mitigating the damages from the drought-induced fossil generation, with the only exception of expansive penetration of CCS in 2050 (see Fig. 5C for the result of 2050, and SI Appendix, Fig. S13 for the result of 2035). Relative to the reference scenario under SSP3-7.0, replacing all coal power plants with natural gas plants only reduces drought-induced damages by 11%. Increased penetration of renewable energy and energy storage has an even smaller impact—a reduction in the damages by 5.4% in 2050. These modest effects are in sharp contrast with the total emission mitigations that could be achieved under these two strategies. Total CO2 emissions from the fossil fuel plants would decline by 72% under the same *high RE* scenarios and by 26% under the *coal phase-out* scenario, respectively. These disparities are due to the differences between the projected changes in *marginal* energy sources (i.e., those sources used to cover short-run increases in demand or decreases in supply) and *overall* energy sources (i.e., those sources used to meet overall average demand) in the future (SI Appendix, Fig. S14). For example, fossil fuel generators are projected to only generate 8.6% of the total electricity in California in 2050 (compared to 41% in 2021), while they are still projected to be the dominant marginal energy source used to meet demand fluctuations, serving as the marginal source in the grid for 71% of the year. As a result of the differential changes between the overall and marginal energy sources, we estimate that the relative contributions of drought-induced GHG emissions will increase by two- to fourfold in many western states over the next 30 y with increasing expansions of renewable energy (Fig. 5D). For example, drought-induced GHG emissions of California associated with an extreme drought year (defined as the 10th percentile lowest runoffs during 2030 to 2059) would account for 41% of the total electricity GHG emissions of California in 2050 (compared to only 11% in 2024).

---

## Discussion

By empirically linking runoff variability to plant-level generation, emissions, and surface PM2.5, our analysis quantifies the environmental and economic impacts associated with drought-induced fossil fuel generation. In the states that heavily rely on hydropower for electricity generation, drought-induced GHG emissions could account for up to 40% of the total electricity emissions of those states during future extreme drought years. Our analysis suggests that the impacts of drought on the electricity system have been underestimated by previous research that largely focuses on the direct economic costs of drought-induced disruptions to the electricity sector.

We find that over 50% of the drought-induced fossil fuel generation—and the resulting economic and health damages—is transboundary. Previous studies have shown that the interregional connection could mitigate drought-induced risks in terms of grid stability and generation cost (19). Our analysis however demonstrates that the drought-induced emissions impacts could be redistributed through the grid interconnection, consistent with findings from prior work (30). More broadly, our results have important implications for research that uses empirical or statistical models to quantify the impacts of climate or other environmental change. Our analysis suggests that, at least in some settings, local economic and health impacts could be driven by distant climate change and that a careful empirical strategy is needed to uncover these teleconnections.

Drought-induced economic and health damages from fossil fuel generation will remain an important challenge under future climate. However, these damages could be substantially reduced under mitigation scenarios which limit the warming level. Surprisingly, we find that increased penetration of renewable energy has a limited effect in reducing drought-induced damages despite a significant reduction in the total fossil fuel generation under the evaluated scenario. This is largely because the amount of renewable energy projected to be deployed under the National Renewable Energy Laboratory scenario displaces a significant fraction of fossil fuel generation on average, but is not yet sufficient to fully replace fossil fuel as the marginal energy source. The drought-induced fossil fuel generation and associated damages will become increasingly important with the overall grid decarbonization. In other words, the electricity sector will become harder to be "fully decarbonized" if we account for the increasingly frequent drought shocks and the associated GHG emissions in systems with at least some hydro. Our research suggests that accounting for the impacts of climate change and its variability on the electricity system is important for decarbonization in the western United States; such factors have been studied in some scenario analyses (49, 50) but not fully integrated in most decarbonization scenarios.

We show that drought conditions could further exacerbate ambient PM2.5 pollution, a leading environmental risk factor around the world, through heavier usages of fossil fuels in the electricity system. More broadly, our analysis contributes to a better quantification of the impacts of climate change on human health through climate-induced changes in air pollution. Our work contributes to an emerging literature that climate change can influence air quality through influencing fossil energy usage (51), extending the focus beyond the impacts on naturally induced emissions (such as through wildfire) or the chemistry/meteorology channels (52–55).

Our analysis contributes important insights to the measurement of air quality impacts of emission changes associated with environmental shocks or policies. We find that our empirical estimates of the PM2.5 impacts differ from the results simulated by InMAP in many important ways. Our empirical method estimates a larger response of PM2.5 to precursor emission changes near the plants but virtually no effect outside the 200-km radius [consistent with prior empirical analysis (45)]. Our empirical estimates are consistent with previous studies that show that InMAP underestimates the PM2.5 concentration (or the PM2.5-emission sensitivities) in the western United States either comparing to the surface PM2.5 monitors (56) or the full-complexity chemical transport model (57). More research is needed to better understand the strengths and limitations of estimating impacts of emissions changes on air quality with both the empirical method as well as process-based air quality models.

Our research reveals multiple pathways for future research to better understand the impacts of drought on the energy systems and associated downstream impacts. In this work, we use the cumulative runoff in the previous 9 mo to characterize drought conditions as it is more directly related to hydropower [compared to standard drought indices such as the Palmer Drought Severity Index (58)]. Therefore, our analysis is designed to capture the relatively longer-term impacts of the "hydrological drought" on the electricity system. As the long-term runoff changes are only partially correlated with temperature variations, our analysis, therefore, only partially captures the effects of the accompanying heat waves on electricity demand and the associated generation from fossil fuel plants. Future studies could build on our empirical framework to directly incorporate the influence of heat waves.

The quantified economic and health damages of drought-induced fossil emissions, while substantial, are likely a lower bound of the full impacts of drought on the electricity system. Our analysis does not capture the potential economic and health impacts of drought-induced blackouts [especially if they overlap with dangerous heat waves (59)]. Our estimates also do not explicitly account for the fluctuation of fuel prices (especially natural gas) which can be an important factor for the economic impacts of drought-induced disruptions (27). Also, we only quantify the impacts on the fossil fuel plants that are connected to the grid due to the data availability. However, drought-induced decreases in hydropower could also increase the usage of backup generators that are not connected to the grid, as well as nonelectricity energy sources especially in other parts of the world (60). Future research is needed to estimate and integrate the impacts that could occur through these various pathways, both in the western United States and in settings outside the United States where these other pathways (e.g., blackouts) could represent more substantial sources of economic loss.

While our study has focused on the western United States, our method and findings are globally relevant as many countries that heavily rely on hydro power have experienced increasing drought risk due to climate change. Globally, we identify 19 countries that are potentially vulnerable to drought-induced shocks to their electricity and energy system (SI Appendix, Fig. S15), primarily located in Central and South America, Africa, and South East Asia. These countries heavily depend on hydropower for their electricity generation (>20% of the annual electricity generation) and could potentially experience increasing drought risks as projected by the climate models (>5% decline in the average 2030 to 2059 runoff, the median across different climate models). For example, Honduras relies on hydropower to provide 53% of the nation's electricity and is projected to experience a 20% decrease in runoff by midcentury under SSP3-7.0. Electricity systems in many countries are more polluting compared to the western United States (with a more coal-dominant grid) and can therefore lead to higher economic and health damages due to deteriorated air quality and GHG emissions (61, 62). Furthermore, drought-induced reductions of hydropower could result in blackouts in countries that do not have enough excess electricity generating capacities, leading to further economic or health consequences (63, 64). Better understanding drought-related impacts on the energy systems and consequent environmental and economic damages in a global sample of countries is an important avenue for future research.

---

## Materials and Methods

### Unit-Level Generation and Emissions Data

Our analysis focuses on the western United States which spans three Energy Information Agency (EIA) electricity regions: California (CA), Northwest (NW), and Southwest (SW) (38). See SI Appendix for results under alternative region definitions. Hourly electricity generation and emissions (CO2, SO2, and NOx) of major fossil fuel electricity generating units (nameplate capacity >25 MW) are obtained from the EPA Air Market Program Data from 2001 to 2021 (65). We aggregate hourly emissions and generation to a monthly level for each unit. Unit-level characteristics such as location, primary fuel type, and stack height are derived from the EPA Emissions & Generation Resource Integrated Database (66). In our main analysis, we only include an observation (i.e., unit-month) if the unit has at least four non-missing values during the month (see SI Appendix for more details on the sample restrictions). Our final sample consists of 95,608 unit-months from 681 electricity generating units—586 units that use natural gas, 91 units that use coal, and four units that use biomass or other fuel types. Our final sample covers 90% of electricity generation from fossil fuel plants (including biomass), and 49% of the total generation in the 11 states of the western United States in 2019 (66) (nonfossil generation includes generation from hydro, nuclear, wind, and solar energy). We perform a sensitivity analysis to examine the effects of runoff changes on generation from fossil fuel plants that are not in our main sample ("non-AMPD" plants) and find that the estimated drought-induced generation from the non-AMPD plants is 7.3% of our main estimates (SI Appendix, Table S3 and SI Appendix).

### Drought Characterization

Following Herrera-Estrada et al. (30), we use the total runoff (sum of surface and subsurface runoffs) to characterize drought conditions. Previous studies have shown that runoff more accurately captures hydrological drought and the influence on hydropower compared to other standardized drought indices (e.g., the Palmer Drought Severity Index) (30, 67). We use monthly runoff data from the VIC land-surface model of phase 2 of the North American Land Data Assimilation System (NLDAS-2) (68), following recommendations from the prior literature (30, 69). For each electricity region, we first calculate the state-level runoff averaged over grid cells in each state and then calculate the regional runoff as a weighted average of state-level runoff (weighted by the state-level hydropower capacity). To capture the long-term dynamics of hydrological drought, we calculate the running average of runoff for the previous 9 mo. The runoff anomalies are then calculated as the relative deviations from the 1980 to 2021 average for each region and month of year. We find largely consistent results when using runoff values calculated with different averaging windows and values from the other NLDAS-2 models (SI Appendix and SI Appendix, Fig. S2). We also find similar results using a distributed lag model (SI Appendix).

### Empirical Strategy: Impacts of Drought on Fossil Fuel Generation

We estimate the following regression to quantify the impacts of drought on electricity generation from fossil fuel units, while accounting for the cross-regional impacts:

$$
y_{igym} = \sum_{k \in \{CA, NW, SW\}} \{\beta_{gk} Q_{kym}\} + \gamma_g X_{igym} + \eta_g y + \psi_{gm} + \theta_i + \epsilon_{igym}
\tag{1}
$$

where `y_igym` denotes the log of electricity generation from unit *i* in electricity region *g*, year *y*, and month of year *m*. `Q_kym` denotes the runoff anomalies of region *k* in year *y* and month of year *m*. Separate equations are estimated for each electricity region *g* (*g* ∈ {CA, NW, SW}). `β_gk` are the parameters of main interest here, which estimate the causal impacts of change in runoff anomalies in region *k* on the generation from fossil fuel units in region *g*, conditional on the runoff anomalies in the other two regions. `X_igym` denotes the regional- and unit-level variables including monthly sales of electricity (i.e., electricity demand), generation of wind power and solar power, and the monthly average air temperature at the plant location. When estimating impacts of drought on fossil generation in the same region (*g* = *k*), `X_igym` captures possible mechanisms through which runoff could influence fossil generation, and therefore in our main analysis, we report estimates without control variables (see below for the mechanism analysis). While estimating drought impacts on generation from the neighboring regions (*g* ≠ *k*), we report estimates with these variables as controls, as they are not likely to represent the underlying mechanisms.

Our main specification includes linear year trend (*y*), month-of-year fixed effects (`ψ_gm`), and unit-level fixed effects (`θ_i`) to control for the underlying trend and seasonality in fossil generation and runoff as well as the time-invariant unobserved factors at the unit level. Our model exploits the deviations in runoff relative to the month-of-year averages (i.e., was it a particularly dry or particularly wet June relative to the regional averages for June conditions) to estimate the effects on fossil fuel generation. `ε_igym` represents the error term. `β_gk` are estimated using the weighted ordinary least square approach, weighted by the unit-level monthly average generation. SEs of the regression coefficients are clustered at the plant level. See SI Appendix for more details on the alternative specifications of the regression models.

To account for the heterogeneous impacts of drought on different fossil fuel plants, we further estimate Eq. 1 at the Balancing Authority (BA) × fuel type level. We separately estimate the regression equations for each group of power plants with the same fuel type in the same BA region. In total, we estimate 54 equations for the 54 BA-fuel subgroups. Resolving the impacts of drought on plant generation at a more disaggregated level is important for the air quality and health impact analysis as one unit of emissions could have different impacts on human health depending on their proximity to population centers. For a small number of units (11 out of 681 units), we use the pooled regression coefficients at the regional level instead of coefficients estimated at the BA-fuel level. (For these 11 units, the estimated displaced generation would exceed their total generation if we use the coefficients from the BA-fuel regressions.) The aggregated impacts on electricity generation are consistent across the regressions at the regional or the BA-fuel level (SI Appendix, Fig. S16).

### Mechanisms of Drought Impacts on Power Plants: Causal Mediation Analysis

We use causal mediation analysis to identify the mechanisms through which runoff changes influence the electricity generation from fossil fuel plants. For the mediation analysis, we only focus on the drought impacts on fossil fuel plants in the same electricity region (i.e., the local effect) and only focus on CA and NW where the estimated local impacts are substantial. Mechanism analysis on the cross-boundary impacts is discussed in a separate section in SI addressing the changes in the import/export of electricity. Causal mediation analysis is a widely used statistical technique across many disciplines that aims to estimate the causal effects of the treatment variable (in our case, runoff) on the outcome variable (in our case, fossil plant generation) through certain causal mechanisms (70). We focus on the following pathways through which drought could influence electricity generation from fossil fuel plants: 1) through changes in hydropower output, 2) through changes in electricity demand, 3) through changes in wind or solar power production, and 4) through changes in the cooling efficiency of thermal power plants due to ambient temperature. More details of the causal mediation analysis can be found in SI Appendix.

### Air Quality Impacts

We estimate an empirical model between predicted drought-induced fossil plant emissions and surface PM2.5 concentration measured by monitors nearby. Using our estimates from the first part of the analysis, we first calculate the predicted drought-induced CO2, SO2, and NOx emission changes at each plant using the following equation:

$$
\Delta Emis_{iym} = \sum_{k \in \{CA, NW, SW\}} \left( e^{(\beta_{ki} \times Q_{kym})} - 1 \right) \times Emis_{iym}
\tag{2}
$$

where `ΔEmis_iym` denotes drought-induced emissions of unit *i* in year *y* and month of year *m*. `Q_kym` denotes the monthly runoff anomaly of electricity region *k*. `β_ki` denotes the coefficients derived from the BA-fuel level regressions which estimate the impacts of runoff in region *k* on unit *i*. `Emis_iym` denotes the observed emissions from unit *i* in that month. `ΔEmis_iym` quantifies the changes in emissions due to runoff anomalies relative to the 1980 to 2021 average. `ΔEmis_iym` can be both positive (when runoff is lower than the 1980 to 2021 average) or negative (when runoff is higher).

Surface PM2.5 concentrations are derived from the US Air Quality Systems administered by the US EPA (71). Due to influences of drought on wildfire and associated PM2.5 (53, 55), we only use observational PM2.5 concentration from monitors on days that are not influenced by wildfire smoke using methods from ref. 72 (see SI Appendix for more details). We calculate the monthly average PM2.5 concentration for each month and monitor using PM2.5 concentration on all nonsmoke days. Our air quality analysis focuses on the period between 2006 and 2020 due to the availability of the wildfire smoke plume data.

We estimate the following regression to quantify the effects of drought-induced emissions on surface PM2.5 concentration:

$$
PM_{iym} = \sum_{d} \beta_d \Delta Emis_{idym} + \gamma W_{iym} + \eta y + \psi_m + \theta_i + \epsilon_{iym}
\tag{3}
$$

where `PM_iym` denotes the monthly nonsmoke PM2.5 concentration measured by monitor *i* on year *y*, month of year *m*, and `ΔEmis_idym` is the drought-induced emission changes (SO2 + NOx) from fossil fuel plants that are located within a certain distance (distance bin *d*) from the monitor *i*. For each monitor, fossil fuel plants are grouped into five groups based on their distances from the monitors: <50 km, 50 to 100 km, 100 to 200 km, 200 to 500 km, and >500 km. `W_iym` are the meteorological variables at the location of monitor *i*. In our main specification, we include the splines of surface temperature, precipitation, dewpoint temperature, boundary layer height, air pressure, 10 m wind direction, and wind speed. Our main specification includes year (`η_y`) and month-of-year fixed effects (`ψ_m`) to capture the interannual variability and seasonality of PM2.5 concentration and monitor-level fixed effects (`θ_i`) to control for the time-invarying unobserved factors at the monitor level. `ε_iym` represents the error term. `β_d` are estimated using the weighted ordinary least square approach, weighted by the variance of the inversely distance-weighted drought-induced emissions of each monitor to reduce the uncertainty of the estimates (i.e., observations from monitors are up-weighted if the monitors are closer to plants with substantial changes in drought-induced emissions). SEs are clustered at the state × year × month-of-year level.

To better understand whether the estimated impacts capture the causal impacts of emission changes on surface PM2.5, drought-induced emissions are classified into "upwind" or "downwind," depending on whether the fossil fuel plants are at the upwind or downwind direction of the monitor following methods in ref. 73. We find the drought-induced emissions from upwind power plants have a larger impact on surface PM2.5 compared to emissions from the downwind power plants, although estimates are somewhat noisy (SI Appendix, Fig. S8).

Our main analysis calculates the drought-induced PM2.5 using the empirical estimates above and accounts for drought-induced emissions within a 100-km radius. As an alternative strategy to model the air quality impacts, we also use the Intervention Model for Air Pollution (InMAP) to calculate the impacts of drought-induced emissions of SO2 and NOx on PM2.5 concentrations (see SI Appendix, Fig. S17 and SI Appendix for more details).

### Health Impacts Analysis

We quantify the health impacts of drought-induced fossil fuel generation in terms of the premature mortality associated with changes in PM2.5. As we calculate PM2.5 changes at the monthly level, we use the concentration–response function (CRF) between mortality and short-term exposure of PM2.5 (e.g., at the daily or weekly level), rather than CRFs derived from long-term epidemiological studies. In our main analysis, we use the CRF from the study of Deryugina et al. to quantify the premature mortalities for adults over 65 y old (32). Deryugina et al. estimate that every 1-μg/m³ increase of PM2.5 at the daily level leads to an increase of 0.69 deaths per million people in the following 3 d for adults over 65 y old in the United States. Their study exploits the variation of daily PM2.5 due to daily wind direction changes to account for the confounding biases. We calculate the premature mortality among the 65+ age population at the monthly and census tract-level associated with drought-induced changes of PM2.5. Population information of different age groups is derived from the 5-y American Community Survey (ACS) data during 2006 to 2010 (74). The health impacts are monetized using a value of statistical life (VSL) of $10.95 million (year 2019 dollars), as recommended by the US EPA (33) and used in previous studies (75). While we use the main estimate of the 3-d window from ref. 32 in our main analysis—as we believe its empirical approach carefully accounts for the confounding biases—we also calculate the health impacts on premature mortality using alternative CRFs from refs. 76–78 and estimates from ref. 32 using different time windows (SI Appendix, Fig. S18).

### Projecting Future Impacts

We project the future drought-induced electricity generation and emissions (CO2, NOx, and SO2) from fossil fuel plants that are still in operation in 2021, under future climate and electricity sector scenarios. We select the year 2035 and 2050 as our projection points to capture both the potential near-term and medium-term energy transitions.

Future damages are calculated using SCC, SC-CH4, and VSL adjusted for future climate damages and income growth. These future damages are then discounted back to the year 2020 using a discount rate of 2.5%. For SCC, we use the values of $158 per ton (emissions year 2035) and $205 per ton (emissions year 2050). For SC-CH4, we use the values of $2,313 per ton (emissions year 2035) and $3,547 per ton (emissions year 2050). Both values are derived from the latest US EPA report, calculated using a 2.5% discount rate (34). For the air quality impacts, we use the derived empirical relationship between surface PM2.5 and drought-induced emissions and project the mortalities using CRFs from ref. 32 and future projected population for the 65+ age group (79). For VSL, we follow a similar method from Carleton et al. (75) to calculate the future VSL values using the projected economic growth in the United States from the OECD-ENV model under the SSP3 scenario (80) and income elasticity of one.

### Future Electricity Sector Scenarios

For the electricity sector scenarios, we construct highly stylized scenarios to quantify the impacts of future drought under potential changes in the electricity sector (Table 1). These scenarios are not designed to correspond to any current or proposed policies but rather to reflect potential comparative changes in the electricity system.

We examine the following scenarios: 1) the *reference* scenario which assumes no changes in the electricity sector; 2) the *coal phase-out* scenario which assumes a partial or full phase-out of coal power plants in the electricity grid and retired coal plants are replaced by new natural gas plants; 3) the *CCS penetration* scenario which assumes that some natural gas plants are retrofitted with CCS **on top of** the *coal phase-out* scenario; and 4) the *high RE* scenario which examines the impacts of expanding renewable energy sources and battery technology.

For the *coal phase-out* scenario, we assume 50% of the coal generation in 2035, and 100% of the coal generation in 2050 is replaced by natural gas plants with average emission factors within each region. For the *CCS* scenario, we use the modeling results from the Princeton Net Zero America study (37) which projects the amount of electricity generated using natural gas with and without the CCS technology. Averaged across their four scenarios (E+, E-, E+RE-, E-B+), 10.7% and 68.5% of the US gas electricity generation is projected to be generated by plants with CCS technology in 2035 and 2050, respectively.

For the *high RE* scenario, we use the hourly simulation outputs from the Cambium data from the National Renewable Energy Laboratory (36). As the model simulates the marginal energy source for each hour and each Balancing Authority Area, we calculate the time percentage for which the fossil energy is on the margin for each region. We assume that when nonfossil energy is on the margin, the drought-induced electricity gap will be provided by the nonfossil energy and thus results in zero drought-induced emission (see SI Appendix for more details).

### Future Climate Change Scenarios

For future climate change scenarios, we use the projected runoff values (surface + subsurface) from the Coupled Model Intercomparison Project Phase 6 (CMIP6). We examine three primary climate-forcing scenarios featured by the IPCC, which were constructed as pairs between the Shared Socio-economic Pathways (SSPs) and the Representative Concentration Pathways (RCPs) (81). We use SSP1-2.6 (which the IPCC refers to as the "Low" scenario), SSP2-4.5 (which the IPCC refers to as the "Intermediate" scenario), and SSP3-7.0 (which the IPCC refers to as the "high" scenario). We use projections from 33 global climate models with available runoff output at the monthly level for the historical and future scenarios (SI Appendix, Table S4). Only one ensemble variant is selected for each model—we use the first ensemble variant of each model ("r1i1p1f1") when possible. To be consistent with our empirical analysis, for each climate model, we first calculate the regional monthly runoff values by taking the weighted average of the state-level runoff weighted by the hydropower capacity (capacity is fixed at the 2021 level). We then calculate the 9-mo moving average values for each region and calculate the monthly anomalies relative to the monthly averages derived from the historical simulation (1980 to 2014) of each model. We use the average runoff anomalies from 2030 to 2059, for each climate model and climate scenario.

---

## Figures and Tables

**Fig. 1.** Drought conditions and the electricity system in the western United States. (A) The declining trend of regional runoff anomalies of the western United States from 1980 to 2021. (B) Relationship between monthly hydro generation anomalies (deviations relative to the monthly mean) and monthly runoff anomalies in the western United States. (C) Fossil fuel power plants in the western United States in our sample during the studied period (2001 to 2021). The western United States is divided into three electricity regions: California (CA), Northwest (NW), and Southwest (SW). Pie charts in C show the percentage of electricity generation from different generating technologies, averaged over 2001 to 2021 (the size of the pie is proportional to the total electricity generation in each region).

**Fig. 2.** Drought increases electricity generation from fossil fuel plants with substantial transboundary effects. (A–C) Relative changes in monthly fossil generation in each region due to runoff changes in our study period. The X axis is sorted by the changes in fossil fuel generation, from months with the lowest runoff on the left to the months with the highest runoff on the right. Black lines show the "local effect" which only accounts for the impact of runoff on power plants in the same region. Orange lines show the "total effect" which accounts for the impacts resulting from runoff changes in all three regions. (D–F) Changes in fossil generation in one electricity region (each panel) due to the 5th to 95th percentile change of runoff anomalies (i.e., changes under dry conditions relative to wet conditions) in each of the three regions (x axis of each panel). The shades in panels (A–C) and error bars in (D–F) show the 95% CI of the estimated generation changes.

**Fig. 3.** Drought-induced emissions increase nearby surface PM2.5 concentration. (A) Predicted drought-induced emissions (SO2 + NOx) from each fossil plant due to runoff anomalies in 2001, an extremely dry year. Colors show the percentage changes relative to the total plant emissions in 2001. (B) Illustration of our method to quantify impacts of drought-induced emissions on PM2.5 concentration measured at surface air quality monitors, using a specific monitor in Washington as an example. For each monitor, we calculate total drought-induced emissions from all fossil fuel plants within a given distance of the monitor (e.g., 100 km) and quantify the impacts on surface air quality due to changes in emissions within that distance. (C) shows the impacts of drought-induced emission from power plants in each distance bin on surface PM2.5 measured at the monitors (the bars show the 95% CI).

**Fig. 4.** Monetized economic and health impacts of drought-induced fossil fuel generation. (A) Monetized damages from extra CO2 emissions, CH4 leakage, and PM2.5-related mortalities, due to runoff changes (relative to the 1980 to 2021 average). Monetized values are calculated using a social cost of carbon value of $117 per ton, a social cost of methane value of $1,257 per ton (year 2020 dollars) from US EPA (34), and a value of statistical life of $10.95 million per mortality (year 2019 dollars). (B) Declines in annual monetized damages over time are a result of declining emissions factors (i.e., emissions per unit energy production) over the western United States (2021 values are normalized to 1). (C) Total damages of the 2012 to 2016 drought in California, compared to estimates of the direct economic impacts from the prior literature due to reductions in hydropower and the increased electricity demand (27, 28). CO2 damages are calculated using two SCC values, $117 per ton as in A and $193 per ton (under a 2% discount rate following ref. 43). In C, we only calculate the impacts originating from fossil fuel plants in CA and impacts in other regions due to the runoff changes in CA.

**Fig. 5.** Future damages of drought-induced fossil generation could be mitigated under low GHG scenarios and lower-carbon electricity sector scenarios. (A) Annual drought-induced damages projected by 33 climate models under the SSP3-7.0 scenario over 2030 to 2059 (relative to the 1980 to 2014 average of each model). (B) Declines in monetized damages under low GHG scenarios (SSP1-2.6 and SSP2-4.5), relative to the SSP3-7.0 scenario. (C) Projected electricity sector transitions reduce drought-induced damages at varying magnitudes (mean values of the 33 models under the SSP3-7.0). (D) Increasing importance of the drought-induced GHG emissions relative to the total GHG emissions from the electricity sector, under the *high RE* scenario. GHG emissions included the CO2 emissions and potential CH4 leakage (aggregated using the global warming potential of 100 y). Drought-induced emissions are calculated using the average runoffs in 2030 to 2059 (Left panel, "average year") or the 10th percentile lowest runoffs during 2030 to 2059 (Right panel, "dry year").

**Table 1. Electricity sector scenarios.**

| Scenarios | 2035 | 2050 |
|---|---|---|
| Reference | No change (same as 2021) | No change (same as 2021) |
| Coal phase-outs | 50% coal replaced by average gas plants | 100% coal replaced by average gas plants |
| CCS penetration | 10.7% gas generation with CCS | 68.5% gas generation with CCS |
| High RE | calculating using %hours of fossil energy on the margin (derived from the NREL hourly simulation results) | — |

*Note: Coal phase-out scenarios assume that the coal power plants are replaced by natural gas plants in the same location. The CCS penetration scenario assumes that some natural gas plants are retrofitted with CCS on top of the coal phase-out scenario. The penetration and removal rate of CCS (removal rate: 90%) are derived from the Princeton Net Zero America study (37). The high RE scenario uses the hourly simulation outputs from the Cambium data from the National Renewable Energy Laboratory (36), which simulates the marginal energy source for each hour in each Balancing Authority Area.*

---

## Data, Materials, and Software Availability

Code and data needed to replicate the results data have been deposited in GitHub (https://github.com/mhqiu/drought-electricity-WUS).

## Acknowledgments

We thank Brandon de la Cuesta for helpful discussions on the mediation analysis. We thank Carlos F. Gould, Jessica Li, and members of Stanford ECHOLab and Center on Food Security and the Environment for helpful comments. Some of the computing for this project was performed on the Stanford Sherlock cluster, and we would like to thank Stanford University and the Stanford Research Computing Center for providing computational resources and support that contributed to these research results. N.S.D. acknowledges the support from Stanford University. M.Q. acknowledges the support from the planetary health fellowship at Stanford's Center for Innovation in Global Health.

## Author Contributions

M.Q., N.R., I.M.L.A., N.S.D., and M.B. designed research; M.Q. performed research; M.Q. and N.R. contributed new reagents/analytic tools; M.Q. and M.B. analyzed data; and M.Q., N.R., I.M.L.A., N.S.D., and M.B. wrote the paper. The authors declare no competing interest.

---

## References

1. D. Dodman et al., "Cities, Settlements and Key Infrastructure" in *Climate Change 2022: Impacts, Adaptation and Vulnerability*. Contribution of Working Group II to the Sixth Assessment Report of the IPCC, H.-O. Pörtner, Eds. (Cambridge University Press, 2022) pp. 907–1040.
2. R. Schaeffer et al., Energy sector vulnerability to climate change: A review. *Energy* **38**, 1–12 (2012).
3. M. T. Van Vliet, D. Wiberg, S. Leduc, K. Riahi, Power-generation system vulnerability and adaptation to changes in climate and water resources. *Nat. Clim. Change* **6**, 375–380 (2016).
4. J. Cronin, G. Anandarajah, O. Dessens, Climate change impacts on the energy system: A review of trends and gaps. *Clim. Change* **151**, 79–93 (2018).
5. D. M. Ward, The effect of weather on grid systems and the reliability of electricity supply. *Clim. Change* **121**, 103–113 (2013).
6. M. Auffhammer, P. Baylis, C. H. Hausman, Climate change is projected to have severe impacts on the frequency and intensity of peak electricity demand across the United States. *PNAS* **114**, 1886–1891 (2017).
7. A. Rode et al., Estimating a social cost of carbon for global energy consumption. *Nature* **598**, 308–314 (2021).
8. M. D. Bartos, M. V. Chester, Impacts of climate change on electric power supply in the Western United States. *Nat. Clim. Change* **5**, 748–752 (2015).
9. M. T. Van Vliet, J. Sheffield, D. Wiberg, E. F. Wood, Impacts of recent drought and warm years on water resources and electricity supply worldwide. *Environ. Res. Lett.* **11**, 124021 (2016).
10. I. Tobin et al., Vulnerabilities and resilience of European power generation to 1.5 °C, 2 °C and 3 °C warming. *Environ. Res. Lett.* **13**, 044024 (2018).
11. E. D. Coffel, J. S. Mankin, Thermal power generation is disadvantaged in a warming world. *Environ. Res. Lett.* **16**, 024043 (2021).
12. S. G. Yalew et al., Impacts of climate change on energy systems in global and regional scenarios. *Nat. Energy* **5**, 794–802 (2020).
13. W. Wan, J. Zhao, E. Popat, C. Herbert, P. Döll, Analyzing the impact of streamflow drought on hydroelectricity production: A global-scale study. *Water Resour. Res.* **57**, e2020WR028087 (2021).
14. E. A. Byers, G. Coxon, J. Freer, J. W. Hall, Drought and climate change impacts on cooling water shortages and electricity prices in Great Britain. *Nat. Commun.* **11**, 1–12 (2020).
15. S. W. Turner, N. Voisin, J. Fazio, D. Hua, M. Jourabchi, Compound climate events transform electrical power shortfall risk in the Pacific Northwest. *Nat. Commun.* **10**, 1–8 (2019).
16. D. L. Donaldson, D. M. Piper, D. Jayaweera, Temporal solar photovoltaic generation capacity reduction from wildfire smoke. *IEEE Access* **9**, 79841–79852 (2021).
17. F. Petrakopoulou, A. Robinson, M. Olmeda-Delgado, Impact of climate change on fossil fuel power-plant efficiency and water use. *J. Cleaner Prod.* **273**, 122816 (2020).
18. P. L. Joskow, California's electricity crisis. *Oxford Rev. Econ. Policy* **17**, 365–388 (2001).
19. N. Voisin et al., Impact of climate change on water availability and its propagation through the Western US power grid. *Appl. Energy* **276**, 115467 (2020).
20. N. S. Diffenbaugh, D. L. Swain, D. Touma, Anthropogenic warming has increased drought risk in California. *PNAS* **112**, 3931–3936 (2015).
21. A. P. Williams et al., Large contribution from anthropogenic warming to an emerging North American megadrought. *Science* **368**, 314–318 (2020).
22. U.S. EPA, *Emissions and Generation Resource Integrated Database (eGRID) 2019* (USEPA, 2019).
23. B. Cook et al., Twenty-first century drought projections in the CMIP6 forcing scenarios. *Earth's Future* **8**, e2019EF001461 (2020).
24. J. Lund, J. Medellin-Azuara, J. Durand, K. Stone, Lessons from California's 2012–2016 drought. *J. Water Resour. Plann. Manage.* **144**, 04018067 (2018).
25. Y. Su, J. D. Kern, P. M. Reed, G. W. Characklis, Compound hydrometeorological extremes across multiple timescales drive volatility in California electricity market prices and emissions. *Appl. Energy* **276**, 115541 (2020).
26. J. Hill, J. Kern, D. E. Rupp, N. Voisin, G. Characklis, The effects of climate change on interregional electricity market dynamics on the US West Coast. *Earth's Future* **9**, e2021EF002400 (2021).
27. J. D. Kern, Y. Su, J. Hill, A retrospective study of the 2012–2016 California drought and its impacts on the power sector. *Environ. Res. Lett.* **15**, 094008 (2020).
28. P. Gleick et al., *Impacts of California's Five-Year (2012–2016) Drought on Hydroelectricity Generation* (Pacific Institute, 2017).
29. E. Hardin et al., California drought increases CO2 footprint of energy. *Sustainable Cities Soc.* **28**, 450–452 (2017).
30. J. E. Herrera-Estrada, N. S. Diffenbaugh, F. Wagner, A. Craft, J. Sheffield, Response of electricity sector air pollution emissions to drought conditions in the Western United States. *Environ. Res. Lett.* **13**, 124032 (2018).
31. J. Eyer, C. J. Wichman, Does water scarcity shift the electricity generation mix toward fossil fuels? Empirical evidence from the United States. *J. Environ. Econ. Manage.* **87**, 224–241 (2018).
32. T. Deryugina, G. Heutel, N. H. Miller, D. Molitor, J. Reif, The mortality and medical costs of air pollution: Evidence from changes in wind direction. *Am. Econ. Rev.* **109**, 4178–4219 (2019).
33. U.S. EPA, *Regulatory Impact Analysis for the Clean Power Plan Final Rule* (USEPA, 2015).
34. USEPA, *Report on the Social Cost of Greenhouse Gases: Estimates Incorporating Recent Scientific Advances* (USEPA, 2022).
35. T. A. Deetjen, I. L. Azevedo, Climate and health benefits of rapid coal-to-gas fuel switching in the US power sector offset methane leakage and production cost increases. *Environ. Sci. Technol.* **54**, 11494–11505 (2020).
36. P. Gagnon, W. Frazier, W. Cole, E. Hale, "Cambium documentation: Version 2021" (No. NREL/TP-6A40-81611, NREL, Golden, CO, 2021).
37. E. Larson et al., "Net-zero America: Potential pathways, infrastructure, and impacts, final report" (Princeton University, 2020).
38. U.S. Energy Information Administration, *Hourly Electric Grid Monitor* (USEIA, 2021).
39. T. W. Juliano et al., Smoke from 2020 United States wildfires responsible for substantial solar energy forecast errors. *Environ. Res. Lett.* **17**, 034010 (2022).
40. S. D. Gilletly, N. D. Jackson, A. Staid, "Quantifying wildfire-induced impacts to photovoltaic energy production in the Western United States" in *2021 IEEE 48th Photovoltaic Specialists Conference (PVSC)* (IEEE, 2021), pp. 1619–1625.
41. L. Lledó, O. Bellprat, F. J. Doblas-Reyes, A. Soret, Investigating the effects of Pacific Sea surface temperatures on the wind drought of 2015 over the United States. *J. Geophys. Res. Atmos.* **123**, 4837–4849 (2018).
42. C. W. Tessum, J. D. Hill, J. D. Marshall, InMAP: A model for air pollution interventions. *PLoS ONE* **12**, e0176131 (2017).
43. T. Carleton, M. Greenstone, A guide to updating the US government's social cost of carbon. *Rev. Environ. Econ. Policy* **16**, 196–218 (2022).
44. J. A. De Gouw, D. D. Parrish, G. J. Frost, M. Trainer, Reduced emissions of CO2, NOx, and SO2 from US power plants owing to switch from coal to natural gas with combined cycle technology. *Earth's Future* **2**, 75–82 (2014).
45. J. A. Burney, The downstream air pollution impacts of the transition from coal to natural gas in the United States. *Nat. Sustainability* **3**, 152–160 (2020).
46. D. Touma, M. Ashfaq, M. A. Nayak, S. C. Kao, N. S. Diffenbaugh, A multi-model and multi-index evaluation of drought characteristics in the 21st century. *J. Hydrol.* **526**, 196–207 (2015).
47. A. L. Swann, F. M. Hoffman, C. D. Koven, J. T. Randerson, Plant responses to increasing CO2 reduce estimates of climate impacts on drought severity. *PNAS* **113**, 10019–10024 (2016).
48. J. S. Mankin, R. Seager, J. E. Smerdon, B. I. Cook, A. P. Williams, Mid-latitude freshwater availability reduced by projected vegetation responses to climate change. *Nat. Geosci.* **12**, 983–988 (2019).
49. A. Miara et al., Climate-water adaptation for future US electricity infrastructure. *Environ. Sci. Technol.* **53**, 14029–14040 (2019).
50. J. Wessel, J. D. Kern, N. Voisin, K. Oikonomou, J. Haas, Technology pathways could help drive the US West Coast grid's exposure to hydrometeorological uncertainty. *Earth's Future* **10**, e2021EF002187 (2022).
51. D. W. Abel et al., Air-quality-related health impacts from climate change and from adaptation of cooling demand for buildings in the Eastern United States: An interdisciplinary modeling study. *PLoS Med.* **15**, e1002599 (2018).
52. D. E. Horton, C. B. Skinner, D. Singh, N. S. Diffenbaugh, Occurrence and persistence of future atmospheric stagnation events. *Nat. Clim. Change* **4**, 698–703 (2014).
53. Y. Wang et al., Adverse effects of increasing drought on air quality via natural processes. *Atmos. Chem. Phys.* **17**, 12827–12843 (2017).
54. P. Achakulwisut et al., Effects of increasing aridity on ambient dust and public health in the US Southwest under climate change. *GeoHealth* **3**, 127–144 (2019).
55. Y. Xie et al., Tripling of Western US particulate pollution from wildfires in a warming climate. *PNAS* **119**, e2111372119 (2022).
56. A. L. Goodkind, C. W. Tessum, J. S. Coggins, J. D. Hill, J. D. Marshall, Fine-scale damage estimates of particulate matter air pollution reveal opportunities for location-specific mitigation of emissions. *PNAS* **116**, 8775–8780 (2019).
57. M. Qiu, C. M. Zigler, N. E. Selin, Impacts of wind power on air quality, premature mortality, and exposure disparities in the United States. *Sci. Adv.* **8**, eabn8762 (2022).
58. J. Sheffield, E. F. Wood, M. L. Roderick, Little change in global drought over the past 60 years. *Nature* **491**, 435–438 (2012).
59. B. Stone Jr et al., Compound climate and infrastructure events: How electrical grid failure alters heat wave risk. *Environ. Sci. Technol.* **55**, 6957–6964 (2021).
60. I. Ahmed, P. Parikh, G. Sianjase, D. Coffman, The impact decades-long dependence on hydropower in El Niño impact-prone Zambia is having on carbon emissions through backup diesel generation. *Environ. Res. Lett.* **15**, 124031 (2020).
61. J. Yang, Y. Huang, K. Takeuchi, Does drought increase carbon emissions? Evidence from Southwestern China. *Ecol. Econ.* **201**, 107564 (2022).
62. N. Wu et al., Daily emission patterns of coal-fired power plants in China based on multisource data fusion. *ACS Environ. Au* **2**, 363–372 (2022).
63. M. A. Cole, R. J. Elliott, E. Strobl, Climate change, hydro-dependency, and the African Dam Boom. *World Dev.* **60**, 84–98 (2014).
64. K. E. Gannon et al., Business experience of floods and drought-related water and electricity supply disruption in three cities in sub-Saharan Africa during the 2015/2016 El Niño. *Global Sust.* **1**, E14 (2018).
65. U.S. EPA, *Air Markets Program Data (AMPD)* (USEPA, 2021).
66. U.S. EPA, *Emissions and Generation Resource Integrated Database (eGRID) 2019* (USEPA, 2019).
67. K. E. Trenberth et al., Global warming and changes in drought. *Nat. Clim. Change* **4**, 17–22 (2014).
68. Y. Xia et al., Continental-scale water and energy flux analysis and validation for the North American land data assimilation system project phase 2 (NLDAS-2): 1. Intercomparison and application of model products. *J. Geophys. Res. Atmos.* **117**, D03109 (2012).
69. Y. Xia et al., Continental-scale water and energy flux analysis and validation for North American land data assimilation system project phase 2 (NLDAS-2): 2. Validation of model-simulated streamflow. *J. Geophys. Res. Atmos.* **117**, D03110 (2012).
70. D. Tingley, T. Yamamoto, K. Hirose, L. Keele, K. Imai, Mediation: R package for causal mediation analysis. *J. Stat. Software* **59**, 1–38 (2014).
71. U.S. EPA, *Air Data: Air Quality Data Collected at Outdoor Monitors Across the US* (USEPA, 2022).
72. M. L. Childs et al., Daily local-level estimates of ambient wildfire smoke PM2.5 for the contiguous US. *Environ. Sci. Technol.* **56**, 13607–13621 (2022).
73. H. K. Pullabhotla, M. Zahid, S. Heft-Neal, V. Rathi, M. Burke, Global biomass fires and infant mortality. *PNAS* **120**, e2218210120 (2023).
74. U.S. Census Bureau, *U.S. Population by Gender and Age groups (ACS 5-Year Estimates, 2006–2010)* (2010).
75. T. Carleton et al., Valuing the global mortality consequences of climate change accounting for adaptation costs and benefits. *Q. J. Econ.* **137**, 2037–2105 (2022).
76. Q. Di et al., Association of short-term exposure to air pollution with mortality in older adults. *JAMA* **318**, 2446–2456 (2017).
77. C. Liu et al., Ambient particulate air pollution and daily mortality in 652 cities. *N. Engl. J. Med.* **381**, 705–715 (2019).
78. P. Orellano, J. Reynoso, N. Quaranta, A. Bardach, A. Ciapponi, Short-term exposure to particulate matter (PM10 and PM2.5), nitrogen dioxide (NO2), and ozone (O3) and all-cause and cause-specific mortality: Systematic review and meta-analysis. *Environ. Int.* **142**, 105876 (2020).
79. U.S. Census Bureau, *The 2017 National Population Projections* (2018).
80. R. Dellink, J. Chateau, E. Lanzi, B. Magné, Long-term economic growth projections in the shared socioeconomic pathways. *Global Environ. Change* **42**, 200–214 (2017).
81. IPCC, *Summary for Policymakers*, V. Masson-Delmotte et al., Eds. (Cambridge University Press, 2021), pp. 3–32.
<!--kb:end-->
