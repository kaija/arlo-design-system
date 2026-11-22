Arlo is a family of free, MIT-licensed, local-first AI agent apps: no vendor backend, ever. This system keeps Arlo's identity (a white page, indigo-tinted neutrals and exactly one indigo accent) and builds on three references: **Material 3** for spacing and type, **Apple's SF Symbols** for icons, and **Apple's Human Interface Guidelines** for components. The one deliberate departure from both: buttons use one fixed corner (`radius-button`, 12px) instead of either system's pill or capsule, so larger buttons stay rectangular and use their space.

## Content fundamentals

- **Tone:** plain, confident, principle-driven. Short declaratives: "Your keys, your machine." / "No backend of ours in between. Ever."
- **Voice:** "we" for commitments ("We never see them"), "you/your" for what the user owns. Explanations justify themselves: "…because there is nowhere for them to go."
- **Casing:** sentence case everywhere: headings, buttons, menu items, tabs. No title case, no all-caps.
- **Punctuation:** em-dashes for asides, middle dots as separators ("TUI · CLI"), arrows in links ("Visit site →"), an ellipsis on menu items that open more UI ("Share…").
- **Never:** emoji, exclamation marks, marketing superlatives. Button labels are verbs ("Delete", "Try again"), never "OK".
- **i18n:** English in markup, zh-Hant and ja as overrides. Proper nouns and acronyms (Rust, iOS, MCP, AG-UI) stay untranslated.

## Color

