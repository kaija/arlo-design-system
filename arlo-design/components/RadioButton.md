# RadioButton

Radio buttons choose exactly one option from a small, visible set (Apple: radio buttons, macOS).

- `ar-radio__dot` 16px circle, white with `color-border-strong` edge; selected (`ar-radio--on`) is `color-accent` with a white centre dot.
- Stack 2–5 options vertically with `space100`–`space150` between rows; more than 5: use `PopUpButton`.
- Wrap the group in `role="radiogroup"` with a visible group label.

**The consumer provides:** native `<input type="radio">` elements sharing a name, labels, and the selected value. **Don't** start a group with nothing selected unless "no choice" is valid.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="gap:12px" role="radiogroup">
<span class="ar-radio ar-radio--on"><span class="ar-radio__dot"></span>Run locally (Arlo Rust)</span>
<span class="ar-radio"><span class="ar-radio__dot"></span>Use my provider directly</span>
<span class="ar-radio ar-radio--disabled"><span class="ar-radio__dot"></span>Hosted (not offered)</span>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/RadioButton.html`
