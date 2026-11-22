# Badge

Badges label status or category in a few words; count badges show unread or pending numbers.

- `ar-badge`: 22px, `radius-pill` (badges stay capsules: they are labels, not buttons), `label-medium` text, `space125` padding.
- `ar-badge--accent` (category), `--neutral` (meta), `--success` / `--warning` / `--danger` (state only). Success and warning text is `color-text-primary` with the status colour on the symbol, because those colours are below 4.5:1 as small text. Always pair a status colour with a word and a symbol.
- `ar-badge--mono`: Arlo's code pill (`code-pill`, mono stack).
- `ar-count`: `color-danger` capsule with white `label-small` numbers, on tab bar items, sidebar rows and symbols.

**The consumer provides:** the text (sentence case, 1–3 words), the tone, and an optional leading symbol. **Don't** make badges clickable or use status colours for decoration.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="gap:12px">
<div class="row"><span class="ar-badge ar-badge--accent">Local-first</span><span class="ar-badge ar-badge--neutral">MIT</span><span class="ar-badge ar-badge--success"><span class="sf" data-symbol="checkmark.circle.fill"></span>Connected</span><span class="ar-badge ar-badge--warning"><span class="sf" data-symbol="exclamationmark.triangle"></span>Rate limited</span><span class="ar-badge ar-badge--danger"><span class="sf" data-symbol="exclamationmark.circle"></span>Key invalid</span></div>
<div class="row"><span class="ar-badge ar-badge--accent ar-badge--mono">cargo install arlo</span><span class="ar-count">3</span><span class="ar-count">128</span></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Badge.html`
