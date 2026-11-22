# SegmentedControl

A segmented control switches between 2–5 closely related views or modes (Apple: segmented controls); it replaces Arlo's pill `Tabs`.

- Track `ar-seg`: `color-bg-tertiary`, `space25` inset, corner `radius-button` + 2px. Segments `ar-seg__item`: 28px (`control-sm`), 13px medium text in `color-text-secondary`; the selected one is `ar-seg__item--selected` (white, `color-text-primary`, `shadow-sm`).
- Segments use the same corner as buttons (`radius-button`, 12px), not a capsule.
- `ar-seg--full` stretches segments equally across a container.
- Text or a symbol in each segment, consistently: don't mix symbol-only and text-only segments.

**Touch.** Each segment has a 44px-tall hit area; on touch devices segments grow to 36px.

**The consumer provides:** the segments, the selected index, and the handler; use `role="tablist"`/`role="tab"` when it switches views. **Don't** use it for actions or for more than 5 options.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col">
<div class="ar-seg"><span class="ar-seg__item ar-seg__item--selected">Chat</span><span class="ar-seg__item">Agents</span><span class="ar-seg__item">Files</span></div>
<div class="ar-seg"><span class="ar-seg__item"><span class="sf" data-symbol="bubble.left"></span>Messages</span><span class="ar-seg__item ar-seg__item--selected"><span class="sf" data-symbol="chevron.left.forwardslash.chevron.right"></span>Code</span></div>
<div class="ar-seg ar-seg--full" style="max-width:360px"><span class="ar-seg__item">Day</span><span class="ar-seg__item ar-seg__item--selected">Week</span><span class="ar-seg__item">Month</span><span class="ar-seg__item">Year</span></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/SegmentedControl.html`