- Use `color-accent` (#5856D6) as the **only** interactive colour: filled buttons, links, focus, selected rows and tabs, toggles on, slider fills. Hover and pressed deepen to `color-accent-hover`. One filled accent button per view.
- Tint with alpha, never new hues: `color-accent-light` (8%) for tinted buttons, selected sidebar rows, symbol tiles and badges; `color-accent-glow` (15%) only as `ring-accent` on hovered cards.
- Text ramp, all indigo-tinted: `color-text-primary` for titles and body, `color-text-secondary` for supporting text, `color-text-tertiary` for placeholders and meta only (3.18:1 on white: never prose or small labels).
- Grounds: `color-bg` for the page, cards, lists and overlays; `color-bg-secondary` for alternating sections, sidebars and grouped-list backgrounds; `color-bg-tertiary` for tracks and gray control fills.
- Borders are black-alpha hairlines: `color-border` between things, `color-border-strong` around controls. Never a grey hex.
- Status colours are Apple's system green, orange and red (`color-success`, `color-warning`, `color-danger`, each with a `-light` fill), using Apple's higher-contrast variants in light and the standard ones in dark. They mean state only, never decoration or emphasis. Warning and danger read as small text in both themes; success is 4.40:1 on white, so small success words stay in `color-text-primary` beside a green symbol. In light, orange and red are close in hue: always pair warning with `exclamationmark.triangle` and errors with `exclamationmark.circle` or `xmark.circle.fill`, and always add a word, so no state relies on colour alone.
- No gradients, no imagery or illustration, no second accent.
- **Dark theme.** Every colour token has a dark value; components switch with no extra CSS. Dark grounds stay indigo-tinted (`color-bg` #1b1b29, `color-bg-secondary` #131320 for sidebars and grouped backgrounds). Raised overlays (menus, popovers, alerts, sheets) use `color-bg-elevated`, which is lighter than the page, because in dark, elevation reads as lightness rather than shadow. Following Material 3's dark scheme, `color-accent` and `color-danger` lighten so they pass 4.5:1 as text on dark grounds, and filled buttons carry `text-on-accent`, which turns to dark ink. Never hard-code white on an accent fill. Hairlines become white-alpha. Toggle knobs and slider thumbs stay white in both themes, as on Apple platforms.

## Typography

Type follows the **Material 3 type scale**: five roles (display, headline, title, body, label) in three sizes each, with M3's sizes, line heights, weights and tracking. The typeface stays Arlo's **Inter** (400–700, Google Fonts) as both M3's brand face (display, headline) and plain face (title, body, label), so the product reads the same as the Arlo sites. On Apple platforms the stack falls back to SF Pro.

- Body copy in `body-large` (16/24) for reading, `body-medium` (14/20) in lists, cards and dialogs, `body-small` for captions.
- Buttons, segments and menu items in `label-large`; badges and field labels in `label-medium`; tab-bar labels in `label-small`.
- Navigation and card titles in `title-medium`; sheet titles in `title-large`; page titles in `headline-medium` (compact) or `headline-large`.
- Arlo's own voice in headings uses the **emphasized** styles (M3's emphasized idea, Arlo's weights): `display-large-emphasized` for one hero per page, `headline-large-emphasized` for section and large navigation titles, `title-large-emphasized` / `title-medium-emphasized` for card, alert and bar titles. Tracking tightens as size grows; it goes positive only in body and label styles.
- Mono (`code-pill`, the SF Mono stack) appears only in code pills and inline code.
- Two weights at most per component. Nothing centred except heroes, alerts on compact, and bar titles.

## Spacing and layout

Spacing follows **Material 3**: an 8px scale where `space100` = 8px and names are multipliers (`space200` = 16, `space300` = 24 … `space900` = 72), plus nested units `space25` (2), `space50` (4), `space75` (6) and `space125` (10) inside components.

- **Padding** inside an element, **gaps** between elements, **margins** only outside a container or at the window edge. Set padding and gaps on the parent; avoid margins on children.
- Buttons and list rows: `space200` horizontal padding. Cards, alerts, sheets: `space300`. Gaps between grouped controls: `space100`; between groups: `space300`.
- Window margins: `margin-compact` (16) under 600px wide, `margin-medium` (24) above. Panes (sidebar and content) are separated by `pane-spacer` (24).
- Marketing pages keep Arlo's centred `container-max` (1120) and `section-padding` (96, Arlo's 100 snapped to the scale), `space800` (64) below section headers, 3-up card grids with `space300` gaps.
- **Touch targets.** Everything tappable has at least a 44×44px hit area (`control-lg`, Apple's minimum). Menu items, sidebar rows, list rows, tab-bar items and navigation-bar actions are 44px tall by default. Controls drawn smaller (36px buttons, 28px segments and steppers, checkboxes, toggles) carry an invisible 44×44 hit area, and on touch devices (`pointer: coarse`) they grow: buttons and fields to 44, small buttons, segments and steppers to 36, checkbox and radio rows to 44. Compact variants (`ar-menu--compact`, `ar-sidebar--compact`) are for pointer-only UI and turn back to 44px on touch. Put `ar-touch` on a container to force touch sizes anywhere.
- **Forms** use one rhythm, by proximity: help text 4px below its field, labels 8px above, 16px under a section title and between side-by-side fields, 24px between fields, 32px between sections and before the action row (see Form).
- **Space between targets.** Keep at least `space100` (8px) between neighbouring tappable controls, so their 44px hit areas don't overlap and a finger can't land on the wrong one; stack tappable rows flush only when each row is itself 44px tall.

## Shape

- Buttons, segmented controls, steppers and pop-up buttons: `radius-button` at every size. The corner is a fixed 12px, **not** Material's full pill or Apple's capsule, which grow with height. The Button card compares it with the earlier 6px and with a pill.
- Everything else keeps Arlo's scale: `radius-xs` checkboxes, `radius-mark` brand marks and 28px symbol tiles, `radius-sm` text and search fields, sidebar rows and 44px tiles, `radius-md` menus, popovers and list groups, `radius-lg` cards, alerts and sheets, `radius-xl` large panels.
- `radius-pill` is for shapes that are capsules by nature: toggles, badges, progress and slider tracks, page-control dots.
- Don't mix radius steps inside one group: a 16px card holds 12px (`radius-button`) buttons and pill badges, not 8px or 6px buttons.

## Elevation and motion

- Depth comes from tonal layers and hairlines first. Resting cards have no shadow.
- `shadow-sm` for knobs and the selected segment, `shadow-md` + `ring-accent` for hovered interactive cards (lift `translateY(-2px)`), `shadow-lg` for menus and popovers, `shadow-xl` for alerts and sheets, `shadow-accent` for the hovered filled button only.
- Keyboard focus on every control is `shadow-focus`: a 2px white gap and a solid 2px `color-accent` ring (5.65:1). Text fields focus with a `color-accent` border plus Arlo's soft `halo-focus`.
- Blur and translucency appear only on bars: navigation bar, tab bar and the site nav (`rgba(255,255,255,.82)` + `saturate(180%) blur(20px)`).
- Motion: 150ms ease for colour and opacity, 250ms ease for transforms and toggles. No bounces, no springs, no scale on press.

## Iconography

- **All interface icons are SF Symbols**, exported as vector SVG from the SF Symbols app (Regular weight, 24pt) into the Symbols asset group, and drawn with the `.sf` class (see the Symbol component) so they take `currentColor`. They replace Arlo's Feather-style set one for one: `submit` → `arrow.up.circle.fill`, `stop` → `stop.fill`, `voice` → `microphone`, `waveform` → `waveform`, `volume` → `speaker.wave.2`, `new-chat` → `square.and.pencil`, `regenerate` → `arrow.trianglehead.clockwise`, `attach` → `paperclip`, `settings` → `gearshape`, `more` → `ellipsis` / `ellipsis.circle`.
- Use the names the SF Symbols app shows today (SF Symbols 27): `document`, `document.on.document`, `microphone`, not their older aliases `doc`, `doc.on.doc`, `mic`. Where the app offers a `trianglehead` arrow, use it (`arrow.trianglehead.clockwise`).
- Follow Apple's guidance for interface icons: simple, recognizable shapes; one consistent weight that matches the adjacent text; outline by default and the `.fill` variant for selected or solid actions; no text inside icons; every icon-only control gets an accessible label.
- **Calendar and travel apps** draw from two more groups: Calendar (37 symbols: views, event states, reminders, attendees) and Travel (54: flights, transport, stays, maps, documents, money, weather). The CalendarSymbols and TravelSymbols cards say which symbol means what; use those meanings everywhere, such as `calendar.badge.plus` for a new event and `airplane.departure` for an outbound flight.
- Badge symbols keep Apple's cut-out gap between glyph and badge (exported as SVG masks); never draw a separate badge on top of a symbol.
- Sizes: `symbol-sm` (16) beside small text and in small buttons, `symbol-md` (20) in buttons, sidebars and lists, `symbol-lg` (24) in tab and navigation bars. Feature tiles put a symbol in `ar-symbol-tile` (28px, `radius-mark`) or `ar-symbol-tile--lg` (44px, `radius-sm`).
- Keep the speech symbols distinct: `microphone` = input, `waveform` = the model is speaking, `speaker.wave.2` = playback.
- Swap `arrow.up.circle.fill` for `stop.fill` in the same button while a response streams, with no layout shift.
- **Licence:** SF Symbols are Apple's and are licensed for designing and building apps on Apple platforms. Don't use them in logos, and don't ship them in Arlo's web or non-Apple builds without checking the licence.
- **Brand marks** (Logos group) stay Arlo's own: a white glyph in the `color-accent` 28px square with a 7px (`radius-mark`) corner. Never redraw them with symbols.

## Components

Components follow Apple's HIG names and behaviour, styled with Arlo's tokens. Classes live in `components/bundle.css` (prefix `ar-`); each component's card has its guidelines.

- **Menus and actions:** Button, PopUpButton, Menu
- **Selection and input:** Form, Toggle, SegmentedControl, TextField, Checkbox, RadioButton, Slider, Stepper
- **Navigation and search:** NavigationBar, TabBar, Sidebar, SearchField, PageControl
- **Layout and organization:** List
- **Presentation:** Alert, Sheet, Popover
- **Status:** ProgressIndicator, Badge
- **Content:** Symbol, CalendarSymbols, TravelSymbols

From the original Arlo kit: `Tabs` became SegmentedControl and TabBar, `Dialog` became Alert and Sheet, `Tooltip` became Popover's help tag, `Table` became List, `Switch` became Toggle, `Select` became PopUpButton, `Spinner` and `Progress` became ProgressIndicator. Marketing-site pieces (project cards, hero badge, stack diagram, site nav, footer) are not part of this app-UI kit.

## Do and don't

- **Do** keep one filled accent button per view, and state actions as verbs in sentence case.
- **Do** reach for a hairline and a tonal shift before a shadow.
- **Do** pair every status colour with a word and a symbol.
- **Don't** add a second accent, a gradient, imagery, or emoji.
- **Don't** round buttons beyond `radius-button`, or use a pill for anything you press.
- **Don't** use `color-text-tertiary` for anything people must read.
