"""Two AI scientists in a dialogue you can interrupt — backend.

This file does exactly two things:
  1. serve index.html
  2. forward the frontend's model calls to an OpenAI-compatible endpoint

Why a backend at all: providers such as DashScope do not allow direct calls from
the browser (CORS), and the api_key has no business sitting in the browser's
network panel.

It also runs a scientist's optional tool script (/api/tool). That is the one place
where this file does more than forward: it executes Python you supplied, in a
subprocess, with a hard timeout. See the tool() docstring for the contract.

All dialogue logic — prompt assembly, rounds, pausing, moderator handling —
lives in index.html. Do not add business logic here.

Run:  python app.py     then open http://127.0.0.1:8000
"""

from __future__ import annotations

import asyncio
import json
import os
import pathlib
import re
import subprocess
import sys
import time
from typing import Any

import httpx
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, Response
from pydantic import BaseModel

BASE_DIR = pathlib.Path(__file__).parent
TIMEOUT = httpx.Timeout(300.0, connect=20.0)
RETRIES = 3          # connection failures are usually a blip; do not kill the dialogue
BACKOFF = (1, 4)     # seconds to wait before retry 2 and retry 3

TOOL_DIR = BASE_DIR / "tools"      # scripts land here; put their data files here too
TOOL_TIMEOUT = 30                  # seconds; a hung script must not hang the roundtable
TOOL_OUT_MAX = 8000                # chars of stdout/stderr handed back to the model
SAFE_NAME = re.compile(r"[^A-Za-z0-9._-]")

# Provider settings for every seat, kept in one file instead of in each scientist's card.
# The index IS the identity: 0 is the moderator's assistant, 1 the first scientist, and so on.
# It holds api keys in plain text. That is a deliberate choice for a local, single-user tool —
# the server binds to 127.0.0.1, the file is never served as a static asset, and it is in
# .gitignore. Do not put it anywhere a repository or a backup will pick it up.
API_FILE = BASE_DIR / "api.json"
API_STARTER = [
    {"label": "Moderator's assistant", "base_url": "", "model": "", "api_key": ""},
    {"label": "Scientist 1", "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
     "model": "qwen-plus", "api_key": ""},
    {"label": "Scientist 2", "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
     "model": "qwen-plus", "api_key": ""},
]

app = FastAPI(title="ESTDialogue", docs_url=None, redoc_url=None)


class ChatRequest(BaseModel):
    base_url: str
    model: str
    messages: list[dict[str, Any]]
    api_key: str = ""
    temperature: float = 0.7
    max_tokens: int | None = None


def _endpoint(base_url: str) -> str:
    """Normalize whatever the user typed into a full chat/completions URL.

    All of these are accepted:
      https://dashscope.aliyuncs.com/compatible-mode/v1
      https://dashscope.aliyuncs.com/compatible-mode/v1/
      https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
    """
    base = base_url.strip().rstrip("/")
    if base.endswith("/chat/completions"):
        return base
    return base + "/chat/completions"


# These files change constantly while the tool is being worked on, and a browser given only an
# ETag will happily serve a heuristically-fresh copy without asking. That produces the worst kind
# of confusion: the file on disk is right, the page is not. Nothing here is worth caching.
NO_STORE = {"Cache-Control": "no-store, must-revalidate", "Pragma": "no-cache"}


def _page(name: str, media: str = "text/html") -> FileResponse:
    return FileResponse(BASE_DIR / name, media_type=media, headers=NO_STORE)


@app.get("/")
def index() -> FileResponse:
    return _page("index.html")


RUNTIMES = {                       # how each runtime is invoked
    "python": lambda path: [sys.executable, str(path)],
    "rscript": lambda path: ["Rscript", str(path)],
}
EXT = {"python": ".py", "rscript": ".R"}

# The tool creator tests a draft by running it through /api/tool, which has to put the code on
# disk to execute it. It runs under this prefix so a draft can never overwrite a tool that has
# already been accepted, and so drafts do not show up in the registry.
DRAFT_PREFIX = "_draft_"


class ToolRequest(BaseModel):
    filename: str
    script: str
    args: dict[str, Any] = {}
    runtime: str = "python"


