# CalendarSymbols

The SF Symbols chosen for a calendar app, shown in a day agenda and as the full Calendar asset group.

- **Views:** `square.grid.3x3` (month), `rectangle.split.3x1` (week), `calendar.day.timeline.left` (day), `list.bullet` (agenda), `calendar` (today, in Symbols).
- **Event actions:** `calendar.badge.plus` (new), `calendar.badge.checkmark` (accepted), `calendar.badge.minus` (declined or removed), `calendar.badge.exclamationmark` (conflict), `calendar.badge.clock` (pending or tentative).
- **Event details:** `clock`, `location`, `person.2` (attendees), `person.badge.plus` (invite), `video` and `phone` (call links), `envelope`, `text.pad.header` (notes), `checklist`, `flag`, `pin`.
- **Time and reminders:** `alarm`, `bell.badge` (unread alert), `bell.slash` (muted), `timer`, `hourglass`, `deskclock`, `repeat` (recurring), `clock.arrow.trianglehead.counterclockwise.rotate.90` (history), `globe.badge.clock` (time zone).
- **Occasions:** `birthday.cake`, `gift`, `party.popper`.

**The consumer provides:** the symbol id from the Calendar group, drawn with `.sf`, and an accessible label on any icon-only control. In lists, put the event's kind in an `ar-symbol-tile` (accent for meetings, `--soft` for personal) and details as `symbol-sm` symbols in `color-text-secondary`.
