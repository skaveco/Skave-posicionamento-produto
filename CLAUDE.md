# Skave · Posicionamento e Produtos

Documentação da Skave (posicionamento, produto, vendas) e operação de conteúdo do perfil pessoal @mateusritter. Usado por mais de uma pessoa, localmente e em sessões do Claude Code na nuvem: tudo o que precisa ser lembrado entre sessões fica neste repositório, não em memória local.

## Mapa das pastas

- `SKAVE - Posicionamento/`: posicionamento da própria Skave.
- `PRODUTO - Posicionamento de marca/`: o produto Posicionamento de Marca.
- `VENDAS - Proposta Comercial/`
  - `Modelos de proposta/`: PDFs das propostas de Brand Launch e Brand Evolution e o resumo `_modelos-de-proposta.md` (estrutura, entregáveis, ticket e inconsistências a corrigir). Fonte do preço vigente.
  - `Estratégia de marca pessoal e conteúdo - Ritter/`: estratégia editorial (dores, pilares, narrativa, banco de temas, provas).
  - `Criação de conteúdo/`: operação de conteúdo.
    - `Brand-kit-mateus-ritter.md`: brand kit em texto.
    - `Ganchos-de-conteúdos.md`: repertório de ganchos.
    - `CHANGELOG.md`: registro simples das mudanças nas regras de conteúdo. Acrescente uma entrada a cada mudança de regra.
    - `Modelos de posts/`: exemplos de referência por formato (hoje, `Tweet.md`, `Reels.md` e `Carrossel.md`). Servem para calibrar tamanho e tom; não são textos para publicar nem copiar.
    - `Linguagem-do-Ritter.md`: jeito real de o Ritter falar, atualizado a cada correção dele. Lido antes de escrever qualquer copy; os vícios de linguagem proibidos estão na skill `skave-ideias-ritter`.
    - `Conteúdos de posts/<NN · Mês, ano>/<intervalo da semana>/<dia · Formato · título>/conteudo.md` (+ `arte/`): fonte oficial de cada post.
    - `Ensaio Fotogáfico Ritter/_catalogo.md`: fotos reais do Ritter, originais em PNG. Nunca comprimir nem converter para JPEG.
- `.claude/skills/`: skills do fluxo de conteúdo, carregadas automaticamente.

## Fluxo de conteúdo

1. **Ideias e textos:** skill `skave-ideias-ritter`. Grava `conteudo.md` com `status: rascunho` e muda para `aprovado` quando o texto é aprovado.
2. **Arte:** `skave-producao-claude-design` (principal) ou `skave-producao-figma` (alternativa). O template é escolhido pela skill; só o modo de cor (claro ou escuro) é perguntado.
3. **Calendário:** cada mudança de status é sincronizada no banco `posts` do calendário.

Status: `rascunho` → `aprovado` → `em produção` → `arte pronta` → `publicado`. Post cuja data já passou conta como publicado (decisão de 16 de Novembro, 2026): o script de sincronização do calendário marca sozinho, no `conteudo.md`, no `_semana.md` e no `_calendario.md`.

## Links fixos (artifacts da conta)

- Calendário de conteúdos (só visualização): https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ
- Brand Kit no Claude Design (somente leitura): https://claude.ai/artifact/3rjExY97iHpq4SxLJbHzUU
- Canvas mensal de produção: link gravado em `_claude-design.md` na pasta de cada mês.

## Regras visuais que valem sempre

- Reels têm dois tipos, mesclados na semana: `Falado` (Ritter fala para a câmera) e `Frase` (vídeo real de fundo, frase na tela e o conteúdo na legenda). O tipo fica em `tipo_reels` no `conteudo.md`.
- Carrosséis mesclam dois tipos: texto corrido e lista (passos, dicas, quantidade), cerca de metade de cada na semana.
- Tweet (antigo TWICH) é só texto e usa sempre o template branco (modo claro), sem perguntar o modo. É curto: de uma a três frases, sem convite para seguir na arte.
- Capa de carrossel: no máximo um ícone; nunca ilustração, diagrama ou foto.
- Slides de desenvolvimento levam um elemento visual com contexto sempre que houver espaço.
- Fotos vêm do catálogo do ensaio, sem perguntar. Nunca gerar imagem com o rosto ou o corpo do Ritter.

## Trabalho a dois

- Antes de começar, atualize o repositório (`git pull origin main`). Ao terminar, faça commit e push para o outro ver.
- Tudo vai direto para o `main`, sem branch nem pull request, inclusive em sessões na nuvem que abram em outro branch. Antes do push, `git pull --rebase origin main` para trazer o que o outro enviou.
- Uma pessoa por vez no mesmo post. O `_semana.md` da semana é o lugar de combinar quem está com o quê.
