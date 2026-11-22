# SegmentedControl

A segmented control switches between 2–5 closely related views or modes (Apple: segmented controls); it replaces Arlo's pill `Tabs`.

- Track `ar-seg`: `color-bg-tertiary`, `space25` inset, corner `radius-button` + 2px. Segments `ar-seg__item`: 28px (`control-sm`), 13px medium text in `color-text-secondary`; the selected one is `ar-seg__item--selected` (white, `color-text-primary`, `shadow-sm`).
- Segments use the same corner as buttons (`radius-button`, 12px), not a capsule.
- `ar-seg--full` stretches segments equally across a container.
- Text or a symbol in each segment, consistently: don't mix symbol-only and text-only segments.

**The consumer provides:** the segments, the selected index, and the handler; use `role="tablist"`/`role="tab"` when it switches views. **Don't** use it for actions or for more than 5 options.
