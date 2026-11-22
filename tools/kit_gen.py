"""AI kit generator: arlo-design/ — everything an agent needs to build Arlo UI."""
import json, os, re, shutil
import build as B

def q(v):
    v = str(v)
    return v if re.fullmatch(r"[A-Za-z0-9 #().,%/+_-]*", v) and not v.startswith(("#", "-")) and v.strip() == v and v else json.dumps(v)

def yaml_map(name, d, indent=0):
    pad = "  " * indent
    out = [f"{pad}{name}:"]
    for k, v in d.items():
        if isinstance(v, dict): out += yaml_map(k, v, indent + 1)
        else: out.append(f"{pad}  {k}: {q(v)}")
    return out

def design_md():
    toks = B.tokens["color"]["tokens"]
    colors = {}
    for t in toks:
        v = B.val(t["value"], "light"); m = re.fullmatch(r"\{(.+)\}", v)
        colors[t["name"]] = "{colors." + m.group(1) + "}" if m else v
    fam_name = {"sans": "Inter", "mono": "SF Mono"}
    typo = {}
    for g in B.tokens["type"]["groups"]:
        for s in g["styles"]:
            typo[s["name"]] = {"fontFamily": fam_name[s.get("family", g["family"])], "fontSize": s["fontSize"],
                               "fontWeight": s["fontWeight"], "lineHeight": s["lineHeight"], "letterSpacing": s.get("letterSpacing", "0px")}
    rounded = {t["name"].replace("radius-", ""): t["value"] for t in B.tokens["radius"]["tokens"]}
    spacing = {t["name"]: t["value"] for t in B.tokens["spacing"]["tokens"]}
    C = "{colors.%s}"
    comps = {
        "button-filled": {"backgroundColor": C % "color-accent", "textColor": C % "text-on-accent", "typography": "{typography.label-large}", "rounded": "{rounded.button}", "height": "36px", "padding": "0 16px"},
        "button-filled-hover": {"backgroundColor": C % "color-accent-hover", "shadow": "0 4px 16px rgba(88,86,214,0.3)"},
        "button-tinted": {"backgroundColor": C % "color-accent-light", "textColor": C % "color-accent", "rounded": "{rounded.button}"},
        "button-gray": {"backgroundColor": C % "color-bg-tertiary", "textColor": C % "color-text-primary", "rounded": "{rounded.button}"},
        "button-outline": {"backgroundColor": C % "color-bg", "textColor": C % "color-text-primary", "rounded": "{rounded.button}", "border": "1px solid {colors.color-border-strong}"},
        "button-plain": {"backgroundColor": "transparent", "textColor": C % "color-accent", "rounded": "{rounded.button}"},
        "button-destructive": {"backgroundColor": C % "color-danger", "textColor": C % "text-on-accent", "rounded": "{rounded.button}"},
        "segmented-control": {"backgroundColor": C % "color-bg-tertiary", "textColor": C % "color-text-secondary", "rounded": "{rounded.button}", "height": "28px"},
        "segmented-control-selected": {"backgroundColor": C % "color-segment", "textColor": C % "color-text-primary"},
        "text-field": {"backgroundColor": C % "color-bg", "textColor": C % "color-text-primary", "typography": "{typography.body-medium}", "rounded": "{rounded.sm}", "height": "36px", "border": "1px solid {colors.color-border-strong}"},
        "text-field-focus": {"borderColor": C % "color-accent", "shadow": "0 0 0 3px rgba(88,86,214,0.08)"},
        "search-field": {"backgroundColor": C % "color-bg-tertiary", "textColor": C % "color-text-primary", "rounded": "{rounded.sm}", "height": "36px"},
        "toggle-on": {"backgroundColor": C % "color-accent", "rounded": "{rounded.pill}", "size": "44px x 26px"},
        "toggle-off": {"backgroundColor": C % "color-bg-tertiary", "rounded": "{rounded.pill}"},
        "list-group": {"backgroundColor": C % "color-bg", "rounded": "{rounded.md}", "border": "1px solid {colors.color-border}"},
        "list-row": {"textColor": C % "color-text-primary", "typography": "{typography.body-medium}", "height": "44px", "padding": "4px 16px"},
        "menu": {"backgroundColor": C % "color-bg-elevated", "rounded": "{rounded.md}", "shadow": "0 8px 32px rgba(0,0,0,0.08)", "padding": "4px"},
        "menu-item-active": {"backgroundColor": C % "color-accent", "textColor": C % "text-on-accent", "height": "28px"},
        "alert": {"backgroundColor": C % "color-bg-elevated", "rounded": "{rounded.lg}", "padding": "24px", "shadow": "0 16px 48px rgba(0,0,0,0.1)"},
        "sheet": {"backgroundColor": C % "color-bg-elevated", "rounded": "16px 16px 0 0", "shadow": "0 16px 48px rgba(0,0,0,0.1)"},
        "popover": {"backgroundColor": C % "color-bg-elevated", "rounded": "{rounded.md}", "padding": "16px", "border": "1px solid {colors.color-border}"},
        "navigation-bar": {"backgroundColor": C % "color-bar", "textColor": C % "color-text-primary", "typography": "{typography.title-medium-emphasized}", "height": "44px"},
        "tab-bar-item-selected": {"textColor": C % "color-accent", "typography": "{typography.label-small}"},
        "tab-bar-item": {"textColor": C % "color-text-secondary", "typography": "{typography.label-small}"},
        "sidebar-item-selected": {"backgroundColor": C % "color-accent-light", "textColor": C % "color-accent", "rounded": "{rounded.sm}", "height": "28px"},
        "badge-accent": {"backgroundColor": C % "color-accent-light", "textColor": C % "color-accent", "typography": "{typography.label-medium}", "rounded": "{rounded.pill}", "height": "22px"},
        "count-badge": {"backgroundColor": C % "color-danger", "textColor": C % "text-on-accent", "typography": "{typography.label-small}", "rounded": "{rounded.pill}"},
        "symbol-tile": {"backgroundColor": C % "color-accent", "textColor": C % "text-on-accent", "rounded": "{rounded.mark}", "size": "28px"},
    }
    front = ["---", "version: alpha", "name: Arlo Design System",
             "description: " + q("Arlo AI's design system: one indigo accent on indigo-tinted neutrals, Material 3 spacing and type scale set in Inter, SF Symbols for every icon, Apple HIG components, a fixed 12px button corner, light and dark themes.")]
    front += yaml_map("colors", colors) + yaml_map("typography", typo) + yaml_map("rounded", rounded) + yaml_map("spacing", spacing) + yaml_map("components", comps)
    front.append("---")
    dark = "\n".join(f"| `{t['name']}` | `{B.val(t['value'], 'light')}` | `{B.val(t['value'], 'dark')}` |" for t in toks if not isinstance(t["value"], str))
    S = B.SECS
    prose = f"""
## Overview

{B.INTRO}

{S["Content fundamentals"]}

## Colors

{S["Color"]}

### Light and dark values

The YAML above lists light values. Every themed colour, light → dark:

| Token | Light | Dark |
| --- | --- | --- |
{dark}

## Typography

{S["Typography"]}

## Layout

{S["Spacing and layout"]}

## Elevation & Depth

{S["Elevation and motion"]}

## Shapes

{S["Shape"]}

## Iconography

{S["Iconography"]}

## Components

{S["Components"]}

Each component's rules and markup: `components/<Name>.md`. Working pages: `examples/<Name>.html`.

## Do's and Don'ts

{S["Do and don't"]}
"""
    return "\n".join(front) + "\n" + prose.lstrip("\n")

