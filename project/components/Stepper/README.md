# Stepper

A stepper raises or lowers a value by a fixed amount (Apple: steppers).

- `ar-stepper`: two 40×28 halves on `color-bg-tertiary`, corner `radius-button`, a `color-border-strong` divider, `minus` / `plus` symbols at 12px.
- Always show the current value next to it; dim a half (`ar-stepper__btn--disabled`) at the limit.

**The consumer provides:** two buttons with `aria-label`s ("Decrease", "Increase"), the value, step and bounds. **Don't** use it when values span a large range; use a `Slider` or `TextField`.
