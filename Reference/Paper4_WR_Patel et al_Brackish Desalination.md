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
