# Environmental Agent Roundtable

A one-off experiment tool: a roundtable of AI environmental scientists and engineers that you can
interrupt. Two or more agents, each grounded in exactly one knowledge base, take turns on a topic in
a fixed order. Every N rounds the roundtable pauses for the moderator (you) to steer it, then continues.

A knowledge base is just a Markdown file. A research paper is the obvious case, but a thesis, a
technical report, a set of standards, a review or your own working notes all work the same way —
nothing in the tool assumes it is a journal article.

## Run it

**Windows:** double-click **`run.bat`**. It installs the dependencies on first run, clears any
proxy variables for that window, starts the server and opens the browser once `/health` answers.
Keep the black window open — closing it stops the server.

By hand, or on another OS:

```bash
pip install fastapi uvicorn httpx pydantic
python app.py
```

Open http://127.0.0.1:8000

## How it works — ask the README

*How it works* under the title used to dump README.md into an overlay. It now opens a small
assistant that **reads the README and answers from it**, running on the moderator's own slot —
that model is already configured, already meant to be small and cheap, and is not one of the
scientists.

Before the moderator's slot is set up there is nothing to ask with, so the overlay says exactly
that and links to Set API. Once it is set, you get a question box, and a **Open README.md ↗**
button below it for anyone who would rather read the file themselves.

It is told to answer from the README **and nothing else**, to name the section it is drawing on so
you can find it, and to say plainly when the README does not cover something rather than filling
the gap from general knowledge — a confident wrong answer about a tool you are operating is worse
than "it does not say". The whole file goes into the system prompt, so each question costs roughly
ten thousand tokens; that is why it runs on the cheap slot.

## The text-based tool — a knowledge base

The card labels it that way on purpose, and puts it directly above its twin:

```
Text-based Tool · knowledge base (Markdown text of research paper etc.)
Code-based Tool · a script (optional)
```

A method is callable in one of two forms: **structured text, or executable code**. A seat carries
one of each, reached by two different call protocols — `@lookup:` and `@tool:`. The distinction
the whole exercise turns on is not code versus prose; it is whether the thing states the
conditions under which it holds.

### It is a knowledge base, not a prompt

The full text never enters the system prompt. It is used in two stages.

**① Onboarding — once per knowledge base**
Click *Onboard*. The agent reads the whole thing and produces a **scientist profile**
of under 900 words:

```
## Core claims           what this source is really trying to establish
## Method framework      techniques, scales, data sources — the skeleton any extrapolation rests on
## Key evidence          citable numbers, conditions, controls, with the section they came from
## Explicit boundaries   what this source did NOT do, and its admitted limitations
## Voice                 quantitative or mechanistic, cautious or willing to extrapolate
```

The profile is the agent's long-term memory and is what goes into the system prompt. **It is not
shown on the card** — nothing on a seat is edited by hand except its name, field and knowledge
base. It persists in localStorage, it is written into the export, and import fills it back, so a
profile you want to correct is corrected in the exported `.md` and re-imported. Change the
knowledge base and the state line warns you to re-onboard.

**A seat without a profile still runs**, and Start asks you to confirm it rather than blocking.
The prompt then says so outright — *you have not distilled a profile; you have the table of
contents and nothing else; if you have not looked it up in this turn, you do not know it* — which
is a coherent and arguably purer way to run: everything has to be retrieved. What it must never
be is silent. An empty profile presented as *"the profile you distilled"* invites the model to
fill the void from general knowledge and tag it `[GROUNDED]`, which is precisely the failure the
rest of the design exists to catch.

**② Lookup — on demand, mid-dialogue**
The system prompt also carries a **table of contents** of the knowledge base (`§1 Abstract`,
`§5 Results and discussion`, …). When an agent needs a specific number, condition or
exact wording, it isn't allowed to reconstruct it from memory — it has to look it up:

```
@lookup: water permeance friction coefficient
@lookup: §4
```

The frontend intercepts that reply, searches the knowledge base, hands back the matching
sections, and only then does the agent speak. Two lookups max per turn.

