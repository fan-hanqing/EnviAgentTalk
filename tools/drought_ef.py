"""Carbon intensity of the fossil generation that drought calls up, by western
US state, 2021.

Normal operation reads one JSON object on stdin and writes one on stdout, and
uses only the standard library. The table it reads, drought_ef_2021.csv, is a
pure aggregation of Data/intermediate/unit_drought_emis_historical.rds from
Qiu et al.'s replication repository; see drought_ef.build.md.

To regenerate that table from the source file:

    python drought_ef.py --rebuild /path/to/unit_drought_emis_historical.rds

That path needs pandas and pyreadr, which are imported only inside it, so the
tool itself still runs on a machine that has neither. The harness never sets
argv, so this branch is unreachable from a tool call.
"""
import sys, json, csv, os

HERE  = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "drought_ef_2021.csv")

YEAR = 2021
T = 0.453592 * 2          # short ton -> tonne (us_to_metric_ton in the source scripts)
MIN_UNIT_MWH = 1000       # a unit must generate this much in the year to define a rate
MIN_PLANTS = 3            # below this the "state margin" is one operator, not a fleet


def rebuild(src):
    """Recompute drought_ef_2021.csv from the source .rds.

    Nothing here is fitted or assumed. Every column is a sum, a ratio, or a
    min/max over columns already present in that file.
    """
    import pyreadr, numpy as np                      # noqa: local to this path

    d = pyreadr.read_r(src)[None]
    y = d[d.year == YEAR].copy()

    # per-unit OBSERVED emission rate -> the physical range the weighted mean
    # must lie in
    u = (y.groupby(["state", "orispl", "unitid"])
           .agg(L=("grossload_mw", "sum"), C=("co2_mass_tons", "sum")).reset_index())
    u = u[u.L >= MIN_UNIT_MWH]
    u["rate"] = u.C / u.L * T
    b = (u.groupby("state")
           .agg(n_units=("rate", "size"), n_plants=("orispl", "nunique"),
                unit_rate_min=("rate", "min"), unit_rate_max=("rate", "max")).reset_index())

    # state aggregates of the drought-induced increments
    g = (y.groupby("state")
           .agg(gen_total_MWh=("gen_total", "sum"),
                co2_total_short_tons=("co2_total", "sum"),
                grossload_MWh=("grossload_mw", "sum"),
                unit_months=("gen_total", "size")).reset_index())
    pos = y.gen_total.clip(lower=0).groupby(y.state).sum()
    neg = (-y.gen_total).clip(lower=0).groupby(y.state).sum()
    g["coherence"] = ((pos - neg).abs() / (pos + neg)).values

    o = g.merge(b, on="state")
    o["ef_kg_co2_per_kwh"] = np.where(o.gen_total_MWh > 0,
                                      o.co2_total_short_tons / o.gen_total_MWh * T, np.nan)
    o = o[["state", "n_plants", "n_units", "unit_months", "gen_total_MWh",
           "co2_total_short_tons", "grossload_MWh", "coherence",
           "unit_rate_min", "unit_rate_max", "ef_kg_co2_per_kwh"]]
    o.round(6).to_csv(TABLE, index=False)
    sys.stderr.write("wrote %s (%d states)\n" % (TABLE, len(o)))


if len(sys.argv) > 1:
    if sys.argv[1] == "--rebuild" and len(sys.argv) == 3:
        rebuild(sys.argv[2])
        raise SystemExit(0)
    raise SystemExit("usage: drought_ef.py [--rebuild <unit_drought_emis_historical.rds>]\n"
                     "with no arguments, reads one JSON object on stdin")

rows = {}
with open(TABLE) as f:
    for r in csv.DictReader(f):
        rows[r["state"]] = r

a = json.load(sys.stdin)
try:
    st = str(a["state"]).strip().upper()
except KeyError:
    sys.exit("missing required argument 'state'; it has no default")

if st not in rows:
    sys.exit(
        "state %r is not in the sample. The source covers the Western "
        "Interconnection only, as the states %s. Texas appears because two El "
        "Paso plants sit in WECC; the rest of Texas is ERCOT and the source "
        "explicitly found NO runoff effect there in a placebo test, so this is "
        "not a gap that better data would fill." % (st, ", ".join(sorted(rows))))

r = rows[st]
G   = float(r["gen_total_MWh"])
C   = float(r["co2_total_short_tons"])
lo  = float(r["unit_rate_min"]); hi = float(r["unit_rate_max"])
coh = float(r["coherence"]); np_ = int(r["n_plants"])

if np_ < MIN_PLANTS:
    sys.exit("%s has only %d fossil plant(s) in the sample; a state-level "
             "marginal intensity built from that is one plant's emission rate, "
             "not a grid margin." % (st, np_))

if G <= 0:
    sys.exit(
        "%s had NEGATIVE drought-induced fossil generation in 2021 (%.0f MWh, "
        "response coherence %.2f): across its units the runoff response "
        "cancelled out rather than adding up. There is no drought margin to "
        "report. This is a property of that state-year, not a missing number."
        % (st, G, coh))

ef = C / G * T

# The intensity is a weighted mean of the state's own units' observed emission
# rates, so with a coherent drought response it MUST fall between the cleanest
# and dirtiest of them.  Falling outside means negative weights dominated the
# sum.  This is a physical bound, not a tuned threshold.
if not (lo <= ef <= hi):
    sys.exit(
        "%s: the computed intensity %.3f kg CO2/kWh falls outside the range of "
        "its own units' observed rates (%.3f-%.3f), so opposing responses have "
        "dominated the weighted mean (coherence %.2f). Refusing rather than "
        "returning an unphysical number." % (st, ef, lo, hi, coh))

json.dump({"ef_kg_co2_per_kwh": round(ef, 4),
           "drought_generation_MWh": round(G, 0)}, sys.stdout)
