# TextField

A text field takes a short line of text; a multiline field takes paragraphs (Apple: text fields, text views).

- `ar-input`: 36px (`control-md`), `color-bg` with a `color-border-strong` 1px edge, `radius-sm`, `body-medium` text, `space125` horizontal padding. Placeholder in `ar-input__ph` (`color-text-tertiary`: never the only label).
- Focus: `ar-input--focus` turns the border `color-accent` and adds `halo-focus`. Error: `ar-input--error` (`color-danger` border, `color-danger-light` fill) with `ar-field__help--error` text that says how to fix it.
- Wrap in `ar-field` with a visible `ar-field__label` (`label-medium`) above and optional `ar-field__help` below.
- A leading `symbol-sm` SF Symbol may say what the field holds (`lock` for secrets).

**Touch.** Fields grow to 44px tall on touch devices.

**The consumer provides:** a real `<input>`/`<textarea>` inside the frame, the label, validation and the help text. **Don't** rely on placeholder text as the label or show errors before the user leaves the field.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="row" style="align-items:flex-start;gap:24px">
<div class="col" style="width:280px">
  <label class="ar-field"><span class="ar-field__label">Provider</span><span class="ar-input"><span class="ar-input__ph">e.g. Anthropic</span></span></label>
  <label class="ar-field"><span class="ar-field__label">API key</span><span class="ar-input ar-input--focus"><span class="sf" data-symbol="lock"></span>sk-ant-•••••••••••</span><span class="ar-field__help">Stored in your Keychain. We never see it.</span></label>
</div>
<div class="col" style="width:280px">
  <label class="ar-field"><span class="ar-field__label">Endpoint</span><span class="ar-input ar-input--error">htps://api.local</span><span class="ar-field__help ar-field__help--error">Enter a URL that starts with https://</span></label>
  <label class="ar-field"><span class="ar-field__label">System prompt</span><span class="ar-input ar-input--multiline"><span class="ar-input__ph">You are a concise assistant…</span></span></label>
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

Working page: `../examples/TextField.html`
