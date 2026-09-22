# LEDSCREEN — landing page

Landing page para venda e instalação de **telas de LED e video walls**, internos
e externos, na região de Orlando / Flórida Central. Público: casas, casas de
temporada (vacation rentals) e comércio.

**No ar:** https://ledscreen-two.vercel.app
(projeto `ledscreen` na Vercel, time ArtudTech, deploy automático a cada push
na `main`.)

Site de **arquivo único**: `index.html` com HTML + CSS + JS puro, sem build e sem
framework. Abrir o arquivo no navegador já é o site rodando.

```
index.html      o site inteiro (marcação, estilo, scripts, conteúdo EN/PT)
img/            fotos reais (ver img/README.md) — enquanto não existem, entram ilustrações
vercel.json     headers e configuração de deploy
robots.txt      indexação
CLAUDE.md       convenções para quem for mexer no código
```

## O que a página tem

- **Hero** com a proposta, dois CTAs (orçamento e ligação) e selos.
- **Onde instalamos**: casas e home theater, lanai/piscina, casas de temporada e
  salas de jogos, comércio e letreiros.
- **Fixação** — a seção que explica os 8 tipos de suporte: fixo, inclinável,
  articulado, carrinho móvel, pedestal, teto/suspenso, embutido e estrutura de
  video wall.
- **Indoor x outdoor**: comparativo de pixel pitch, brilho (nits), distância de
  visão e vedação, com a regra prática do pitch × 10 = distância mínima em pés.
- **Galeria** com slots de foto (ver abaixo).
- **Processo** em 4 passos e **o que o orçamento cobre** (8 itens).
- **FAQ** com as 7 perguntas que aparecem em quase todo projeto.
- **Formulário de orçamento** completo (detalhes abaixo).
- Bilíngue **EN/PT** com botão no topo; o idioma fica salvo no `localStorage` e
  navegador em português já abre em PT.

## O formulário

Curto de propósito — formulário longo espanta cliente. Nove campos, todos numa
tela:

- **Nome\***, **telefone celular\*** (é por onde respondemos), e-mail
  (opcional), **cidade ou ZIP\***
- Tipo de imóvel e **interno / externo coberto / externo aberto**
- **Tipo de fixação** (fixo, inclinável, articulado, embutido, pedestal,
  carrinho móvel, teto, estrutura — com "não sei, me recomende" como padrão)
- Área aproximada da parede em pés (opcional)
- Campo livre de observações

Pitch, tamanho exato, superfície da parede, cabeamento e escopo ficam para a
visita — o texto ao lado do formulário diz isso ao cliente.

Validação no cliente (nome, telefone e cidade obrigatórios; e-mail validado se
preenchido) e um campo-armadilha invisível contra robôs de spam.

### Para onde o pedido vai

O formulário é enviado **pelo próprio site** e chega no e-mail, pelo
**FormSubmit.co** — o mesmo serviço do site da Bravo. O visitante aperta
"Enviar meu pedido", vê a confirmação na própria página e o pedido cai na
caixa de entrada com os campos numa tabela.

- Destino: `SETTINGS.formTarget`.
- Envio por `fetch` no endpoint `/ajax/`; se o `fetch` falhar (rede, bloqueio
  de script), o navegador faz o POST normal do formulário como rede de
  segurança — a mesma trava do site da Bravo.
- Assunto do e-mail já vem pronto: `NOVO PEDIDO — Orlando LED Screens: <nome>
  (<cidade>)`. O e-mail do cliente entra como `_replyto`, então é só responder.
- Os valores vão **sempre em inglês** no e-mail, mesmo quando o visitante
  navega o site em português.
- Campo-armadilha `_honey` contra robôs e `_captcha=false` para não travar o
  cliente com desafio.

Duas coisas a fazer no FormSubmit:

1. **Primeiro envio** dispara um e-mail de ativação do FormSubmit — clicar no
   link uma vez e pronto (o endereço já foi ativado no site da Bravo, mas a
   confirmação pode vir de novo para este domínio).
2. **Esconder o e-mail do código**: o e-mail de ativação traz um alias
   (`formsubmit.co/el/xxxxx`). Colar esse alias em `SETTINGS.formTarget` no
   lugar do endereço — o site passa a funcionar sem o Gmail aparecer nem no
   código-fonte.

O botão "Ou ligar agora" disca **+1 (863) 869-1567**. Não há WhatsApp: nos
Estados Unidos o padrão é ligação e SMS.

## Fotos

Já estão no ar: `hero.jpg` (área de piscina), `living-room.jpg`,
`video-wall.jpg`, `signage.jpg` e `mount-detail.jpg` — imagens de referência dos
tipos de instalação, apresentadas como referência, não como obra entregue. Os
nomes e as medidas estão em `img/README.md`; trocar uma foto é só substituir o
arquivo de mesmo nome.

Se algum arquivo não existir, a ilustração em SVG correspondente aparece no
lugar e nada quebra.

## TODO(Victor) — antes de divulgar

Tudo que depende de um dado real está marcado com `TODO(Victor)` no código:

1. **Nome** — está como `Orlando LED Screens`, nome de trabalho descritivo que
   funciona bem em busca e não afirma que existe empresa registrada. Trocar em
   `SETTINGS.brand` (e no `<title>`, nas metatags e no JSON-LD) quando houver.
2. **Domínio** — substituir `https://TODO-dominio.com/` no canonical, nas tags
   Open Graph, no JSON-LD e no `robots.txt`, e gerar a imagem `og.png`.
3. **E-mail do domínio** — quando existir, preencher `SETTINGS.email`.
4. **Fotos de obra** — as atuais são de referência. Assim que houver projeto
   entregue, trocar pelas fotos reais (mesmos nomes) e ajustar a legenda.

O telefone já está configurado: **+1 (863) 869-1567**, em `SETTINGS.phone` e
`SETTINGS.phoneDisplay`. É o número de ligação e de SMS.

Enquanto não há empresa aberta, a página **não** afirma nada que dependa disso:
sem licença, sem seguro, sem tempo de mercado, sem depoimento inventado, sem
número de obras. Os preços também não estão fixados — o texto explica que o
valor sai depois da avaliação, o que é verdade e é como os concorrentes da
região trabalham. Quando abrir a empresa e tiver licença, colocar isso no hero:
é o selo que mais converte nesse mercado.

## Deploy

Projeto estático, já publicado na Vercel: projeto `ledscreen` (time ArtudTech),
ligado a este repositório. Todo push na `main` publica sozinho — sem build,
sem framework preset.

URLs: `ledscreen-two.vercel.app` e `ledscreen-artud-tech.vercel.app`.
Domínio próprio: adicionar em Project → Settings → Domains e atualizar o
canonical, as tags Open Graph, o JSON-LD e o `robots.txt`.

O `vercel.json` traz os headers de segurança e o cache do HTML.

## Desenvolvimento

Sem dependências e sem build:

```bash
python3 -m http.server 8000
# http://localhost:8000
```