Retrieval is **heading-based sectioning + keyword scoring** — no vectors, no
embeddings, no extra dependencies. Sections come from Markdown headings (anything
over 2600 chars is chunked), title matches are weighted, and `§4` works as a direct
address. When nothing matches it says so explicitly, which pushes the agent to admit
it has no basis rather than invent one.

Each lookup shows up in the transcript as a quiet grey line; expand it to see **the
retrieved source text verbatim**. This is one of the most interesting things to watch:
you can see exactly when an agent decides it needs evidence.

> Lookups are scoped to the turn. They don't enter the transcript history and the other
> participants never see them — each reads their own book. To make something stick,
> put it in the profile.

## Code-based Tool (optional)

Each scientist can be given **one script** as an instrument. The collapsed *Code-based Tool
(optional)* section offers two ways to attach one:

**From `tools/`** — a dropdown listing everything in the tool folder, with its state
(*ready*, *no spec*, *conditions missing*). This is the normal path: `tools/` is where the
[Tool creator](#the-tool-creator) writes what it builds, so a tool you assembled in the other tab
appears here the moment you open the dropdown. The section links straight through to it, and once a
tool is selected the link deep-links to that tool (`/toolcreator?tool=damage`).

**By upload** — a `.py` or `.R` that is not in `tools/` yet. It has no specification, so its
conditions of validity are whatever the code happens to say. That is exactly the situation the
Tool creator exists to fix, and the hint under the file box says so.

The scientist runs it mid-turn:

```
@tool: {"permeance_LMH_bar": {"v": 12.4, "src": "source"},
        "pressure_bar":      {"v": 55,   "src": "assumed"},
        "osmotic_bar":       {"v": 25,   "src": "R3"}}
```

Every argument says where its value came from — see
[argument provenance](#argument-provenance--the-agent-does-not-choose-assumed).

The frontend intercepts it exactly like a lookup, runs the script, hands back the output, and only
then does the scientist speak. **Six runs max per turn** — enough to vary an assumed value and
report whether the conclusion moves (see [Tags](#tags-two-independent-questions)).

**The contract is one line each way:** the script reads one JSON object from stdin and writes one
JSON object to stdout.

```python
import sys, json
args = json.load(sys.stdin)
flux = float(args["permeance_LMH_bar"]) * float(args["pressure_bar"])
json.dump({"flux_LMH": round(flux, 3)}, sys.stdout)
```

### The calling card

The card is not shown on the seat either. The scientist does not see the code; it sees a **calling
card**, and so does everyone else at the table — the name, purpose, parameters and return line go into every seat's prompt as the
[instrument roster](#the-instrument-roster--how-the-gap-becomes-visible). `CONDITIONS` stays with
its owner. The card carries the name, purpose, every parameter with its unit and resolution, what
comes back, and an example call. Where it comes from depends on how the tool was attached:

- **From `tools/` with a spec** — the card is *generated from the spec*, with no model call at all.
  It cannot drift from the spec, and it carries two lines an uploaded script cannot produce:

```
CONDITIONS: US contiguous grid, 2017-2021. The damage per kg is a national average and
            is not valid for a single urban plume.
SOURCE: published — Qiu et al., PNAS 2023
```

  Those go into the system prompt, and the prompt makes them binding: *if the card states
  CONDITIONS, they bind you — check the arguments you passed against them before reporting a
  computed number. A tool that runs is not a tool that applies.*

- **From an upload** — the model reads the script at onboarding and writes the card itself. It can
  only describe what the code says, so `CONDITIONS` will be missing or guessed. Which is the
  argument for building the tool in the Tool creator instead of uploading a bare script.

Change the script and the seat's state line says *script changed, re-onboard*.

### Details that matter in practice

- Scripts are written into **`tools/`** next to `app.py` and run with that as the working
  directory. If your script loads a trained model or a lookup table, put the file in `tools/`
  and open it by relative path.
- Python runs with **the same interpreter that runs `app.py`**, so its imports must exist in that
  environment. Launching from your conda env is usually what you want. `.R` tools run with
  `Rscript`.
- Hard timeout of 30 s, output capped at 8000 characters. A hung script cannot hang the roundtable.
- **Failures go back to the model verbatim.** Wrong parameter name, exception, timeout — the
  scientist sees the actual error and its card, and may correct itself once. In testing, a
  deliberately wrong key (`permeance` instead of `permeance_LMH_bar`) was fixed on the retry.

**Security.** This executes code on your machine. It is safe because the server binds to
`127.0.0.1` and the script is one you supplied or accepted. Do not change that binding to
`0.0.0.0` — with this feature enabled, that would be remote code execution on your laptop.

## The tool creator

A script is easy to run and hard to trust. The roundtable will happily call a tool that returns a
confident number outside the range where the method holds, and nothing in the transcript will show
it. So making a tool is a separate activity, on a separate page, with its own standard of care:

    http://127.0.0.1:8000/toolcreator          (or the link under the title)

The page is a **terminal**, not a form. Everything happens in one stream, except the things that
are not conversation — those live in the left column:

- **the tools in `tools/`**, each with a state light. A filled green dot means complete;
  a hollow one means something is still missing (*no spec*, *conditions missing*, *no script*).
  Click a row to load it, **+ New** to start one, and the **✕** on a row to delete it — script,
  specification and assembly log together. A new tool appears at the top of the list as an italic
  *draft* until you `/accept` it; nothing is on disk before that, and the ✕ on a draft row throws
  it away rather than deleting anything.
- **reading material** — papers, replication code, derivations. Attach as many as you need, in one
  pick or several; they accumulate, and the header shows how many and how large.
- **which roundtable seat you are talking to.**

**`/` is you. `@` is the agent.**

```
/draft           print the spec and the code
/run             run every example and report the relative error
/run {"a": 1}    …or run one call with these arguments
/accept          print what the tool declares, and write it into tools/
/discard         throw the draft away
```

Five commands is the whole surface. Making and deleting tools moved into the left column where
they belong; `/new`, `/spec`, `/code`, `/examples`, `/tools`, `/open` and `/clear` still work as
unlisted aliases if you reach for them, but nothing needs them: a bare `/run` means "run the
tests", and everything else is a click.

A one-line status bar above the input is all that is left of a panel:

    damage · ✓ spec · ✓ code · ✓ conditions · ✓ units                       python

### The agent writes its own tool

You are talking to **one of the roundtable's agents**, with the provider settings of that seat's
API slot — so you are assembling the tool with the scientist whose method it is. Attach the paper, the
replication code, the derivation, and say what you want made callable. It replies in prose and can
act:

| | |
|---|---|
| `@write_spec` + a ```json block | replaces the draft spec |
| `@write_code` + a ```python block | replaces the draft code |
| `@run: {"energy_MWh": 1000}` | runs the draft and gets the **real** output back |

`@run` is the one that matters. The agent sees its own `KeyError`, its own traceback, its own
domain guard firing, and fixes the code before handing it to you. In testing it wrote
`a["enrgy_MWh"]`, ran it, read the KeyError, corrected the key and re-ran — without being told. It
may act up to five times before it must come back to you.

**The same three verbs work when you type them.** A message beginning with `@write_spec` or
`@write_code` edits the draft directly and spends no model call — that is how you hand-correct
something instead of arguing with it in prose.

### The spec is the point

The script is the smaller half. The spec is what makes the method callable *by someone else*:

- **every parameter carries a unit, and a resolution where that matters** — `kg SO2e/MWh`,
  *balancing authority × month*. This is where two methods are found not to compose. An annual,
  plant-level number and a monthly, balancing-authority number can be multiplied without error and
  the result means nothing; only the declared resolution catches it.
- **`conditions` is mandatory.** `/accept` refuses without it. It travels with every result the
  tool returns, so a downstream agent has to say when it is working outside them.
- **`provenance`** is either `published`, with a citation, or `model_drafted, not validated`. A
  method with no source is allowed; dressing it up as one that has a source is not.
- **`examples`** are best used to reproduce a number the source itself reports. `/examples` reports
  the relative error rather than a pass/fail tick — a tool that misses the paper's own Table 2 by
  0.8% is telling you something, and rounding that to ✗ throws the information away.

### What Accept refuses

Each of these blocks the write, and each exists because leaving it out does not break
anything — it quietly produces a tool that composes with someone else's and means nothing.

| refused when | why |
|---|---|
| `conditions` is empty | a method without stated conditions is not a method |
| `provenance` is not set | published, with a citation, or model-drafted — not silence |
| a parameter has no **unit** | |
| a parameter has no **resolution** | a unit alone makes two methods look composable when they are not |
| a **default** has no `default_source` | see below |
| a returned value has no **unit or resolution** | this is the half a caller matches against their own parameters |

**The rule about defaults is the important one.** A required parameter with no default is how a
specification says *"I need this and my source cannot give it"* — which is the most useful
sentence it can contain. A plausible-looking default erases that sentence, silently, and the gap
never reaches the roundtable. So a default is allowed only when you can say where that specific
value came from; if you cannot, the parameter goes back to required.

Softer things only warn: conditions that name no boundary, no example, no example that
reproduces a number the source reports, and **hard-coded constants found in the code** — each of
those is either a documented constant of the source or an assumption a caller can neither see nor
vary. The prompt tells the agent to hunt them and lift them into the parameter table.

A tool that has code but no specification — an uploaded script, say — is fixed the same way as
any other: click it on the left to load it, then ask the agent to specify it.

### Accept

`/accept` prints what the tool declares about itself — every parameter with its unit and
resolution, every returned value with the same, the conditions, the provenance, and any soft
warnings — and then writes it. Three files:

    tools/<name>.py          the script
    tools/<name>.json        the specification
    tools/<name>.build.md    the whole assembly session

The third is the point of the second page. It records what the agent read, what it proposed, what
failed when it ran, and what went to disk — a supporting-information artifact for a tool that was
partly written by a model.

The judgement about whether a method's domain of validity covers the case you mean to use it for
is still yours, and it is still not something a model can make for you. But it is not a field in
a JSON file: a name you type into your own tool proves nothing, and verifying who typed it is not
this system's job. What the artifact records instead is everything a reader would need to make
that judgement themselves — the conditions, the resolutions, the provenance, and the session that
produced them.

Nothing else touches `tools/`. Testing a draft has to put code on disk to execute it, so drafts
run as `_draft_<name>` — a draft can never overwrite an accepted script, and drafts do not appear
in the registry.

### Runtime data, and R

A script runs with `tools/` as its working directory, so a coefficient table or a trained model
goes in that folder and is opened by relative path. Put those there yourself; the tool creator does
not upload them, because the file the script reads should be the file you put on disk.

`runtime: rscript` runs the script with `Rscript` instead. The stdin/stdout contract is identical.
If R is not on your `PATH` you get a clear message saying so rather than a traceback.

## Tags: two independent questions

Every substantive claim answers two questions, and they are orthogonal — which is why the tag
often has two parts.

**How was the number produced?** Exactly one of:

| | |
|---|---|
| `[GROUNDED]` | it is in your knowledge base; a `@lookup` result is always this |
| `[COMPUTED from R3]` | you ran a method — always cite the run |
| `[EXTENDED]` | no calculation; a projection from your method, with the assumption that makes it travel and the condition where it stops |

**Did anything you invented go into it?** If yes, `[ASSUMED]` goes **in front**:

```
[ASSUMED][COMPUTED from R7]   computed, but on a value nobody has established
[ASSUMED][EXTENDED]           a projection resting on an invented premise
[COMPUTED from R7]            every input sourced
```

`[ASSUMED][GROUNDED]` does not exist — nothing taken from your source was invented.
(`[EXTRAPOLATED]` was the old name for `[EXTENDED]`; imported transcripts still render.)

Splitting it this way is not only simpler, it is more honest: production and contamination are
different facts, and forcing one label made the second invisible whenever the first was
interesting. It is also easier to obey — two independent yes/no questions rather than a
three-way judgement with preconditions.

**An `[ASSUMED]` number is not finished until it has been tested.** The prompt requires a second
run at a different, equally defensible value and a statement of whether the conclusion moves. If
it does, the conclusion *is* the sensitivity. That is what six tool runs per turn are for.

**Refusing is a legal move.** If the value you would have to assume is one your work gives no
basis for, saying so is a complete answer. Without this the agent always assumes, and
`[ASSUMED]` decays into the default setting rather than a declared act.

## Argument provenance — the agent does not choose ASSUMED

The second question above is not answered by the agent. It is read off the call.

Every argument declares where its value came from:

```
@tool: {"energy_MWh":       {"v": 1.0e6, "src": "R3"},
        "ef_co2_t_per_MWh": {"v": 0.5,   "src": "assumed"},
        "pm25_usd_per_MWh": {"v": 2.0,   "src": "source"}}
```

Three sources, and the asymmetry is the design:

| `src` | what happens |
|---|---|
| `"R7"` | **checked exactly** — the value must occur in what R7 returned |
| `"source"` | checked weakly against your profile, this turn's lookups and the transcript |
| `"assumed"` | not checked; nobody lies in this direction |

A **bare value** with no wrapper, and a `"source"` claim whose value cannot be found, are both
recorded as **assumed**. That is the conservative reading, it keeps older cards and transcripts
working, and it makes laziness loud instead of silent: skipping the wrapper marks you as
assuming, which is the safe direction to fail.

Then the verdict is derived, before the script even runs:

> **This run is ASSUMED.** ef_co2_t_per_MWh: declared assumed by the caller.
> Report it as `[ASSUMED][COMPUTED from R7]`, and in the same sentence name the quantity, the
> value you used, where that value came from, and why it may not transfer here. Then run again
> with that quantity at a different, equally defensible value and say whether your conclusion
> moves.

**This closes the one hole the earlier design had.** Before, an agent could invent an emission
factor, run a real tool, get a real number and report it as `[COMPUTED from R1]` — and every
check passed, because they all tested bookkeeping (did you run something, did you cite
something) and none could ask where the number in the parameter came from. The tag was the
agent's to choose. Now it is not.

Matching a value against text is done on a **number boundary**, and only through renderings that
mean the same number: `0.5`, `0.50` and `5.0e-1` all count, `1` does not, because substring
matching would wave through every small integer and rounding would invent citations that are not
there.

The strictness is productive. A `"source"` value that cannot be found is marked assumed **and the
agent is told why** — and the obvious repair is to `@lookup` the number first, which then
verifies. The check pushes agents toward retrieving evidence rather than recalling it.

### Contamination propagates

If R7 rests on an invented input and R9 consumes R7's output, **R9 is ASSUMED too** — the ledger
records `R9 · ASSUMED (via R7)` and any turn citing R9 must carry `[ASSUMED]`. Nothing tracked
this before. For a write-up it is the strongest thing the machinery produces: not "an agent made
an assumption", but *an undeclared assumption contaminated three downstream steps, and here is
which three.*

### What it still cannot catch

`src: "R3"` where the value really is in R3 but is the **wrong kind of quantity** — a
drought-displacement marginal used where an incremental-load marginal is needed — verifies
cleanly. Provenance answers *where did this number come from*, not *is it the right sort of
thing*. The second is the harder half, and it stays with the human.

## The instrument roster — how the gap becomes visible

A tool card used to reach only its owner's prompt. That quietly made the interesting failure
impossible: Agent-F never learns that Agent-Q needs kWh, Agent-Q never learns to ask for it, and
the mismatch the exercise is about is never reached.

So every seat's prompt now carries every seat's instruments, **with each argument's unit and its
resolution**:

```
# Instruments at this table

Agent-F  (yours) —
  NAME: sec_ro
  PARAMETERS:
    - pi_feed_bar (number, required) — design point, one feed composition [bar]
    - recovery (number, required) — design point [-]
  RETURNS: sec_kWh_per_m3 [kWh/m3]

Agent-Q —
  NAME: damage
  PARAMETERS:
    - energy_MWh (number, required) — annual, plant-level [MWh]
    - ef_kg_per_MWh (number, required) — balancing authority x month,
        drought-displacement marginal [kg SO2e/MWh]
  RETURNS: total_usd [USD]
```

The resolution line is the point. With units alone, two marginals look composable and multiply
without complaint; the resolutions are what show that *balancing authority × month,
drought-displacement* is not the *plant-level annual, incremental-load* quantity the other method
needs. **The gap emerges from the parameter table** — no separate mechanism proposes it.

`conditions` stays with its owner: it is long, and enforcing it is the owner's job. Nobody can run
anyone else's tool; the prompt says to ask for the number instead, naming the unit and resolution
required.

## The result ledger — how a number is handed over

Every tool run anyone makes is logged with an id and injected into everybody's prompt:

```
# Results on the table

[R1] Agent-F · sec_ro
     args {"pi_feed_bar":2.1,"recovery":0.75,"pump_eff":0.8}
     → {"sec_kWh_per_m3":0.2917}     (returns: sec_kWh_per_m3 [kWh/m3])
```

A number produced by one participant is then picked up by another **by reference**, not by
retyping: `[COMPUTED from R1]`. Three things follow. The unit travels with the number. A retyped
number with no reference becomes detectable. And the ledger is a table you can check by hand
afterwards — it goes into the export.

The run id is handed to the model in the tool result itself (*"logged as R4 — report it as
`[COMPUTED from R4]`, or as `[ASSUMED]` if you supplied a value nobody has established"*), so
citing is always possible.

## Mechanical checks

A model will say it followed a rule without following it. Four syntactic tests run after every
turn; failures are flagged under the bubble and collected in the export.

| | fires when |
|---|---|
| **C1** | `[COMPUTED]` but no tool ran this turn and no earlier run was cited |
| **C2** | `[ASSUMED]` after fewer than two runs — the assumed value was never varied |
| **C3** | a substantial turn with no tag at all |
| **C4** | a `[COMPUTED]` claim with no `[R…]` reference |

These are **not defects of the run — they are its data.** They answer the question the exercise is
actually asking: did the constraint bind? A transcript with zero flags and one with several are
both results, and the export reports either way.

## The export

Beyond the transcript, four appendices: the **result ledger** (every run, its arguments and its
return value), the **mechanical checks**, the **tool cards** as the agents saw them, and an
**adjudication table** — one row per tagged claim, pre-filled with speaker, tag and the words
leading up to it, with the last two columns (*basis shown*, *tag correct?*) left empty. Those two
are the judgement no model makes for you.

## As many seats as you want

Click the dashed **+** on the ring to add a seat, or the **✕** in a seat's panel to drop one (never
below two). The ring's radius grows so the boxes never collide, the moderator keeps its own
reserved wedge at the top, and the diagram crops itself to whatever it needs.

The ceiling is the number of usable [API slots](#api-slots--one-file-not-thirty-fields): one seat
per slot, with slot 0 reserved for the moderator's assistant. Press **+** with none left and it
says so and points you at Set API rather than adding a seat you cannot run.

The limit that does bite is cost, not layout: **one round = one model call per seat**, and every
seat sees the whole transcript. The hint under the diagram spells this out as you add seats. Eight
voices in a long conversation is a lot of tokens, and it also gets harder for any single point to
be answered rather than talked past.

The seat's dot shows its state at a glance: hollow grey = no knowledge base, hollow coloured =
loaded but not onboarded, filled = onboarded and ready.

**The line-up is fixed once the dialogue starts.** Add and remove are disabled while it runs or
is paused; press Stop to change the roster, which starts a new dialogue. Turns already in the
transcript are never rewritten — removing someone before a new run does not erase what they said
in the old one.

Speaking order is the seat order — the order they were added, clockwise from the top-right:
**one round = every scientist speaks once**. Whoever speaks later in a round sees what everyone before them just said, in the same round.

## The moderator is you — and you have an assistant

**You are the moderator.** You steer by typing notes into the box at the bottom whenever the
dialogue pauses.

Between those notes, a separate model does the bookkeeping for you: **after every completed round
your assistant rewrites a short running summary** of where the discussion stands, who is committed
to what, and which of your instructions are still unresolved.

That summary is appended to every scientist's next prompt **at the very end, immediately before
"it is your turn"** — the position a model weighs most heavily. With three or four voices and a
long history, this is what stops the discussion from dissolving into parallel monologues.

The assistant is **not one of the scientists**. It has no knowledge base, it never takes a turn, and
nothing it writes appears in the transcript. Everything about it lives in one place: **click
MODERATOR at the head of the roundtable** and its panel opens in the same slot the seats use. That
panel only explains what the assistant is and where it is configured — **slot 0** in `api.json`.
Leave that slot blank and it borrows slot 1; a small, fast, cheap model of its own is usually the
better call, since it runs once per round.

**The summary lives at the bottom, not in that panel.** *Assistant & summary* in the running
controls opens it, and you can edit it there — your version is what the scientists see next round.
It sits with the running controls because that is what it is: something rewritten every round and
fed into the next prompt, not part of setting a seat up. Opening it does not disturb whichever
seat panel you were looking at, and clicking a seat does not close it.

## Interface

- **Left, top** — the roundtable itself: the moderator at the head of the table, the shared
  question in the hub, and the seats around the ring. It is a plain SVG diagram — labelled boxes and lines, no
  avatars, no animation. A dashed **+** node on the ring adds a seat.
- **Left, below** — the panel of whatever you clicked on the diagram. Every box on the ring is a
  tab, the moderator included: clicking MODERATOR opens the assistant's panel in this same slot,
  so there is only ever one panel open. A seat holds four things and nothing else: its name, its
  field, and the two forms a callable method takes — **Text-based Tool** (*its knowledge base*)
  and a collapsed **Code-based Tool** (*a script, optional*) showing its state when closed — then the Onboard button and one state line. The scientist profile and the calling card
  are real state but are not shown: nothing on a seat is edited by hand. The **✕** in the panel
  header removes that seat.
- **Right** — the transcript, in its own scrolling column so the diagram stays put while the
  conversation grows.
  Scientists are coloured by seat order from a palette of eight,
  **MODERATOR outlined in orange**, lookups and tool runs grey and collapsed.
  `[GROUNDED]`, `[COMPUTED]`, `[ASSUMED]` and `[EXTENDED]` render as coloured badges.
- **Bottom** — the running controls: topic, pause-every-N (default 2), Start / Resume / Stop,
  import, export, your moderator note box, and *Assistant & summary*, which unfolds the running
  summary in place.

*Start* onboards anyone who still needs it before the dialogue begins.

## Saving and resuming

The transcript lives in memory only — close the tab and it is gone. Configuration and
scientist profiles do persist in localStorage, so a reload never costs you the onboarding wait.

*Export .md* writes the whole session: every turn, the lookup queries, the tool calls, the running
summary, every profile and tool card, the result ledger, the mechanical checks, and an
adjudication table to fill in by hand.
*Import .md* reads one back and continues from it — the roster is rebuilt with the right number
of scientists and their names, the transcript is restored, the summary comes back, the round
counter picks up where it left off, and if the export stopped mid-round the next speaker is
whoever was actually due. The import lands in **paused** state, so you can add a moderator
note before it carries on.

Two things are deliberately not in the export: **the knowledge bases and the api keys**. Fill those
into the cards before pressing Resume. Profiles from the export are written into any card
whose profile is still empty, so importing on a different machine does not re-run onboarding —
but it will never overwrite a profile you already have.

Lookup passages and tool output are not stored either; an imported line keeps the query or the
call and notes that the retrieved text is gone.

## API slots — one file, not thirty fields

Provider settings used to sit in every scientist's card: three inputs each, retyped or inherited,
and duplicated in localStorage. They now live in **one file**, `api.json`, next to `app.py`, edited
on a page of its own:

    http://127.0.0.1:8000/setapi          (or "Set API ↗" under the title)

```json
[
  {"label": "Moderator's assistant", "base_url": "…", "model": "qwen-turbo", "api_key": "sk-…"},
  {"label": "Fan lab",   "base_url": "…", "model": "qwen-plus", "api_key": "sk-…"},
  {"label": "Qiu lab",   "base_url": "…", "model": "qwen-plus", "api_key": "sk-…"}
]
```

**The index is the identity.** Slot 0 is the moderator's assistant; slot 1 is whoever sits in the
first seat, slot 2 the second. The binding is by *position*, not by name — remove a seat and
everyone below it moves up a slot and starts using a different key.

Because the mapping *is* the seating order, it does not need repeating on every card. One clause
under the diagram says it for the whole table, and only speaks up when a seated slot is not
actually usable:

    3 seats · one round = 3 model calls · slots 1–3
    3 seats · one round = 3 model calls · slot 2 not set up

Slot 0 may be left blank; the assistant then borrows slot 1.

**A seat needs a slot.** Pressing **+** at the roundtable when every usable slot is taken does not
add a seat — it says so and points at Set API. A slot counts as usable only once it has both a
`base_url` and a `model`, so `api.json` needs at least three entries before a two-scientist
roundtable can run. Start re-reads the file before checking, so a slot you add in the other tab is
picked up without a reload.

**The keys are in plain text.** That is a deliberate choice for a local, single-user tool: the
server only listens on `127.0.0.1` and never serves `api.json` as a static asset. It is in
`.gitignore` for a reason — do not commit it, and keep it out of backups.

`base_url` is normalized for you: with or without a trailing slash, with or without
`/chat/completions`, all work. Anything OpenAI-compatible is fine — DashScope, DeepSeek, a local
Ollama, OpenAI itself.


## Layout

```
run.bat               Windows launcher: deps, proxy, server, browser. Double-click it.
app.py                backend. Serves the page, forwards API calls, runs tool scripts.
tools/                where uploaded tool scripts land — put their data files here too.
index.html            all UI + dialogue loop + onboarding + lookup + prompt assembly.
                      Vanilla JS, no framework, no build step.
paper_HanqingFan.md   knowledge base: Fan et al., Nature Water 2026 (multiscale transport mechanisms)
paper_MeiqiYang.md    knowledge base: Yang et al., ES&T 2024 (ML-driven pervaporation polymer design)
pdf2md.py             PDF -> knowledge-base .md converter, for adding another scientist
                      (only needed if your source is a PDF — any Markdown file works as-is)
```

Why a backend at all: providers such as DashScope don't allow direct browser calls
(CORS), and the api_key has no business sitting in the browser's network panel.

### Adding or swapping a knowledge base

Any Markdown file works. Headings matter: they are what the lookup splits on, so a document with
sensible `##` sections retrieves far better than one long wall of text. If your source is already
Markdown, just paste it in — the converter below is only for PDFs.

```bash
pip install pdfplumber
python pdf2md.py fan  newpaper.pdf  paper_XXX.md     # Nature-style layout
python pdf2md.py yang newpaper.pdf  paper_XXX.md     # ACS-style (1. / 2.1. numbering)
```

The converter is layout-aware: it partitions pages by tinted panels (Nature's BOXes),
splits columns, and strips superscript citations by font size and baseline position.
References and acknowledgements never enter the knowledge base.
**Always check the heading list it prints** — heading detection is the first thing that
breaks on an unfamiliar layout, and headings determine section quality for lookup.

## What each agent sees on every call

```
system:    identity + who else is here + scientist profile + table of contents
           + instrument roster + result ledger + lookup protocol + tool card + hard rules + topic
user:      [Yang] ...             ← another participant
user:      [MODERATOR] ...        ← declared highest priority in the rules
assistant: ...                    ← its own past turns
user:      [MODERATOR — running summary of the discussion so far]
           ...
           It is your turn, X. Please respond.
```

The seven hard rules: moderator outranks everything / only your own knowledge base (numbers must
come from the profile, a lookup or your tool) / tag every claim `[GROUNDED]`, `[EXTRAPOLATED]` or
`[COMPUTED]` / under 150 words / "my knowledge base offers no evidence on this" is a valid answer /
address the others by name / no speaker prefix.

## Known failure modes

**"The moderator outranks everything" is written in the prompt — that does not mean the
agents obey it.** Models routinely forget the moderator's instruction after two or three
rounds and drift back to their own hobby-horse. This gets worse, not better, with four voices.

The running summary is the main defence: it is regenerated every round, it names unresolved
moderator instructions, and it sits at the end of the prompt. If drift still happens, edit the
summary by hand — an explicit line like "the moderator has twice asked for testable predictions
and neither has given one" is far blunter than anything the note-taker will write on its own.

**Second thing to watch:** an agent may never look anything up and run the whole dialogue
off its profile. If you see it citing numbers that never appeared in the profile, it is
making them up — either move the lookup protocol earlier in the prompt, or write the
"Key evidence" section of the profile in more detail.
