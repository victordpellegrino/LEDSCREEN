# -*- coding: utf-8 -*-
"""Gera os flyers (EN/PT) em HTML; o PDF sai do Chrome em modo print."""
import re, pathlib

qr = re.sub(r"<\?xml[^>]*\?>\s*", "", pathlib.Path("qr.svg").read_text())
qr = qr.replace('width="31mm" height="31mm"', 'width="100%" height="100%"')

T = {
"en": {
 "lang":"en",
 "tag":"Orlando · Kissimmee · Davenport · Windermere · Winter Park",
 "h1":"LED screens, installed the right way",
 "sub":"Indoor and outdoor LED screens and video walls for homes and businesses across Central Florida. We size the screen for the room, pick the mount for the wall, and install it with the cabling out of sight.",
 "cta_top":"Free assessment",
 "s1":"Where we install",
 "w1t":"Living rooms &amp; home theaters","w1d":"Screen sized to the seating distance, wiring inside the wall.",
 "w2t":"Lanai, patio &amp; pool","w2d":"Weather-rated screens bright enough for Florida daylight.",
 "w3t":"Game rooms","w3d":"The room guests photograph — built to survive the party.",
 "w4t":"Business &amp; signage","w4d":"Storefronts, menu boards, lobby video walls.",
 "s2":"Mounting — the part most installers get wrong",
 "m":[("Fixed / flush","Tight to the wall, cleanest look."),
      ("Tilt","Angles down from above a fireplace or bar."),
      ("Full-motion","Pulls out and swivels for corners and lanais."),
      ("Recessed","Built into the wall, flush with the drywall."),
      ("Floor stand","No holes in the wall — rentals, glass, stone."),
      ("Mobile cart","Rolls room to room and locks in place."),
      ("Ceiling / suspended","Over a bar, a counter or an open space."),
      ("Custom structure","Frames and freestanding steel for video walls.")],
 "s3":"Same resolution outside — different build",
 "in":"Indoor","out":"Outdoor",
 "rows":[("Pixel pitch","P1 – P3, fine pitch","P1, P2 and P3 too, in IP-rated cabinets"),
         ("Brightness","600 – 1,500 nits","5,000 – 10,000+ nits for daylight"),
         ("Protection","Standard cabinet","Sealed cabinet, IP-rated for sun and rain"),
         ("Typical use","Media rooms, lobbies, bars","Lanai, pool, patio, storefronts")],
 "tip":"Outdoor does not mean a coarse, low-resolution screen: we install fine pitch outside too, in sealed IP-rated cabinets. Pitch follows the viewing distance — rule of thumb, pitch in millimetres × 10 = the minimum comfortable distance in feet.",
 "s4":"What a quote covers",
 "inc":["Screen or LED panels, sized and specified","Mount, anchors and any structure or frame",
        "Video processor or controller for video walls","Cabling, conduit and cable concealment",
        "Installation labour and testing","Spare modules on video wall projects",
        "Setup of sources, app and picture settings","Manufacturer warranty, written in the quote"],
 "s5":"How it works",
 "steps":[("Assessment","Send photos of the wall or book a visit. We check surface, power, light and viewing distance."),
          ("Spec &amp; quote","Screen, pitch, mount and cabling in writing, with a closed price before anything is ordered."),
          ("Installation","Anchors rated for your wall, cables concealed, everything tested, space left clean."),
          ("Handover","Sources connected, picture calibrated, remote and app set up, walkthrough done.")],
 "foot_h":"Free assessment. Call or text.",
 "foot_s":"Serving Orlando, Kissimmee, Davenport, Clermont, Windermere, Winter Garden and nearby.",
 "foot_l":"English &amp; Portuguese",
 "scan":"Scan for photos, details and a quote",
 "cap":["Living room &amp; home theater","Lobby video wall","Storefront &amp; menu board"],
},
"pt": {
 "lang":"pt-BR",
 "tag":"Orlando · Kissimmee · Davenport · Windermere · Winter Park",
 "h1":"Telas de LED instaladas do jeito certo",
 "sub":"Telas de LED e video walls, internos e externos, para casas e comércios na Flórida Central. Dimensionamos a tela para o ambiente, escolhemos a fixação certa para a parede e instalamos com a fiação fora da vista.",
 "cta_top":"Avaliação gratuita",
 "s1":"Onde instalamos",
 "w1t":"Sala e home theater","w1d":"Tela dimensionada pela distância do sofá, fiação por dentro da parede.",
 "w2t":"Lanai, varanda e piscina","w2d":"Telas para área externa, com brilho para o sol da Flórida.",
 "w3t":"Sala de jogos","w3d":"O ambiente que rende foto — e aguenta a festa.",
 "w4t":"Comércio e letreiros","w4d":"Fachadas, menu boards, video wall de recepção.",
 "s2":"Fixação — a parte que a maioria erra",
 "m":[("Fixo (rente à parede)","Colado na parede, o visual mais limpo."),
      ("Inclinável","Inclina para baixo quando a tela fica alta."),
      ("Articulado","Sai da parede e gira: cantos, cozinha, lanai."),
      ("Embutido","Dentro da parede, no mesmo nível do drywall."),
      ("Pedestal / chão","Sem furo: imóvel alugado, vidro, pedra."),
      ("Carrinho móvel","Vai de um ambiente a outro e trava."),
      ("Teto / suspenso","Sobre o bar, o balcão ou um vão sem parede."),
      ("Estrutura sob medida","Quadro e estrutura de aço para video wall.")],
 "s3":"Mesma resolução lá fora — construção diferente",
 "in":"Interno","out":"Externo",
 "rows":[("Pixel pitch","P1 – P3, fine pitch","P1, P2 e P3 também, em gabinete IP"),
         ("Brilho","600 – 1.500 nits","5.000 – 10.000+ nits para luz do dia"),
         ("Proteção","Gabinete comum","Gabinete selado, índice IP para sol e chuva"),
         ("Uso típico","Home theater, recepção, bar","Lanai, piscina, varanda, fachada")],
 "tip":"Externo não quer dizer tela grossa: instalamos fine pitch também na área externa, em gabinete selado com índice IP. O pitch segue a distância de visão — regra prática, pitch em milímetros × 10 = a distância mínima confortável, em pés.",
 "s4":"O que o orçamento cobre",
 "inc":["Tela ou módulos de LED, dimensionados e especificados","Suporte, buchas e a estrutura, quando houver",
        "Processador ou controladora, em video wall","Cabeamento, conduíte e embutimento dos cabos",
        "Mão de obra de instalação e testes","Módulos reserva em projetos de video wall",
        "Configuração das fontes, do app e da imagem","Garantia do fabricante, escrita no orçamento"],
 "s5":"Como funciona",
 "steps":[("Avaliação","Mande fotos da parede ou agende uma visita. Conferimos superfície, energia, luz e distância de visão."),
          ("Especificação e orçamento","Tela, pitch, suporte e cabeamento por escrito, com preço fechado antes de qualquer compra."),
          ("Instalação","Buchas adequadas à parede, cabos embutidos, tudo testado e o ambiente entregue limpo."),
          ("Entrega","Fontes conectadas, imagem calibrada, controle e app configurados, demonstração feita.")],
 "foot_h":"Avaliação gratuita. Ligue ou mande mensagem.",
 "foot_s":"Atendemos Orlando, Kissimmee, Davenport, Clermont, Windermere, Winter Garden e região.",
 "foot_l":"Atendimento em português e inglês",
 "scan":"Aponte a câmera para ver fotos e pedir orçamento",
 "cap":["Sala e home theater","Video wall de recepção","Fachada e menu board"],
},
}

