# Toggle

A toggle switches one setting on or off with immediate effect (Apple: toggles / switches).

- `ar-toggle` 44×26 (touch), `ar-toggle--sm` 32×18 (desktop forms). Off: `color-bg-tertiary` track with a `color-border-strong` edge. On: `ar-toggle--on`, `color-accent` track. Knob white with `shadow-sm`; it slides in 250ms ease.
- The toggle keeps Apple's capsule (`radius-pill`): it is a switch, not a button, so `radius-button` does not apply.
- Place it trailing in a `List` row with the label leading. The change applies at once; no Save button.

**Touch.** The toggle has a 44×44 hit area; `ar-toggle--sm` returns to full size on touch devices. In a list row, make the whole row toggle it.

**The consumer provides:** `role="switch"`, `aria-checked`, the label, and the handler. **Don't** use a toggle for choices that need confirmation (use `Checkbox` in a form) or for more than two states.
