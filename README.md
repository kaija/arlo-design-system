# Arlo Design System

The design system for the Arlo AI project family: Arlo's indigo palette, Material 3 spacing and type scale set in Inter, SF Symbols for every icon, Apple HIG components, a fixed 12px button corner, and light and dark themes.

**Docs site:** https://kaija.github.io/arlo-design-system/ (deployed from `site/` by GitHub Actions on every push to `main`)

| Folder | What |
| --- | --- |
| [`project/`](project/README.md) | The source: tokens, brand book, component guidelines and previews, symbol and logo assets. Edit here. |
| [`site/`](site/index.html) | Documentation website in the style of m3.material.io. Generated. Open `site/index.html` directly or serve the folder. |
| [`arlo-design/`](arlo-design/README.md) | The system packaged for AI agents: `SKILL.md`, `DESIGN.md` (Google DESIGN.md format), tokens, component specs with HTML, examples, SF Symbols by name. Generated. |
| [`tools/`](tools/make.py) | Generators for `site/` and `arlo-design/`. |

## Rebuild

After changing anything in `project/`:

```bash
python3 tools/make.py
```

`site/` and `arlo-design/` are rebuilt from scratch, so don't edit them by hand.

To preview the site with live preview sizing:

```bash
python3 -m http.server 8765 --directory site
```

## Licences

SF Symbols are Apple's and are licensed for designing and building apps on Apple platforms. Inter is loaded from Google Fonts (SIL Open Font License).
