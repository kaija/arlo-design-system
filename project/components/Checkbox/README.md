# Checkbox

A checkbox turns an option on or off inside a form that is confirmed later (Apple: checkboxes, macOS).

- `ar-check__box` 16×16, `radius-xs`, white with a `color-border-strong` edge and `shadow-sm`. Checked (`ar-check--on`) and mixed (`ar-check--mixed`) fill with `color-accent` and show a white `checkmark` or dash.
- Label to the right in `body-medium`; the whole row is the hit target (at least 28px tall on desktop, 44px on touch).
- Group related checkboxes in `ar-choices` with an `ar-choices__label` (or a `<fieldset>` and `<legend>`): 8px between rows on pointer devices, flush on touch where rows are 44px.
- Use for independent options in a list; use `Toggle` when the change applies immediately.

**Touch.** Make the whole row (box and label) the hit target; on touch devices rows are at least 44px tall.

**The consumer provides:** a real `<input type="checkbox">`, the label, and the checked/indeterminate state. **Don't** use a checkbox for mutually exclusive choices (use `RadioButton`).
