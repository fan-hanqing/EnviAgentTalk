"""PDF -> knowledge-base .md.

Usage:
    pip install pdfplumber
    python pdf2md.py fan  paper.pdf  paper_HanqingFan.md
    python pdf2md.py yang paper.pdf  paper_MeiqiYang.md

What it does:
  1. Layout-aware extraction. Pages are partitioned by tinted panels (Nature's BOXes),
     each region is split into columns, and paragraph boundaries come from first-line
     indent and bold/regular switches. Without this, a full-width BOX and the body
     text underneath it interleave line by line.
  2. Superscript citations are removed by font size and baseline position, so
     "membranes20,21" loses its citation but "Figure 2" and "seed 220" survive.
  3. References, acknowledgements and author information never enter the knowledge base.
  4. Figure captions are collected into a Figure captions section at the end.

Adapting it to a new paper:
  The heading lists in the two build functions (FAN_H2 / FAN_H3, or the numbering
  regexes for Yang) are tied to the journal's layout. Nature-style journals
  (unnumbered, bold subheadings) need the strings in FAN_H2 / FAN_H3 changed;
  ACS-style (1. / 2.1. numbering) usually needs nothing.
  Always eyeball the heading list this prints -- when the layout changes, heading
  detection is the first thing to break, and headings are what determine section
  quality for lookup.
"""
import re, sys, pathlib

try:
    import pdfplumber
except ImportError:
    sys.exit("pdfplumber is required: pip install pdfplumber")


CITE = re.compile(r'(?<=[a-z\)’])\d{1,3}(?:[,–—-]\d{1,3})*(?=[\s.,;:\)’”]|$)')
GLUE = {'ionexchange': 'ion-exchange', 'molecularlevel': 'molecular-level',
        'confinementinduced': 'confinement-induced', 'commercialscale': 'commercial-scale',
        'physicsbased': 'physics-based', 'jumplength': 'jump-length',
        'mixedquality': 'mixed-quality', 'polymersthen': 'polymers, then',
        'model ling': 'modelling', 'ﬀ': 'ff', 'ﬁ': 'fi'}
MATH = re.compile(r'[=≈∝]')


def clean(s):
    s = s.replace('‐', '-').replace('­', '')
    s = re.sub(r'\s+', ' ', s).strip()
    s = CITE.sub('', s)
    for k, v in GLUE.items():
        s = s.replace(k, v)
    return re.sub(r'\s+([.,;:)])', r'\1', s).strip()


def keep(t):
    """Drop stray figure labels; keep equations even though they are short."""
    return len(t) >= 60 or (len(t) >= 5 and MATH.search(t))


CUT = ('References', 'Acknowledgements', 'ASSOCIATED CONTENT', 'AUTHOR INFORMATION', 'REFERENCES')


# ══════════════════════════════════════════════════════════════
# Fan — Nature Water Perspective (unnumbered, bold headings)
# ══════════════════════════════════════════════════════════════
FAN_H2 = ["Macroscopic transport phenomena and models",
          "Microscopic behaviour in nano- and ångström-scale channels",
          "Molecular-level mechanisms in membranes and nanochannels",
          "Bridging molecular, microscopic and macroscopic scales",
          "Outlook"]
FAN_H3 = ["Water transport", "Ion transport", "The challenge", "Nanofluidics—where are we?",
          "Key lessons from nanofluidics",
          "The membrane perspective and limitations of the nanofluidic approach",
          "Ion exclusion in confinement", "Water transport and friction",
          "Relevance to membrane science", "Membrane microstructure",
          "Water transport mechanisms", "Ion transport mechanisms",
          "Limitations of MD simulations"]
FAN_SKIP = re.compile(r'^(Nature Water|Perspective|https://doi|Check for updates|'
                      r'Received:|Accepted:|Published online|A full list of affiliations|e-mail:)')
ONCE = ("Water transport", "Ion transport")


def split_heads(p, seen):
    """A paragraph may be a section heading glued to a subheading. Returns [(level, text)], or None."""
    for h in FAN_H2:
        if p == h:
            return [(2, h)]
        if p.startswith(h + ' '):
            rest = split_heads(p[len(h):].strip(), seen)
            if rest:
                return [(2, h)] + rest
    for h in FAN_H3:
        if p == h and not (h in ONCE and h in seen):
            return [(3, h)]
    return None


