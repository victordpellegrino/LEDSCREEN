# -*- coding: utf-8 -*-
"""Card 1080x1920 para WhatsApp (status e chat) — Orlando LED Screens."""
import re, pathlib
qr = re.sub(r"<\?xml[^>]*\?>\s*", "", pathlib.Path("qr.svg").read_text())
qr = re.sub(r'width="\d+mm" height="\d+mm"', 'width="100%" height="100%"', qr)

T = {
 "en": dict(lang="en", eyebrow="Orlando · Kissimmee · Davenport · Windermere",
   h1='LED screens,<br>installed <span>the right way</span>',
   sub="Indoor and outdoor LED screens and video walls — homes, lanais, game rooms and businesses across Central Florida.",
   chips=["Indoor &amp; outdoor","Fine pitch outside too, IP-rated","Any mount: fixed, articulating, mobile","Free assessment"],
   cta="Free assessment · call or text", scan="Scan for photos &amp; quote"),
 "pt": dict(lang="pt-BR", eyebrow="Orlando · Kissimmee · Davenport · Windermere",
   h1='Telas de LED<br>instaladas <span>do jeito certo</span>',
   sub="Telas de LED e video walls, internos e externos — casas, lanai, sala de jogos e comércio na Flórida Central.",
   chips=["Interno e externo","Fine pitch externo, com gabinete IP","Qualquer fixação: fixa, articulada, móvel","Avaliação gratuita"],
   cta="Avaliação gratuita · ligue ou mande mensagem", scan="Aponte a câmera"),
}

TPL = """<!doctype html><html lang="%(lang)s"><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact}
body{width:1080px;height:1920px;overflow:hidden;background:#08090e;color:#f3f5fa;
     font-family:"Liberation Sans",Arial,Helvetica,sans-serif;position:relative}
.photo{position:absolute;inset:0}
.photo img{width:100%%;height:100%%;object-fit:cover;display:block}
.veil{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(5,6,10,.88) 0%%,rgba(5,6,10,.45) 26%%,rgba(5,6,10,.72) 55%%,rgba(5,6,10,.98) 78%%)}
.wrap{position:absolute;inset:0;display:flex;flex-direction:column;padding:56px 64px 56px}
.brand{display:flex;align-items:center;gap:20px;font-size:40px;font-weight:700;letter-spacing:-.01em}
.dot{width:52px;height:52px;border-radius:15px;background:linear-gradient(140deg,#00e0ff,#ff3ea5);box-shadow:0 0 40px -4px rgba(0,224,255,.8)}
.mid{margin-top:auto}
.eyebrow{font-size:24px;letter-spacing:.2em;text-transform:uppercase;color:#00e0ff;font-weight:700;margin-bottom:26px}
h1{font-size:96px;line-height:1.03;letter-spacing:-.025em;font-weight:700;margin-bottom:28px}
h1 span{background:linear-gradient(100deg,#00e0ff,#ff3ea5);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font-size:33px;line-height:1.42;color:#d3d9e6;max-width:880px;margin-bottom:38px}
.chips{display:flex;flex-direction:column;gap:14px;margin-bottom:46px}
.chip{display:flex;align-items:center;gap:16px;font-size:29px;color:#e8ecf5}
.chip i{width:14px;height:14px;border-radius:4px;background:#00e0ff;flex:none;box-shadow:0 0 18px rgba(0,224,255,.9)}
.foot{display:flex;align-items:center;gap:32px;border-top:1px solid rgba(255,255,255,.16);padding-top:32px}
.cta{font-size:24px;color:#98a1b4;letter-spacing:.03em;text-transform:uppercase;margin-bottom:8px;max-width:560px;line-height:1.3}
.tel{font-size:72px;font-weight:700;color:#00e0ff;letter-spacing:-.02em;line-height:1.05}
.site{font-size:30px;color:#d3d9e6;margin-top:8px}
.qrw{margin-left:auto;text-align:center}
.qr{width:200px;height:200px;background:#fff;border-radius:20px;padding:11px}
.qrlab{font-size:20px;color:#98a1b4;width:210px;margin-top:9px;line-height:1.25}
</style></head><body>
<div class="photo"><img src="../img/hero.jpg"></div><div class="veil"></div>
<div class="wrap">
  <div class="brand"><span class="dot"></span>Orlando LED Screens</div>
  <div class="mid">
    <div class="eyebrow">%(eyebrow)s</div>
    <h1>%(h1)s</h1>
    <div class="sub">%(sub)s</div>
    <div class="chips">%(chips)s</div>
    <div class="foot">
      <div><div class="cta">%(cta)s</div><div class="tel">+1 (863) 869-1567</div>
      <div class="site">ledscreen-two.vercel.app</div></div>
      <div class="qrw"><div class="qr">%(qr)s</div><div class="qrlab">%(scan)s</div></div>
    </div>
  </div>
</div></body></html>"""

for code, d in T.items():
    d = dict(d)
    d["chips"] = "".join('<div class="chip"><i></i>%s</div>' % c for c in d["chips"])
    d["qr"] = qr
    pathlib.Path("social-%s.html" % code).write_text(TPL % d, encoding="utf-8")
    print("social-%s.html ok" % code)
