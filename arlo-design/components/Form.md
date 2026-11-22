# Form

A form lays out fields, choices and actions with one fixed spacing scale, so every settings screen, sheet and dialog groups information the same way.

**Spacing, by proximity** (the closer two things are, the more they belong together):

| Between | Space | Token |
| --- | --- | --- |
| Help or error text and its field | 4px | `space50` |
| Label and its field; choices in a group (pointer) | 8px | `space100` |
| Section title and its first field; side-by-side fields | 16px | `space200` |
| Field and field (stacked) | 24px | `space300` |
| Section and section; last field and the action row | 32px | `space300` + `space100` |

- `ar-form`: a column with 24px between fields, max 560px wide. Put a single column on phones; `ar-form__row` places 2–3 short related fields side by side (16px apart, wrapping below 160px each).
- `ar-form__section` groups related fields under an `ar-form__title` (`title-medium-emphasized`) with an optional `ar-form__note` 4px below it.
- `ar-field`: `ar-field__label` 8px above the control, `ar-field__help` 4px below. Mark optional fields with `ar-field__opt` ("Optional"), not required ones with asterisks. Error text replaces the help text in place, so the layout doesn't jump.
- `ar-choices`: a labelled group of checkboxes or radio buttons, 8px apart on pointer devices and flush on touch, where each row is already 44px.
- `ar-form__actions`: right-aligned, 32px below the last field, buttons 8px apart, the default action last. Below 480px wide the buttons stack full width with the default on top.
- Fields are 36px tall with 10px side padding on pointer devices and 44px with 16px on touch.

**The consumer provides:** real `<form>`, `<label>`, `<input>` and `<fieldset>`/`<legend>` (or `role="group"` with `aria-labelledby`) elements inside these classes, validation, and the submit handler. **Don't** put help text above a field, centre labels, or space fields by hand: use these classes so every form keeps the same rhythm.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<p class="spec"><span><b>4</b> help ↔ field</span><span><b>8</b> label ↔ field</span><span><b>16</b> section title ↔ first field · side-by-side fields</span><span><b>24</b> field ↔ field</span><span><b>32</b> section ↔ section · last field ↔ actions</span></p>
<form class="ar-form" onsubmit="return false">
  <section class="ar-form__section">
    <h3 class="ar-form__title">Provider</h3>
    <p class="ar-form__note">Requests go straight from this device to your provider.</p>
    <div class="ar-form__row">
      <label class="ar-field"><span class="ar-field__label">Provider</span><button type="button" class="ar-btn ar-btn--outline ar-popup" style="min-width:0">Anthropic <span class="ar-popup__chev"><span class="sf" data-symbol="chevron.down"></span></span></button></label>
      <label class="ar-field"><span class="ar-field__label">Model</span><button type="button" class="ar-btn ar-btn--outline ar-popup" style="min-width:0">Opus 5.5 <span class="ar-popup__chev"><span class="sf" data-symbol="chevron.down"></span></span></button></label>
    </div>
    <label class="ar-field"><span class="ar-field__label">API key</span><span class="ar-input ar-input--focus"><span class="sf" data-symbol="lock"></span>sk-ant-•••••••••••</span><span class="ar-field__help">Stored in your Keychain. We never see it.</span></label>
    <label class="ar-field"><span class="ar-field__label">Endpoint<span class="ar-field__opt">Optional</span></span><span class="ar-input ar-input--error">htps://api.local</span><span class="ar-field__help ar-field__help--error">Enter a URL that starts with https://</span></label>
  </section>
  <section class="ar-form__section">
    <h3 class="ar-form__title">Behaviour</h3>
    <div class="ar-choices" role="radiogroup" aria-labelledby="f-run"><span class="ar-choices__label" id="f-run">Where agents run</span>
      <span class="ar-radio ar-radio--on"><span class="ar-radio__dot"></span>Run locally (Arlo Rust)</span>
      <span class="ar-radio"><span class="ar-radio__dot"></span>Use my provider directly</span>
    </div>
    <div class="ar-choices" role="group" aria-labelledby="f-exp"><span class="ar-choices__label" id="f-exp">Include in exports</span>
      <span class="ar-check ar-check--on"><span class="ar-check__box"><span class="sf" data-symbol="checkmark"></span></span>Tool calls</span>
      <span class="ar-check"><span class="ar-check__box"></span>System prompt</span>
    </div>
    <label class="ar-field"><span class="ar-field__label">System prompt<span class="ar-field__opt">Optional</span></span><span class="ar-input ar-input--multiline"><span class="ar-input__ph">You are a concise assistant…</span></span></label>
  </section>
  <div class="ar-form__actions"><button type="button" class="ar-btn ar-btn--gray">Cancel</button><button type="button" class="ar-btn ar-btn--filled">Save</button></div>
</form>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.spec { display:flex; flex-wrap:wrap; gap:8px 16px; margin:0 0 24px; font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
.spec b { color:var(--color-accent); font-weight:600; }
```

Working page: `../examples/Form.html`
