"""Docs site generator: site/ (static, open site/index.html directly)."""
import html, json, os, re, shutil
import build as B

SITE_CSS = r"""
/* Arlo Design System docs — site chrome, built on the system's own tokens */
*,*::before,*::after{box-sizing:border-box}
html{scroll-padding-top:88px}
body{margin:0;background:var(--color-bg);color:var(--color-text-primary);font-family:var(--font-sans);font-size:16px;line-height:24px;letter-spacing:.25px;-webkit-font-smoothing:antialiased}
a{color:var(--color-accent);text-decoration:none}
a:hover{text-decoration:underline}
code{font-family:var(--font-mono);font-size:.875em;letter-spacing:0;background:var(--color-bg-tertiary);padding:1px 6px;border-radius:6px}
:focus-visible{outline:none;box-shadow:var(--shadow-focus);border-radius:6px}

.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:var(--space200);height:64px;padding:0 var(--space300);background:var(--color-bar);-webkit-backdrop-filter:saturate(180%) blur(20px);backdrop-filter:saturate(180%) blur(20px);border-bottom:1px solid var(--color-border)}
.brand{display:flex;align-items:center;gap:var(--space125);white-space:nowrap;min-width:0;color:var(--color-text-primary);font:600 16px/24px var(--font-sans);letter-spacing:-.16px}
.brand:hover{text-decoration:none}
.brand img{width:28px;height:28px}
.tabs{display:flex;gap:var(--space50);margin-left:var(--space300)}
.tabs a{padding:6px 14px;border-radius:var(--radius-button);color:var(--color-text-secondary);font:500 14px/20px var(--font-sans);letter-spacing:.1px}
.tabs a:hover{background:var(--color-bg-tertiary);text-decoration:none}
.tabs a.on{background:var(--color-accent-light);color:var(--color-accent)}
.spacer{flex:1}
.iconbtn{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border:0;border-radius:var(--radius-button);background:transparent;color:var(--color-text-secondary);cursor:pointer;--sf-size:20px}
.iconbtn:hover{background:var(--color-bg-tertiary)}
.menu-btn{display:none}
.density{height:36px;padding:0 14px;border:1px solid var(--color-border-strong);border-radius:var(--radius-button);background:transparent;color:var(--color-text-secondary);font:500 13px/16px var(--font-sans);cursor:pointer}
.density:hover{background:var(--color-bg-tertiary)}
.density.on{background:var(--color-accent-light);border-color:transparent;color:var(--color-accent)}
@media (pointer: coarse){.density{display:none}}

.shell{display:grid;grid-template-columns:280px minmax(0,1fr);min-height:calc(100vh - 64px)}
.rail{position:sticky;top:64px;height:calc(100vh - 64px);overflow:auto;padding:var(--space200) var(--space125) var(--space600);border-right:1px solid var(--color-border)}
.rail h4{margin:var(--space200) var(--space150,12px) var(--space50);font:500 12px/16px var(--font-sans);letter-spacing:.5px;color:var(--color-text-secondary)}
.rail a{display:flex;align-items:center;gap:var(--space125);height:40px;padding:0 var(--space200);border-radius:var(--radius-button);color:var(--color-text-primary);font:400 14px/20px var(--font-sans);letter-spacing:.1px}
.rail a:hover{background:var(--color-bg-tertiary);text-decoration:none}
.rail a.on{background:var(--color-accent-light);color:var(--color-accent);font-weight:600}

main{padding:var(--space400) var(--space600) var(--space900);max-width:1120px;width:100%}
.hero{padding:var(--space600) var(--space500);margin-bottom:var(--space600);border-radius:var(--radius-xl);background:var(--color-bg-secondary)}
.eyebrow{margin:0 0 var(--space100);font:500 14px/20px var(--font-sans);letter-spacing:.1px;color:var(--color-accent)}
.hero h1{margin:0;font:700 45px/52px var(--font-sans);letter-spacing:-1.2px}
.lede{margin:var(--space200) 0 0;max-width:720px;font-size:18px;line-height:28px;color:var(--color-text-secondary)}
.prose{max-width:760px}
.prose h2,main>h2{margin:var(--space600) 0 var(--space200);font:600 28px/36px var(--font-sans);letter-spacing:-.4px}
.prose h3,main>h3{margin:var(--space400) 0 var(--space100);font:600 22px/28px var(--font-sans);letter-spacing:-.22px}
.prose p,.prose li{color:var(--color-text-primary)}
.prose ul{padding-left:var(--space300)}
.prose li{margin:var(--space100) 0}
.prose table,.tbl{border-collapse:collapse;width:100%;font-size:14px;line-height:20px}
.prose th,.prose td,.tbl th,.tbl td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--color-border);vertical-align:top}
.prose th,.tbl th{font:500 12px/16px var(--font-sans);letter-spacing:.5px;color:var(--color-text-secondary)}
.section{margin-top:var(--space600)}
.section>h2{margin:0 0 var(--space100);font:600 28px/36px var(--font-sans);letter-spacing:-.4px}
.section>p.sub{margin:0 0 var(--space300);color:var(--color-text-secondary);max-width:720px}

.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:var(--space200)}
.card{display:flex;flex-direction:column;gap:var(--space100);padding:var(--space300);border:1px solid var(--color-border);border-radius:var(--radius-lg);background:var(--color-bg);color:var(--color-text-primary);transition:box-shadow 250ms ease,transform 250ms ease}
a.card:hover{text-decoration:none;box-shadow:var(--shadow-md),var(--ring-accent);transform:translateY(-2px)}
.card h3{margin:0;font:600 18px/24px var(--font-sans);letter-spacing:-.18px}
.card p{margin:0;font-size:14px;line-height:20px;color:var(--color-text-secondary)}
.card .ar-symbol-tile{margin-bottom:var(--space50)}

.frame{border:1px solid var(--color-border);border-radius:var(--radius-lg);overflow:hidden;background:var(--color-bg)}
.frame iframe{display:block;width:100%;border:0;background:var(--color-bg)}
.cover-box{overflow:hidden}.cover-box iframe{max-width:none}
.frame-bar{display:flex;align-items:center;gap:var(--space100);padding:var(--space100) var(--space200);border-bottom:1px solid var(--color-border);background:var(--color-bg-secondary);font:500 12px/16px var(--font-sans);letter-spacing:.5px;color:var(--color-text-secondary)}
pre.code{margin:0;max-height:360px;overflow:auto;padding:var(--space200);background:var(--color-bg-secondary);font:400 12px/18px var(--font-mono);letter-spacing:0;color:var(--color-text-primary);white-space:pre-wrap;word-break:break-word}
details.code-box{margin-top:var(--space200);border:1px solid var(--color-border);border-radius:var(--radius-md);overflow:hidden}
details.code-box summary{cursor:pointer;padding:var(--space125) var(--space200);font:500 14px/20px var(--font-sans);color:var(--color-text-secondary)}

.swatches{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:var(--space200)}
.swatch{border:1px solid var(--color-border);border-radius:var(--radius-lg);overflow:hidden;background:var(--color-bg)}
.chips{display:grid;grid-template-columns:1fr 1fr;height:88px}
.chip{display:flex;align-items:flex-end;padding:var(--space100);font:500 11px/16px var(--font-mono);letter-spacing:0}
.chip.l{background:#fff;color:#1a1a2e}.chip.d{background:#1b1b29;color:#ececf6}
.chip{min-width:0}.chip span{max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;padding:2px 6px;border-radius:6px;background:rgba(127,127,127,.18)}
.swatch .meta{padding:var(--space150,12px) var(--space200) var(--space200)}
.swatch b{display:block;font:600 14px/20px var(--font-mono);letter-spacing:0}
.swatch p{margin:var(--space50) 0 0;font-size:12px;line-height:16px;color:var(--color-text-secondary)}

.specimen{display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:var(--space300);align-items:baseline;padding:var(--space300) 0;border-bottom:1px solid var(--color-border)}
.specimen .s{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.specimen .m{font:400 12px/18px var(--font-mono);letter-spacing:0;color:var(--color-text-secondary)}
.specimen .m b{display:block;font-family:var(--font-sans);font-weight:600;color:var(--color-text-primary)}
.specimen .u{grid-column:1/-1;margin-top:-12px;font-size:13px;line-height:18px;color:var(--color-text-secondary)}

.scale{display:grid;grid-template-columns:160px 80px 1fr;gap:var(--space200);align-items:center;padding:var(--space125) 0;border-bottom:1px solid var(--color-border);font-size:14px;line-height:20px}
.scale code{justify-self:start}
.bar{height:16px;border-radius:4px;background:var(--color-accent)}
.scale .u{grid-column:1/-1;margin-top:-8px;font-size:12px;line-height:16px;color:var(--color-text-secondary)}
.radii{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:var(--space200)}
.radius-box{height:96px;background:var(--color-accent-light);border:2px solid var(--color-accent)}
.shadows{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:var(--space300)}
.shadow-box{height:96px;border-radius:var(--radius-lg);background:var(--color-bg-elevated);border:1px solid var(--color-border)}
.tok{margin-top:var(--space125)}
.tok b{display:block;font:600 13px/18px var(--font-mono);letter-spacing:0}
.tok span{display:block;font-size:12px;line-height:16px;color:var(--color-text-secondary)}

.sym-tools{display:flex;gap:var(--space200);align-items:center;margin-bottom:var(--space200)}
.sym-tools .ar-search{flex:1;max-width:420px}
.sym-tools input{flex:1;border:0;background:transparent;font:inherit;color:inherit;outline:none}
.symgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(124px,1fr));gap:var(--space100)}
.sym{display:flex;flex-direction:column;align-items:center;gap:var(--space125);padding:var(--space200) var(--space100);border:0;border-radius:var(--radius-md);background:var(--color-bg-secondary);color:var(--color-text-primary);cursor:pointer;font:inherit}
.sym:hover{background:var(--color-accent-light);color:var(--color-accent)}
.sym .sf{--sf-size:28px}
.sym small{font:400 10px/14px var(--font-mono);letter-spacing:0;color:var(--color-text-secondary);text-align:center;word-break:break-all}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(80px);transition:transform 250ms ease;z-index:50}
.toast.on{transform:translateX(-50%)}
.logos{display:flex;flex-wrap:wrap;gap:var(--space300)}
.logos figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:var(--space100);padding:var(--space300);border:1px solid var(--color-border);border-radius:var(--radius-lg);min-width:160px}
.logos img{width:56px;height:56px}
.logos figcaption{font:400 12px/16px var(--font-mono);color:var(--color-text-secondary)}
.dos{display:grid;grid-template-columns:1fr 1fr;gap:var(--space200)}
.foot{margin-top:var(--space900);padding-top:var(--space300);border-top:1px solid var(--color-border);font-size:13px;line-height:18px;color:var(--color-text-secondary)}

@media (max-width: 900px){
  .shell{grid-template-columns:1fr}
  .rail{position:fixed;top:64px;left:0;z-index:15;width:280px;background:var(--color-bg);transform:translateX(-100%);transition:transform 250ms ease;box-shadow:var(--shadow-xl)}
  body.nav-open .rail{transform:none}
  .menu-btn{display:inline-flex}
  .iconbtn{width:44px;height:44px}
  .rail a{height:44px}
  .density{height:44px}
  .tabs{display:none}
  main{padding:var(--space300) var(--space200) var(--space800)}
  .hero{padding:var(--space400) var(--space300)}
  .hero h1{font-size:36px;line-height:44px}
  .specimen{grid-template-columns:1fr}
  .scale{grid-template-columns:120px 64px 1fr}
  .dos{grid-template-columns:1fr}
}
"""

