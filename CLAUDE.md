# Skave · Posicionamento e Produtos

Documentação da Skave (posicionamento, produto, vendas) e operação de conteúdo do perfil pessoal @mateusritter. Usado por mais de uma pessoa, localmente e em sessões do Claude Code na nuvem: tudo o que precisa ser lembrado entre sessões fica neste repositório, não em memória local.

## Mapa das pastas

- `SKAVE - Posicionamento/`: posicionamento da própria Skave.
- `PRODUTO - Posicionamento de marca/`: o produto Posicionamento de Marca.
- `VENDAS - Proposta Comercial/`
  - `Modelos de proposta/`: PDFs das propostas de Brand Launch e Brand Evolution e o resumo `_modelos-de-proposta.md` (estrutura, entregáveis, ticket e inconsistências a corrigir). Fonte do preço vigente.
  - `Prospecção/`: leads do Instagram por rodada (`leads-AAAA-MM-DD.md`) e o índice `_leads.md` com o status de abordagem. Gerados pela skill `skave-prospeccao`, rodada manualmente com o Chrome conectado.
  - `Estratégia de marca pessoal e conteúdo - Ritter/`: estratégia editorial (dores, pilares, narrativa, banco de temas, provas).
  - `Criação de conteúdo/`: operação de conteúdo.
    - `Brand-kit-mateus-ritter.md`: brand kit em texto.
    - `Ganchos-de-conteúdos.md`: repertório de ganchos.
    - `CHANGELOG.md`: registro simples das mudanças nas regras de conteúdo. Acrescente uma entrada a cada mudança de regra.
    - `Modelos de posts/`: exemplos de referência por formato (hoje, `Tweet.md`, `Reels.md` e `Carrossel.md`). Servem para calibrar tamanho e tom; não são textos para publicar nem copiar.
    - `Linguagem-do-Ritter.md`: jeito real de o Ritter falar, atualizado a cada correção dele. Lido antes de escrever qualquer copy; os vícios de linguagem proibidos estão na skill `skave-ideias-ritter`.
    - `Conteúdos de posts/<NN · Mês, ano>/<intervalo da semana>/<dia · Formato · título>/conteudo.md` (+ `arte/`): fonte oficial de cada post. Posts do LinkedIn ficam em `<intervalo da semana>/LinkedIn/`, separados dos do Instagram (filtro de rede no calendário).
    - `Stories/`: base de stories do RSL (`Sequencias-de-stories.md`, com as 10 sequências de venda, e `Ganchos-para-stories.md`, com os 30 ganchos), os PDFs originais e o `Registro-de-stories.md` (sugestões, postagens e métricas). Usada pela skill `skave-stories-do-dia`.
    - `Materiais de captação/`: materiais enviados por palavra-chave no direct (hoje, o teste de posicionamento da palavra FRASE).
    - `Ensaio Fotogáfico Ritter/_catalogo.md`: fotos reais do Ritter, originais em PNG. Nunca comprimir nem converter para JPEG.
- `.claude/skills/`: skills do fluxo de conteúdo, carregadas automaticamente.

## Fluxo de conteúdo

1. **Ideias e textos:** skill `skave-ideias-ritter`. Grava `conteudo.md` com `status: rascunho` e muda para `aprovado` quando o texto é aprovado.
2. **Arte:** `skave-producao-claude-design` (principal) ou `skave-producao-figma` (alternativa). O template é escolhido pela skill; só o modo de cor (claro ou escuro) é perguntado.
3. **Stories do dia:** skill `skave-stories-do-dia`. A cada pedido, sugere a sequência do dia quadro a quadro e registra em `Stories/Registro-de-stories.md`; só grava pasta de post se o texto for aprovado.
4. **Calendário:** cada mudança de status é sincronizada no banco `posts` do calendário.

Status: `rascunho` → `aprovado` → `em produção` → `arte pronta` → `publicado`. Post cuja data já passou conta como publicado (decisão de 16 de Novembro, 2026): o script de sincronização do calendário marca sozinho, no `conteudo.md`, no `_semana.md` e no `_calendario.md`.

## Links fixos (artifacts da conta)

- Calendário de conteúdos (só visualização): https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ
- Brand Kit no Claude Design (somente leitura): https://claude.ai/artifact/3rjExY97iHpq4SxLJbHzUU
- Canvas mensal de produção: link gravado em `_claude-design.md` na pasta de cada mês.

## Regras visuais que valem sempre

- Reels têm dois tipos, mesclados na semana: `Falado` (Ritter fala para a câmera) e `Frase` (vídeo real de fundo, frase na tela e o conteúdo na legenda). O tipo fica em `tipo_reels` no `conteudo.md`.
- Carrosséis mesclam dois tipos: texto corrido e lista (passos, dicas, quantidade), cerca de metade de cada na semana.
- Tweet (antigo TWICH) é só texto e usa sempre o template branco (modo claro), sem perguntar o modo. É curto: de uma a três frases, sem convite para seguir na arte.
- Carrossel no modelo Tweet (decisão de 23 de Novembro, 2026): capa e último slide no template Tweet com foto, com fotos diferentes do catálogo, e os slides do meio no Tweet textual, sem ícone, ilustração ou diagrama. O modo de cor alterna entre os dias, e o fechamento segue o modo do carrossel. Os templates de carrossel de texto (Capa, Conteúdo, Fechamento) deixam de ser usados.
- Fotos vêm do catálogo do ensaio, sem perguntar. Prioridade para as fotos naturais de palestras e eventos; as de estúdio entram de forma pontual, no máximo uma ou duas peças por semana (decisão de 23 de Novembro, 2026). Nunca gerar imagem com o rosto ou o corpo do Ritter.

## Trabalho a dois

- Antes de começar, atualize o repositório (`git pull origin main`). Ao terminar, faça commit e push para o outro ver.
- Tudo vai direto para o `main`, sem branch nem pull request, inclusive em sessões na nuvem que abram em outro branch. Antes do push, `git pull --rebase origin main` para trazer o que o outro enviou.
- Uma pessoa por vez no mesmo post. O `_semana.md` da semana é o lugar de combinar quem está com o quê.
