---
version: alpha
name: Arlo Design System
description: "Arlo AI's design system: one indigo accent on indigo-tinted neutrals, Material 3 spacing and type scale set in Inter, SF Symbols for every icon, Apple HIG components, a fixed 12px button corner, light and dark themes."
colors:
  color-accent: "#5856D6"
  color-accent-hover: "#4745B5"
  color-accent-light: rgba(88,86,214,0.08)
  color-accent-glow: rgba(88,86,214,0.15)
  color-text-primary: "#1a1a2e"
  color-text-secondary: "#64648c"
  color-text-tertiary: "#8e8eaa"
  color-bg: "#ffffff"
  color-bg-secondary: "#f8f8fc"
  color-bg-tertiary: "#f0f0f8"
  color-bg-elevated: "#ffffff"
  color-segment: "#ffffff"
  color-border: rgba(0,0,0,0.06)
  color-border-strong: rgba(0,0,0,0.1)
  color-success: "#1f9d6b"
  color-success-light: rgba(31,157,107,0.08)
  color-warning: "#c07a12"
  color-warning-light: rgba(192,122,18,0.08)
  color-danger: "#d1435b"
  color-danger-light: rgba(209,67,91,0.08)
  color-scrim: rgba(26,26,46,0.4)
  text-on-accent: "#ffffff"
  color-bar: rgba(255,255,255,0.82)
  color-fill-hover: "#e6e6f2"
  surface-page: "{colors.color-bg}"
  surface-section: "{colors.color-bg-secondary}"
  surface-card: "{colors.color-bg}"
  surface-sunken: "{colors.color-bg-tertiary}"
  text-body: "{colors.color-text-primary}"
  text-muted: "{colors.color-text-secondary}"
  text-faint: "{colors.color-text-tertiary}"
  status-info: "{colors.color-accent}"
typography:
  display-large:
    fontFamily: Inter
    fontSize: 57px
    fontWeight: 400
    lineHeight: 64px
    letterSpacing: "-0.25px"
  display-medium:
    fontFamily: Inter
    fontSize: 45px
    fontWeight: 400
    lineHeight: 52px
    letterSpacing: 0px
  display-small:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: 400
    lineHeight: 44px
    letterSpacing: 0px
  headline-large:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: 400
    lineHeight: 40px
    letterSpacing: 0px
  headline-medium:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: 400
    lineHeight: 36px
    letterSpacing: 0px
  headline-small:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 400
    lineHeight: 32px
    letterSpacing: 0px
  title-large:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 400
    lineHeight: 28px
    letterSpacing: 0px
  title-medium:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0.15px
  title-small:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0.1px
  body-large:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0.5px
  body-medium:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0.25px
  body-small:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0.4px
  label-large:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0.1px
  label-medium:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.5px
  label-small:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.5px
  display-large-emphasized:
    fontFamily: Inter
    fontSize: 57px
    fontWeight: 700
    lineHeight: 64px
    letterSpacing: "-1.7px"
  headline-large-emphasized:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
    letterSpacing: "-0.64px"
  title-large-emphasized:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: "-0.22px"
  title-medium-emphasized:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
    letterSpacing: "-0.16px"
  code-pill:
    fontFamily: SF Mono
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0px
rounded:
  none: 0px
  xs: 5px
  mark: 7px
  sm: 8px
  button: 12px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 999px
spacing:
  space0: 0px
  space25: 2px
  space50: 4px
  space75: 6px
  space100: 8px
  space125: 10px
  space200: 16px
  space300: 24px
  space400: 32px
  space500: 40px
  space600: 48px
  space700: 56px
  space800: 64px
  space900: 72px
  margin-compact: 16px
  margin-medium: 24px
  pane-spacer: 24px
  section-padding: 96px
  container-max: 1120px
