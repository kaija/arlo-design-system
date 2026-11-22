# Button

A button starts an action; Arlo buttons follow Apple's styles (filled, tinted, gray, plain) with one fixed 12px corner, `radius-button`.

**Styles.** Use them in this order of emphasis:
- `ar-btn--filled`: the one primary action on a screen or in a dialog (`color-accent`, hover `color-accent-hover` + `shadow-accent`).
- `ar-btn--tinted`: a secondary action that should still read as accent (`color-accent-light` fill).
- `ar-btn--gray`: neutral secondary actions such as Cancel (`color-bg-tertiary`).
- `ar-btn--outline`: Arlo's original white-with-border secondary button, for marketing pages and toolbars on white.
- `ar-btn--plain`: low-emphasis and inline actions, toolbar icons.
- `ar-btn--destructive` / `ar-btn--destructive-plain`: actions that delete or can't be undone.

**Sizes.** `ar-btn--sm` (28, `control-sm`) for toolbars and dense desktop UI, default 36 (`control-md`), `ar-btn--lg` (44, `control-lg`) for touch-first primary actions. Add `ar-btn--icon` for symbol-only square buttons, which must have an `aria-label`.

**Corner.** Every size uses the same `radius-button`. The token is 12px: Material's full pill and Apple's capsule are deliberately not used, so 36px and 44px buttons stay soft rectangles while 28px buttons come out nearly round.

**Touch.** Every button has a 44×44 hit area even when drawn smaller. On touch devices `ar-btn` grows to 44px and `ar-btn--sm` to 36px; leave at least 8px (`space100`) between neighbouring buttons, and 16px (`space200`) beside a 28px `ar-btn--sm`, so hit areas never overlap.

**The consumer provides:** a `<button>` (or `<a>` for navigation) with a verb label in sentence case, an optional leading SF Symbol (`.sf`, sized by the button), and a disabled state.

**Do:** use one filled button per view. Swap `arrow.up.circle.fill` (submit) to `stop.fill` in the same button while a response streams.
**Don't:** use title case or ending punctuation, put two filled buttons side by side, or scale on press.
