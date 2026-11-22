# TravelSymbols

The SF Symbols chosen for a travel app, shown in a trip itinerary with a tab bar and as the full Travel asset group.

- **Flights:** `airplane`, `airplane.departure`, `airplane.arrival`, `airplane.landed`, `airplaneseat`, `clock.badge.airplane` (flight time).
- **Ground and water:** `car`, `bus`, `train.side.front.car`, `tram`, `ferry`, `car.ferry`, `sailboat`, `bicycle`, `figure.walk`, `fuelpump`.
- **Stay and eat:** `bed.double` (hotel), `building.2` (city stay), `house.lodge`, `tent`, `fork.knife`, `cup.and.saucer`, `wineglass`.
- **Plan and navigate:** `map`, `mappin`, `mappin.and.ellipse`, `location.north`, `signpost.right`, `globe.americas` / `globe.europe.africa` / `globe.asia.australia` (pick the traveller's region), `list.clipboard` (itinerary).
- **Bags and documents:** `suitcase`, `suitcase.rolling`, `figure.walk.suitcase.rolling`, `person.text.rectangle` (passport or ID), `ticket`, `wallet.pass`, `qrcode`.
- **Money:** `creditcard`, `banknote`, `dollarsign.arrow.trianglehead.counterclockwise.rotate.90` (exchange).
- **On the ground:** `translate`, `wifi`, `powerplug`, `binoculars`, `mountain.2`, `beach.umbrella`.
- **Weather:** `sun.max`, `cloud.sun`, `cloud.rain`, `snowflake`, `umbrella`, `thermometer.medium`.

**The consumer provides:** the symbol id from the Travel group, drawn with `.sf`, and labels on icon-only controls. Use one transport symbol per itinerary row in an `ar-symbol-tile`; keep weather symbols monochrome in `color-text-secondary` unless they report a warning.
