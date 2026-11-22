# List

Lists present rows of related content: settings, conversations, files (Apple: lists and tables, inset grouped style); it replaces Arlo's `Table` in app UI.

- Group `ar-list`: `color-bg` card, `color-border` hairline, `radius-md`, on a `color-bg-secondary` page. Rows `ar-list__row`: at least 44px (`control-lg`), `space200` horizontal padding, `body-medium` text.
- Separators are inset hairlines (`color-border`); with leading symbol tiles add `ar-list--icons` so they start after the tile.
- Leading: an optional `ar-symbol-tile` (28px, `radius-mark`, `color-accent` with a white symbol). Trailing: detail text in `color-text-secondary`, then `chevron.right` in `color-text-tertiary` for rows that navigate, or a `Toggle`.
- `ar-list-header` above (label-medium, `color-text-secondary`) and `ar-list-footer` below explain a group. A destructive row is centred `color-danger` text in its own group.
- Selected row: `ar-list__row--selected` (`color-accent-light`).

**The consumer provides:** the rows (title, optional subtitle, detail, symbol, accessory), selection and navigation. **Don't** put more than one chevron or accessory per row, or mix navigating and non-navigating rows without a cue.
