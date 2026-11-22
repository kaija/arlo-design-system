# Alert

An alert interrupts to report a problem or confirm a consequential action (Apple: alerts); it replaces Arlo's `Dialog` for short decisions.

- `ar-alert` on an `ar-scrim` (`color-scrim`): 320px, `color-bg`, `radius-lg`, `shadow-xl`, `space300` padding.
- Title (`title-medium-emphasized`) as a short question or statement; message in `body-medium` `color-text-secondary` saying what happens. Optional 44px symbol tile above.
- Actions bottom-right: Cancel as `ar-btn--gray`, the default as `ar-btn--filled`, or `ar-btn--destructive` when it deletes. On compact widths stack them (`ar-alert__actions--stacked`, default on top).
- At most two or three buttons, labelled with verbs ("Delete", not "OK").

**The consumer provides:** title, message, the actions, focus trapping and Escape = Cancel. **Don't** use alerts for information that can wait; use a badge or banner in context.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="ar-scrim" style="border-radius:var(--radius-md);gap:24px;flex-wrap:wrap">
<div class="ar-alert">
  <div class="ar-alert__icon"><span class="ar-symbol-tile ar-symbol-tile--lg" style="background:var(--color-danger-light);color:var(--color-danger)"><span class="sf" data-symbol="trash"></span></span></div>
  <p class="ar-alert__title">Delete this chat?</p>
  <p class="ar-alert__msg">It's removed from this Mac. There's no copy anywhere else, so this can't be undone.</p>
  <div class="ar-alert__actions"><button class="ar-btn ar-btn--gray">Cancel</button><button class="ar-btn ar-btn--destructive">Delete</button></div>
</div>
<div class="ar-alert" style="width:280px">
  <p class="ar-alert__title">Provider unreachable</p>
  <p class="ar-alert__msg">Check your connection or endpoint, then try again.</p>
  <div class="ar-alert__actions ar-alert__actions--stacked"><button class="ar-btn ar-btn--gray">Not now</button><button class="ar-btn ar-btn--filled">Try again</button></div>
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

Working page: `../examples/Alert.html`
