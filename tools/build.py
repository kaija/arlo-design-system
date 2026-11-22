#!/usr/bin/env python3
"""Build the Arlo Design System docs site (site/) and the AI kit (arlo-design/)
from the design-system source in project/.

Shared pieces for tools/make.py, which writes both folders.
"""
import base64, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "project")
SITE = os.path.join(ROOT, "site")
KIT = os.path.join(ROOT, "arlo-design")

tokens = json.load(open(os.path.join(SRC, "tokens.json")))
index = json.load(open(os.path.join(SRC, "design-system.json")))
readme = open(os.path.join(SRC, "README.md")).read()
bundle_css = open(os.path.join(SRC, "components", "bundle.css")).read()

# ------------------------------------------------------------------ symbols
GROUPS = [g for g in index["groups"] if g != "Logos"]          # Symbols, Calendar, Travel
blob_to_symbol, symbols = {}, {}                                # name -> (group, path)
for g in GROUPS:
    for fname, rec in index["assetGroups"][g]["files"].items():
        name = fname[:-4]
        blob_to_symbol[rec["blob"]] = name
        symbols.setdefault(name, (g, os.path.join(SRC, "assets", g, fname)))
logos = index["assetGroups"]["Logos"]["order"]

def symbols_css():
    out = ["/* Arlo Design System — SF Symbols by name. Use <span class=\"sf\" data-symbol=\"gearshape\"></span>.",
           "   SF Symbols are Apple's, licensed for apps on Apple platforms. */"]
    for name in sorted(symbols):
        data = base64.b64encode(open(symbols[name][1], "rb").read()).decode()
        out.append(f'.sf[data-symbol="{name}"]{{--sf:url("data:image/svg+xml;base64,{data}")}}')
    return "\n".join(out) + "\n"

SF_RE = re.compile(r'<span class="sf([^"]*)" style="--sf:url\(/_blob/([0-9a-f]{32})\)"></span>')
def symbolize(h):
    def rep(m):
        cls = m.group(1).strip()
        return f'<span class="sf{(" " + cls) if cls else ""}" data-symbol="{blob_to_symbol[m.group(2)]}"></span>'
    h = SF_RE.sub(rep, h)
    left = re.findall(r"/_blob/[0-9a-f]{32}", h)
    if left: sys.exit(f"unresolved asset reference {left[0]}")
    return h

# ------------------------------------------------------------------ tokens
def val(v, theme):
    return v if isinstance(v, str) else v.get(theme, v["light"])
def css_value(v):
    m = re.fullmatch(r"\{(.+)\}", v)
    return f"var(--{m.group(1)})" if m else v

def tokens_css():
    themed = tokens["color"]["tokens"] + tokens["shadow"]["tokens"]
    def block(theme):
        return "".join(f"  --{t['name']}: {css_value(val(t['value'], theme))};\n" for t in themed)
    flat = ""
    for fam in ("spacing", "radius", "size"):
        flat += "".join(f"  --{t['name']}: {t['value']};\n" for t in tokens[fam]["tokens"])
    flat += "".join(f"  --font-{k}: {v};\n" for k, v in tokens["type"]["families"].items())
    css = ["/* Arlo Design System — generated from tokens.json. Light by default; dark via [data-theme=\"dark\"] or the OS setting. */",
           ':root, [data-theme="light"] {\n' + block("light") + "}",
           '[data-theme="dark"] {\n' + block("dark") + "  color-scheme: dark;\n}",
           '@media (prefers-color-scheme: dark) {\n  :root:not([data-theme="light"]) {\n' +
           block("dark").replace("  --", "    --") + "    color-scheme: dark;\n  }\n}",
           ":root {\n" + flat + "}"]
    for grp in tokens["type"]["groups"]:
        for s in grp["styles"]:
            fam = s.get("family", grp["family"])
            lh = s["lineHeight"] if isinstance(s["lineHeight"], str) else str(s["lineHeight"])
            css.append(f".{s['name']} {{ font-family: var(--font-{fam}); font-size: {s['fontSize']}; line-height: {lh}; "
                       f"font-weight: {s['fontWeight']}; letter-spacing: {s.get('letterSpacing', '0px')}; }}")
    return "\n".join(css) + "\n"

# ------------------------------------------------------------------ markdown (the subset the READMEs use)
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t

