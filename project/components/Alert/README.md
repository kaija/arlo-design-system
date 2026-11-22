# Alert

An alert interrupts to report a problem or confirm a consequential action (Apple: alerts); it replaces Arlo's `Dialog` for short decisions.

- `ar-alert` on an `ar-scrim` (`color-scrim`): 320px, `color-bg`, `radius-lg`, `shadow-xl`, `space300` padding.
- Title (`title-medium-emphasized`) as a short question or statement; message in `body-medium` `color-text-secondary` saying what happens. Optional 44px symbol tile above.
- Actions bottom-right: Cancel as `ar-btn--gray`, the default as `ar-btn--filled`, or `ar-btn--destructive` when it deletes. On compact widths stack them (`ar-alert__actions--stacked`, default on top).
- At most two or three buttons, labelled with verbs ("Delete", not "OK").

**The consumer provides:** title, message, the actions, focus trapping and Escape = Cancel. **Don't** use alerts for information that can wait; use a badge or banner in context.
