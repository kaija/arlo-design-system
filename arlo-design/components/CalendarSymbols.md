# CalendarSymbols

The SF Symbols chosen for a calendar app, shown in a day agenda and as the full Calendar asset group.

- **Views:** `square.grid.3x3` (month), `rectangle.split.3x1` (week), `calendar.day.timeline.left` (day), `list.bullet` (agenda), `calendar` (today, in Symbols).
- **Event actions:** `calendar.badge.plus` (new), `calendar.badge.checkmark` (accepted), `calendar.badge.minus` (declined or removed), `calendar.badge.exclamationmark` (conflict), `calendar.badge.clock` (pending or tentative).
- **Event details:** `clock`, `location`, `person.2` (attendees), `person.badge.plus` (invite), `video` and `phone` (call links), `envelope`, `text.pad.header` (notes), `checklist`, `flag`, `pin`.
- **Time and reminders:** `alarm`, `bell.badge` (unread alert), `bell.slash` (muted), `timer`, `hourglass`, `deskclock`, `repeat` (recurring), `clock.arrow.trianglehead.counterclockwise.rotate.90` (history), `globe.badge.clock` (time zone).
- **Occasions:** `birthday.cake`, `gift`, `party.popper`.

**The consumer provides:** the symbol id from the Calendar group, drawn with `.sf`, and an accessible label on any icon-only control. In lists, put the event's kind in an `ar-symbol-tile` (accent for meetings, `--soft` for personal) and details as `symbol-sm` symbols in `color-text-secondary`.

## Markup

Load `tokens.css`, `components.css` and `symbols.css`, put `class="ar-root"` on the body, then:

