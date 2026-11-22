# ProgressIndicator

Progress indicators show that work is happening: a bar or ring when the amount is known, a spinner when it isn't (Apple: progress indicators).

- Bar `ar-progress`: 4px, `radius-pill`, `color-bg-tertiary` track, `color-accent` fill (`color-success` when complete via `ar-progress--success`). Label above with the task and percent.
- Spinner `ar-spinner` 20px (inline) or `ar-spinner--lg` 32px (page), `color-accent` arc on a `color-bg-tertiary` ring, 800ms linear.
- Ring `ar-ring` (20px, set `--p`) for compact determinate progress, such as a download in a list row.

**The consumer provides:** the value (or none for indeterminate) and an accessible label (`role="progressbar"`, `aria-valuenow`). **Don't** show a spinner for under ~1 second or stack several on one screen.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="max-width:420px">
<div class="ar-field"><span class="ar-field__label">Indexing repository · 64%</span><div class="ar-progress"><div class="ar-progress__fill" style="width:64%"></div></div></div>
<div class="ar-field"><span class="ar-field__label">Model downloaded</span><div class="ar-progress ar-progress--success"><div class="ar-progress__fill" style="width:100%"></div></div></div>
<div class="row" style="gap:20px"><span class="ar-spinner"></span><span class="ar-spinner ar-spinner--lg"></span><span class="ar-ring" style="--p:40%"></span><span class="cap">Thinking…</span></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/ProgressIndicator.html`
