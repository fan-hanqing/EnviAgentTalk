import sys, json

# Specific energy consumption of brackish water desalination, digitised from
# Fig. 3 of Patel, Lee, Westerhoff & Elimelech, Water Research 250 (2024)
# 121009.  The source computed these FIVE feed salinities only; values between
# them are linear interpolation, which is ours, not the source's.
#
# The source states salinity in g/L.  Converted here at 1 g/L = 1000 ppm, i.e.
# assuming a solution density of 1 kg/L.  Over 1-10 g/L the true density rises
# to about 1.007 kg/L, so this understates ppm by at most 0.7% -- an order of
# magnitude below the digitisation error, but it is an assumption, not an
# identity.
#
# Both axes of the source figure are linear, so the interpolation is linear in
# (ppm, kWh/m3) -- the space the figure was drawn in.
NODES = {
    "ED": [(1000, 0.0846), (3000, 0.7618), (5000, 1.2508),
           (7000, 1.7962), (10000, 2.7743)],
    "RO": [(1000, 0.3197), (3000, 0.5549), (5000, 0.7806),
           (7000, 0.9969), (10000, 1.4577)],
}
LO, HI = 1000.0, 10000.0

a = json.load(sys.stdin)
try:
    ppm = a["feed_ppm"]
    t = a["technology"]
except KeyError as e:
    sys.exit("missing required argument %s; both feed_ppm and technology are "
             "required and neither has a default" % e)

if not isinstance(ppm, (int, float)) or isinstance(ppm, bool):
    sys.exit("feed_ppm must be a number, in ppm TDS")

t = str(t).strip().upper()
if t not in NODES:
    sys.exit("technology %r is not one of RO, ED. The source models only these "
             "two for brackish water. Its third curve, 'optimized ED', is a "
             "hypothetical membrane-improvement case and is deliberately not "
             "offered here." % t)

if ppm < LO or ppm > HI:
    sys.exit(
        "feed_ppm %g is outside 1000-10000 ppm (1-10 g/L), the brackish range "
        "the source modelled. This tool does not extrapolate. Below 1000 ppm "
        "the water is not brackish; above 10000 ppm neither the fixed 80%% "
        "recovery nor the cost-optimised productivities behind these numbers "
        "still hold." % ppm)

pts = NODES[t]
for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
    if x0 <= ppm <= x1:
        sec = y0 + (y1 - y0) * (ppm - x0) / (x1 - x0)
        break

json.dump({"sec_kwh_per_m3": round(sec, 4)}, sys.stdout)
