"""Status color lab: site/foundations/status-lab.html — try candidate status palettes in real UI, light and dark."""
import html, json, os
import build as B
import site_gen as S

PALETTES = [
    ("arlo", "Arlo original", "The colours the system started with, from the Arlo sites. Low-chroma so they sit quietly beside the indigo; green and orange are under 4.5:1 as small text on white, so the system keeps words in ink and puts the colour on symbols.",
     {"light": ["#1f9d6b", "#c07a12", "#d1435b"], "dark": ["#3dbf8a", "#e0a33f", "#f27a8e"]}),
    ("aa", "Arlo AA", "The same three hues, darkened just enough that each reads as small text on white (4.6:1). Dark theme unchanged. The least visible change.",
     {"light": ["#1a855a", "#a3670f", "#ce425a"], "dark": ["#3dbf8a", "#e0a33f", "#f27a8e"]}),
    ("apple", "Apple system · in use", "The current tokens. iOS system green, orange and red, using Apple's higher-contrast light variants and the standard dark variants. Brighter and more saturated: reads as native on Apple platforms.",
     {"light": ["#248A3D", "#C93400", "#D70015"], "dark": ["#30D158", "#FF9F0A", "#FF453A"]}),
    ("m3", "Material 3 tonal", "Material 3-style tones: tone 40 in light, tone 80 in dark. Deep and calm in light, pastel in dark; every pair clears 6:1.",
     {"light": ["#1E6B35", "#8A5100", "#BA1A1A"], "dark": ["#8FD8A0", "#FFB869", "#FFB4AB"]}),
]
NAMES = ["success", "warning", "danger"]