@app.post("/api/tool")
def tool(req: ToolRequest) -> JSONResponse:
    """Run a scientist's tool script.

    Contract — deliberately the simplest thing that works in any language:
        the script reads one JSON object from stdin and writes one JSON object to stdout.

        import sys, json
        args = json.load(sys.stdin)
        json.dump({"flux": 12.4, "units": "LMH/bar"}, sys.stdout)

    The script is written into ./tools/ and run with that as the working directory, so a
    script can load its own data files (a trained model, a lookup table) by relative path —
    put them in ./tools/ next to it.

    It runs with the same interpreter as this server, so its imports must be installed in
    the environment you launched app.py from.

    SECURITY: this executes code on your machine. It is safe because the server binds to
    127.0.0.1 and the script is one you supplied yourself. Do not change the host binding.
    """
    rt = req.runtime if req.runtime in RUNTIMES else "python"
    ext = EXT[rt]
    name = SAFE_NAME.sub("_", pathlib.Path(req.filename).name) or ("tool" + ext)
    if not name.lower().endswith(ext.lower()):
        name = pathlib.Path(name).stem + ext

    TOOL_DIR.mkdir(exist_ok=True)
    path = TOOL_DIR / name
    # only touch the disk when the content actually changed, so the file you inspect
    # is exactly the one that ran
    if not path.exists() or path.read_text(encoding="utf-8", errors="replace") != req.script:
        path.write_text(req.script, encoding="utf-8")

    payload = json.dumps(req.args, ensure_ascii=False)
    t0 = time.monotonic()
    try:
        proc = subprocess.run(
            RUNTIMES[rt](path),
            input=payload, capture_output=True, text=True,
            timeout=TOOL_TIMEOUT, cwd=str(TOOL_DIR),
        )
    except subprocess.TimeoutExpired:
        print(f"  [tool {name}] TIMEOUT after {TOOL_TIMEOUT}s", flush=True)
        return JSONResponse(content={
            "ok": False,
            "error": f"the script did not finish within {TOOL_TIMEOUT} s and was killed",
            "seconds": TOOL_TIMEOUT,
        })
    except FileNotFoundError:
        return JSONResponse(content={
            "ok": False, "seconds": 0,
            "error": (f"the {rt} interpreter was not found on PATH. "
                      + ("Install R and make sure `Rscript` is callable."
                         if rt == "rscript" else "")),
        })
    except Exception as e:                       # unreadable script, bad interpreter, ...
        return JSONResponse(content={
            "ok": False, "error": f"{type(e).__name__}: {e}", "seconds": 0,
        })

    dt = time.monotonic() - t0
    out = (proc.stdout or "").strip()[:TOOL_OUT_MAX]
    err = (proc.stderr or "").strip()[:TOOL_OUT_MAX]
    print(f"  [tool {name}] rc={proc.returncode} · {dt:.2f}s · {len(out)} chars out", flush=True)

    if proc.returncode != 0:
        return JSONResponse(content={
            "ok": False,
            "error": f"the script exited with code {proc.returncode}",
            "stderr": err, "stdout": out, "seconds": round(dt, 2),
        })
    if not out:
        return JSONResponse(content={
            "ok": False,
            "error": "the script printed nothing to stdout — it must write one JSON object there",
            "stderr": err, "seconds": round(dt, 2),
        })

    # JSON is the contract, but a script that just prints a number is still useful:
    # hand the raw text back rather than failing on a technicality.
    try:
        result = json.loads(out)
        return JSONResponse(content={"ok": True, "result": result,
                                     "stderr": err, "seconds": round(dt, 2)})
    except json.JSONDecodeError:
        return JSONResponse(content={"ok": True, "raw": out, "not_json": True,
                                     "stderr": err, "seconds": round(dt, 2)})


# ══════════════════════════════════════════════════════════════
# Tool registry — the only thing the roundtable and the tool creator share.
# A tool is a pair of files in ./tools/ :  <name><ext>  and  <name>.json
# plus an optional assembly transcript <name>.build.md
# ══════════════════════════════════════════════════════════════

def _safe_stem(name: str) -> str:
    stem = SAFE_NAME.sub("_", pathlib.Path(name).stem)
    return stem or "tool"


def _paths(stem: str, runtime: str = "python") -> dict[str, pathlib.Path]:
    return {
        "script": TOOL_DIR / (stem + EXT.get(runtime, ".py")),
        "spec":   TOOL_DIR / (stem + ".json"),
        "build":  TOOL_DIR / (stem + ".build.md"),
    }


def _read(p: pathlib.Path) -> str | None:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else None


def _status(spec: dict[str, Any] | None, has_script: bool) -> str:
    """What the tool creator shows as a state dot."""
    if not has_script:
        return "no script"
    if not spec:
        return "no spec"
    if not str(spec.get("conditions", "")).strip():
        return "conditions missing"
    return "ready"


@app.get("/toolcreator")
def toolcreator() -> FileResponse:
    return _page("toolcreator.html")


