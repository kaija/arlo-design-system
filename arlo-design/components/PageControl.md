# PageControl

A page control shows how many pages a horizontally paged view has and which one is showing (Apple: page controls), such as onboarding.

- `ar-pages`: 8px dots, `space100` apart. Current dot `color-text-primary`; others `color-text-tertiary` at reduced opacity. `ar-pages--platter` adds a `color-bg-tertiary` capsule for busy backgrounds.
- Up to ~10 pages; beyond that, use a different navigation.

**Touch.** The control is 44px tall on touch devices; tapping either side moves one page.

**The consumer provides:** page count, current page, and taps/arrow keys to move. **Don't** use it for hierarchical navigation; use `NavigationBar`.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="row" style="gap:24px">
<span class="ar-pages"><span class="ar-pages__dot ar-pages__dot--current"></span><span class="ar-pages__dot"></span><span class="ar-pages__dot"></span><span class="ar-pages__dot"></span></span>
<span class="ar-pages ar-pages--platter"><span class="ar-pages__dot"></span><span class="ar-pages__dot ar-pages__dot--current"></span><span class="ar-pages__dot"></span></span>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/PageControl.html`
