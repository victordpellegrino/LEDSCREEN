# Material comercial

| Arquivo | Formato | Para quem |
|---|---|---|
| `orlando-led-screens-en.pdf` | Flyer 2 páginas, Letter | Clientes e parceiros americanos |
| `orlando-led-screens-pt.pdf` | Flyer 2 páginas, Letter | Rede brasileira em Orlando |
| `whatsapp-led-en.png` | 1080 × 1920 | Status do WhatsApp e envio no chat |
| `whatsapp-led-pt.png` | 1080 × 1920 | Status do WhatsApp e envio no chat |

**Flyer, página 1:** foto grande, onde instalamos, três fotos de referência e o
que o orçamento cobre. **Página 2:** os oito tipos de fixação, comparativo
indoor × outdoor e o passo a passo. As duas páginas terminam com telefone, site
e QR code.

**Card do WhatsApp:** foto da área de piscina, manchete, quatro pontos de
venda, telefone, site e QR. 9:16, que é o formato do status e também aparece
grande no chat.

## Como gerar de novo

```bash
python3 -m http.server 8931          # a partir da raiz do repositório
python3 material/build.py            # flyer: gera flyer-en.html e flyer-pt.html
python3 material/social.py           # card: gera social-en.html e social-pt.html

chrome --headless=new --no-pdf-header-footer \
  --print-to-pdf=material/orlando-led-screens-en.pdf \
  http://localhost:8931/material/flyer-en.html

chrome --headless=new --hide-scrollbars --window-size=1080,1920 \
  --screenshot=material/whatsapp-led-en.png \
  http://localhost:8931/material/social-en.html
```

Textos ficam nos dicionários `T` de cada script, um bloco por idioma. O QR
(`qr.svg`) aponta para o site; refazer com a biblioteca `qrcode` se o domínio
mudar.

Cuidado com altura: cada `.page` do flyer tem 8,5 × 11 in e o card tem 1920 px,
os dois com `overflow:hidden` — conteúdo que passa disso é cortado em silêncio.
Depois de editar, meça com `getBoundingClientRect()` e confirme que o rodapé
fecha em 1056 px (flyer) ou 1920 px (card) antes de exportar.

O tema é escuro, pensado para tela. Para impressão em quantidade, vale gerar
uma versão de fundo claro.
