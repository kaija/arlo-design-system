# Menu

A menu lists actions or options in a temporary panel opened from a button, a pop-up button or a right-click (Apple: menus, context menus, pull-down buttons).

- Panel: `ar-menu`, `color-bg-elevated` (white in light, lifted in dark), `radius-md`, `color-border` hairline, `shadow-lg`, `space50` inset.
- Items: `ar-menu__item`, at least 44px tall (`control-lg`, Apple's minimum touch target) so a finger can't hit the neighbouring item, `label-large`-sized text, leading SF Symbol at `symbol-sm` in `color-text-secondary`, keyboard shortcut in `ar-menu__key`. The hovered or keyboard-focused item is `ar-menu__item--active` (`color-accent` fill, `text-on-accent`).
- Pointer-only desktop UI may use `ar-menu--compact` (28px items, `control-sm`); anything that can be touched keeps the 44px default.
- Group with `ar-menu__sep` and optional `ar-menu__title`. Put destructive items last, after a separator, with `ar-menu__item--destructive`.
- Selection menus show a `checkmark` in `ar-menu__check`; keep the column even when unchecked.

**The consumer provides:** the items (label, symbol, shortcut, handler), the anchor, and dismissal on outside click or Escape. **Don't** nest more than one submenu level or put more than ~12 items in one group.
