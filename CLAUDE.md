# LEDSCREEN — landing page de painéis de LED (Orlando)

Landing page de venda e instalação de painéis de LED na Flórida Central.
Arquivo único: `index.html` (HTML + CSS + JS puro, **sem build**, sem framework,
sem dependência de CDN além da fonte do Google Fonts).

## Regras

- Tudo vive em `index.html`. Não introduzir bundler, framework ou `node_modules`
  sem falar com o Victor.
- **Texto bilíngue**: o inglês é o conteúdo que está na marcação; o português
  fica no dicionário `I18N.pt`. Todo texto visível novo precisa de
  `data-i18n="chave"` (ou `data-i18n-ph` para placeholder) **e** da entrada
  correspondente em `I18N.pt`. Texto sem chave não traduz.
- **Contato num lugar só**: o objeto `CONTACT` no topo do `<script>`. Nada de
  telefone, WhatsApp ou e-mail escrito direto na marcação.
- **Não inventar número de negócio.** Preço, prazo, garantia, quantidade de
  obras, tempo de mercado: se não veio do Victor, deixar `TODO(Victor)` e um
  texto neutro. O mesmo vale para depoimento — só com cliente real.
- Sem claim de licença, seguro ou certificação enquanto o Victor não confirmar.
- Acessibilidade: manter foco visível, `prefers-reduced-motion` respeitado e
  contraste do texto sobre o fundo escuro.
- Mexeu em SEO? Canonical, Open Graph e JSON-LD apontam para o mesmo domínio.

## Tokens de estilo

Cores, raios e espaçamento estão em `:root`. Usar as variáveis existentes
(`--cy`, `--mg`, `--vi`, `--surface`, `--line`, `--muted`...) em vez de valores
soltos.
