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
