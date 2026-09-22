# Material comercial

Flyer de duas páginas para mandar por WhatsApp, e-mail ou imprimir.

| Arquivo | Para quem |
|---|---|
| `orlando-led-screens-en.pdf` | Clientes e parceiros americanos |
| `orlando-led-screens-pt.pdf` | Sua rede brasileira em Orlando |

**Página 1:** foto grande, onde instalamos, três fotos de referência e o que o
orçamento cobre. **Página 2:** os oito tipos de fixação, comparativo
indoor × outdoor com a regra do pitch × 10, e o passo a passo do projeto.
As duas páginas terminam com telefone, site e QR code para o site.

## Como gerar de novo

Editar os textos em `build.py` (dicionário `T`, uma entrada por idioma) e:

```bash
python3 -m http.server 8931          # a partir da raiz do repositório
python3 material/build.py            # gera flyer-en.html e flyer-pt.html
chrome --headless=new --no-pdf-header-footer \
  --print-to-pdf=material/orlando-led-screens-en.pdf \
  http://localhost:8931/material/flyer-en.html
```

O QR (`qr.svg`) aponta para o site; refazer com `qrcode` se o domínio mudar.

Regras do layout: cada `.page` tem 8,5 × 11 in e `overflow:hidden` — se o
conteúdo passar disso, ele é cortado em silêncio. Depois de mexer nos textos,
meça a altura real com `min-height`/`overflow:visible` e confirme que cada
página fecha em 1056 px antes de gerar o PDF.

O tema é escuro, pensado para tela (WhatsApp, e-mail). Para impressão em
quantidade, vale gerar uma versão de fundo claro.