@app.get("/api/tools")
def list_tools() -> JSONResponse:
    TOOL_DIR.mkdir(exist_ok=True)
    out = []
    stems = sorted({p.stem for p in TOOL_DIR.iterdir()
                    if p.is_file() and p.suffix.lower() in (".py", ".r", ".json")
                    and not p.name.endswith(".build.md")
                    # scratch files the tool creator runs drafts from — not tools
                    and not p.name.startswith(DRAFT_PREFIX)})
    for stem in stems:
        spec_p = TOOL_DIR / (stem + ".json")
        spec = None
        if spec_p.exists():
            try:
                spec = json.loads(spec_p.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                spec = {"_broken": "this .json does not parse"}
        runtime = (spec or {}).get("runtime", "python")
        script_p = TOOL_DIR / (stem + EXT.get(runtime, ".py"))
        if not script_p.exists():                     # spec says one thing, disk another
            script_p = next((TOOL_DIR / (stem + e) for e in (".py", ".R")
                             if (TOOL_DIR / (stem + e)).exists()), script_p)
        out.append({
            "name": stem,
            "runtime": runtime,
            "has_script": script_p.exists(),
            "has_spec": spec is not None,
            "status": _status(spec, script_p.exists()),
            "title": (spec or {}).get("title", ""),
            "provenance": (spec or {}).get("provenance", {}),
            "mtime": max([p.stat().st_mtime for p in (script_p, spec_p) if p.exists()] or [0]),
        })
    return JSONResponse(content={"tools": out, "dir": str(TOOL_DIR)})


@app.get("/api/tools/{name}")
def get_tool(name: str) -> JSONResponse:
    stem = _safe_stem(name)
    spec_txt = _read(TOOL_DIR / (stem + ".json"))
    spec = None
    if spec_txt:
        try:
            spec = json.loads(spec_txt)
        except json.JSONDecodeError as e:
            return JSONResponse(status_code=422, content={
                "error": f"{stem}.json does not parse: {e}", "spec_raw": spec_txt})
    runtime = (spec or {}).get("runtime", "python")
    script = _read(TOOL_DIR / (stem + EXT.get(runtime, ".py")))
    if script is None:                                # fall back to whichever exists
        for rt, ext in EXT.items():
            script = _read(TOOL_DIR / (stem + ext))
            if script is not None:
                runtime = rt
                break
    return JSONResponse(content={
        "name": stem, "runtime": runtime, "script": script, "spec": spec,
        "build": _read(TOOL_DIR / (stem + ".build.md")),
    })


class ToolSave(BaseModel):
    script: str | None = None
    spec: dict[str, Any] | None = None
    build: str | None = None
    runtime: str = "python"


@app.put("/api/tools/{name}")
def put_tool(name: str, body: ToolSave) -> JSONResponse:
    """Commit a draft to disk. The tool creator only calls this on Accept."""
    stem = _safe_stem(name)
    rt = body.runtime if body.runtime in RUNTIMES else "python"
    TOOL_DIR.mkdir(exist_ok=True)
    written = []
    if body.script is not None:
        p = TOOL_DIR / (stem + EXT[rt])
        p.write_text(body.script, encoding="utf-8")
        written.append(p.name)
    if body.spec is not None:
        spec = dict(body.spec)
        spec.setdefault("name", stem)
        spec["runtime"] = rt
        p = TOOL_DIR / (stem + ".json")
        p.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
        written.append(p.name)
    if body.build is not None:
        p = TOOL_DIR / (stem + ".build.md")
        p.write_text(body.build, encoding="utf-8")
        written.append(p.name)
    for scratch in TOOL_DIR.glob(DRAFT_PREFIX + stem + ".*"):   # the draft is now the tool
        scratch.unlink(missing_ok=True)
    print(f"  [registry] saved {', '.join(written) or '(nothing)'}", flush=True)
    return JSONResponse(content={"ok": True, "name": stem, "written": written})


@app.delete("/api/tools/{name}")
def delete_tool(name: str) -> JSONResponse:
    stem = _safe_stem(name)
    removed = []
    for p in TOOL_DIR.glob(stem + ".*"):
        if p.is_file() and p.suffix.lower() in (".py", ".r", ".json", ".md"):
            p.unlink()
            removed.append(p.name)
    return JSONResponse(content={"ok": True, "removed": removed})


@app.get("/readme")
def readme() -> FileResponse:
    """The help overlay reads this, and the button opens it raw."""
    return _page("README.md", "text/plain; charset=utf-8")


# ══════════════════════════════════════════════════════════════
# API slots — one file, edited on /setapi, read by both pages
# ══════════════════════════════════════════════════════════════

def _read_slots() -> list[dict[str, str]]:
    """Whatever is in api.json, normalized. A missing or broken file gives the starter."""
    if not API_FILE.exists():
        API_FILE.write_text(json.dumps(API_STARTER, ensure_ascii=False, indent=2), encoding="utf-8")
        return list(API_STARTER)
    try:
        raw = json.loads(API_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [{"label": "api.json does not parse — fix or replace it on /setapi",
                 "base_url": "", "model": "", "api_key": ""}]
    if not isinstance(raw, list):
        raw = raw.get("slots", []) if isinstance(raw, dict) else []
    out = []
    for i, e in enumerate(raw):
        e = e if isinstance(e, dict) else {}
        out.append({
            "label": str(e.get("label") or ("Moderator's assistant" if i == 0 else f"Scientist {i}")),
            "base_url": str(e.get("base_url") or ""),
            "model": str(e.get("model") or ""),
            "api_key": str(e.get("api_key") or ""),
        })
    return out


class SlotsSave(BaseModel):
    slots: list[dict[str, Any]]


@app.get("/setapi")
def setapi() -> FileResponse:
    return _page("setapi.html")


@app.get("/api/slots")
def get_slots() -> JSONResponse:
    return JSONResponse(content={"slots": _read_slots(), "file": str(API_FILE)})


@app.put("/api/slots")
def put_slots(body: SlotsSave) -> JSONResponse:
    clean = []
    for i, e in enumerate(body.slots):
        clean.append({
            "label": str(e.get("label") or ("Moderator's assistant" if i == 0 else f"Scientist {i}")).strip(),
            "base_url": str(e.get("base_url") or "").strip(),
            "model": str(e.get("model") or "").strip(),
            "api_key": str(e.get("api_key") or "").strip(),
        })
    API_FILE.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")
    filled = sum(1 for c in clean[1:] if c["base_url"] and c["model"])
    print(f"  [api.json] saved {len(clean)} slots · {filled} scientist slots usable", flush=True)
    return JSONResponse(content={"ok": True, "slots": clean})


@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> Response:
    return Response(status_code=204)          # no icon; keeps the console clean


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/chat")
async def chat(req: ChatRequest) -> JSONResponse:
    # Prefer the key from the request; fall back to the environment for anyone
    # who would rather not type it into the page.
    api_key = req.api_key.strip() or os.getenv("MODEL_API_KEY", "")

    payload: dict[str, Any] = {
        "model": req.model,
        "messages": req.messages,
        "temperature": req.temperature,
    }
    if req.max_tokens:
        payload["max_tokens"] = req.max_tokens

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    url = _endpoint(req.base_url)

    n_in = sum(len(str(m.get("content", ""))) for m in req.messages)
    t0 = time.monotonic()
    last: Exception | None = None
    r = None

    for attempt in range(RETRIES):
        try:
            async with httpx.AsyncClient(timeout=TIMEOUT, trust_env=True) as client:
                r = await client.post(url, json=payload, headers=headers)
            break
        except (httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout,
                httpx.RemoteProtocolError) as e:
            last = e
            print(f"  [{req.model}] attempt {attempt + 1}/{RETRIES} failed: "
                  f"{type(e).__name__}: {e or '(no detail)'}", flush=True)
            if attempt < RETRIES - 1:
                await asyncio.sleep(BACKOFF[attempt])
        except httpx.HTTPError as e:
            last = e
            break

    if r is None:
        proxy = os.getenv("HTTPS_PROXY") or os.getenv("HTTP_PROXY") or "(none)"
        return JSONResponse(
            status_code=502,
            content={"error":
                     f"could not reach {url} after {RETRIES} attempts — "
                     f"{type(last).__name__}: {last or '(no detail)'}. "
                     f"Proxy env for this process: {proxy}. "
                     f"A VPN routing traffic overseas will break a domestic endpoint like "
                     f"DashScope; a stale HTTP(S)_PROXY variable does the same."},
        )

    if r.status_code != 200:
        print(f"  [{req.model}] HTTP {r.status_code} after "
              f"{time.monotonic() - t0:.1f}s", flush=True)
        return JSONResponse(
            status_code=502,
            content={"error": f"model endpoint returned {r.status_code}: {r.text[:800]}"},
        )

    try:
        data = r.json()
        content = data["choices"][0]["message"]["content"]
    except Exception:
        return JSONResponse(
            status_code=502,
            content={"error": f"response is not OpenAI-compatible: {r.text[:800]}"},
        )

    print(f"  [{req.model}] ok · {n_in:,} chars in · {time.monotonic() - t0:.1f}s", flush=True)
    return JSONResponse(content={"content": content, "usage": data.get("usage")})


if __name__ == "__main__":
    import uvicorn

    print("\n  open http://127.0.0.1:8000   (Ctrl+C to quit)\n")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