def build_fan(ps):
    out, boxes, figs = [], [], []
    box, seen = None, set()
    i = 0
    while i < len(ps):
        p = ps[i]; i += 1
        if p == '@@BOX@@':
            tag = ps[i] if i < len(ps) else 'BOX'
            title = ps[i + 1] if i + 1 < len(ps) else ''
            i += 2
            if i < len(ps) and ps[i][:1].islower():        # heading wrapped: its tail is stuck to the start of the body
                ws = ps[i].split()
                k = next((j for j, w in enumerate(ws) if w[:1].isupper()), len(ws))
                title += ' ' + ' '.join(ws[:k])
                ps[i] = ' '.join(ws[k:])
            box = {"title": f"{tag} · {title}", "parts": []}
            boxes.append(box)
            continue
        if p == '@@ENDBOX@@':
            box = None
            continue
        if FAN_SKIP.match(p):
            continue
        if re.match(r'^Fig\.\s*\d+\s*\|', p):
            cap = [p]
            while i < len(ps) and ps[i][:1].islower():      # caption continuation line
                cap.append(ps[i]); i += 1
            figs.append(re.sub(r'^Fig\.\s*(\d+)\s*\|\s*', r'**Fig. \1** ', ' '.join(cap)))
            continue
        hs = split_heads(p, seen)
        if hs:
            for lv, h in hs:
                seen.add(h)
                (box["parts"] if box else out).append((lv, h))
            continue
        if keep(p):
            (box["parts"] if box else out).append(p)

    for j, x in enumerate(out):          # drop the cover-page header and author block; start at the abstract
        if isinstance(x, str) and x.startswith("Membranes with nanometre"):
            out = out[j:]
            break

    md = ["# A multiscale perspective for understanding transport mechanisms in "
          "desalination and ion-selective membranes", "",
          "*Hanqing Fan, Makenna Parkinson, Kumar Varoon Agrawal, Mihail Barboiu, Lydéric Bocquet, "
          "Bezawit A. Getachew, Qilin Li, Ying Li, Shihong Lin, Chong Liu, Aleksandr Noy, Boya Radha, "
          "Dietmar Schwahn, Anthony Szymczyk, Menachem Elimelech.* "
          "*Nature Water* (2026), Perspective. DOI: 10.1038/s44221-026-00585-1", "",
          "## Abstract", ""]
    intro_done = False
    for x in out:
        if isinstance(x, tuple):
            md += ["#" * x[0] + " " + x[1], ""]
        else:
            md += [x, ""]
            if not intro_done:           # the introduction follows immediately after the abstract
                md += ["## Introduction", ""]
                intro_done = True
    for b in boxes:
        md += [f"## {b['title']}", ""]
        for x in b["parts"]:
            md += (["### " + x[1], ""] if isinstance(x, tuple) else [x, ""])
    if figs:
        md += ["## Figure captions", ""] + [f + "\n" for f in figs]
    return "\n".join(md)


# ══════════════════════════════════════════════════════════════
# Yang — ES&T Article (numbered sections; reading order is scrambled,
# so sections are re-sorted by number)
# ══════════════════════════════════════════════════════════════
YTOP = re.compile(r'^(\d+)\.\s+([A-Z][A-Z ]{3,60}?)(?:\s+[a-z]{1,3})?\s*$')
YSUB = re.compile(r'^(\d+\.\d+)\.\s+([A-Z][A-Za-z0-9 ,\-/&()]{2,95}?)\.\s*(.*)$')
YSKIP = re.compile(r'^(pubs\.acs\.org|Article$|Cite This|ACCESS|Metrics|Read Online|Downloaded|'
                   r'Received:|Revised:|Accepted:|Published:|https?://|© 20|Environ\. Sci\. Technol|'
                   r'Environmental Science & Technology|from$|\d+\s*$|\d{4,5}\s+https)')
SMALL = {'and', 'or', 'of', 'for', 'in', 'to', 'the', 'from', 'with'}


def nicecase(s):
    ws = s.title().split()
    return ' '.join(w if k == 0 or w.lower() not in SMALL else w.lower() for k, w in enumerate(ws))


