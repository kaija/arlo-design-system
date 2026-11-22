# Slider

A slider picks a value from a continuous range (Apple: sliders).

- Rail `ar-slider__rail` 4px, `radius-pill`, `color-bg-tertiary`; fill `ar-slider__fill` in `color-accent` from the minimum to the value; thumb 20px white with a soft shadow.
- Optional min/max SF Symbols at either end (`speaker.wave.2`) in `color-text-secondary`, via `ar-slider-row`.
- Show the current value in the label when the exact number matters.

**Touch.** On touch devices the slider is 44px tall with a 28px thumb.

**The consumer provides:** a native `<input type="range">` (style its track and thumb with these values), min/max/step, value and label. **Don't** use a slider for precise numeric entry; pair it with a `Stepper` or `TextField`.
