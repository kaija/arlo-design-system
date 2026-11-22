# PopUpButton

A pop-up button shows the current choice from a short, mutually exclusive list and opens a menu to change it (Apple: pop-up buttons).

- Use it for 3–12 options where the current value matters at a glance (model, language, sort order). Fewer than 4 always-visible options: use `SegmentedControl`. More than 12 or searchable: use a `SearchField` with a list.
- Build it from `ar-btn` + `ar-popup` (outline or gray style), the value as the label and a trailing `chevron.down` in `ar-popup__chev`.
- The open state is a `Menu` whose current item carries `checkmark` in `ar-menu__check`.

**The consumer provides:** the options, the selected value, and the change handler. **Don't** use it for actions; that is a pull-down `Menu` from a button.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="row" style="align-items:flex-start;gap:24px">
<div class="col" style="gap:16px">
  <div class="cap">Closed</div>
  <button class="ar-btn ar-btn--outline ar-popup">claude-opus-5-5 <span class="ar-popup__chev"><span class="sf" data-symbol="chevron.down"></span></span></button>
  <button class="ar-btn ar-btn--gray ar-btn--sm ar-popup" style="min-width:120px">English <span class="ar-popup__chev"><span class="sf" data-symbol="chevron.down"></span></span></button>
</div>
<div class="col" style="gap:8px">
  <div class="cap">Open</div>
  <div class="ar-menu">
    <div class="ar-menu__item"><span class="ar-menu__check"><span class="sf sf--sm" data-symbol="checkmark"></span></span>claude-opus-5-5</div>
    <div class="ar-menu__item ar-menu__item--active"><span class="ar-menu__check"></span>claude-sonnet-5-5</div>
    <div class="ar-menu__item"><span class="ar-menu__check"></span>claude-haiku-5-5</div>
  </div>
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

Working page: `../examples/PopUpButton.html`
