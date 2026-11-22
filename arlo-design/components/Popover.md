# Popover

A popover shows transient detail or a few controls anchored to the element that opened it (Apple: popovers); help tags are the hover-only variant, replacing Arlo's `Tooltip`.

- `ar-popover`: `color-bg`, `radius-md`, `color-border` hairline, `shadow-lg`, `space200` padding, max 280px, with an arrow pointing at its source (`--arrow-x`). Optional `ar-popover__title`.
- `ar-helptag`: a dark (`color-text-primary`) label, white `body-small` text, for icon-only buttons on hover or focus, after a short delay.
- Dismiss a popover on outside click or Escape.

**The consumer provides:** the anchor, content, placement, and dismissal. **Don't** put essential actions only in a help tag, or open a popover on hover.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="row" style="align-items:flex-start;gap:32px">
<div class="col" style="gap:10px">
  <button class="ar-btn ar-btn--gray ar-btn--sm"><span class="sf" data-symbol="info.circle"></span>Context</button>
  <div class="ar-popover" style="--arrow-x:20px">
    <p class="ar-popover__title">Context window</p>
    82,000 of 200,000 tokens used. Older messages are summarised when it fills.
    <div class="ar-progress" style="margin-top:12px"><div class="ar-progress__fill" style="width:41%"></div></div>
  </div>
</div>
<div class="col" style="gap:8px;align-items:flex-start">
  <button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="Copy"><span class="sf" data-symbol="document.on.document"></span></button>
  <span class="ar-helptag">Copy message</span>
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

Working page: `../examples/Popover.html`
