# Slider

A slider picks a value from a continuous range (Apple: sliders).

- Rail `ar-slider__rail` 4px, `radius-pill`, `color-bg-tertiary`; fill `ar-slider__fill` in `color-accent` from the minimum to the value; thumb 20px white with a soft shadow.
- Optional min/max SF Symbols at either end (`speaker.wave.2`) in `color-text-secondary`, via `ar-slider-row`.
- Show the current value in the label when the exact number matters.

**Touch.** On touch devices the slider is 44px tall with a 28px thumb.

**The consumer provides:** a native `<input type="range">` (style its track and thumb with these values), min/max/step, value and label. **Don't** use a slider for precise numeric entry; pair it with a `Stepper` or `TextField`.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="col" style="max-width:360px">
<div class="ar-slider-row"><span class="sf" data-symbol="speaker.wave.2"></span><div class="ar-slider"><span class="ar-slider__rail"></span><span class="ar-slider__fill" style="width:62%"></span><span class="ar-slider__thumb" style="left:62%"></span></div></div>
<div class="ar-field"><span class="ar-field__label">Temperature · 0.3</span><div class="ar-slider"><span class="ar-slider__rail"></span><span class="ar-slider__fill" style="width:30%"></span><span class="ar-slider__thumb" style="left:30%"></span></div></div>
</div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.row { display:flex; flex-wrap:wrap; align-items:center; gap:12px; }
.col { display:flex; flex-direction:column; gap:16px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); }
```

Working page: `../examples/Slider.html`
