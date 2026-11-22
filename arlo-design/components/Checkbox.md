# Checkbox

A checkbox turns an option on or off inside a form that is confirmed later (Apple: checkboxes, macOS).

- `ar-check__box` 16×16, `radius-xs`, white with a `color-border-strong` edge and `shadow-sm`. Checked (`ar-check--on`) and mixed (`ar-check--mixed`) fill with `color-accent` and show a white `checkmark` or dash.
- Label to the right in `body-medium`; the whole row is the hit target (at least 28px tall on desktop, 44px on touch).
- Use for independent options in a list; use `Toggle` when the change applies immediately.

**The consumer provides:** a real `<input type="checkbox">`, the label, and the checked/indeterminate state. **Don't** use a checkbox for mutually exclusive choices (use `RadioButton`).

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="gap:12px">
<span class="ar-check ar-check--on"><span class="ar-check__box"><span class="sf" data-symbol="checkmark"></span></span>Include tool calls in export</span>
<span class="ar-check"><span class="ar-check__box"></span>Include system prompt</span>
<span class="ar-check ar-check--mixed"><span class="ar-check__box"><span class="ar-check__dash"></span></span>All attachments (some selected)</span>
<span class="ar-check ar-check--disabled"><span class="ar-check__box"></span>Include hidden reasoning</span>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Checkbox.html`
