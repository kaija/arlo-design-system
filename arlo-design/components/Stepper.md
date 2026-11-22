# Stepper

A stepper raises or lowers a value by a fixed amount (Apple: steppers).

- `ar-stepper`: two 44×28 halves on `color-bg-tertiary`, corner `radius-button`, a `color-border-strong` divider, `minus` / `plus` symbols at 12px.
- Always show the current value next to it; dim a half (`ar-stepper__btn--disabled`) at the limit.

**Touch.** Each half has a 44×44 hit area; on touch devices the stepper grows to 36×96px.

**The consumer provides:** two buttons with `aria-label`s ("Decrease", "Increase"), the value, step and bounds. **Don't** use it when values span a large range; use a `Slider` or `TextField`.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="row" style="gap:16px">
<span style="font:400 14px/20px var(--font-sans)">Max tokens · 4,096</span>
<span class="ar-stepper"><span class="ar-stepper__btn"><span class="sf" data-symbol="minus"></span></span><span class="ar-stepper__sep"></span><span class="ar-stepper__btn"><span class="sf" data-symbol="plus"></span></span></span>
<span class="ar-stepper"><span class="ar-stepper__btn ar-stepper__btn--disabled"><span class="sf" data-symbol="minus"></span></span><span class="ar-stepper__sep"></span><span class="ar-stepper__btn"><span class="sf" data-symbol="plus"></span></span></span>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Stepper.html`