```html
<div class="wrap"><div>
<p class="cap">In use · day agenda</p>
<div class="ar-navbar" style="border:1px solid var(--color-border);border-bottom:0;border-radius:var(--radius-md) var(--radius-md) 0 0">
  <div class="ar-navbar__lead"><button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="Month view"><span class="sf sf--md" data-symbol="square.grid.3x3"></span></button></div>
  <div class="ar-navbar__title">Tue, 24 Nov</div>
  <div class="ar-navbar__trail"><button class="ar-btn ar-btn--plain ar-btn--icon" aria-label="New event"><span class="sf sf--md" data-symbol="calendar.badge.plus"></span></button></div>
</div>
<div class="ar-list" style="border-radius:0 0 var(--radius-md) var(--radius-md)">
  <div class="ar-list__row"><span class="ar-symbol-tile"><span class="sf" data-symbol="video"></span></span><span class="ar-list__text"><span>Design review</span><span class="meta"><span><span class="sf" data-symbol="person.2"></span>4</span><span><span class="sf" data-symbol="repeat"></span>Weekly</span></span></span><span class="when">10:00</span></div>
  <div class="ar-list__row"><span class="ar-symbol-tile ar-symbol-tile--soft"><span class="sf" data-symbol="birthday.cake"></span></span><span class="ar-list__text"><span>Mei's birthday</span><span class="meta"><span><span class="sf" data-symbol="gift"></span>Dinner booked</span></span></span><span class="when">All day</span></div>
  <div class="ar-list__row"><span class="ar-symbol-tile ar-symbol-tile--soft"><span class="sf" data-symbol="location"></span></span><span class="ar-list__text"><span>Dentist</span><span class="meta"><span><span class="sf" data-symbol="alarm"></span>30 min before</span></span></span><span class="when">15:30</span></div>
</div>
</div><div><p class="cap">Calendar group · 37 SF Symbols</p><div class="grid"><div class="cell"><span class="sf sf--lg" data-symbol="1.calendar"></span><span>1.calendar</span></div><div class="cell"><span class="sf sf--lg" data-symbol="alarm"></span><span>alarm</span></div><div class="cell"><span class="sf sf--lg" data-symbol="bell.badge"></span><span>bell.badge</span></div><div class="cell"><span class="sf sf--lg" data-symbol="bell.slash"></span><span>bell.slash</span></div><div class="cell"><span class="sf sf--lg" data-symbol="birthday.cake"></span><span>birthday.cake</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.and.person"></span><span>calendar.and.person</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.badge.checkmark"></span><span>calendar.badge.checkmark</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.badge.clock"></span><span>calendar.badge.clock</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.badge.exclamationmark"></span><span>calendar.badge.exclamationmark</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.badge.minus"></span><span>calendar.badge.minus</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.badge.plus"></span><span>calendar.badge.plus</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.circle"></span><span>calendar.circle</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.day.timeline.left"></span><span>calendar.day.timeline.left</span></div><div class="cell"><span class="sf sf--lg" data-symbol="calendar.day.timeline.right"></span><span>calendar.day.timeline.right</span></div><div class="cell"><span class="sf sf--lg" data-symbol="checklist"></span><span>checklist</span></div><div class="cell"><span class="sf sf--lg" data-symbol="clock.arrow.trianglehead.counterclockwise.rotate.90"></span><span>clock.arrow.trianglehead.counterclockwise.rotate.90</span></div><div class="cell"><span class="sf sf--lg" data-symbol="clock"></span><span>clock</span></div><div class="cell"><span class="sf sf--lg" data-symbol="deskclock"></span><span>deskclock</span></div><div class="cell"><span class="sf sf--lg" data-symbol="envelope"></span><span>envelope</span></div><div class="cell"><span class="sf sf--lg" data-symbol="flag"></span><span>flag</span></div><div class="cell"><span class="sf sf--lg" data-symbol="gift"></span><span>gift</span></div><div class="cell"><span class="sf sf--lg" data-symbol="globe.badge.clock"></span><span>globe.badge.clock</span></div><div class="cell"><span class="sf sf--lg" data-symbol="hourglass"></span><span>hourglass</span></div><div class="cell"><span class="sf sf--lg" data-symbol="list.bullet"></span><span>list.bullet</span></div><div class="cell"><span class="sf sf--lg" data-symbol="location"></span><span>location</span></div><div class="cell"><span class="sf sf--lg" data-symbol="party.popper"></span><span>party.popper</span></div><div class="cell"><span class="sf sf--lg" data-symbol="person.2"></span><span>person.2</span></div><div class="cell"><span class="sf sf--lg" data-symbol="person.badge.plus"></span><span>person.badge.plus</span></div><div class="cell"><span class="sf sf--lg" data-symbol="phone"></span><span>phone</span></div><div class="cell"><span class="sf sf--lg" data-symbol="pin"></span><span>pin</span></div><div class="cell"><span class="sf sf--lg" data-symbol="rectangle.split.3x1"></span><span>rectangle.split.3x1</span></div><div class="cell"><span class="sf sf--lg" data-symbol="repeat"></span><span>repeat</span></div><div class="cell"><span class="sf sf--lg" data-symbol="square.grid.3x3"></span><span>square.grid.3x3</span></div><div class="cell"><span class="sf sf--lg" data-symbol="text.badge.plus"></span><span>text.badge.plus</span></div><div class="cell"><span class="sf sf--lg" data-symbol="text.pad.header"></span><span>text.pad.header</span></div><div class="cell"><span class="sf sf--lg" data-symbol="timer"></span><span>timer</span></div><div class="cell"><span class="sf sf--lg" data-symbol="video"></span><span>video</span></div></div></div></div>
```

The example's layout helpers (`.row`, `.col`, `.cap` and the like) are not part of `components.css`; they come from this page-level style:

```css
body { margin:0; padding:24px; }
.cap { font:500 12px/16px var(--font-sans); letter-spacing:.5px; color:var(--color-text-secondary); margin:0 0 8px; }
.wrap { display:grid; grid-template-columns:minmax(280px,380px) 1fr; gap:24px; align-items:start; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(92px,1fr)); gap:6px; }
.cell { display:flex; flex-direction:column; align-items:center; gap:6px; padding:10px 4px; border-radius:var(--radius-sm); background:var(--color-bg-secondary); color:var(--color-text-primary); }
.cell span:last-child { font:400 9px/12px var(--font-mono); color:var(--color-text-secondary); text-align:center; word-break:break-all; }
.when { font:500 12px/16px var(--font-sans); color:var(--color-text-secondary); white-space:nowrap; }
.meta { display:flex; gap:12px; color:var(--color-text-secondary); font-size:12px; line-height:16px; --sf-size:14px; }
.meta span { display:inline-flex; align-items:center; gap:4px; }
```

Working page: `../examples/CalendarSymbols.html`
