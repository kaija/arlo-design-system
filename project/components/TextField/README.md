# TextField

A text field takes a short line of text; a multiline field takes paragraphs (Apple: text fields, text views).

- `ar-input`: 36px (`control-md`), `color-bg` with a `color-border-strong` 1px edge, `radius-sm`, `body-medium` text, 10px (`space125`) side padding, 16px (`space200`) on touch devices. A leading symbol is `color-text-secondary`. Placeholder in `ar-input__ph` (`color-text-tertiary`: never the only label).
- Focus: `ar-input--focus` turns the border `color-accent` and adds `halo-focus`. Error: `ar-input--error` (`color-danger` border, `color-danger-light` fill) with `ar-field__help--error` text that says how to fix it.
- Wrap in `ar-field` with a visible `ar-field__label` (`label-medium`) 8px above and optional `ar-field__help` 4px below, so help text sits closer to its own field than to the next label. Stack fields 24px apart inside an `ar-form` (see Form).
- A leading `symbol-sm` SF Symbol may say what the field holds (`lock` for secrets).

**Touch.** Fields grow to 44px tall on touch devices.

**The consumer provides:** a real `<input>`/`<textarea>` inside the frame, the label, validation and the help text. **Don't** rely on placeholder text as the label or show errors before the user leaves the field.