components:
  button-filled:
    backgroundColor: "{colors.color-accent}"
    textColor: "{colors.text-on-accent}"
    typography: "{typography.label-large}"
    rounded: "{rounded.button}"
    height: 36px
    padding: 0 16px
  button-filled-hover:
    backgroundColor: "{colors.color-accent-hover}"
    shadow: 0 4px 16px rgba(88,86,214,0.3)
  button-tinted:
    backgroundColor: "{colors.color-accent-light}"
    textColor: "{colors.color-accent}"
    rounded: "{rounded.button}"
  button-gray:
    backgroundColor: "{colors.color-bg-tertiary}"
    textColor: "{colors.color-text-primary}"
    rounded: "{rounded.button}"
  button-outline:
    backgroundColor: "{colors.color-bg}"
    textColor: "{colors.color-text-primary}"
    rounded: "{rounded.button}"
    border: "1px solid {colors.color-border-strong}"
  button-plain:
    backgroundColor: transparent
    textColor: "{colors.color-accent}"
    rounded: "{rounded.button}"
  button-destructive:
    backgroundColor: "{colors.color-danger}"
    textColor: "{colors.text-on-accent}"
    rounded: "{rounded.button}"
  segmented-control:
    backgroundColor: "{colors.color-bg-tertiary}"
    textColor: "{colors.color-text-secondary}"
    rounded: "{rounded.button}"
    height: 28px
  segmented-control-selected:
    backgroundColor: "{colors.color-segment}"
    textColor: "{colors.color-text-primary}"
  text-field:
    backgroundColor: "{colors.color-bg}"
    textColor: "{colors.color-text-primary}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.color-border-strong}"
  text-field-focus:
    borderColor: "{colors.color-accent}"
    shadow: 0 0 0 3px rgba(88,86,214,0.08)
  search-field:
    backgroundColor: "{colors.color-bg-tertiary}"
    textColor: "{colors.color-text-primary}"
    rounded: "{rounded.sm}"
    height: 36px
  toggle-on:
    backgroundColor: "{colors.color-accent}"
    rounded: "{rounded.pill}"
    size: 44px x 26px
  toggle-off:
    backgroundColor: "{colors.color-bg-tertiary}"
    rounded: "{rounded.pill}"
  list-group:
    backgroundColor: "{colors.color-bg}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.color-border}"
  list-row:
    textColor: "{colors.color-text-primary}"
    typography: "{typography.body-medium}"
    height: 44px
    padding: 4px 16px
  menu:
    backgroundColor: "{colors.color-bg-elevated}"
    rounded: "{rounded.md}"
    shadow: 0 8px 32px rgba(0,0,0,0.08)
    padding: 4px
  menu-item-active:
    backgroundColor: "{colors.color-accent}"
    textColor: "{colors.text-on-accent}"
    height: 28px
  alert:
    backgroundColor: "{colors.color-bg-elevated}"
    rounded: "{rounded.lg}"
    padding: 24px
    shadow: 0 16px 48px rgba(0,0,0,0.1)
  sheet:
    backgroundColor: "{colors.color-bg-elevated}"
    rounded: 16px 16px 0 0
    shadow: 0 16px 48px rgba(0,0,0,0.1)
  popover:
    backgroundColor: "{colors.color-bg-elevated}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.color-border}"
  navigation-bar:
    backgroundColor: "{colors.color-bar}"
    textColor: "{colors.color-text-primary}"
    typography: "{typography.title-medium-emphasized}"
    height: 44px
  tab-bar-item-selected:
    textColor: "{colors.color-accent}"
    typography: "{typography.label-small}"
  tab-bar-item:
    textColor: "{colors.color-text-secondary}"
    typography: "{typography.label-small}"
  sidebar-item-selected:
    backgroundColor: "{colors.color-accent-light}"
    textColor: "{colors.color-accent}"
    rounded: "{rounded.sm}"
    height: 28px
  badge-accent:
    backgroundColor: "{colors.color-accent-light}"
    textColor: "{colors.color-accent}"
    typography: "{typography.label-medium}"
    rounded: "{rounded.pill}"
    height: 22px
  count-badge:
    backgroundColor: "{colors.color-danger}"
    textColor: "{colors.text-on-accent}"
    typography: "{typography.label-small}"
    rounded: "{rounded.pill}"
  symbol-tile:
    backgroundColor: "{colors.color-accent}"
    textColor: "{colors.text-on-accent}"
    rounded: "{rounded.mark}"
    size: 28px
---
## Overview

Arlo is a family of free, MIT-licensed, local-first AI agent apps: no vendor backend, ever. This system keeps Arlo's identity (a white page, indigo-tinted neutrals and exactly one indigo accent) and builds on three references: **Material 3** for spacing and type, **Apple's SF Symbols** for icons, and **Apple's Human Interface Guidelines** for components. The one deliberate departure from both: buttons use one fixed corner (`radius-button`, 12px) instead of either system's pill or capsule, so larger buttons stay rectangular and use their space.

- **Tone:** plain, confident, principle-driven. Short declaratives: "Your keys, your machine." / "No backend of ours in between. Ever."
- **Voice:** "we" for commitments ("We never see them"), "you/your" for what the user owns. Explanations justify themselves: "…because there is nowhere for them to go."
- **Casing:** sentence case everywhere: headings, buttons, menu items, tabs. No title case, no all-caps.
- **Punctuation:** em-dashes for asides, middle dots as separators ("TUI · CLI"), arrows in links ("Visit site →"), an ellipsis on menu items that open more UI ("Share…").
- **Never:** emoji, exclamation marks, marketing superlatives. Button labels are verbs ("Delete", "Try again"), never "OK".
- **i18n:** English in markup, zh-Hant and ja as overrides. Proper nouns and acronyms (Rust, iOS, MCP, AG-UI) stay untranslated.

