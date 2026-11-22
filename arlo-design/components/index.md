# Components

Apple-HIG components styled with Arlo tokens. Classes are in `components.css` (prefix `ar-`). Each entry links to its rules and markup.

## Menus and actions

- [Button](Button.md) — A button starts an action; Arlo buttons follow Apple's styles (filled, tinted, gray, plain) with one fixed 12px corner, `radius-button`.
- [Menu](Menu.md) — A menu lists actions or options in a temporary panel opened from a button, a pop-up button or a right-click (Apple: menus, context menus, pull-down buttons).
- [PopUpButton](PopUpButton.md) — A pop-up button shows the current choice from a short, mutually exclusive list and opens a menu to change it (Apple: pop-up buttons).

## Selection and input

- [Checkbox](Checkbox.md) — A checkbox turns an option on or off inside a form that is confirmed later (Apple: checkboxes, macOS).
- [Form](Form.md) — A form lays out fields, choices and actions with one fixed spacing scale, so every settings screen, sheet and dialog groups information the same way.
- [RadioButton](RadioButton.md) — Radio buttons choose exactly one option from a small, visible set (Apple: radio buttons, macOS).
- [SegmentedControl](SegmentedControl.md) — A segmented control switches between 2–5 closely related views or modes (Apple: segmented controls); it replaces Arlo's pill `Tabs`.
- [Slider](Slider.md) — A slider picks a value from a continuous range (Apple: sliders).
- [Stepper](Stepper.md) — A stepper raises or lowers a value by a fixed amount (Apple: steppers).
- [TextField](TextField.md) — A text field takes a short line of text; a multiline field takes paragraphs (Apple: text fields, text views).
- [Toggle](Toggle.md) — A toggle switches one setting on or off with immediate effect (Apple: toggles / switches).

## Navigation and search

- [NavigationBar](NavigationBar.md) — A navigation bar sits at the top of a view: where you are, how to go back, and the view's main actions (Apple: navigation bars and toolbars).
- [PageControl](PageControl.md) — A page control shows how many pages a horizontally paged view has and which one is showing (Apple: page controls), such as onboarding.
- [SearchField](SearchField.md) — A search field filters or finds content (Apple: search fields).
- [Sidebar](Sidebar.md) — A sidebar lists an app's top-level sections and collections on medium and wider windows (Apple: sidebars).
- [TabBar](TabBar.md) — A tab bar switches between the top-level sections of an app on compact windows (Apple: tab bars).

## Layout and organization

- [List](List.md) — Lists present rows of related content: settings, conversations, files (Apple: lists and tables, inset grouped style); it replaces Arlo's `Table` in app UI.

## Presentation

- [Alert](Alert.md) — An alert interrupts to report a problem or confirm a consequential action (Apple: alerts); it replaces Arlo's `Dialog` for short decisions.
- [Popover](Popover.md) — A popover shows transient detail or a few controls anchored to the element that opened it (Apple: popovers); help tags are the hover-only variant, replacing Arlo's `Tooltip`.
- [Sheet](Sheet.md) — A sheet presents a focused task that relates to the current view, such as creating or editing something (Apple: sheets).

## Status

- [Badge](Badge.md) — Badges label status or category in a few words; count badges show unread or pending numbers.
- [ProgressIndicator](ProgressIndicator.md) — Progress indicators show that work is happening: a bar or ring when the amount is known, a spinner when it isn't (Apple: progress indicators).

## Content

- [Symbol](Symbol.md) — Every interface icon is an SF Symbol, drawn by the `.sf` class as a mask tinted by `currentColor`, so a symbol takes the colour of the text around it.
- [CalendarSymbols](CalendarSymbols.md) — The SF Symbols chosen for a calendar app, shown in a day agenda and as the full Calendar asset group.
- [TravelSymbols](TravelSymbols.md) — The SF Symbols chosen for a travel app, shown in a trip itinerary with a tab bar and as the full Travel asset group.
