# Toggle

A toggle switches one setting on or off with immediate effect (Apple: toggles / switches).

- `ar-toggle` 44×26 (touch), `ar-toggle--sm` 32×18 (desktop forms). Off: `color-bg-tertiary` track with a `color-border-strong` edge. On: `ar-toggle--on`, `color-accent` track. Knob white with `shadow-sm`; it slides in 250ms ease.
- The toggle keeps Apple's capsule (`radius-pill`): it is a switch, not a button, so `radius-button` does not apply.
- Place it trailing in a `List` row with the label leading. The change applies at once; no Save button.

**Touch.** The toggle has a 44×44 hit area; `ar-toggle--sm` returns to full size on touch devices. In a list row, make the whole row toggle it.

**The consumer provides:** `role="switch"`, `aria-checked`, the label, and the handler. **Don't** use a toggle for choices that need confirmation (use `Checkbox` in a form) or for more than two states.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col">
<div class="ar-list" style="max-width:420px">
  <div class="ar-list__row"><span class="ar-list__text">Stream responses</span><span class="ar-toggle ar-toggle--on" role="switch" aria-checked="true"></span></div>
  <div class="ar-list__row"><span class="ar-list__text">Send usage data</span><span class="ar-toggle" role="switch" aria-checked="false"></span></div>
  <div class="ar-list__row"><span class="ar-list__text" style="color:var(--color-text-tertiary)">Sync keys to iCloud</span><span class="ar-toggle ar-toggle--disabled" role="switch" aria-disabled="true"></span></div>
</div>
<div class="row"><span class="cap">Small (desktop)</span><span class="ar-toggle ar-toggle--sm ar-toggle--on"></span><span class="ar-toggle ar-toggle--sm"></span></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Toggle.html`