SITE_JS = r"""
(function(){
  var root=document.documentElement, KEY='arlo-ds-theme';
  function sys(){return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}
  function get(){try{return localStorage.getItem(KEY)}catch(e){return null}}
  var DKEY='arlo-ds-touch';
  function touchOn(){try{return localStorage.getItem(DKEY)==='1'}catch(e){return false}}
  function apply(t){root.setAttribute('data-theme',t);var tc=touchOn();root.classList.toggle('ar-touch',tc);
    document.querySelectorAll('iframe[data-src]').forEach(function(f){var u=f.getAttribute('data-src')+'?theme='+t+(tc?'&touch=1':'');if(f.getAttribute('src')!==u)f.setAttribute('src',u)});
    var d=document.getElementById('density');if(d){d.setAttribute('aria-pressed',tc);d.classList.toggle('on',tc)}
    var b=document.getElementById('theme');if(b){b.setAttribute('aria-label',t==='dark'?'Switch to light theme':'Switch to dark theme');b.querySelector('.sf').setAttribute('data-symbol',t==='dark'?'sun.max':'moon')}}
  apply(get()||sys());
  document.addEventListener('DOMContentLoaded',function(){
    apply(root.getAttribute('data-theme'));
    var b=document.getElementById('theme');
    if(b)b.addEventListener('click',function(){var t=root.getAttribute('data-theme')==='dark'?'light':'dark';try{localStorage.setItem(KEY,t)}catch(e){}apply(t)});
    function fit(f){try{var d=f.contentDocument;if(!d||!d.body)return;var old=f.style.height;f.style.height='40px';var h=d.documentElement.scrollHeight;f.style.height=(h>40?h:parseInt(old))+'px'}catch(e){}}
    document.querySelectorAll('iframe[data-fit]').forEach(function(f){f.addEventListener('load',function(){fit(f);setTimeout(function(){fit(f)},300)});fit(f)});
    function cover(){document.querySelectorAll('.cover-box').forEach(function(b){var k=Math.min(1,b.clientWidth/960);var f=b.querySelector('iframe');f.style.transform='scale('+k+')';b.style.height=(296*k)+'px'})}
    cover();window.addEventListener('resize',cover);
    var d=document.getElementById('density');
    if(d)d.addEventListener('click',function(){try{localStorage.setItem(DKEY,touchOn()?'0':'1')}catch(e){}apply(root.getAttribute('data-theme'))});
    var m=document.getElementById('menu');if(m)m.addEventListener('click',function(){document.body.classList.toggle('nav-open')});
    var q=document.getElementById('symq');
    if(q)q.addEventListener('input',function(){var v=q.value.trim().toLowerCase();document.querySelectorAll('.sym').forEach(function(s){s.style.display=!v||s.dataset.name.indexOf(v)>-1?'':'none'})});
    var toast=document.getElementById('toast'),tt;
    document.querySelectorAll('.sym').forEach(function(s){s.addEventListener('click',function(){
      var n=s.dataset.name;function done(){if(!toast)return;toast.querySelector('span:last-child').textContent='Copied '+n;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('on')},1600)}
      try{navigator.clipboard.writeText(n).then(done,done)}catch(e){done()}})});
  });
})();
"""