## Colors

- Use `color-accent` (#5856D6) as the **only** interactive colour: filled buttons, links, focus, selected rows and tabs, toggles on, slider fills. Hover and pressed deepen to `color-accent-hover`. One filled accent button per view.
- Tint with alpha, never new hues: `color-accent-light` (8%) for tinted buttons, selected sidebar rows, symbol tiles and badges; `color-accent-glow` (15%) only as `ring-accent` on hovered cards.
- Text ramp, all indigo-tinted: `color-text-primary` for titles and body, `color-text-secondary` for supporting text, `color-text-tertiary` for placeholders and meta only (3.18:1 on white: never prose or small labels).
- Grounds: `color-bg` for the page, cards, lists and overlays; `color-bg-secondary` for alternating sections, sidebars and grouped-list backgrounds; `color-bg-tertiary` for tracks and gray control fills.
- Borders are black-alpha hairlines: `color-border` between things, `color-border-strong` around controls. Never a grey hex.
- Status colours (`color-success`, `color-warning`, `color-danger` with their `-light` fills) mean state only. Success and warning are under 4.5:1 as small text, so put the colour on the symbol and keep the words in `color-text-primary`; always pair colour with a word and a symbol.
- No gradients, no imagery or illustration, no second accent.
- **Dark theme.** Every colour token has a dark value; components switch with no extra CSS. Dark grounds stay indigo-tinted (`color-bg` #1b1b29, `color-bg-secondary` #131320 for sidebars and grouped backgrounds). Raised overlays (menus, popovers, alerts, sheets) use `color-bg-elevated`, which is lighter than the page, because in dark, elevation reads as lightness rather than shadow. Following Material 3's dark scheme, `color-accent` and `color-danger` lighten so they pass 4.5:1 as text on dark grounds, and filled buttons carry `text-on-accent`, which turns to dark ink. Never hard-code white on an accent fill. Hairlines become white-alpha. Toggle knobs and slider thumbs stay white in both themes, as on Apple platforms.

### Light and dark values

The YAML above lists light values. Every themed colour, light → dark:

| Token | Light | Dark |
| --- | --- | --- |
| `color-accent` | `#5856D6` | `#8b89f4` |
| `color-accent-hover` | `#4745B5` | `#a9a8f8` |
| `color-accent-light` | `rgba(88,86,214,0.08)` | `rgba(139,137,244,0.16)` |
| `color-accent-glow` | `rgba(88,86,214,0.15)` | `rgba(139,137,244,0.3)` |
| `color-text-primary` | `#1a1a2e` | `#ececf6` |
| `color-text-secondary` | `#64648c` | `#a6a6c4` |
| `color-text-tertiary` | `#8e8eaa` | `#7a7a9e` |
| `color-bg` | `#ffffff` | `#1b1b29` |
| `color-bg-secondary` | `#f8f8fc` | `#131320` |
| `color-bg-tertiary` | `#f0f0f8` | `#33334a` |
| `color-bg-elevated` | `#ffffff` | `#252536` |
| `color-segment` | `#ffffff` | `#55556f` |
| `color-border` | `rgba(0,0,0,0.06)` | `rgba(255,255,255,0.08)` |
| `color-border-strong` | `rgba(0,0,0,0.1)` | `rgba(255,255,255,0.16)` |
| `color-success` | `#1f9d6b` | `#3dbf8a` |
| `color-success-light` | `rgba(31,157,107,0.08)` | `rgba(61,191,138,0.14)` |
| `color-warning` | `#c07a12` | `#e0a33f` |
| `color-warning-light` | `rgba(192,122,18,0.08)` | `rgba(224,163,63,0.14)` |
| `color-danger` | `#d1435b` | `#f27a8e` |
| `color-danger-light` | `rgba(209,67,91,0.08)` | `rgba(242,122,142,0.14)` |
| `color-scrim` | `rgba(26,26,46,0.4)` | `rgba(0,0,0,0.6)` |
| `text-on-accent` | `#ffffff` | `#13131f` |
| `color-bar` | `rgba(255,255,255,0.82)` | `rgba(27,27,41,0.82)` |
| `color-fill-hover` | `#e6e6f2` | `#3e3e57` |

## Typography

Type follows the **Material 3 type scale**: five roles (display, headline, title, body, label) in three sizes each, with M3's sizes, line heights, weights and tracking. The typeface stays Arlo's **Inter** (400–700, Google Fonts) as both M3's brand face (display, headline) and plain face (title, body, label), so the product reads the same as the Arlo sites. On Apple platforms the stack falls back to SF Pro.

- Body copy in `body-large` (16/24) for reading, `body-medium` (14/20) in lists, cards and dialogs, `body-small` for captions.
- Buttons, segments and menu items in `label-large`; badges and field labels in `label-medium`; tab-bar labels in `label-small`.
- Navigation and card titles in `title-medium`; sheet titles in `title-large`; page titles in `headline-medium` (compact) or `headline-large`.
- Arlo's own voice in headings uses the **emphasized** styles (M3's emphasized idea, Arlo's weights): `display-large-emphasized` for one hero per page, `headline-large-emphasized` for section and large navigation titles, `title-large-emphasized` / `title-medium-emphasized` for card, alert and bar titles. Tracking tightens as size grows; it goes positive only in body and label styles.
- Mono (`code-pill`, the SF Mono stack) appears only in code pills and inline code.
- Two weights at most per component. Nothing centred except heroes, alerts on compact, and bar titles.

## Layout

Spacing follows **Material 3**: an 8px scale where `space100` = 8px and names are multipliers (`space200` = 16, `space300` = 24 … `space900` = 72), plus nested units `space25` (2), `space50` (4), `space75` (6) and `space125` (10) inside components.

- **Padding** inside an element, **gaps** between elements, **margins** only outside a container or at the window edge. Set padding and gaps on the parent; avoid margins on children.
- Buttons and list rows: `space200` horizontal padding. Cards, alerts, sheets: `space300`. Gaps between grouped controls: `space100`; between groups: `space300`.
- Window margins: `margin-compact` (16) under 600px wide, `margin-medium` (24) above. Panes (sidebar and content) are separated by `pane-spacer` (24).
- Marketing pages keep Arlo's centred `container-max` (1120) and `section-padding` (96, Arlo's 100 snapped to the scale), `space800` (64) below section headers, 3-up card grids with `space300` gaps.
- Hit targets: at least `control-lg` (44) on touch; desktop controls are `control-sm` (28) or `control-md` (36).

## Elevation & Depth

- Depth comes from tonal layers and hairlines first. Resting cards have no shadow.
- `shadow-sm` for knobs and the selected segment, `shadow-md` + `ring-accent` for hovered interactive cards (lift `translateY(-2px)`), `shadow-lg` for menus and popovers, `shadow-xl` for alerts and sheets, `shadow-accent` for the hovered filled button only.
- Keyboard focus on every control is `shadow-focus`: a 2px white gap and a solid 2px `color-accent` ring (5.65:1). Text fields focus with a `color-accent` border plus Arlo's soft `halo-focus`.
- Blur and translucency appear only on bars: navigation bar, tab bar and the site nav (`rgba(255,255,255,.82)` + `saturate(180%) blur(20px)`).
- Motion: 150ms ease for colour and opacity, 250ms ease for transforms and toggles. No bounces, no springs, no scale on press.

## Shapes

- Buttons, segmented controls, steppers and pop-up buttons: `radius-button` at every size. The corner is a fixed 12px, **not** Material's full pill or Apple's capsule, which grow with height. The Button card compares it with the earlier 6px and with a pill.
- Everything else keeps Arlo's scale: `radius-xs` checkboxes, `radius-mark` brand marks and 28px symbol tiles, `radius-sm` text and search fields, sidebar rows and 44px tiles, `radius-md` menus, popovers and list groups, `radius-lg` cards, alerts and sheets, `radius-xl` large panels.
- `radius-pill` is for shapes that are capsules by nature: toggles, badges, progress and slider tracks, page-control dots.
- Don't mix radius steps inside one group: a 16px card holds 12px (`radius-button`) buttons and pill badges, not 8px or 6px buttons.

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
- **Selection and input:** Toggle, SegmentedControl, TextField, Checkbox, RadioButton, Slider, Stepper
- **Navigation and search:** NavigationBar, TabBar, Sidebar, SearchField, PageControl
- **Layout and organization:** List
- **Presentation:** Alert, Sheet, Popover
- **Status:** ProgressIndicator, Badge
- **Content:** Symbol, CalendarSymbols, TravelSymbols

From the original Arlo kit: `Tabs` became SegmentedControl and TabBar, `Dialog` became Alert and Sheet, `Tooltip` became Popover's help tag, `Table` became List, `Switch` became Toggle, `Select` became PopUpButton, `Spinner` and `Progress` became ProgressIndicator. Marketing-site pieces (project cards, hero badge, stack diagram, site nav, footer) are not part of this app-UI kit.

Each component's rules and markup: `components/<Name>.md`. Working pages: `examples/<Name>.html`.

## Do's and Don'ts

- **Do** keep one filled accent button per view, and state actions as verbs in sentence case.
- **Do** reach for a hairline and a tonal shift before a shadow.
- **Do** pair every status colour with a word and a symbol.
- **Don't** add a second accent, a gradient, imagery, or emoji.
- **Don't** round buttons beyond `radius-button`, or use a pill for anything you press.
- **Don't** use `color-text-tertiary` for anything people must read.
