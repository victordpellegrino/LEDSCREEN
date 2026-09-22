# LEDSCREEN — landing page

Landing page para venda e instalação de **telas de LED e video walls**, internos
e externos, na região de Orlando / Flórida Central. Público: casas, casas de
temporada (vacation rentals) e comércio.

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

- **Hero** com a proposta, dois CTAs (orçamento e WhatsApp) e selos.
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

Quatro blocos, pensados para o orçamento sair quase pronto da primeira mensagem:

1. **O ambiente** — tipo de imóvel, interno/externo coberto/externo aberto, e o
   que vai passar na tela.
2. **Tamanho e fixação** — faixa de tamanho, área de parede em pés, tipo de
   fixação (fixo, inclinável, articulado, embutido, pedestal, carrinho móvel,
   teto, estrutura), superfície da parede (drywall, madeira, bloco, stucco,
   tijolo, vidro) e distância de quem está mais perto — que é o que define o
   pixel pitch.
3. **Escopo** — o que o cliente precisa (fornecer a tela, instalar, suporte,
   tomada nova, esconder cabos, som, conserto, só orientação), prazo e faixa de
   orçamento.
4. **Contato** — nome, telefone, e-mail, cidade/ZIP, meio preferido e observações.

Validação no cliente (nome, telefone e cidade obrigatórios; e-mail validado se
preenchido) e um campo-armadilha invisível contra robôs de spam.

### Para onde o pedido vai

Hoje o botão **"Enviar meu pedido"** abre o aplicativo de e-mail do visitante
com tudo preenchido, endereçado para `victor.d.pellegrino@gmail.com`. O botão
verde manda o mesmo resumo pelo WhatsApp.

Para o pedido **cair direto na caixa de entrada**, sem depender do visitante
apertar enviar, basta um serviço de formulário (Web3Forms, Formspree, Getform e
similares: você cadastra o e-mail, eles devolvem um endpoint). Depois é só
preencher no `SETTINGS` dentro do `<script>`:

```js
formEndpoint: 'https://api.web3forms.com/submit',
formAccessKey: 'sua-chave'
```

Com o endpoint preenchido, o site envia por `fetch`, mostra a confirmação na
própria página e cai de volta no e-mail automaticamente se a chamada falhar.

## Fotos

`img/README.md` lista os nomes exatos dos arquivos. Solte a foto na pasta e ela
substitui a ilustração sozinha — nenhum código precisa mudar. Até lá a página
mostra ilustrações em SVG feitas para o projeto (nada de banco de imagem com
marca d'água).

## TODO(Victor) — antes de divulgar

Tudo que depende de um dado real está marcado com `TODO(Victor)` no código:

1. **Telefone / WhatsApp** — `SETTINGS.whatsapp` (só dígitos, com código do
   país, ex.: `14075551234`) e `SETTINGS.phoneDisplay`. É o único dado que falta
   para a página funcionar de ponta a ponta.
2. **Nome** — está como `Orlando LED Screens`, nome de trabalho descritivo que
   funciona bem em busca e não afirma que existe empresa registrada. Trocar em
   `SETTINGS.brand` (e no `<title>`, nas metatags e no JSON-LD) quando houver.
3. **Domínio** — substituir `https://TODO-dominio.com/` no canonical, nas tags
   Open Graph, no JSON-LD e no `robots.txt`, e gerar a imagem `og.png`.
4. **Fotos** — ver acima.
5. **E-mail** — hoje o pessoal. Vale trocar por um e-mail do domínio quando ele
   existir: aparece melhor e evita spam no pessoal.

Enquanto não há empresa aberta, a página **não** afirma nada que dependa disso:
sem licença, sem seguro, sem tempo de mercado, sem depoimento inventado, sem
número de obras. Os preços também não estão fixados — o texto explica que o
valor sai depois da avaliação, o que é verdade e é como os concorrentes da
região trabalham. Quando abrir a empresa e tiver licença, colocar isso no hero:
é o selo que mais converte nesse mercado.

## Deploy

Projeto estático. Na Vercel, importar o repositório sem framework preset:

- Build command: *(vazio)*
- Output directory: `.`

O `vercel.json` traz os headers de segurança e o cache do HTML.

## Desenvolvimento

Sem dependências e sem build:

```bash
python3 -m http.server 8000
# http://localhost:8000
```
