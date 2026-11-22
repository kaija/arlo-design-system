# Sidebar

A sidebar lists an app's top-level sections and collections on medium and wider windows (Apple: sidebars).

- `ar-sidebar`: 240px wide, `color-bg-secondary`, `color-border` right edge, `space100` padding. Optional `SearchField` at the top.
- Section headers `ar-sidebar__section` (`label-small`, `color-text-secondary`). Rows `ar-sidebar__item`: 44px (`control-lg`), `radius-sm`, a `symbol-sm` SF Symbol in `color-accent`, `body-medium` text, optional trailing count.
- Rows are at least 44px tall (`control-lg`) so a finger can't hit the neighbouring row. Pointer-only desktop UI may use `ar-sidebar--compact` (32px rows); on touch devices compact rows return to 44px.
- Selected row: `ar-sidebar__item--selected` (`color-accent-light` fill, `color-accent` text).
- Separate the sidebar from content with `pane-spacer` (24px) of padding in the content pane.

**The consumer provides:** sections and items (symbol, title, count), the selection, and a way to collapse it (`sidebar.left`). **Don't** nest more than two levels or use it for actions.
