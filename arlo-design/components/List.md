# List

Lists present rows of related content: settings, conversations, files (Apple: lists and tables, inset grouped style); it replaces Arlo's `Table` in app UI.

- Group `ar-list`: `color-bg` card, `color-border` hairline, `radius-md`, on a `color-bg-secondary` page. Rows `ar-list__row`: at least 44px (`control-lg`), `space200` horizontal padding, `body-medium` text.
- Separators are inset hairlines (`color-border`); with leading symbol tiles add `ar-list--icons` so they start after the tile.
- Leading: an optional `ar-symbol-tile` (28px, `radius-mark`, `color-accent` with a white symbol). Trailing: detail text in `color-text-secondary`, then `chevron.right` in `color-text-tertiary` for rows that navigate, or a `Toggle`.
- `ar-list-header` above (label-medium, `color-text-secondary`) and `ar-list-footer` below explain a group. A destructive row is centred `color-danger` text in its own group.
- Selected row: `ar-list__row--selected` (`color-accent-light`).

**The consumer provides:** the rows (title, optional subtitle, detail, symbol, accessory), selection and navigation. **Don't** put more than one chevron or accessory per row, or mix navigating and non-navigating rows without a cue.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div style="max-width:440px;padding:16px;background:var(--color-bg-secondary);border-radius:var(--radius-lg)">
<div class="ar-list-header">Model</div>
<div class="ar-list ar-list--icons">
<div class="ar-list__row "><span class="ar-symbol-tile"><span class="sf" data-symbol="bolt.fill"></span></span><span class="ar-list__text"><span>Provider</span></span><span class="ar-list__detail">Anthropic</span><span class="ar-list__chev"><span class="sf" data-symbol="chevron.right"></span></span></div>
<div class="ar-list__row "><span class="ar-symbol-tile"><span class="sf" data-symbol="sparkles"></span></span><span class="ar-list__text"><span>Default model</span></span><span class="ar-list__detail">Opus 5.5</span><span class="ar-list__chev"><span class="sf" data-symbol="chevron.right"></span></span></div>
<div class="ar-list__row "><span class="ar-symbol-tile"><span class="sf" data-symbol="globe"></span></span><span class="ar-list__text"><span>Language</span></span><span class="ar-list__detail">English</span><span class="ar-list__chev"><span class="sf" data-symbol="chevron.right"></span></span></div>
</div>
<div class="ar-list-footer">Requests go straight from this device to your provider.</div>
<div style="height:24px"></div>
<div class="ar-list-header">Recent</div>
<div class="ar-list">
<div class="ar-list__row ar-list__row--selected"><span class="ar-list__text"><span>Refactor the AG-UI event stream</span><span class="ar-list__sub">Arlo Rust · 2 min ago</span></span></div>
<div class="ar-list__row "><span class="ar-list__text"><span>Draft release notes for 0.9</span><span class="ar-list__sub">Arlo Lite · Yesterday</span></span></div>
<div class="ar-list__row ar-list__row--destructive">Clear history</div>
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

Working page: `../examples/List.html`
