# SearchField

A search field filters or finds content (Apple: search fields).

- `ar-search`: 36px, `color-bg-tertiary` fill (no border), `radius-sm`, leading `magnifyingglass` in `color-text-secondary`, placeholder "Search …" naming what is searched.
- Focus: `ar-search--focus` switches to `color-bg` with a `color-accent` 1px inner edge and `halo-focus`. When it has text, show `xmark.circle.fill` (`ar-search__clear`) to clear it.
- Put it at the top of the content it filters: in a navigation bar, a sidebar header, or above a list.

**Touch.** The field grows to 44px on touch devices, and the clear button has a 44×44 hit area.

**The consumer provides:** the input, live results or a submit handler, and the clear action. **Don't** hide it behind an icon when search is the main way to navigate.
