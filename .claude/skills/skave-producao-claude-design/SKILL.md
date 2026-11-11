---
name: skave-producao-claude-design
description: "Produz posts estáticos e carrosséis de Mateus Ritter no Claude Design (canvas do tipo Design) a partir do conteúdo aprovado em Conteúdos de posts, usando os templates do Brand Kit no Claude Design. Fluxo principal de produção visual; o Figma é a alternativa. Use quando o usuário escolher o Claude Design para a peça ou lote, ou pedir ajustes ou a exportação de uma peça feita nele; ideias e redação pertencem à skave-ideias-ritter."
---

# Produção de conteúdo — Ritter no Claude Design

Transforme o conteúdo aprovado em artboards editáveis no Claude Design, usando os templates do brand kit, e leve os PNGs aprovados para a pasta da publicação. Esta skill recebe o trabalho da [skill editorial](../skave-ideias-ritter/SKILL.md) e segue o mesmo fluxo da skill de [Figma](../skave-producao-figma/SKILL.md), que continua como alternativa.

## Referências fixas

- **Brand Kit no Claude Design:** <https://claude.ai/artifact/3rjExY97iHpq4SxLJbHzUU> ("Brand Kit — Mateus Ritter"). Contém os fundamentos (paleta, tipografia, componentes, aplicação) e os templates de 1080 × 1350 px na página "Brandkit + Modelos". **Somente leitura nesta skill:** não publique nada nele, salvo pedido expresso do usuário.
- **Brand kit em texto:** [Brand-kit-mateus-ritter.md](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Brand-kit-mateus-ritter.md), para regras de cor, tipografia, composição e CTA.
- **Canvas de produção:** um por mês, chamado `Publicações — <Mês>, <ano>`. O link fica registrado em `_claude-design.md`, na pasta do mês em [Conteúdos de posts](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Conteúdos%20de%20posts/).

### Templates do brand kit

| Template (título no canvas) | Arquivo no brand kit | Uso |
| --- | --- | --- |
| Carrossel · Capa | `project/Capa.dc.html` | Gancho com título (80 px) e subtítulo opcional (32 px) |
| Carrossel · Conteúdo | `project/Conteudo.dc.html` | Desenvolvimento textual, até dois blocos de 44 px |
| Carrossel · Conteúdo com foto | `project/ConteudoFoto.dc.html` | Imagem e comentário de 35 px |
| Carrossel · Fechamento | `project/Fechamento.dc.html` | Conclusão e CTA contextual (padrão escuro) |
| Estático · TWICH | `project/Twich.dc.html` | Texto curto com assinatura |
| Estático · TWICH com foto | `project/TwichFoto.dc.html` | Texto com imagem |
| Imagem de fundo | `project/Imagem.dc.html` | Fotografia de fundo com título |
| Carrossel · Conteúdo com ícone | `project/ConteudoIcone.dc.html` | Ícone em círculo `soft` acima de dois blocos de 44 px |
| Carrossel · Conteúdo com ilustração | `project/ConteudoIlustracao.dc.html` | Ilustração de 690 × 460 acima de dois blocos de 40 px |
| Carrossel · Conteúdo com diagrama | `project/ConteudoDiagrama.dc.html` | Diagrama A (comparação); base para os outros padrões |

A página **Elementos visuais** do brand kit também guarda a biblioteca: ícones em `project/ElementosVisuais.dc.html`, ilustrações em `project/Ilustracoes.dc.html` e padrões de diagrama em `project/Diagramas.dc.html`. Os templates novos usam também a cor `soft` (superfície de ilustração).

Cada template tem o tweak `mode` (`light` ou `dark`) e usa o avatar como asset do brand kit. Antes de oferecer as opções, liste os arquivos do brand kit (`list` com `scope: "files"`) para confirmar que os templates continuam lá; se um nome mudou, use o atual e informe a mudança.

## 1. Receba o conteúdo aprovado