CSS = """
@page { size: letter; margin: 0; }
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;background:#08090e;color:#f3f5fa;font-family:"Liberation Sans",Arial,Helvetica,sans-serif;font-size:10.2pt;line-height:1.5}
.page{width:8.5in;height:11in;overflow:hidden;position:relative;display:flex;flex-direction:column;background:#08090e}
.page + .page{page-break-before:always}
.bar{display:flex;align-items:center;gap:10px;padding:16px 42px;border-bottom:1px solid rgba(255,255,255,.1)}
.dot{width:20px;height:20px;border-radius:6px;background:linear-gradient(140deg,#00e0ff,#ff3ea5);flex:none}
.brand{font-weight:700;font-size:12pt;letter-spacing:-.01em}
.bar .right{margin-left:auto;text-align:right;font-size:9pt;color:#98a1b4;line-height:1.35}
.bar .right b{display:block;color:#00e0ff;font-size:11pt;letter-spacing:.01em}
.hero{position:relative;height:2.95in;overflow:hidden}
.hero img{width:100%;height:100%;object-fit:cover;display:block}
.hero .veil{position:absolute;inset:0;background:linear-gradient(to top,rgba(5,6,10,.99) 12%,rgba(5,6,10,.82) 38%,rgba(5,6,10,.30) 70%,rgba(5,6,10,.15))}
.hero .txt{position:absolute;left:42px;right:42px;bottom:26px}
.eyebrow{font-size:7.6pt;letter-spacing:.17em;text-transform:uppercase;color:#00e0ff;font-weight:700;margin-bottom:8px}
h1{font-size:27pt;line-height:1.07;margin:0 0 10px;letter-spacing:-.025em;font-weight:700;max-width:7in}
.sub{color:#c7cede;font-size:10.4pt;max-width:6.1in;line-height:1.45}
.body{padding:18px 42px 0;flex:1}
h2{font-size:12.5pt;margin:0 0 8px;letter-spacing:-.015em}
h2 span{color:#00e0ff}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:13px}
.card{border:1px solid rgba(255,255,255,.11);border-radius:11px;padding:13px;background:#101219}
.card b{display:block;font-size:9.6pt;margin-bottom:5px}
.card span{color:#98a1b4;font-size:8.5pt;line-height:1.4}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:11px}
.shot{border-radius:11px;overflow:hidden;position:relative;height:1.5in;border:1px solid rgba(255,255,255,.11)}
.shot img{width:100%;height:100%;object-fit:cover;display:block}
.shot span{position:absolute;left:0;right:0;bottom:0;padding:16px 11px 8px;font-size:8.2pt;font-weight:700;background:linear-gradient(to top,rgba(5,6,10,.92),transparent)}
.mounts{display:grid;grid-template-columns:1fr 1fr;gap:7px 22px;margin-bottom:18px}
.mount{border-top:1px solid rgba(255,255,255,.12);padding-top:8px}
.mount b{font-size:9.4pt}
.mount span{display:block;color:#98a1b4;font-size:8.4pt;line-height:1.35}
table{width:100%;border-collapse:collapse;margin-bottom:12px;font-size:9.2pt}
th{text-align:left;padding:8px 10px;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;color:#6f7889;border-bottom:1px solid rgba(255,255,255,.14)}
th.c{color:#00e0ff}th.m{color:#ff3ea5}
td{padding:6px 10px;border-bottom:1px solid rgba(255,255,255,.08)}
td:first-child{color:#98a1b4;width:1.5in}
.tip{border:1px solid rgba(0,224,255,.24);background:rgba(0,224,255,.07);border-radius:10px;padding:10px 13px;font-size:8.8pt;color:#c7cede;margin-bottom:18px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4px 22px;margin-bottom:18px}
.two div{font-size:9pt;padding:5px 0 5px 16px;position:relative;border-bottom:1px solid rgba(255,255,255,.07)}
.two div:before{content:"";position:absolute;left:0;top:11px;width:6px;height:6px;border-radius:2px;background:#00e0ff}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
.step{border-top:2px solid rgba(255,255,255,.18);padding-top:9px}
.step i{font-style:normal;font-size:8pt;font-weight:700;color:#00e0ff;letter-spacing:.08em}
.step b{display:block;font-size:9.4pt;margin:3px 0 4px}
.step span{color:#98a1b4;font-size:8.3pt;line-height:1.4}
.foot{margin-top:auto;display:flex;align-items:center;gap:22px;padding:18px 42px;
  background:linear-gradient(100deg,rgba(0,224,255,.12),rgba(139,92,246,.10));border-top:1px solid rgba(255,255,255,.14)}
.foot .big{font-size:15pt;font-weight:700;letter-spacing:-.02em;margin-bottom:3px}
.foot .tel{font-size:18pt;font-weight:700;color:#00e0ff;letter-spacing:-.01em;line-height:1.15}
.foot .site{font-size:10pt;color:#c7cede;margin-top:2px}
.foot .small{font-size:8.2pt;color:#98a1b4;margin-top:6px;max-width:4.2in}
.qr{width:1.02in;height:1.02in;background:#fff;border-radius:10px;padding:5px;flex:none}
.qrlab{font-size:7.2pt;color:#98a1b4;width:1.3in;line-height:1.3;text-align:center;flex:none}
.qrwrap{margin-left:auto;display:flex;flex-direction:column;align-items:center;gap:5px}
"""