FOUNDATIONS = [("content", "Content", "Content fundamentals", "Voice, tone and the words Arlo uses — and never uses."),
               ("color", "Color", "Color", "One indigo accent, indigo-tinted neutrals, a light and a dark theme."),
               ("typography", "Typography", "Typography", "The Material 3 type scale, set in Inter, with Arlo's emphasized headings."),
               ("spacing", "Spacing and layout", "Spacing and layout", "Material 3's 8dp spacing scale, window margins and control sizes."),
               ("shape", "Shape", "Shape", "Arlo's radius scale and the fixed 12px button corner."),
               ("elevation", "Elevation and motion", "Elevation and motion", "Hairlines and tonal layers first, soft shadows second, calm motion."),
               ("iconography", "Iconography", "Iconography", "SF Symbols for every interface icon, and Arlo's own brand marks.")]
SYMBOL_PAGES = [("interface", "Symbols", "Interface symbols", "The general SF Symbols set used across Arlo components."),
                ("calendar", "Calendar", "Calendar symbols", "SF Symbols for calendar and scheduling apps."),
                ("travel", "Travel", "Travel symbols", "SF Symbols for travel apps: flights, stays, maps, money and weather."),
                ("logos", "Logos", "Brand marks", "Arlo's project marks. Never redrawn, never recoloured.")]

