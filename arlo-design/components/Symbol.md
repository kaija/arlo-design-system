# Symbol

Every interface icon is an SF Symbol, drawn by the `.sf` class as a mask tinted by `currentColor`, so a symbol takes the colour of the text around it.

- Markup: `<span class="sf" style="--sf:url(/_blob/<id>)"></span>`; the ids are in the Symbols asset group. Size with `sf--sm` (16), `sf--md` (20), `sf--lg` (24) or `--sf-size`; components set the right size themselves.
- Match the symbol's weight and size to the adjacent text: `symbol-sm` beside `body-medium`/`label-large`, `symbol-md` beside `body-large`/`title-medium`, `symbol-lg` in tab bars and navigation bars.
- Colour: `color-text-secondary` at rest in toolbars and composers, `color-accent` when active or in sidebars, status colours only for state. On a filled tile (`ar-symbol-tile`) the symbol is `text-on-accent`.
- Use the outline variant by default and the `.fill` variant for selected states and small solid actions (`paperplane.fill`, `stop.fill`, `arrow.up.circle.fill`).

**The consumer provides:** the symbol name and an accessible label on the control (symbols themselves are decorative). **Don't** redraw, recolour parts of, or stretch a symbol, or use one as a logo.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col">
<div class="cap">Sizes beside text · symbol-sm 16 · symbol-md 20 · symbol-lg 24</div>
<div class="row" style="gap:24px;font:400 14px/20px var(--font-sans)">
  <span class="row" style="gap:6px"><span class="sf sf--sm" data-symbol="bubble.left"></span>Chats</span>
  <span class="row" style="gap:8px;font-size:16px"><span class="sf sf--md" data-symbol="bubble.left"></span>Chats</span>
  <span class="row" style="gap:8px;font-size:22px;line-height:28px"><span class="sf sf--lg" data-symbol="bubble.left"></span>Chats</span>
  <span class="ar-symbol-tile"><span class="sf" data-symbol="bolt.fill"></span></span><span class="ar-symbol-tile ar-symbol-tile--soft ar-symbol-tile--lg"><span class="sf" data-symbol="sparkles"></span></span>
  <span style="color:var(--color-accent)" class="row"><span class="sf sf--lg" data-symbol="checkmark.circle.fill"></span></span><span style="color:var(--color-danger)" class="row"><span class="sf sf--lg" data-symbol="exclamationmark.triangle"></span></span>
</div>
<div class="cap">Arlo action set, now SF Symbols</div>
<div class="grid"><div class="cell"><span class="sf sf--lg" data-symbol="bubble.left"></span><span>bubble.left</span></div><div class="cell"><span class="sf sf--lg" data-symbol="square.and.pencil"></span><span>square.and.pencil</span></div><div class="cell"><span class="sf sf--lg" data-symbol="magnifyingglass"></span><span>magnifyingglass</span></div><div class="cell"><span class="sf sf--lg" data-symbol="gearshape"></span><span>gearshape</span></div><div class="cell"><span class="sf sf--lg" data-symbol="paperclip"></span><span>paperclip</span></div><div class="cell"><span class="sf sf--lg" data-symbol="photo"></span><span>photo</span></div><div class="cell"><span class="sf sf--lg" data-symbol="camera"></span><span>camera</span></div><div class="cell"><span class="sf sf--lg" data-symbol="microphone"></span><span>microphone</span></div><div class="cell"><span class="sf sf--lg" data-symbol="waveform"></span><span>waveform</span></div><div class="cell"><span class="sf sf--lg" data-symbol="speaker.wave.2"></span><span>speaker.wave.2</span></div><div class="cell"><span class="sf sf--lg" data-symbol="document"></span><span>document</span></div><div class="cell"><span class="sf sf--lg" data-symbol="chevron.left.forwardslash.chevron.right"></span><span>chevron.left.forwardslash.chevron.right</span></div><div class="cell"><span class="sf sf--lg" data-symbol="document.on.document"></span><span>document.on.document</span></div><div class="cell"><span class="sf sf--lg" data-symbol="arrow.trianglehead.clockwise"></span><span>arrow.trianglehead.clockwise</span></div><div class="cell"><span class="sf sf--lg" data-symbol="pencil"></span><span>pencil</span></div><div class="cell"><span class="sf sf--lg" data-symbol="hand.thumbsup"></span><span>hand.thumbsup</span></div><div class="cell"><span class="sf sf--lg" data-symbol="hand.thumbsdown"></span><span>hand.thumbsdown</span></div><div class="cell"><span class="sf sf--lg" data-symbol="square.and.arrow.up"></span><span>square.and.arrow.up</span></div><div class="cell"><span class="sf sf--lg" data-symbol="square.and.arrow.down"></span><span>square.and.arrow.down</span></div><div class="cell"><span class="sf sf--lg" data-symbol="trash"></span><span>trash</span></div><div class="cell"><span class="sf sf--lg" data-symbol="sparkles"></span><span>sparkles</span></div><div class="cell"><span class="sf sf--lg" data-symbol="bolt.fill"></span><span>bolt.fill</span></div><div class="cell"><span class="sf sf--lg" data-symbol="globe"></span><span>globe</span></div><div class="cell"><span class="sf sf--lg" data-symbol="lock"></span><span>lock</span></div></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(112px,1fr)); gap:8px; }
.cell { display:flex; flex-direction:column; align-items:center; gap:8px; padding:12px 4px; border-radius:var(--radius-sm); background:var(--color-bg-secondary); color:var(--color-text-primary); }
.cell span:last-child { font:400 10px/14px var(--font-mono); color:var(--color-text-secondary); text-align:center; word-break:break-all; }
```

Working page: `../examples/Symbol.html`
