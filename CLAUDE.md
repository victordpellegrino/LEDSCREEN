# LEDSCREEN — landing page de telas de LED (Orlando)

Landing page de venda e instalação de telas de LED e video walls, internos e
externos, na Flórida Central. Arquivo único: `index.html` (HTML + CSS + JS puro,
**sem build**, sem framework, sem dependência externa além da fonte do Google
Fonts).

## Regras

- Tudo vive em `index.html`. Não introduzir bundler, framework ou
  `node_modules` sem falar com o Victor.
- **Texto bilíngue**: o inglês é o conteúdo que está na marcação; o português
  fica no dicionário `I18N.pt`. Todo texto visível novo precisa de
  `data-i18n="chave"` (ou `data-i18n-ph` para placeholder) **e** da entrada
  correspondente em `I18N.pt`. Texto criado por JS (as legendas da galeria, por
  exemplo) precisa da chave nos dois dicionários — `EN_EXTRA` e `I18N.pt`.
- **Configuração num lugar só**: o objeto `SETTINGS` no topo do `<script>`
  (marca, WhatsApp, e-mail, endpoint do formulário). Nada de telefone, e-mail ou
  nome da marca escrito direto na marcação — use `data-brand`, `data-phone-link`,
  `data-email-link`, `data-whatsapp`.
- **Nenhum e-mail pessoal no site.** `SETTINGS.email` fica vazio até existir
  e-mail do domínio; com ele vazio, o pedido sai pelo WhatsApp e o botão de
  e-mail some. Não reintroduzir endereço pessoal na marcação.
- **Não inventar número de negócio.** Preço, prazo, garantia, quantidade de
  obras, tempo de mercado: se não veio do Victor, deixar `TODO(Victor)` e um
  texto neutro. Nada de depoimento sem cliente real.
- A empresa ainda não existe: nenhum claim de licença, seguro, certificação ou
  "equipe" além do que for verdade.
- Dados técnicos (pixel pitch, nits, distância de visão) seguem as faixas de
  mercado citadas na seção "Indoor x outdoor". Mudou o número? Confira a fonte
  antes.
- **Fotos**: `img/<nome>.jpg` conforme `img/README.md`. O `onerror` remove a
  imagem e deixa a ilustração SVG aparecer — não quebre esse fallback.
- Acessibilidade: foco visível, `prefers-reduced-motion` respeitado, contraste
  do texto sobre o fundo escuro, e todo campo de formulário com `<label>`.
- Mexeu em SEO? Canonical, Open Graph e JSON-LD apontam para o mesmo domínio.

## Tokens de estilo

Cores, raios e espaçamento estão em `:root`. Usar as variáveis existentes
(`--cy`, `--mg`, `--vi`, `--surface`, `--line`, `--muted`...) em vez de valores
soltos.