def sf(name, cls=""):
    return f'<span class="sf{(" " + cls) if cls else ""}" data-symbol="{name}"></span>'

def shell(depth, active_tab, active_link, eyebrow, title, lede, body, extra_head=""):
    up = "../" * depth
    def link(href, label, key):
        return f'<a href="{up}{href}"{" class=\"on\"" if key == active_link else ""}>{label}</a>'
    rail = ['<h4>Get started</h4>', link("index.html", "Overview", "overview"), '<h4>Foundations</h4>']
    rail += [link(f"foundations/{k}.html", label, k) for k, label, *_ in FOUNDATIONS]
    rail.append(link("foundations/status-lab.html", "Status color lab", "status-lab"))
    rail += ['<h4>Symbols</h4>'] + [link(f"symbols/{k}.html", label, "sym-" + k) for k, label, *_ in SYMBOL_PAGES]
    rail += ['<h4>Components</h4>', link("components/index.html", "All components", "components")]
    for g in B.COMP_GROUPS:
        for c in [c for c in B.components if c["group"] == g]:
            rail.append(link(f"components/{c['name']}.html", B.spaced(c["name"]), "c-" + c["name"]))
    tabs = "".join(f'<a href="{up}{h}"{" class=\"on\"" if k == active_tab else ""}>{l}</a>'
                   for k, h, l in [("foundations", "foundations/color.html", "Foundations"),
                                   ("symbols", "symbols/interface.html", "Symbols"),
                                   ("components", "components/index.html", "Components")])
    hero = (f'<section class="hero"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1>'
            + (f'<p class="lede">{lede}</p>' if lede else "") + "</section>") if title else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(re.sub('<[^>]+>', '', title or 'Arlo Design System'))} · Arlo Design System</title>
