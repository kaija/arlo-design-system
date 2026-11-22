# Menu

A menu lists actions or options in a temporary panel opened from a button, a pop-up button or a right-click (Apple: menus, context menus, pull-down buttons).

- Panel: `ar-menu`, `color-bg-elevated` (white in light, lifted in dark), `radius-md`, `color-border` hairline, `shadow-lg`, `space50` inset.
- Items: `ar-menu__item`, at least 44px tall (`control-lg`, Apple's minimum touch target) so a finger can't hit the neighbouring item, `label-large`-sized text, leading SF Symbol at `symbol-sm` in `color-text-secondary`, keyboard shortcut in `ar-menu__key`. The hovered or keyboard-focused item is `ar-menu__item--active` (`color-accent` fill, `text-on-accent`).
- Pointer-only desktop UI may use `ar-menu--compact` (28px items, `control-sm`); anything that can be touched keeps the 44px default.
- Group with `ar-menu__sep` and optional `ar-menu__title`. Put destructive items last, after a separator, with `ar-menu__item--destructive`.
- Selection menus show a `checkmark` in `ar-menu__check`; keep the column even when unchecked.

**The consumer provides:** the items (label, symbol, shortcut, handler), the anchor, and dismissal on outside click or Escape. **Don't** nest more than one submenu level or put more than ~12 items in one group.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="row" style="align-items:flex-start;gap:24px">
<div class="ar-menu">
  <div class="ar-menu__item"><span class="sf" data-symbol="document.on.document"></span>Copy<span class="ar-menu__key">⌘C</span></div>
  <div class="ar-menu__item ar-menu__item--active"><span class="sf" data-symbol="arrow.trianglehead.clockwise"></span>Regenerate<span class="ar-menu__key">⌘R</span></div>
  <div class="ar-menu__item"><span class="sf" data-symbol="pencil"></span>Edit message</div>
  <div class="ar-menu__item"><span class="sf" data-symbol="square.and.arrow.up"></span>Share…</div>
  <div class="ar-menu__sep"></div>
  <div class="ar-menu__item ar-menu__item--destructive"><span class="sf" data-symbol="trash"></span>Delete</div>
</div>
<div class="ar-menu">
  <div class="ar-menu__title">Sort by</div>
  <div class="ar-menu__item"><span class="ar-menu__check"><span class="sf sf--sm" data-symbol="checkmark"></span></span>Last updated</div>
  <div class="ar-menu__item"><span class="ar-menu__check"></span>Name</div>
  <div class="ar-menu__sep"></div>
  <div class="ar-menu__title">Show</div>
  <div class="ar-menu__item"><span class="ar-menu__check"><span class="sf sf--sm" data-symbol="checkmark"></span></span>Pinned first</div>
</div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Menu.html`
