# NavigationBar

A navigation bar sits at the top of a view: where you are, how to go back, and the view's main actions (Apple: navigation bars and toolbars).

- `ar-navbar`: 44px (`control-lg`), full width, `radius-none`, Arlo's frosted glass (`rgba(255,255,255,.82)` + `saturate(180%) blur(20px)`) with a `color-border` bottom hairline. This is the one place blur is allowed.
- Leading: `ar-navbar__back` (`chevron.left` + the previous title in `color-accent`) or a plain icon button. Centre: `ar-navbar__title` (`title-medium-emphasized`). Trailing: up to three `ar-btn--plain ar-btn--icon` buttons with `symbol-md` symbols.
- Top-level views use `ar-navbar--large` with `ar-navbar__large-title` (`headline-large-emphasized`).
- Marketing pages keep Arlo's 64px (`nav-height`) site nav.

**The consumer provides:** the title, back target, actions with `aria-label`s, and scroll-linked collapse of the large title. **Don't** put more than three trailing actions; move the rest into a `Menu` behind `ellipsis.circle`.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="max-width:480px;border:1px solid var(--color-border);border-radius:var(--radius-md);overflow:hidden;gap:0">
<div class="ar-navbar">
  <div class="ar-navbar__lead"><span class="ar-navbar__back"><span class="sf" data-symbol="chevron.left"></span>Chats</span></div>
  <div class="ar-navbar__title">Refactor event stream</div>
  <div class="ar-navbar__trail"><button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="Share"><span class="sf sf--md" data-symbol="square.and.arrow.up"></span></button><button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="More"><span class="sf sf--md" data-symbol="ellipsis.circle"></span></button></div>
</div>
<div style="height:24px"></div>
<div class="ar-navbar ar-navbar--large" style="border-top:1px solid var(--color-border)">
  <div class="ar-navbar__lead"><button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="Sidebar"><span class="sf sf--md" data-symbol="sidebar.left"></span></button></div>
  <div></div>
  <div class="ar-navbar__trail"><button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="New chat"><span class="sf sf--md" data-symbol="square.and.pencil"></span></button></div>
  <div class="ar-navbar__large-title">Chats</div>
</div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/NavigationBar.html`