def md(text, shift=0):
    out, para, items, rows = [], [], [], []
    def flush():
        nonlocal para, items, rows
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if items: out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"); items = []
        if rows:
            head, body = rows[0], [r for r in rows[1:] if not re.fullmatch(r"[\s|:-]+", "|".join(r))]
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>" +
                       "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table>")
            rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s: flush(); continue
        m = re.match(r"(#{1,6})\s+(.*)", s)
        if m:
            flush(); lvl = min(6, len(m.group(1)) + shift)
            out.append(f'<h{lvl} id="{slug(m.group(2))}">{inline(m.group(2))}</h{lvl}>'); continue
        if s.startswith("|"):
            if para or items: flush()
            rows.append([c.strip() for c in s.strip("|").split("|")]); continue
        if s.startswith("- "):
            if para or rows: flush()
            items.append(s[2:]); continue
        if items and line.startswith("  "): items[-1] += " " + s; continue
        if items or rows: flush()
        para.append(s)
    flush()
    return "\n".join(out)

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>|`|\*", "", t).lower()).strip("-")

def sections(text):
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    intro, secs = parts[0].strip(), {}
    for i in range(1, len(parts), 2): secs[parts[i].strip()] = parts[i + 1].strip()
    return intro, secs

INTRO, SECS = sections(readme)

# ------------------------------------------------------------------ components
COMPONENT_ORDER = []   # (group, name, height, summary, readme_md, preview_html)
for name in sorted(os.listdir(os.path.join(SRC, "components"))):
    d = os.path.join(SRC, "components", name)
    pv = os.path.join(d, "preview.html")
    if not os.path.isdir(d) or not os.path.exists(pv): continue
    src = open(pv).read()
    marker = re.match(r"<!--\s*@dsCard([^>]*)-->", src)
    attrs = {k: a or b for k, a, b in re.findall(r'(\w+)=(?:"([^"]*)"|(\S+))', marker.group(1))}
    rd = open(os.path.join(d, "README.md")).read() if os.path.exists(os.path.join(d, "README.md")) else ""
    body = re.sub(r"^#\s+.*\n", "", rd).strip()
    summary = re.split(r"(?<=\.)\s", body.split("\n\n")[0])[0] if body else ""
    COMPONENT_ORDER.append(dict(name=name, group=attrs.get("group", "Cover"), height=int(attrs.get("height", 200)),
                                summary=summary, readme=body, preview=symbolize(src[marker.end():].lstrip())))
COMP_GROUPS = ["Menus and actions", "Selection and input", "Navigation and search", "Layout and organization",
               "Presentation", "Status", "Content"]
SHOWCASE = {"CalendarSymbols": "Calendar", "TravelSymbols": "Travel"}
components = [c for c in COMPONENT_ORDER if c["name"] != "Cover" and c["name"] not in SHOWCASE]
byname = {c["name"]: c for c in COMPONENT_ORDER}

def spaced(n):  # SegmentedControl -> Segmented control
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", n).capitalize().replace("Pop up", "Pop-up")

def preview_doc(c, css_prefix):
    head = (f'<link rel="stylesheet" href="{css_prefix}tokens.css">\n'
            f'<link rel="stylesheet" href="{css_prefix}components.css">\n'
            f'<link rel="stylesheet" href="{css_prefix}symbols.css">\n'
            '<script>try{var t=new URLSearchParams(location.search).get("theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>\n'
            '<style>html,body{background:var(--color-bg)}</style>\n')
    return c["preview"].replace("<head>", "<head>\n" + head, 1)

def preview_doc_kit(c):
    head = ('<link rel="stylesheet" href="../tokens/tokens.css">\n'
            '<link rel="stylesheet" href="../components/components.css">\n'
            '<link rel="stylesheet" href="../symbols/symbols.css">\n'
            '<style>html,body{background:var(--color-bg)}</style>\n')
    return c["preview"].replace("<head>", "<head>\n" + head, 1)

def snippet(c):
    m = re.search(r"<body[^>]*>(.*)</body>", c["preview"], re.S)
    return m.group(1).strip() if m else ""

def example_css(c):
    m = re.search(r"<style>(.*?)</style>", c["preview"], re.S)
    return "\n".join(l.strip() for l in m.group(1).strip().splitlines() if l.strip()) if m else ""

def reset(path):
    if os.path.isdir(path): shutil.rmtree(path)
    os.makedirs(path)

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(text)

TOKENS_CSS, SYMBOLS_CSS = tokens_css(), symbols_css()
