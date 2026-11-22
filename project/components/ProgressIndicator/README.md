# ProgressIndicator

Progress indicators show that work is happening: a bar or ring when the amount is known, a spinner when it isn't (Apple: progress indicators).

- Bar `ar-progress`: 4px, `radius-pill`, `color-bg-tertiary` track, `color-accent` fill (`color-success` when complete via `ar-progress--success`). Label above with the task and percent.
- Spinner `ar-spinner` 20px (inline) or `ar-spinner--lg` 32px (page), `color-accent` arc on a `color-bg-tertiary` ring, 800ms linear.
- Ring `ar-ring` (20px, set `--p`) for compact determinate progress, such as a download in a list row.

**The consumer provides:** the value (or none for indeterminate) and an accessible label (`role="progressbar"`, `aria-valuenow`). **Don't** show a spinner for under ~1 second or stack several on one screen.