README = """# arlo-design — the Arlo Design System for AI agents

This folder is the machine-readable form of the Arlo Design System. Read it before you design or write UI for any Arlo app (Arlo Rust, Arlo Lite, AG-UI Rust and their sites). Everything here is generated from the design-system source by `tools/build.py`; do not edit it by hand.

## Read in this order

1. `DESIGN.md` — the whole system in Google's DESIGN.md format: YAML tokens (colours, type, radii, spacing, component specs) plus the brand book as prose rules. Start here.
2. `components/index.md` — the component catalogue; then `components/<Name>.md` for the one you need (rules + copy-paste HTML).
3. `symbols/README.md` and `symbols/symbols.json` — every SF Symbol available, by group and meaning.
4. `tokens/tokens.json` — raw tokens with a usage note on every one (light and dark values).

## Use it in a page

```html
<link rel="stylesheet" href="arlo-design/tokens/tokens.css">        <!-- CSS variables, light + dark -->
<link rel="stylesheet" href="arlo-design/components/components.css"> <!-- ar-* component classes, loads Inter -->
<link rel="stylesheet" href="arlo-design/symbols/symbols.css">       <!-- SF Symbols by name -->

<body class="ar-root">
  <button class="ar-btn ar-btn--filled"><span class="sf" data-symbol="paperplane.fill"></span>Send</button>
</body>
```

- Theme: light by default, follows the OS; force with `<html data-theme="dark">` or `"light"`.
- Symbols: `<span class="sf" data-symbol="NAME"></span>` draws an SF Symbol in `currentColor`; size with `sf--sm` (16), `sf--md` (20), `sf--lg` (24). Only names in `symbols/symbols.json` exist.
- Never hard-code a colour, size or radius that a token covers: use `var(--token-name)`.
- `examples/<Name>.html` are complete working pages for each component; open them to see the expected result.

## Folder map

| Path | What |
| --- | --- |
| `DESIGN.md` | System spec (YAML tokens + rules) |
| `SKILL.md` | Agent skill entry point |
| `tokens/tokens.json`, `tokens/tokens.css` | Tokens as data and as CSS custom properties |
| `components/components.css` | All `ar-*` component classes |
| `components/index.md`, `components/<Name>.md` | Catalogue, and rules + markup per component |
| `examples/<Name>.html` | Working page per component |
| `symbols/symbols.css`, `symbols/symbols.json`, `symbols/<Group>/*.svg` | SF Symbols (Symbols, Calendar, Travel) |
| `logos/*.svg` | Arlo brand marks (never redraw) |

SF Symbols are Apple's and are licensed for designing and building apps on Apple platforms.
"""

