# Sheet

A sheet presents a focused task that relates to the current view, such as creating or editing something (Apple: sheets).

- `ar-sheet`: `color-bg`, top corners `radius-lg`, `shadow-xl`, rising from the bottom on compact windows (centred, all corners rounded, on wider ones), over `color-scrim`.
- A grabber (`ar-sheet__grabber`, 36×5, `color-border-strong`) when it can be resized or swiped away.
- Bar `ar-sheet__bar`: Cancel (`ar-btn--plain`) leading, title (`title-medium-emphasized`) centred, confirm (`ar-btn--plain`, semibold) trailing.
- Body with `space200` side padding; forms use `TextField`.

**The consumer provides:** the content, the confirm/cancel handlers, and a check for unsaved changes on dismiss. **Don't** stack sheets on sheets or use one for a yes/no question (use `Alert`).
