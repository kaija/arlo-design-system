# SearchField

A search field filters or finds content (Apple: search fields).

- `ar-search`: 36px, `color-bg-tertiary` fill (no border), `radius-sm`, leading `magnifyingglass` in `color-text-secondary`, placeholder "Search …" naming what is searched.
- Focus: `ar-search--focus` switches to `color-bg` with a `color-accent` 1px inner edge and `halo-focus`. When it has text, show `xmark.circle.fill` (`ar-search__clear`) to clear it.
- Put it at the top of the content it filters: in a navigation bar, a sidebar header, or above a list.

**The consumer provides:** the input, live results or a submit handler, and the clear action. **Don't** hide it behind an icon when search is the main way to navigate.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="max-width:360px">
<div class="ar-search"><span class="sf" data-symbol="magnifyingglass"></span><span class="ar-input__ph">Search chats</span></div>
<div class="ar-search ar-search--focus"><span class="sf" data-symbol="magnifyingglass"></span>local-first<span class="ar-search__clear"><span class="sf" data-symbol="xmark.circle.fill"></span></span></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/SearchField.html`