SKILL = """---
name: arlo-design
description: Design and build UI for Arlo AI apps and sites with the Arlo Design System — tokens, Apple-HIG components (ar-* CSS classes), SF Symbols by name, light and dark themes. Use whenever creating or reviewing any Arlo screen, component, mockup or page.
---

# Arlo Design System

1. Read `DESIGN.md` in this folder (tokens + rules). Follow its Do's and Don'ts strictly.
2. Pick components from `components/index.md`; read `components/<Name>.md` and copy its markup. Don't invent components the catalogue lacks without saying so.
3. Load `tokens/tokens.css`, `components/components.css`, `symbols/symbols.css`; put `class="ar-root"` on the body.
4. Icons are SF Symbols only: `<span class="sf" data-symbol="NAME"></span>`, names from `symbols/symbols.json` (calendar and travel apps: use the Calendar and Travel groups and the meanings in `symbols/README.md`).
5. Use tokens, never raw values: one `color-accent` filled button per view; `radius-button` (12px) for buttons, segmented controls and steppers; Material 3 spacing (`space100` = 8px); Material 3 type roles in Inter.
6. Check both themes (`data-theme="light"` / `"dark"`) and keep text at 4.5:1 or better.
7. Voice: sentence case, plain and confident, no emoji, no exclamation marks, verbs on buttons.
"""

