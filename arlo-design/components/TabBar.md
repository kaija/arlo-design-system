# TabBar

A tab bar switches between the top-level sections of an app on compact windows (Apple: tab bars).

- `ar-tabbar`: bottom edge, frosted like `NavigationBar`, `color-border` top hairline. 3–5 items, each an SF Symbol at `symbol-lg` over a `label-small` title.
- Selected item: `color-accent`. Others: `color-text-secondary` (`color-text-tertiary` is too light for 11px labels).
- A count badge (`ar-count`) may sit on an item's symbol.
- On medium and wider windows switch to a `Sidebar`.

**Touch.** Each item is at least 44px tall and 64px wide.

**The consumer provides:** the sections (symbol, title, badge), the selected section, and navigation. **Don't** use a tab bar for actions, or hide it inside a section.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div style="max-width:420px;border:1px solid var(--color-border);border-radius:var(--radius-md);overflow:hidden">
<div class="ar-tabbar">
  <span class="ar-tabbar__item ar-tabbar__item--selected"><span class="sf" data-symbol="bubble.left"></span>Chats</span>
  <span class="ar-tabbar__item"><span class="sf" data-symbol="sparkles"></span>Agents<span class="ar-tabbar__badge ar-count">3</span></span>
  <span class="ar-tabbar__item"><span class="sf" data-symbol="document"></span>Files</span>
  <span class="ar-tabbar__item"><span class="sf" data-symbol="gearshape"></span>Settings</span>
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

Working page: `../examples/TabBar.html`
