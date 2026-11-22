# NavigationBar

A navigation bar sits at the top of a view: where you are, how to go back, and the view's main actions (Apple: navigation bars and toolbars).

- `ar-navbar`: 44px (`control-lg`), full width, `radius-none`, Arlo's frosted glass (`rgba(255,255,255,.82)` + `saturate(180%) blur(20px)`) with a `color-border` bottom hairline. This is the one place blur is allowed.
- Leading: `ar-navbar__back` (`chevron.left` + the previous title in `color-accent`) or a plain icon button. Centre: `ar-navbar__title` (`title-medium-emphasized`). Trailing: up to three `ar-btn--plain ar-btn--icon` buttons with `symbol-md` symbols.
- Top-level views use `ar-navbar--large` with `ar-navbar__large-title` (`headline-large-emphasized`).
- Marketing pages keep Arlo's 64px (`nav-height`) site nav.

**The consumer provides:** the title, back target, actions with `aria-label`s, and scroll-linked collapse of the large title. **Don't** put more than three trailing actions; move the rest into a `Menu` behind `ellipsis.circle`.
