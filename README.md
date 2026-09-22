# LEDSCREEN — landing page

Landing page de venda e instalação de painéis de LED em residências, casas de
temporada e espaços comerciais na região de Orlando / Flórida Central.

Site de **arquivo único**: `index.html` com HTML + CSS + JS puro, sem build e sem
dependência de framework. Abrir o arquivo no navegador já é o site rodando.

## Estrutura

```
index.html      o site inteiro (marcação, estilo, scripts, conteúdo EN/PT)
vercel.json     headers e configuração de deploy
robots.txt      indexação
CLAUDE.md       convenções para quem for mexer no código
```

## O que já está pronto

- Página completa: hero, serviços, por que LED, galeria, pacotes, processo,
  bloco para donos de casa de temporada, FAQ e formulário de orçamento.
- **Bilíngue EN/PT** com botão no topo. O inglês é o texto que está no HTML; o
  português vem do dicionário `I18N.pt` dentro do `<script>`. O idioma escolhido
  fica salvo no `localStorage` e a primeira visita de um navegador em português
  já abre em PT.
- Formulário sem backend: valida os campos e monta uma mensagem pronta no
  WhatsApp (ou no e-mail, no botão alternativo). Nada é enviado sem o usuário
  confirmar.
- Responsivo, tema escuro, respeita `prefers-reduced-motion`, com meta tags de
  SEO, Open Graph e JSON-LD `LocalBusiness`.

## TODO(Victor) — antes de publicar

Tudo que depende de um dado real do negócio está marcado com `TODO(Victor)` no
código. Os itens:

1. **Contato** — no início do `<script>`, objeto `CONTACT`:
   `whatsapp` (só dígitos, com código do país, ex.: `14075551234`),
   `phoneDisplay` e `email`. É o único lugar a editar: telefone, e-mail,
   botão flutuante e links da página saem todos daí.
2. **Marca** — a página usa o nome provisório "Orlando LED" (no header, no
   rodapé e no JSON-LD). Trocar pelo nome definitivo.
3. **Domínio** — substituir `https://TODO-dominio.com/` no `<link rel=canonical>`,
   nas tags Open Graph e no JSON-LD, e gerar a imagem `og.png`.
4. **Preços dos pacotes** — os três pacotes estão como "Sob consulta". Definir
   o "a partir de US$ ..." de cada um (ou manter sob consulta, é uma decisão).
5. **Fotos** — a galeria usa tiles conceituais em CSS. Trocar por fotos reais
   das primeiras instalações (criar `/img` e substituir as `div.tile`).
6. **Garantia** — o texto da FAQ fala em garantia sem prazo. Confirmar o prazo
   de peças e de mão de obra antes de publicar.
7. **Depoimentos** — não existem na página de propósito. Só entram com
   depoimentos reais de clientes.

Nenhuma promessa que precise de licença, seguro ou certificação foi escrita na
página. Se a empresa for licenciada e segurada na Flórida, vale adicionar isso
no hero — é o selo que mais converte nesse mercado.

## Deploy

Projeto estático. Na Vercel, importar o repositório sem framework preset:

- Build command: *(vazio)*
- Output directory: `.`

O `vercel.json` já traz os headers de segurança e o cache do site.

## Desenvolvimento

Não há dependências nem build. Para ver localmente:

```bash
python3 -m http.server 8000
# http://localhost:8000
```
