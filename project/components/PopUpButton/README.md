# PopUpButton

A pop-up button shows the current choice from a short, mutually exclusive list and opens a menu to change it (Apple: pop-up buttons).

- Use it for 3–12 options where the current value matters at a glance (model, language, sort order). Fewer than 4 always-visible options: use `SegmentedControl`. More than 12 or searchable: use a `SearchField` with a list.
- Build it from `ar-btn` + `ar-popup` (outline or gray style), the value as the label and a trailing `chevron.down` in `ar-popup__chev`.
- The open state is a `Menu` whose current item carries `checkmark` in `ar-menu__check`.

**The consumer provides:** the options, the selected value, and the change handler. **Don't** use it for actions; that is a pull-down `Menu` from a button.
