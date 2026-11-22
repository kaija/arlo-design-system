
(function(){
  var root=document.documentElement, KEY='arlo-ds-theme';
  function sys(){return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}
  function get(){try{return localStorage.getItem(KEY)}catch(e){return null}}
  function apply(t){root.setAttribute('data-theme',t);
    document.querySelectorAll('iframe[data-src]').forEach(function(f){var u=f.getAttribute('data-src')+'?theme='+t;if(f.getAttribute('src')!==u)f.setAttribute('src',u)});
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
    var m=document.getElementById('menu');if(m)m.addEventListener('click',function(){document.body.classList.toggle('nav-open')});
    var q=document.getElementById('symq');
    if(q)q.addEventListener('input',function(){var v=q.value.trim().toLowerCase();document.querySelectorAll('.sym').forEach(function(s){s.style.display=!v||s.dataset.name.indexOf(v)>-1?'':'none'})});
    var toast=document.getElementById('toast'),tt;
    document.querySelectorAll('.sym').forEach(function(s){s.addEventListener('click',function(){
      var n=s.dataset.name;function done(){if(!toast)return;toast.querySelector('span:last-child').textContent='Copied '+n;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('on')},1600)}
      try{navigator.clipboard.writeText(n).then(done,done)}catch(e){done()}})});
  });
})();
