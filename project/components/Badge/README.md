# Badge

Badges label status or category in a few words; count badges show unread or pending numbers.

- `ar-badge`: 22px, `radius-pill` (badges stay capsules: they are labels, not buttons), `label-medium` text, `space125` padding.
- `ar-badge--accent` (category), `--neutral` (meta), `--success` / `--warning` / `--danger` (state only). Success and warning text is `color-text-primary` with the status colour on the symbol, because those colours are below 4.5:1 as small text. Always pair a status colour with a word and a symbol.
- `ar-badge--mono`: Arlo's code pill (`code-pill`, mono stack).
- `ar-count`: `color-danger` capsule with white `label-small` numbers, on tab bar items, sidebar rows and symbols.

**The consumer provides:** the text (sentence case, 1–3 words), the tone, and an optional leading symbol. **Don't** make badges clickable or use status colours for decoration.