def run():
    B.reset(B.KIT)
    w = lambda rel, text: B.write(os.path.join(B.KIT, rel), text)
    w("README.md", README); w("SKILL.md", SKILL); w("DESIGN.md", design_md())
    os.makedirs(os.path.join(B.KIT, "tokens"), exist_ok=True)
    shutil.copy(os.path.join(B.SRC, "tokens.json"), os.path.join(B.KIT, "tokens", "tokens.json"))
    w("tokens/tokens.css", B.TOKENS_CSS)
    w("components/components.css", B.bundle_css)
    w("symbols/symbols.css", B.SYMBOLS_CSS)
    # symbols
    entries = []
    for name, (g, path) in sorted(B.symbols.items(), key=lambda x: (B.GROUPS.index(x[1][0]), x[0])):
        os.makedirs(os.path.join(B.KIT, "symbols", g), exist_ok=True)
        shutil.copy(path, os.path.join(B.KIT, "symbols", g, name + ".svg"))
        entries.append({"name": name, "group": g, "file": f"symbols/{g}/{name}.svg", "markup": f'<span class="sf" data-symbol="{name}"></span>'})
    w("symbols/symbols.json", json.dumps({"note": "SF Symbols exported from the SF Symbols app names (Regular, 24pt). Draw with the markup; only these names exist.", "symbols": entries}, indent=1))
    sym_readme = ["# Symbols", "", "Every icon is an SF Symbol. Draw one with `<span class=\"sf\" data-symbol=\"NAME\"></span>` after loading `symbols.css`; it takes `currentColor`. Sizes: `sf--sm` 16, `sf--md` 20, `sf--lg` 24. SF Symbols are Apple's, licensed for apps on Apple platforms.", ""]
    for g in B.GROUPS:
        names = sorted(n for n, (gg, _) in B.symbols.items() if gg == g)
        p = os.path.join(B.SRC, "assets", g, "README.md")
        sym_readme += [f"## {g} ({len(names)})", "", re.sub(r"^#\s+.*\n", "", open(p).read()).strip() if os.path.exists(p) else "", ""]
        show = {"Calendar": "CalendarSymbols", "Travel": "TravelSymbols"}.get(g)
        if show: sym_readme += ["### Meanings", "", "\n".join(l for l in B.byname[show]["readme"].splitlines() if l.startswith("- ")), ""]
        sym_readme += ["Names: " + ", ".join(f"`{n}`" for n in names), ""]
    w("symbols/README.md", "\n".join(sym_readme))
    os.makedirs(os.path.join(B.KIT, "logos"), exist_ok=True)
    for f in B.logos: shutil.copy(os.path.join(B.SRC, "assets", "Logos", f), os.path.join(B.KIT, "logos", f))
    # components
    cat = ["# Components", "", "Apple-HIG components styled with Arlo tokens. Classes are in `components.css` (prefix `ar-`). Each entry links to its rules and markup.", ""]
    for g in B.COMP_GROUPS:
        cs = [c for c in B.components if c["group"] == g] + ([B.byname[n] for n in ("CalendarSymbols", "TravelSymbols")] if g == "Content" else [])
        if not cs: continue
        cat += [f"## {g}", ""] + [f"- [{c['name']}]({c['name']}.md) — {c['summary']}" for c in cs] + [""]
    w("components/index.md", "\n".join(cat))
    for c in B.components + [B.byname["CalendarSymbols"], B.byname["TravelSymbols"]]:
        w(f"components/{c['name']}.md", f"# {c['name']}\n\n{c['readme']}\n\n## Markup\n\nLoad `tokens.css`, `components.css` and `symbols.css`, put `class=\"ar-root\"` on the body, then:\n\n```html\n{B.snippet(c)}\n```\n\nThe example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:\n\n```css\n{B.example_css(c)}\n```\n\nWorking page: `../examples/{c['name']}.html`\n")
        w(f"examples/{c['name']}.html", B.preview_doc_kit(c))
    n = sum(len(fs) for _, _, fs in os.walk(B.KIT))
    print(f"kit: {n} files in {B.KIT}")