YSUB2 = re.compile(r'^(\d+\.\d+)\.\s+([A-Z][A-Za-z0-9 ,\-/&()]{3,95})$')


def build_yang(ps):
    secs, figs, front = {}, [], []
    cur, carry = None, None
    for p in ps:
        if carry:                      # previous paragraph was a wrapped heading: pull its tail back out of this one
            head, _, rest = p.partition('. ')
            if len(head.split()) <= 3 and head[:1].isupper():
                secs[carry]["title"] += ' ' + head
                p = rest.strip()
            carry = None
            if not p:
                continue
        if p in ('@@BOX@@', '@@ENDBOX@@') or YSKIP.match(p):
            continue
        if re.match(r'^Figure\s+\d+\.', p):
            figs.append(re.sub(r'^Figure\s+(\d+)\.\s*', r'**Figure \1.** ', p))
            continue
        m = YTOP.match(p)
        if m:
            cur = m.group(1)
            secs.setdefault(cur, {"title": nicecase(m.group(2)), "parts": []})
            continue
        m = YSUB.match(p)
        if m:
            cur = m.group(1)
            secs.setdefault(cur, {"title": m.group(2), "parts": []})
            if keep(m.group(3)):
                secs[cur]["parts"].append(m.group(3).strip())
            continue
        m = YSUB2.match(p)
        if m:
            cur = carry = m.group(1)
            secs.setdefault(cur, {"title": m.group(2), "parts": []})
            continue
        if keep(p):
            (secs[cur]["parts"] if cur else front).append(p)

    md = ["# Machine Learning for Polymer Design to Enhance Pervaporation-Based Organic Recovery", "",
          "*Meiqi Yang, Jun-Jie Zhu, Allyson L. McGaughey, Rodney D. Priestley, Eric M. V. Hoek, "
          "David Jassby, Zhiyong Jason Ren.* "
          "*Environmental Science & Technology* (2024), 58, 10128−10139. "
          "DOI: 10.1021/acs.est.4c00060", "",
          "## Abstract", ""]
    md += [p + "\n" for p in front]
    for k in sorted(secs, key=lambda k: tuple(int(x) for x in k.split('.'))):
        s = secs[k]
        md += [("### " if '.' in k else "## ") + f"{k}. {s['title']}", ""]
        md += [p + "\n" for p in s["parts"]]
    if figs:
        md += ["## Figure captions", ""] + [f + "\n" for f in figs]
    return "\n".join(md)




