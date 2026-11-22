# TabBar

A tab bar switches between the top-level sections of an app on compact windows (Apple: tab bars).

- `ar-tabbar`: bottom edge, frosted like `NavigationBar`, `color-border` top hairline. 3–5 items, each an SF Symbol at `symbol-lg` over a `label-small` title.
- Selected item: `color-accent`. Others: `color-text-secondary` (`color-text-tertiary` is too light for 11px labels).
- A count badge (`ar-count`) may sit on an item's symbol.
- On medium and wider windows switch to a `Sidebar`.

**The consumer provides:** the sections (symbol, title, badge), the selected section, and navigation. **Don't** use a tab bar for actions, or hide it inside a section.