def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def lum(h):
    c = [x / 255 for x in hexrgb(h)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def cr(a, b):
    a, b = lum(a), lum(b); return (max(a, b) + 0.05) / (min(a, b) + 0.05)
def rgba(h, a):
    r, g, b = hexrgb(h); return f"rgba({r},{g},{b},{a})"

def palette_css():
    out = []
    for key, _, _, p in PALETTES:
        for theme, alpha in (("light", 0.08), ("dark", 0.14)):
            decl = "".join(f"--color-{n}:{p[theme][i]};--color-{n}-light:{rgba(p[theme][i], alpha)};" for i, n in enumerate(NAMES))
            out.append(f'.pal-{key} .panel[data-theme="{theme}"]{{{decl}}}')
    return "\n".join(out)

def contrast_table(p):
    def cell(v, floor=4.5):
        ok = v >= floor
        return f'<td><span class="ratio {"ok" if ok else "bad"}">{v:.2f}:1</span></td>'
    rows = []
    for i, n in enumerate(NAMES):
        l, d = p["light"][i], p["dark"][i]
        rows.append(f'<tr><th scope="row"><span class="dot" style="background:{l}"></span><span class="dot" style="background:{d}"></span>{n}</th>'
                    f'<td><code>{l}</code> / <code>{d}</code></td>{cell(cr(l, "#ffffff"))}{cell(cr("#ffffff", l))}{cell(cr(d, "#1b1b29"))}{cell(cr("#13131f", d))}</tr>')
    return ('<table class="tbl ctab"><thead><tr><th>Status</th><th>Light / dark</th><th>Text on white</th><th>White on fill</th>'
            '<th>Text on dark page</th><th>Dark ink on fill</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table>")

sf = S.sf

def examples():
    ex = []
    ex.append(("Badges", "Status labels and a count badge, as the Badge component draws them.",
        f'''<div class="row"><span class="ar-badge ar-badge--success">{sf("checkmark.circle.fill")}Connected</span>
<span class="ar-badge ar-badge--warning">{sf("exclamationmark.triangle")}Rate limited</span>
<span class="ar-badge ar-badge--danger">{sf("exclamationmark.circle")}Key invalid</span><span class="ar-count">3</span></div>'''))
    ex.append(("Banners", "Inline messages at the top of a view: the status colour on the symbol and the tint, the words in ink.",
        f'''<div class="col">
<div class="banner success">{sf("checkmark.circle.fill", "sf--md")}<div><b>Model downloaded</b><span>Llama 3.1 8B is ready to run offline.</span></div></div>
<div class="banner warning">{sf("exclamationmark.triangle", "sf--md")}<div><b>Approaching your rate limit</b><span>82% of this minute's tokens used.</span></div><button class="ar-btn ar-btn--plain ar-btn--sm">Details</button></div>
<div class="banner danger">{sf("exclamationmark.circle", "sf--md")}<div><b>API key rejected</b><span>Anthropic returned 401. Check the key in Settings.</span></div><button class="ar-btn ar-btn--plain ar-btn--sm">Fix</button></div>
</div>'''))
    ex.append(("Form validation", "Status colour as small text: the hardest case for contrast.",
        f'''<div class="col" style="max-width:340px">
<label class="ar-field"><span class="ar-field__label">API key</span><span class="ar-input">{sf("lock")}sk-ant-•••••••<span class="st success" style="margin-left:auto">{sf("checkmark.circle.fill", "sf--sm")}</span></span><span class="ar-field__help st success">Key verified · Opus 5.5 available</span></label>
<label class="ar-field"><span class="ar-field__label">Endpoint</span><span class="ar-input ar-input--error">htps://api.local</span><span class="ar-field__help ar-field__help--error">Enter a URL that starts with https://</span></label>
<span class="ar-field__help st warning">{sf("exclamationmark.triangle", "sf--sm")} Self-signed certificate: requests may fail.</span>
</div>'''))
    ex.append(("Agent runs", "A list where each row reports a state with a dot, a word and a time.",
        f'''<div class="ar-list" style="max-width:420px">
<div class="ar-list__row"><span class="ar-list__text"><span>Refactor event stream</span><span class="ar-list__sub">arlo-rust · 2 min</span></span><span class="state success"><i></i>Done</span></div>
<div class="ar-list__row"><span class="ar-list__text"><span>Index repository</span><span class="ar-list__sub">ag-ui-rust · running 6 min</span></span><span class="state warning"><i></i>Waiting for approval</span></div>
<div class="ar-list__row"><span class="ar-list__text"><span>Release notes draft</span><span class="ar-list__sub">arlo-lite · 14:02</span></span><span class="state danger"><i></i>Failed</span></div>
</div>'''))
    ex.append(("Progress", "Completion and failure on a progress bar, with the status word beside it.",
        f'''<div class="col" style="max-width:380px">
<div class="ar-field"><span class="ar-field__label pr">Llama 3.1 8B<span class="st success">{sf("checkmark.circle.fill", "sf--sm")} Complete</span></span><div class="ar-progress ar-progress--success"><div class="ar-progress__fill" style="width:100%"></div></div></div>
<div class="ar-field"><span class="ar-field__label pr">Qwen 2.5 32B<span class="st warning">Paused · low disk space</span></span><div class="ar-progress"><div class="ar-progress__fill" style="width:58%;background:var(--color-warning)"></div></div></div>
<div class="ar-field"><span class="ar-field__label pr">Mistral 7B<span class="st danger">{sf("xmark.circle.fill", "sf--sm")} Checksum failed</span></span><div class="ar-progress"><div class="ar-progress__fill" style="width:34%;background:var(--color-danger)"></div></div></div>
</div>'''))
    ex.append(("Calendar", "Event states in a day agenda: accepted, conflicting, declined.",
        f'''<div class="ar-list" style="max-width:420px">
<div class="ar-list__row"><span class="tile success">{sf("calendar.badge.checkmark")}</span><span class="ar-list__text"><span>Design review</span><span class="ar-list__sub st success">Accepted</span></span><span class="when">10:00</span></div>
<div class="ar-list__row"><span class="tile warning">{sf("calendar.badge.exclamationmark")}</span><span class="ar-list__text"><span>Vendor call</span><span class="ar-list__sub st warning">Overlaps Design review</span></span><span class="when">10:30</span></div>
<div class="ar-list__row"><span class="tile danger">{sf("calendar.badge.minus")}</span><span class="ar-list__text"><span style="text-decoration:line-through;color:var(--color-text-secondary)">Team lunch</span><span class="ar-list__sub st danger">Declined</span></span><span class="when">12:30</span></div>
</div>'''))
    ex.append(("Flight status", "A departures board: the status word itself carries the colour.",
        f'''<div class="ar-list" style="max-width:420px">
<div class="ar-list__row">{sf("airplane.departure", "sf--md")}<span class="ar-list__text"><span>BR 192 · TPE → HND</span><span class="ar-list__sub">Gate C4 · 08:40</span></span><b class="st success">On time</b></div>
<div class="ar-list__row">{sf("clock.badge.airplane", "sf--md")}<span class="ar-list__text"><span>JL 802 · TPE → NRT</span><span class="ar-list__sub">Gate B7 · 09:15 → 09:40</span></span><b class="st warning">Delayed 25 min</b></div>
<div class="ar-list__row">{sf("airplane", "sf--md")}<span class="ar-list__text"><span>CI 100 · TPE → NRT</span><span class="ar-list__sub">Gate A2 · 10:05</span></span><b class="st danger">Cancelled</b></div>
</div>'''))
    ex.append(("Destructive actions", "Danger as a filled button, a plain button and a menu item.",
        f'''<div class="col"><div class="row"><button class="ar-btn ar-btn--gray">Cancel</button><button class="ar-btn ar-btn--destructive">{sf("trash")}Delete chat</button><button class="ar-btn ar-btn--destructive-plain">Remove key</button></div>
<div class="ar-menu" style="min-width:240px"><div class="ar-menu__item">{sf("square.and.arrow.up")}Share…</div><div class="ar-menu__sep"></div><div class="ar-menu__item ar-menu__item--destructive">{sf("trash")}Delete</div></div></div>'''))
    return ex

LAB_CSS = """
.lab-controls{position:sticky;top:64px;z-index:5;display:flex;flex-wrap:wrap;align-items:center;gap:var(--space200);padding:var(--space200) 0;margin-bottom:var(--space200);background:var(--color-bg);border-bottom:1px solid var(--color-border)}
.lab-controls .ar-seg__item{cursor:pointer;border:0;background:transparent;font:inherit;font-weight:500}
.lab-controls .ar-seg__item--selected{background:var(--color-segment)}
.pal-note{margin:0 0 var(--space200);max-width:760px;color:var(--color-text-secondary)}
.ex{margin-top:var(--space500)}
.ex h2{margin:0 0 var(--space50);font:600 22px/28px var(--font-sans);letter-spacing:-.22px}
.ex>p{margin:0 0 var(--space200);color:var(--color-text-secondary);font-size:14px;line-height:20px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:var(--space200)}
.panel{position:relative;padding:var(--space400) var(--space300) var(--space300);border:1px solid var(--color-border);border-radius:var(--radius-lg);background:var(--color-bg);color:var(--color-text-primary);font-size:14px;line-height:20px;letter-spacing:.25px}
.panel>.tag{position:absolute;top:var(--space100);right:var(--space125);font:500 11px/16px var(--font-sans);letter-spacing:.5px;color:var(--color-text-secondary)}
.panel .row{display:flex;flex-wrap:wrap;align-items:center;gap:12px}
.panel .col{display:flex;flex-direction:column;gap:16px}
.banner{display:flex;align-items:flex-start;gap:var(--space125);padding:var(--space150,12px) var(--space200);border-radius:var(--radius-md)}
.banner>div{display:flex;flex-direction:column;flex:1;gap:2px}
.banner b{font-weight:600}.banner span{color:var(--color-text-secondary)}
.banner .ar-btn{margin:-4px -8px -4px 0}
.banner.success{background:var(--color-success-light)}.banner.success>.sf{color:var(--color-success)}
.banner.warning{background:var(--color-warning-light)}.banner.warning>.sf{color:var(--color-warning)}
.banner.danger{background:var(--color-danger-light)}.banner.danger>.sf{color:var(--color-danger)}
.st{display:inline-flex;align-items:center;gap:4px;--sf-size:14px}
.st.success{color:var(--color-success)}.st.warning{color:var(--color-warning)}.st.danger{color:var(--color-danger)}
b.st{font-weight:600;white-space:nowrap}
.state{display:inline-flex;align-items:center;gap:6px;color:var(--color-text-secondary);white-space:nowrap}
.state i{width:8px;height:8px;border-radius:50%}
.state.success i{background:var(--color-success)}.state.warning i{background:var(--color-warning)}.state.danger i{background:var(--color-danger)}
.tile{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:var(--radius-mark);--sf-size:16px}
.tile.success{background:var(--color-success-light);color:var(--color-success)}.tile.warning{background:var(--color-warning-light);color:var(--color-warning)}.tile.danger{background:var(--color-danger-light);color:var(--color-danger)}
.when{font:500 12px/16px var(--font-sans);color:var(--color-text-secondary)}
.pr{display:flex;justify-content:space-between;gap:12px}
.ctab code{font-size:12px}
.ctab th[scope=row]{display:flex;align-items:center;gap:4px;font:600 14px/20px var(--font-sans);letter-spacing:0;color:var(--color-text-primary)}
.dot{width:12px;height:12px;border-radius:50%;border:1px solid var(--color-border)}
.ratio{display:inline-block;padding:1px 8px;border-radius:999px;font:500 12px/18px var(--font-mono);letter-spacing:0}
.ratio.ok{background:var(--color-success-light);color:var(--color-text-primary)}
.ratio.bad{background:var(--color-danger-light);color:var(--color-text-primary);box-shadow:inset 0 0 0 1px var(--color-danger)}
.pal-pane{display:none}
@media (max-width:900px){.pair{grid-template-columns:1fr}.lab-controls{top:64px}}
"""

LAB_JS = """
document.addEventListener('DOMContentLoaded',function(){
  var btns=document.querySelectorAll('[data-pal]');
  function set(k){document.body.className=document.body.className.replace(/\\bpal-\\S+/g,'').trim()+' pal-'+k;
    btns.forEach(function(b){var on=b.dataset.pal===k;b.classList.toggle('ar-seg__item--selected',on);b.setAttribute('aria-pressed',on)});
    document.querySelectorAll('.pal-pane').forEach(function(p){p.style.display=p.dataset.for===k?'block':'none'});
    try{history.replaceState(null,'','#'+k)}catch(e){}}
  btns.forEach(function(b){b.addEventListener('click',function(){set(b.dataset.pal)})});
  var h=(location.hash||'').slice(1);set(btns.length&&[].some.call(btns,function(b){return b.dataset.pal===h})?h:'apple');
});
"""

def run():
    seg = "".join(f'<button class="ar-seg__item" data-pal="{k}" aria-pressed="false">{label}</button>' for k, label, _, _ in PALETTES)
    panes = "".join(f'<div class="pal-pane" data-for="{k}"><p class="pal-note">{html.escape(note)}</p>{contrast_table(p)}</div>' for k, _, note, p in PALETTES)
    exs = "".join(f'<section class="ex"><h2>{t}</h2><p>{d}</p><div class="pair">'
                  f'<div class="panel ar-root" data-theme="light"><span class="tag">Light</span>{body}</div>'
                  f'<div class="panel ar-root" data-theme="dark"><span class="tag">Dark</span>{body}</div></div></section>'
                  for t, d, body in examples())
    body = (f'<div class="lab-controls"><span class="ar-seg" role="group" aria-label="Status palette">{seg}</span>'
            f'<span style="color:var(--color-text-secondary);font-size:13px">Pick a palette: every example below repaints, light and dark side by side.</span></div>'
            f'{panes}{exs}')
    extra = f"<style>{LAB_CSS}\n{palette_css()}</style>\n<script>{LAB_JS}</script>\n"
    page = S.shell(1, "foundations", "status-lab", "Foundations · experiment", "Status color lab",
                   "Success, warning and danger in real Arlo screens. The system uses Apple system colours; compare them with the alternatives that were considered.", body, extra)
    B.write(os.path.join(B.SITE, "foundations", "status-lab.html"), page)
    print("status lab: foundations/status-lab.html")
