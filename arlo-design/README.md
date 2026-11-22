# arlo-design — the Arlo Design System for AI agents

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
