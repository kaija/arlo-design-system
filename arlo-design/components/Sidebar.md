# Sidebar

A sidebar lists an app's top-level sections and collections on medium and wider windows (Apple: sidebars).

- `ar-sidebar`: 240px wide, `color-bg-secondary`, `color-border` right edge, `space100` padding. Optional `SearchField` at the top.
- Section headers `ar-sidebar__section` (`label-small`, `color-text-secondary`). Rows `ar-sidebar__item`: 44px (`control-lg`), `radius-sm`, a `symbol-sm` SF Symbol in `color-accent`, `body-medium` text, optional trailing count.
- Rows are at least 44px tall (`control-lg`) so a finger can't hit the neighbouring row. Pointer-only desktop UI may use `ar-sidebar--compact` (32px rows); on touch devices compact rows return to 44px.
- Selected row: `ar-sidebar__item--selected` (`color-accent-light` fill, `color-accent` text).
- Separate the sidebar from content with `pane-spacer` (24px) of padding in the content pane.

**The consumer provides:** sections and items (symbol, title, count), the selection, and a way to collapse it (`sidebar.left`). **Don't** nest more than two levels or use it for actions.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div style="display:flex;height:390px;border:1px solid var(--color-border);border-radius:var(--radius-md);overflow:hidden;max-width:560px">
<div class="ar-sidebar">
  <div class="ar-search"><span class="sf" data-symbol="magnifyingglass"></span><span class="ar-input__ph">Search</span></div>
  <div class="ar-sidebar__section">Workspace</div>
  <div class="ar-sidebar__item ar-sidebar__item--selected"><span class="sf" data-symbol="bubble.left"></span>Chats<span class="ar-sidebar__count">12</span></div>
  <div class="ar-sidebar__item"><span class="sf" data-symbol="sparkles"></span>Agents</div>
  <div class="ar-sidebar__item"><span class="sf" data-symbol="document"></span>Files</div>
  <div class="ar-sidebar__section">Projects</div>
  <div class="ar-sidebar__item"><span class="sf" data-symbol="chevron.left.forwardslash.chevron.right"></span>arlo-rust</div>
  <div class="ar-sidebar__item"><span class="sf" data-symbol="chevron.left.forwardslash.chevron.right"></span>ag-ui-rust</div>
</div>
<div style="flex:1;padding:24px" class="cap">Content pane · pane-spacer 24px</div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Sidebar.html`