O conteúdo vem do `conteudo.md` de cada publicação, organizado por mês > semana > publicação conforme a [skill editorial](../skave-ideias-ritter/SKILL.md#organização-dos-arquivos). Leia o arquivo de cada peça do pedido: formato e data estão no frontmatter; o texto da arte está em `## Texto publicável` (`### Slide N` nos carrosséis, `### Arte` nos estáticos). Preserve a ordem e os textos aprovados. Legendas, classificações editoriais e notas de produção não entram na arte, salvo pedido expresso.

Produza apenas arquivos com `status: aprovado`. Se o status for `rascunho` mas o usuário aprovar o texto ou pedir explicitamente a produção daquele conteúdo, mude para `aprovado` e siga. Um OK sobre configuração de skills ou outra decisão não é aprovação editorial. Não peça aprovação novamente se ela já está clara. Se o usuário citar uma peça sem caminho, localize-a pela data e pelo título; se houver mais de uma correspondência, pergunte qual. Reels e stories não entram neste fluxo.

## 2. Escolha o template e confirme o modo de cor

**O template não é perguntado: a skill escolhe a partir do conteúdo aprovado** e informa a escolha ao entregar. O usuário pode pedir outro template depois, como ajuste.

- **Carrossel:** `### Slide 1` usa a Capa; o último slide usa o Fechamento. Nos slides do meio, a linha do slide em `## Visual` define o template: `nenhum` → Conteúdo; `ícone` → Conteúdo com ícone; `ilustração` → Conteúdo com ilustração; `diagrama` → Conteúdo com diagrama; `foto` → Conteúdo com foto. Sem a seção `## Visual` (posts antigos), use Conteúdo, ou Conteúdo com foto quando houver imagem indicada para o slide.
- **Ícone na Capa ou no Fechamento:** quando `## Visual` pedir, mantenha o template e acrescente o ícone pequeno (48–56 px, traço `{{txt}}`) acima do título, sem reduzir o texto. Na Capa, nunca use ilustração, diagrama ou foto, mesmo que `## Visual` indique; nesse caso, avise e mantenha só o texto.
- **TWICH:** usa o TWICH textual. Use TWICH com foto apenas quando o `conteudo.md` indicar uma imagem para a peça.
- **Estático:** usa Imagem de fundo quando o `conteudo.md` indicar uma fotografia como base da peça; caso contrário, TWICH textual.
- Se o texto de um slide não couber no template escolhido sem reduzir a fonte, não troque de template por conta própria: proponha o corte ou a divisão do texto para validação.

**Modo de cor:** pergunte apenas o modo, claro ou escuro, quando ainda não tiver sido informado para a peça ou o lote. Nos carrosséis, o Fechamento segue o padrão escuro do brand kit, salvo se o usuário pedir o mesmo modo do restante. Em lotes semanais, faça uma única pergunta de modo para o lote, aceitando exceções por dia ou título. Uma preferência informada como recorrente vale para as semanas seguintes.

**Foto:** use o arquivo indicado em `## Visual`, sem perguntar. As fotos de Ritter ficam no [catálogo do ensaio](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Ensaio%20Fotogáfico%20Ritter/_catalogo.md), em PNG original, sem compressão: envie o arquivo como está como asset do canvas de produção (`publish` com `asset: true`). Nunca converta para JPEG nem comprima. O limite de asset é 15 MB: quando houver uma cópia da foto em `Ensaio Fotogáfico Ritter/claude-design/` (mesmo nome, PNG em 2160 px), envie a cópia; senão, envie o original. Reutilize o `/_blob/<id>` se a mesma foto já tiver sido enviada ao canvas do mês (registre o mapeamento em `_claude-design.md`). Ajuste o enquadramento com `object-fit: cover` e `object-position` para manter olhos e boca inteiros na área de 856 × 508, e aplique os cuidados de recorte do catálogo (pessoas de terceiros e banners fora do quadro). Só pergunte quando `## Visual` pedir foto sem arquivo e nenhuma do catálogo servir; nesse caso, ofereça trocar para o template sem foto. **Nunca gere imagem com o rosto ou o corpo de Ritter.** Imagem gerada só para cenas sem pessoas reconhecíveis, informando que foi gerada. Não deixe placeholder.

Com conteúdo aprovado, template escolhido e modo definido, registre no frontmatter de cada `conteudo.md` `status: em produção`, `producao: Claude Design`, `template` e `modo_cor`, e execute a montagem sem uma nova aprovação.

## 3. Prepare o canvas do mês

1. Leia `_claude-design.md` na pasta do mês. Se ele existir, use o canvas indicado; leia o `project/canvas.json` dele antes de alterar.
2. Se não existir, crie o canvas a partir do tipo Design do Artifact (`type_url` do tipo "Design", `title: "Publicações — <Mês>, <ano>"`, `auto_open: "after_first_write"`). Depois, copie o avatar do brand kit para o novo canvas (`publish` com `asset: true`, `from_url` = brand kit, `asset_ids` = id do avatar, lido do `<img>` dos templates). Grave `_claude-design.md` na pasta do mês com o link do canvas, a data de criação e o mapeamento do avatar (`id no brand kit → /_blob/<id no canvas>`).
3. **Os `/_blob/<id>` do brand kit só funcionam dentro dele.** Em toda cópia de template, troque o endereço do avatar pelo endereço registrado em `_claude-design.md`. Faça o mesmo com qualquer outro asset: copie-o antes e use o novo endereço.
4. Organize o canvas assim:
   - **Uma página por semana**, com o nome da pasta da semana (`16 a 22 de Novembro, 2026`) e id curto (`s16-22`).
   - **Uma linha por publicação**, com uma nota `title1` acima dela no formato da pasta da publicação (`16 de Novembro · Carrossel · <título>`).
   - **Artboards de 1080 × 1350**, 80 px entre slides e 120 px entre linhas (mais o espaço da nota, ao menos 223 px acima de cada linha).
   - **Nome do arquivo:** `d<dia>-<formato>-<palavra-chave>-<NN>.dc.html`, em minúsculas e sem acentos ou espaços (`d16-carrossel-demo-01.dc.html`). **Título do artboard:** `<dia> de <Mês> · <Formato> · <palavra-chave> · <N>/<total>`.
   - Atualize `launch.page` para a semana em produção.

## 4. Monte as peças

Para cada slide ou estático, leia o template correspondente do brand kit e grave uma cópia como novo artboard do canvas de produção:

- Preserve estrutura, fontes (`<link>` do Google Fonts), tamanhos, margens, cabeçalho, assinatura, selo, seta e o bloco `data-dc-script`. Mude o `default` de `mode` para o modo escolhido.
- Substitua somente os textos de exemplo pelo texto aprovado, distribuído entre título, subtítulo e blocos conforme o slide. Remova o subtítulo quando não houver. Escape `&`, `<` e `>` no texto.
- **TWICH textual: mantenha o layout padrão e preencha apenas o texto**, sem ícones, blocos ou destaques fora do padrão.
- **Elementos visuais:** leia o artboard da biblioteca correspondente no brand kit e copie o `<svg>` do item indicado em `## Visual`.
  - **Ícone:** copie os `<path>`, `<rect>` e `<circle>` do ícone para o `<svg>` do template Conteúdo com ícone, no lugar do ícone de exemplo; mantenha `stroke="{{txt}}"` e stroke 1,75.
  - **Ilustração:** substitua o `<svg>` de exemplo do template pelo da biblioteca, mantendo `width="690" height="460"` e o `viewBox="0 0 240 160"`. Troque as cores fixas: `#252F25` → `{{txt}}`, `#667266` → `{{sup}}`, `#E4E4D2` → `{{soft}}`. Nenhum hex da biblioteca pode sobrar na peça.
  - **Diagrama:** use o template Conteúdo com diagrama. Para o padrão A, preencha os dois blocos. Para os padrões B a F, reconstrua na área de 864 px a estrutura do artboard Diagramas, em escala do slide (rótulos Courier Prime Bold 20 px, texto 40–48 px), com as cores por variável (`{{txt}}`, `{{sup}}`, `{{line}}`, `{{soft}}`).
  - O texto do slide continua sendo o aprovado. Se ele não couber com o elemento sem reduzir a fonte, proponha o corte do texto ou a troca para `nenhum` e aguarde validação.
- **Carrosséis:** use um destaque tipográfico leve por composição quando ajudar a leitura. Aplique o sublinhado em um `<span>` do trecho e a cor de apoio (`{{sup}}` no texto principal, ou `{{txt}}` quando o bloco já está na cor de apoio). Em um contraste real, os dois blocos do Conteúdo podem alternar `{{txt}}` e `{{sup}}`.
- Preserve o CTA contextual aprovado. O texto de exemplo do template de Fechamento ("Siga @mateusritter…") nunca entra na peça.
- Se for preciso cortar, reescrever, fundir ou mudar a quantidade de slides, apresente a proposta editorial e aguarde a validação antes de aplicar.

Siga as instruções do tipo Design que o Artifact devolve ao criar ou ler o canvas: `canvas.json` primeiro, depois um artboard por vez. Não renderize, não tire screenshot e não abra o canvas para conferir sem que o usuário peça.

## 5. Entregue para aprovação

Entregue o link do canvas, apontando a página da semana, com o número de peças, os templates e o modo usados. Grave o link em `link_arte` no `conteudo.md` e atualize a linha da publicação em `_semana.md`. O status continua `em produção` até a aprovação da arte. Em seguida, sincronize o [Calendário de conteúdos](https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ) conforme a seção [Sincronize o calendário](../skave-ideias-ritter/SKILL.md#sincronize-o-calendário) da skill editorial. Informe pendências reais, como foto faltando ou texto que estourou o espaço. Ajustes visuais pedidos pelo usuário são feitos nos mesmos artboards, sem duplicá-los; o usuário também pode editar direto no canvas, e nesse caso leia os arquivos de novo antes de mexer.

## 6. Depois da aprovação: PNGs na pasta da publicação

Quando o usuário aprovar a arte de uma publicação:

1. **Baixe a versão atual do canvas.** O usuário pode ter editado os artboards antes de aprovar. Leia com `read` (`paths`) os artboards da publicação e o avatar (`path` = id do asset no canvas), salvando tudo numa pasta de trabalho do scratchpad, e exporte sempre a partir dessa leitura, não da sua cópia local.
2. **Renderize localmente** com [scripts/render_dc.py](scripts/render_dc.py), que transforma cada `.dc.html` em HTML puro (cores do modo no `default` de `mode`, avatar local) e tira o PNG com o Google Chrome em modo headless:

   ```bash
   python3 -I "<skill>/scripts/render_dc.py" "<pasta>/project" "<pasta>/out" '{"<id do avatar no canvas>": "<caminho local do avatar>"}' <artboard-01>.dc.html <artboard-02>.dc.html ...
   ```

   O script gera `01.png`, `02.png`... na ordem dos argumentos, em 1080 × 1350 px. Ele cobre os templates estáticos do brand kit (cores por `mode`); se um artboard tiver outras variáveis `{{...}}`, o script para e aponta o que faltou. Nesse caso, ajuste o script ou peça ao usuário para exportar pelo canvas (Share › Export, PNG).
   - **Por que não exportar pelo navegador:** o navegador embutido abre o canvas sem login no claude.ai, então a exportação pela interface não funciona daqui sem o usuário entrar.
3. **Confira os PNGs** abrindo cada imagem: fontes Instrument Sans e Courier Prime carregadas, avatar visível, nenhum texto cortado, ordem correta. Se a fonte não carregou (aparência de fonte do sistema), rode de novo; o script espera até 8 segundos pelo Google Fonts.
4. Copie para a pasta `arte/` da publicação: `01.png`, `02.png`... nos carrosséis e `arte.png` nos estáticos. Confira se a quantidade e a ordem batem com os slides do `conteudo.md`.
5. Mude o `status` para `arte pronta` e atualize `_semana.md` e `_calendario.md`. Em seguida, sincronize o [Calendário de conteúdos](https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ) conforme a seção [Sincronize o calendário](../skave-ideias-ritter/SKILL.md#sincronize-o-calendário) da skill editorial.

A criação no Claude Design não publica nada nas redes. O canvas é privado: se outra pessoa precisar vê-lo, ela só consegue abrir depois que o usuário compartilhar pelo menu Share.
