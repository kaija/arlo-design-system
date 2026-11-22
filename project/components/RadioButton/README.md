# RadioButton

Radio buttons choose exactly one option from a small, visible set (Apple: radio buttons, macOS).

- `ar-radio__dot` 16px circle, white with `color-border-strong` edge; selected (`ar-radio--on`) is `color-accent` with a white centre dot.
- Stack 2–5 options vertically with `space100`–`space150` between rows; more than 5: use `PopUpButton`.
- Wrap the group in `role="radiogroup"` with a visible group label.

**The consumer provides:** native `<input type="radio">` elements sharing a name, labels, and the selected value. **Don't** start a group with nothing selected unless "no choice" is valid.