<link rel="icon" href="{up}assets/logos/favicon.svg">
<link rel="stylesheet" href="{up}css/tokens.css">
<link rel="stylesheet" href="{up}css/components.css">
<link rel="stylesheet" href="{up}css/symbols.css">
<link rel="stylesheet" href="{up}css/site.css">
<script src="{up}js/site.js"></script>
{extra_head}</head>
<body>
<header class="topbar">
  <button class="iconbtn menu-btn" id="menu" aria-label="Open navigation">{sf("sidebar.left")}</button>
  <a class="brand" href="{up}index.html"><img src="{up}assets/logos/arlo-mark.svg" alt="">Arlo Design System</a>
  <nav class="tabs" aria-label="Sections">{tabs}</nav>
  <span class="spacer"></span>
  <button class="density" id="density" aria-pressed="false" title="Show components at touch sizes, as on a phone">Touch sizes</button>
  <button class="iconbtn" id="theme" aria-label="Switch theme">{sf("moon")}</button>
</header>
<div class="shell">
<nav class="rail" aria-label="Pages">{''.join(rail)}</nav>
<main>
{hero}
{body}
<p class="foot">Arlo Design System · generated from the design-system source by tools/build.py · SF Symbols are Apple's, licensed for apps on Apple platforms.</p>
</main>
</div>
<div class="toast" id="toast" role="status"><span class="ar-helptag"><span>{sf("checkmark", "sf--sm")}</span> <span>Copied</span></span></div>
</body>
</html>
"""

def frame(c, depth, label=None):
    h = c["height"] + 8
    return (f'<div class="frame"><div class="frame-bar">{sf("eye", "sf--sm") if False else ""}{html.escape(label or "Preview")}</div>'
            f'<iframe title="{html.escape(c["name"])} preview" data-src="{"../" * depth}previews/{c["name"]}.html" '
            f'src="{"../" * depth}previews/{c["name"]}.html" style="height:{h}px" data-fit></iframe></div>')

def code_box(c):
    return (f'<details class="code-box"><summary>HTML</summary><pre class="code">{html.escape(B.snippet(c))}\n\n&lt;!-- page-level layout helpers used by this example --&gt;\n&lt;style&gt;\n{html.escape(B.example_css(c))}\n&lt;/style&gt;</pre></details>')

# --------------------------------------------------------------- foundation bodies
def color_body():
    groups = [("Accent", lambda n: n.startswith("color-accent") or n == "text-on-accent"),
              ("Text", lambda n: n.startswith("color-text")),
              ("Surfaces", lambda n: n.startswith("color-bg") or n in ("color-bar", "color-fill-hover", "color-segment", "color-scrim")),
              ("Borders", lambda n: n.startswith("color-border")),
              ("Status", lambda n: n.split("-")[1] in ("success", "warning", "danger") if n.startswith("color-") else False),
              ("Semantic aliases", lambda n: not n.startswith("color-") and n != "text-on-accent")]
    toks = B.tokens["color"]["tokens"]
    resolved = {}
    def res(t, th):
        v = B.val(t["value"], th); m = re.fullmatch(r"\{(.+)\}", v)
        return res(next(x for x in toks if x["name"] == m.group(1)), th) if m else v
    out, used = [], set()
    for gname, test in groups:
        items = [t for t in toks if t["name"] not in used and test(t["name"])]
        used |= {t["name"] for t in items}
        cards = []
        for t in items:
            lv, dv = res(t, "light"), res(t, "dark")
            alias = re.fullmatch(r"\{(.+)\}", B.val(t["value"], "light"))
            cards.append(f'<div class="swatch"><div class="chips"><div class="chip l" style="background:linear-gradient({lv},{lv}),#fff"><span>{html.escape(lv)}</span></div>'
                         f'<div class="chip d" style="background:linear-gradient({dv},{dv}),#1b1b29"><span>{html.escape(dv)}</span></div></div>'
                         f'<div class="meta"><b>{t["name"]}</b>' + (f'<p>Alias of <code>{alias.group(1)}</code></p>' if alias else "")
                         + f'<p>{B.inline(t.get("usage", ""))}</p></div></div>')
        out.append(f'<div class="section"><h2>{gname}</h2><p class="sub">Left half light theme, right half dark theme.{' <a href="status-lab.html">Compare with the palettes that were considered →</a>' if gname == "Status" else ""}</p><div class="swatches">{"".join(cards)}</div></div>')
    return f'<div class="prose">{B.md(B.SECS["Color"])}</div>' + "".join(out)

def type_body():
    out = [f'<div class="prose">{B.md(B.SECS["Typography"])}</div>']
    for g in B.tokens["type"]["groups"]:
        rows = []
        for s in g["styles"]:
            sample = s.get("sample") or ("The quick agent runs on your machine" if "display" not in s["name"] else "Your keys, your machine")
            lh = s["lineHeight"]
            rows.append(f'<div class="specimen"><div class="s {s["name"]}">{html.escape(sample)}</div>'
                        f'<div class="m"><b>{s["name"]}</b>{s["fontSize"]} / {lh} · {s["fontWeight"]} · {s.get("letterSpacing", "0px")}</div>'
                        f'<div class="u">{B.inline(s.get("usage", ""))}</div></div>')
        out.append(f'<div class="section"><h2>{g["name"]}</h2>{"".join(rows)}</div>')
    return "".join(out)

def scale_rows(fam, cap=480):
    rows = []
    for t in B.tokens[fam]["tokens"]:
        px = float(re.sub(r"[^\d.]", "", t["value"]) or 0)
        rows.append(f'<div class="scale"><code>{t["name"]}</code><span>{t["value"]}</span>'
                    f'<div class="bar" style="width:{min(px, cap)}px"></div><div class="u">{B.inline(t["usage"])}</div></div>')
    return "".join(rows)

def spacing_body():
    return (f'<div class="prose">{B.md(B.SECS["Spacing and layout"])}</div>'
            f'<div class="section"><h2>Spacing tokens</h2><p class="sub">{B.inline(B.tokens["spacing"].get("note", ""))}</p>{scale_rows("spacing")}</div>'
            f'<div class="section"><h2>Sizes</h2><p class="sub">{B.inline(B.tokens["size"].get("note", ""))}</p>{scale_rows("size")}</div>')

def shape_body():
    boxes = "".join(f'<div><div class="radius-box" style="border-radius:{t["value"]}"></div><div class="tok"><b>{t["name"]} · {t["value"]}</b><span>{B.inline(t["usage"])}</span></div></div>'
                    for t in B.tokens["radius"]["tokens"])
    return (f'<div class="prose">{B.md(B.SECS["Shape"])}</div><div class="section"><h2>Radius tokens</h2>'
            f'<p class="sub">{B.inline(B.tokens["radius"].get("note", ""))}</p><div class="radii">{boxes}</div></div>'
            f'<div class="section"><h2>Button corner</h2>{frame(B.byname["Button"], 1)}</div>')

def elevation_body():
    boxes = "".join(f'<div><div class="shadow-box" style="box-shadow:var(--{t["name"]})"></div><div class="tok"><b>{t["name"]}</b><span>{B.inline(t["usage"])}</span></div></div>'
                    for t in B.tokens["shadow"]["tokens"])
    return (f'<div class="prose">{B.md(B.SECS["Elevation and motion"])}</div>'
            f'<div class="section"><h2>Shadow tokens</h2><p class="sub">Shown on <code>color-bg-elevated</code>; switch the theme to see the dark values.</p><div class="shadows">{boxes}</div></div>')

def icon_body():
    return (f'<div class="prose">{B.md(B.SECS["Iconography"])}</div>'
            f'<div class="section"><h2>In practice</h2>{frame(B.byname["Symbol"], 1)}</div>'
            f'<div class="section"><h2>Browse</h2><div class="cards">'
            + "".join(f'<a class="card" href="../symbols/{k}.html"><span class="ar-symbol-tile ar-symbol-tile--lg">{sf(ic)}</span><h3>{t}</h3><p>{l}</p></a>'
                      for (k, _, t, l), ic in zip(SYMBOL_PAGES, ["gearshape", "calendar", "airplane", "star"]))
            + "</div></div>")

def symbol_grid(group):
    names = sorted(n for n, (g, _) in B.symbols.items() if g == group)
    tiles = "".join(f'<button class="sym" data-name="{n}" title="Copy {n}">{sf(n)}<small>{n}</small></button>' for n in names)
    return (f'<div class="sym-tools"><label class="ar-search">{sf("magnifyingglass")}<input id="symq" type="search" placeholder="Filter {len(names)} symbols" aria-label="Filter symbols"></label>'
            f'<span class="cap" style="color:var(--color-text-secondary);font-size:13px">Click a symbol to copy its name</span></div><div class="symgrid">{tiles}</div>')

def group_readme(g):
    p = os.path.join(B.SRC, "assets", g, "README.md")
    return re.sub(r"^#\s+.*\n", "", open(p).read()).strip() if os.path.exists(p) else ""

def run():
    B.reset(B.SITE)
    w = lambda rel, text: B.write(os.path.join(B.SITE, rel), text)
    w("css/tokens.css", B.TOKENS_CSS); w("css/components.css", B.bundle_css); w("css/symbols.css", B.SYMBOLS_CSS)
    w("css/site.css", SITE_CSS); w("js/site.js", SITE_JS)
    os.makedirs(os.path.join(B.SITE, "assets", "logos"))
    for f in B.logos: shutil.copy(os.path.join(B.SRC, "assets", "Logos", f), os.path.join(B.SITE, "assets", "logos", f))
    for c in B.COMPONENT_ORDER: w(f"previews/{c['name']}.html", B.preview_doc(c, "../css/"))
    # theme-toggle symbols must exist in the symbol CSS
    for need in ("moon", "sun.max", "sidebar.left", "magnifyingglass", "checkmark"):
        if need not in B.symbols: print(f"  note: symbol {need} missing from the system")

    # overview
    cover = B.byname["Cover"]
    found_cards = "".join(f'<a class="card" href="foundations/{k}.html"><span class="ar-symbol-tile">{sf(ic)}</span><h3>{t}</h3><p>{l}</p></a>'
                          for (k, _, t, l), ic in zip(FOUNDATIONS, ["bubble.left", "sparkles", "text.pad.header", "square.grid.3x3", "square.and.pencil", "info.circle", "star"]))
    comp_cards = "".join(f'<a class="card" href="components/{c["name"]}.html"><h3>{B.spaced(c["name"])}</h3><p>{B.inline(c["summary"])}</p></a>' for c in B.components[:6])
    dos = B.md(B.SECS.get("Do and don't", ""))
    body = (f'<div class="frame cover-box" style="margin-bottom:48px"><iframe title="Cover" data-src="previews/Cover.html" src="previews/Cover.html" style="width:960px;height:296px;transform-origin:0 0"></iframe></div>'
            f'<div class="prose"><p class="lede" style="margin:0">{B.inline(B.INTRO)}</p></div>'
            f'<div class="section"><h2>Foundations</h2><p class="sub">The rules every screen is built from.</p><div class="cards">{found_cards}</div></div>'
            f'<div class="section"><h2>Components</h2><p class="sub">{len(B.components)} components that follow Apple\'s Human Interface Guidelines, styled with Arlo\'s tokens. <a href="components/index.html">See all →</a></p><div class="cards">{comp_cards}</div></div>'
            f'<div class="section"><h2>Do and don\'t</h2><div class="prose">{dos}</div></div>')
    w("index.html", shell(0, "", "overview", "Arlo AI", "", "", body))

    # foundations
    bodies = {"content": lambda: f'<div class="prose">{B.md(B.SECS["Content fundamentals"])}</div>', "color": color_body,
              "typography": type_body, "spacing": spacing_body, "shape": shape_body, "elevation": elevation_body, "iconography": icon_body}
    for k, _, t, l in FOUNDATIONS:
        w(f"foundations/{k}.html", shell(1, "foundations", k, "Foundations", t, l, bodies[k]()))

    # symbols
    for k, _, t, l in SYMBOL_PAGES:
        if k == "logos":
            figs = "".join(f'<figure><img src="../assets/logos/{f}" alt="{f[:-4]}"><figcaption>{f}</figcaption></figure>' for f in B.logos)
            body = f'<div class="prose">{B.md(group_readme("Logos"))}</div><div class="section logos">{figs}</div>'
        else:
            g = {"interface": "Symbols", "calendar": "Calendar", "travel": "Travel"}[k]
            show = {"calendar": "CalendarSymbols", "travel": "TravelSymbols"}.get(k)
            body = f'<div class="prose">{B.md(group_readme(g))}</div>'
            if show:
                c = B.byname[show]
                body += f'<div class="section"><h2>In use</h2>{frame(c, 1)}</div><div class="section"><h2>Meanings</h2><div class="prose">{B.md(c["readme"])}</div></div>'
            body += f'<div class="section"><h2>All {g.lower() if g != "Symbols" else "interface"} symbols</h2>{symbol_grid(g)}</div>'
        w(f"symbols/{k}.html", shell(1, "symbols", "sym-" + k, "Symbols", t, l, body))

    # components
    groups_html = []
    for g in B.COMP_GROUPS:
        cs = [c for c in B.components if c["group"] == g]
        if not cs: continue
        groups_html.append(f'<div class="section"><h2>{g}</h2><div class="cards">' + "".join(
            f'<a class="card" href="{c["name"]}.html"><h3>{B.spaced(c["name"])}</h3><p>{B.inline(c["summary"])}</p></a>' for c in cs) + "</div></div>")
    w("components/index.html", shell(1, "components", "components", "Components", "Components",
                                     B.inline(B.SECS["Components"].split("\n\n")[0]), "".join(groups_html)))
    for c in B.components:
        paras = c["readme"].split("\n\n")
        rest = "\n\n".join(paras[1:]) if paras and paras[0].strip() == c["summary"].strip() else c["readme"]
        body = (f'{frame(c, 1)}{code_box(c)}<div class="section prose"><h2>Guidelines</h2>{B.md(rest, shift=1)}</div>')
        w(f"components/{c['name']}.html", shell(1, "components", "c-" + c["name"], c["group"], B.spaced(c["name"]), B.inline(c["summary"]), body))
    n = sum(len(fs) for _, _, fs in os.walk(B.SITE))
    print(f"site: {n} files in {B.SITE}")
