# Sheet

A sheet presents a focused task that relates to the current view, such as creating or editing something (Apple: sheets).

- `ar-sheet`: `color-bg`, top corners `radius-lg`, `shadow-xl`, rising from the bottom on compact windows (centred, all corners rounded, on wider ones), over `color-scrim`.
- A grabber (`ar-sheet__grabber`, 36×5, `color-border-strong`) when it can be resized or swiped away.
- Bar `ar-sheet__bar`: Cancel (`ar-btn--plain`) leading, title (`title-medium-emphasized`) centred, confirm (`ar-btn--plain`, semibold) trailing.
- Body with `space200` side padding; forms use `TextField`.

**The consumer provides:** the content, the confirm/cancel handlers, and a check for unsaved changes on dismiss. **Don't** stack sheets on sheets or use one for a yes/no question (use `Alert`).

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div style="max-width:420px;padding-top:24px;background:var(--color-scrim);border-radius:var(--radius-md);overflow:hidden">
<div class="ar-sheet">
  <div class="ar-sheet__grabber"></div>
  <div class="ar-sheet__bar"><button class="ar-btn ar-btn--plain">Cancel</button><span class="ar-sheet__title">New agent</span><button class="ar-btn ar-btn--plain" style="font-weight:600">Create</button></div>
  <div class="ar-sheet__body ar-form">
    <label class="ar-field"><span class="ar-field__label">Name</span><span class="ar-input ar-input--focus">Release notes writer</span></label>
    <label class="ar-field"><span class="ar-field__label">Instructions</span><span class="ar-input ar-input--multiline"><span class="ar-input__ph">What should this agent do?</span></span></label>
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

Working page: `../examples/Sheet.html`
