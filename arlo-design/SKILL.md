---
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
