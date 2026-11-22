# PageControl

A page control shows how many pages a horizontally paged view has and which one is showing (Apple: page controls), such as onboarding.

- `ar-pages`: 8px dots, `space100` apart. Current dot `color-text-primary`; others `color-text-tertiary` at reduced opacity. `ar-pages--platter` adds a `color-bg-tertiary` capsule for busy backgrounds.
- Up to ~10 pages; beyond that, use a different navigation.

**The consumer provides:** page count, current page, and taps/arrow keys to move. **Don't** use it for hierarchical navigation; use `NavigationBar`.
