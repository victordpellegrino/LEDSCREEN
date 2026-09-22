# -*- coding: utf-8 -*-
"""Renderiza o card e corta no tamanho exato (o headless reserva ~87px de barra)."""
import subprocess, sys, os
from PIL import Image

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H, PAD = 1080, 1920, 120   # folga maior que a barra do headless

def shot(url, out):
    tmp = out + ".raw.png"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--virtual-time-budget=9000", "--window-size=%d,%d" % (W, H + PAD),
                    "--screenshot=" + tmp, url],
                   check=True, capture_output=True)
    im = Image.open(tmp).convert("RGB").crop((0, 0, W, H))
    im.save(out, optimize=True)
    os.remove(tmp)
    px = im.getpixel((60, H - 2))
    print("%s -> %dx%d | pixel do rodapé: %s" % (os.path.basename(out), im.width, im.height, px))

for url, out in [(sys.argv[i], sys.argv[i+1]) for i in range(1, len(sys.argv), 2)]:
    shot(url, out)
