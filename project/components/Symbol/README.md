# Symbol

Every interface icon is an SF Symbol, drawn by the `.sf` class as a mask tinted by `currentColor`, so a symbol takes the colour of the text around it.

- Markup: `<span class="sf" style="--sf:url(/_blob/<id>)"></span>`; the ids are in the Symbols asset group. Size with `sf--sm` (16), `sf--md` (20), `sf--lg` (24) or `--sf-size`; components set the right size themselves.
- Match the symbol's weight and size to the adjacent text: `symbol-sm` beside `body-medium`/`label-large`, `symbol-md` beside `body-large`/`title-medium`, `symbol-lg` in tab bars and navigation bars.
- Colour: `color-text-secondary` at rest in toolbars and composers, `color-accent` when active or in sidebars, status colours only for state. On a filled tile (`ar-symbol-tile`) the symbol is `text-on-accent`.
- Use the outline variant by default and the `.fill` variant for selected states and small solid actions (`paperplane.fill`, `stop.fill`, `arrow.up.circle.fill`).

**The consumer provides:** the symbol name and an accessible label on the control (symbols themselves are decorative). **Don't** redraw, recolour parts of, or stretch a symbol, or use one as a logo.