def lines_of(words, ytol=4.0):
    """Cluster words into lines by y -> [{x0, text, bold}]"""
    rows = []
    for w in sorted(words, key=lambda w: (round(w["top"], 1), w["x0"])):
        if rows and abs(w["top"] - rows[-1][0]) <= ytol:
            rows[-1][1].append(w)
        else:
            rows.append([w["top"], [w]])
    # sub/superscript fragments typeset on their own line (e.g. the B/A subscript of beta) rejoin the line above
    merged = []
    for top, ws in rows:
        txt = "".join(w["text"] for w in ws)
        small = max((w.get("size", 0) for w in ws), default=99)
        if merged and len(txt) <= 6 and small < 0.85 * max(
                (w.get("size", 0) for w in merged[-1][1]), default=0):
            merged[-1][1].extend(ws)
        else:
            merged.append([top, ws])
    rows = merged

    out = []
    for _, ws in rows:
        ws.sort(key=lambda w: w["x0"])
        # drop superscript citations (digit-only, smaller font, sitting high); leave subscripts alone
        big = max((w.get("size", 0) for w in ws), default=0)
        norm = [w["top"] for w in ws if w.get("size", 0) > big * 0.85]
        ref = sorted(norm)[len(norm) // 2] if norm else 0
        ws = [w for w in ws
              if not (w.get("size", 0) < big * 0.85
                      and re.fullmatch(r"[\d,\u2013\u2014-]+", w["text"])
                      and w["top"] < ref + 0.5)]
        if not ws:
            continue
        n = sum(len(w["text"]) for w in ws) or 1
        b = sum(len(w["text"]) for w in ws
                if re.search(r"bold|semibold|black", w.get("fontname", ""), re.I))
        out.append({"x0": ws[0]["x0"], "text": " ".join(w["text"] for w in ws),
                    "bold": b / n > 0.6})
    return out


def join(chunk):
    """Join the lines of a paragraph, undoing end-of-line hyphenation."""
    s = ""
    for t in chunk:
        if s.endswith("-") and t[:1].islower():
            s = s[:-1] + t
        elif s:
            s += " " + t
        else:
            s = t
    return s


def paras(rows, indent=3.0):
    """New paragraph on first-line indent, or on a bold/regular switch (a heading)."""
    if not rows:
        return []
    base = min(r["x0"] for r in rows)
    out, cur, prev_bold = [], [], None
    for r in rows:
        if cur and (r["x0"] > base + indent or (prev_bold is not None and r["bold"] != prev_bold)):
            out.append(join(cur)); cur = []
        cur.append(r["text"]); prev_bold = r["bold"]
    if cur:
        out.append(join(cur))
    return out


def page_text(page):
    W, H = page.width, page.height
    words = page.extract_words(keep_blank_chars=False, use_text_flow=False, x_tolerance=1.5,
                               extra_attrs=["size", "fontname"])
    boxes = [r for r in page.rects
             if (r["x1"] - r["x0"]) > 0.6 * W and (r["bottom"] - r["top"]) > 0.08 * H
             and r.get("fill")]
    boxes.sort(key=lambda r: r["top"])

    # slice the page into horizontal bands: panel / non-panel
    cuts, y = [], 0.0
    for b in boxes:
        if b["top"] > y + 2:
            cuts.append((y, b["top"], False))
        cuts.append((b["top"], b["bottom"], True))
        y = b["bottom"]
    if y < H:
        cuts.append((y, H, False))

    chunks = []
    for y0, y1, is_box in cuts:
        band = [w for w in words if y0 - 1 <= (w["top"] + w["bottom"]) / 2 <= y1 + 1]
        if not band:
            continue
        # cluster into rows first, then decide whether each row spans both columns or belongs to one
        mid = W / 2
        rows = []
        for w in sorted(band, key=lambda w: (round(w["top"], 1), w["x0"])):
            if rows and abs(w["top"] - rows[-1][0]) <= 4.0:
                rows[-1][1].append(w)
            else:
                rows.append([w["top"], [w]])

        ps, lbuf, rbuf, wbuf = [], [], [], []

        def flush_wide():
            if wbuf:
                ps.extend(paras(lines_of(wbuf)))
                wbuf.clear()

        def flush_cols():
            flush_wide()
            for buf in (lbuf, rbuf):
                if buf:
                    ps.extend(paras(lines_of(buf)))
                buf.clear()

        for _, ws in rows:
            ws.sort(key=lambda w: w["x0"])
            L = [w for w in ws if w["x1"] <= mid]
            R = [w for w in ws if w["x1"] > mid]
            gutter = (R[0]["x0"] - L[-1]["x1"]) if (L and R) else 99
            if any(w["x0"] < mid < w["x1"] for w in ws) or gutter < 8:   # full-width row
                if lbuf or rbuf:
                    flush_cols()
                wbuf.extend(ws)
            else:
                flush_wide()
                lbuf.extend(L)
                rbuf.extend(R)
        flush_cols()
        if not ps:
            continue
        if is_box:
            chunks.append("@@BOX@@")
        chunks += ps
        if is_box:
            chunks.append("@@ENDBOX@@")
    return chunks




def extract(path):
    chunks = []
    with pdfplumber.open(path) as pdf:
        for pg in pdf.pages:
            chunks += page_text(pg)
    return chunks


def prep(chunks):
    ps = [clean(x) for x in chunks if x.strip()]
    for i, x in enumerate(ps):
        if x.startswith(CUT):
            return ps[:i]
    return ps


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("fan", "yang"):
        sys.exit(__doc__)
    kind, src, dst = sys.argv[1:]
    ps = prep(extract(src))
    md = build_fan(ps) if kind == "fan" else build_yang(ps)
    pathlib.Path(dst).write_text(md, encoding="utf-8")
    print(f"{dst}  {len(md):,} chars")
    for h in [l for l in md.split("\n") if l.startswith("#")]:
        print("   ", h)
