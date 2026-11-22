# Popover

A popover shows transient detail or a few controls anchored to the element that opened it (Apple: popovers); help tags are the hover-only variant, replacing Arlo's `Tooltip`.

- `ar-popover`: `color-bg`, `radius-md`, `color-border` hairline, `shadow-lg`, `space200` padding, max 280px, with an arrow pointing at its source (`--arrow-x`). Optional `ar-popover__title`.
- `ar-helptag`: a dark (`color-text-primary`) label, white `body-small` text, for icon-only buttons on hover or focus, after a short delay.
- Dismiss a popover on outside click or Escape.

**The consumer provides:** the anchor, content, placement, and dismissal. **Don't** put essential actions only in a help tag, or open a popover on hover.