def flyer(d):
    four = "".join('<div class="card"><b>%s</b><span>%s</span></div>' % (d["w%dt"%i], d["w%dd"%i]) for i in (1,2,3,4))
    shots = "".join('<div class="shot"><img src="../img/%s"><span>%s</span></div>' % (f, c)
                    for f, c in zip(["living-room.jpg","video-wall.jpg","signage.jpg"], d["cap"]))
    mounts = "".join('<div class="mount"><b>%s</b><span>%s</span></div>' % (a,b) for a,b in d["m"])
    rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in d["rows"])
    inc = "".join("<div>%s</div>" % i for i in d["inc"])
    steps = "".join('<div class="step"><i>0%d</i><b>%s</b><span>%s</span></div>' % (n+1, a, b)
                    for n,(a,b) in enumerate(d["steps"]))
    qrblock = ('<div class="qrwrap"><div class="qr">%s</div><div class="qrlab">%s</div></div>' % (qr, d["scan"]))
    bar = ('<div class="bar"><span class="dot"></span><span class="brand">Orlando LED Screens</span>'
           '<span class="right"><b>+1 (863) 869-1567</b>ledscreen-two.vercel.app</span></div>')
    foot = ('<div class="foot"><div><div class="big">%s</div><div class="tel">+1 (863) 869-1567</div>'
            '<div class="site">ledscreen-two.vercel.app</div><div class="small">%s · %s</div></div>%s</div>'
            % (d["foot_h"], d["foot_s"], d["foot_l"], qrblock))
    return """<!doctype html><html lang="%s"><head><meta charset="utf-8"><style>%s</style></head><body>
<div class="page">
  %s
  <div class="hero"><img src="../img/hero.jpg"><div class="veil"></div>
    <div class="txt"><div class="eyebrow">%s</div><h1>%s</h1><div class="sub">%s</div></div></div>
  <div class="body">
    <h2>%s</h2>
    <div class="four">%s</div>
    <div class="shots">%s</div>
    <h2 style="margin-top:16px">%s</h2>
    <div class="two">%s</div>
  </div>
  %s
</div>
<div class="page">
  %s
  <div class="body" style="padding-top:22px">
    <h2>%s</h2>
    <div class="mounts">%s</div>
    <h2>%s</h2>
    <table><tr><th>&nbsp;</th><th class="c">%s</th><th class="m">%s</th></tr>%s</table>
    <div class="tip">%s</div>
    <h2>%s</h2>
    <div class="steps">%s</div>
  </div>
  %s
</div>
</body></html>""" % (d["lang"], CSS, bar, d["tag"], d["h1"], d["sub"], d["s1"], four, shots,
                     d["s4"], inc, foot,
                     bar, d["s2"], mounts, d["s3"], d["in"], d["out"], rows, d["tip"],
                     d["s5"], steps, foot)

for code, d in T.items():
    pathlib.Path("flyer-%s.html" % code).write_text(flyer(d), encoding="utf-8")
    print("flyer-%s.html" % code, "ok")
