---
name: skave-producao-figma
description: "Produz posts estáticos e carrosséis de Mateus Ritter no Figma a partir do conteúdo aprovado em Conteúdos de posts. Escolhe o template pelo conteúdo, pergunta só o modo de cor, duplica os modelos e entrega peças editáveis revisadas. Use após a aprovação editorial ou em ajustes de uma peça já produzida; ideias e redação pertencem à skave-ideias-ritter."
---

# Produção de conteúdo — Ritter no Figma

Transforme o conteúdo aprovado em peças editáveis usando os templates atuais da marca. Esta skill recebe o trabalho da [skill editorial](../skave-ideias-ritter/SKILL.md), conduz a escolha do modelo e executa a produção visual.

## 1. Receba o conteúdo aprovado

O conteúdo vem do arquivo `conteudo.md` de cada publicação em [Conteúdos de posts](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Conteúdos%20de%20posts/), organizado por mês > semana > publicação conforme a [skill editorial](../skave-ideias-ritter/SKILL.md#organização-dos-arquivos). Leia o arquivo de cada peça do pedido: o formato e a data estão no frontmatter; o texto da arte está em `## Texto publicável` (`### Slide N` nos carrosséis, `### Arte` nos estáticos). Preserve a ordem e os textos aprovados. Legendas, classificações editoriais e notas de produção não entram na arte, salvo solicitação expressa.

Produza apenas arquivos com `status: aprovado`. Se o status for `rascunho` mas o usuário aprovar o texto ou pedir explicitamente a produção daquele conteúdo, mude para `aprovado` e siga. Um OK sobre configuração de skills ou outra decisão não é aprovação editorial. Não peça aprovação novamente se ela já está clara. Se o usuário citar uma peça sem caminho, localize-a pela data e pelo título nas pastas; se houver mais de uma correspondência, pergunte qual.

Se o usuário ainda estiver revisando o conteúdo, conclua essa revisão com a skill editorial antes de montar a peça. Não transforme aprovação de uma peça em aprovação de todo o lote.

## 2. Consulte a marca, escolha o template e confirme o modo de cor

Leia o [brand kit atual](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Brand-kit-mateus-ritter.md). Ele contém o arquivo de destino, a biblioteca de templates, os links dos nós, as fontes, os modos de cor e as regras visuais. Consulte também o Figma para confirmar que os modelos indicados continuam disponíveis. Não mantenha uma cópia da paleta ou dos IDs nesta skill.

**O template não é perguntado: a skill escolhe a partir do conteúdo aprovado** e informa a escolha ao entregar. O usuário pode pedir outro template depois, como ajuste.

- **Carrossel:** `### Slide 1` usa a Capa; o último slide usa o Fechamento; os slides do meio usam Conteúdo. Use Conteúdo com foto quando `## Visual` indicar `foto` para o slide. Quando indicar ícone, ilustração ou diagrama, use o modelo Conteúdo e acrescente o elemento conforme as regras de elementos visuais abaixo.
- **Tweet** (formato que antes se chamava TWICH; no Figma os modelos continuam com o nome TWICH): usa o Tweet textual, **sempre no modo claro (template branco)**, sem perguntar o modo. Use Tweet com foto apenas quando o `conteudo.md` indicar uma imagem para a peça.
- **Estático:** usa IMAGEM quando o `conteudo.md` indicar uma fotografia como base da peça; caso contrário, Tweet textual.
- Se o texto de um slide não couber no template escolhido sem reduzir a fonte, não troque de template por conta própria: proponha o corte ou a divisão do texto para validação.

**Modo de cor:** pergunte apenas o modo, claro ou escuro, quando ainda não tiver sido informado para a peça ou o lote. Nos carrosséis, o Fechamento segue o padrão escuro do brand kit, salvo se o usuário pedir o mesmo modo do restante. Em lotes semanais, faça uma única pergunta de modo para o lote, aceitando exceções por dia ou título. Uma preferência informada como recorrente vale para as semanas seguintes.

**Foto:** use o arquivo indicado em `## Visual`, sem perguntar. As fotos de Ritter ficam no [catálogo do ensaio](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Ensaio%20Fotogáfico%20Ritter/_catalogo.md), em PNG original, sem compressão; nunca converta para JPEG nem comprima. Só pergunte quando `## Visual` pedir foto sem arquivo e nenhuma do catálogo servir; nesse caso, ofereça trocar para o template sem foto. Não deixe placeholder nem apresente imagem gerada como registro real.

Ao entregar, cite os templates usados pelos nomes e links do brand kit.

Com conteúdo aprovado, template escolhido e modo de cor definido, registre no frontmatter de cada `conteudo.md` `status: em produção`, `producao`, `template` e `modo_cor`, e execute a montagem. Não acrescente uma etapa de “posso criar?” ou uma nova aprovação do mesmo texto.

## 3. Prepare a composição

**Tweet textual, sempre no modo claro (template branco): mantenha o layout padrão e preencha apenas o campo de texto do template.** Preserve a tipografia, a hierarquia, as cores e a assinatura originais. O conteúdo é somente texto, sem adicionar ícones, gráficos, ilustrações, blocos visuais ou destaques tipográficos fora do padrão. Esta regra se aplica ao modelo `Tweet` textual. Os carrosséis seguem as orientações de composição flexível abaixo.

- Para cada slide, associe o texto aprovado à função visual: capa, conteúdo, conteúdo com foto ou fechamento. Não use a capa em todos os slides se a biblioteca fornecer modelos específicos.
- **Quando o modelo tiver foto, use o arquivo do catálogo indicado em `## Visual`.** Envie o PNG original como está (`upload_assets`) e aplique-o como preenchimento da área de imagem com modo de recorte (`FILL`), ajustando a posição para manter olhos e boca inteiros e para tirar do quadro pessoas de terceiros ou banners, conforme a coluna "Cuidados" do catálogo. Não substitua o arquivo indicado por outra imagem.
- **Nunca gere imagem com o rosto ou o corpo de Ritter.** Geração com `generate_image` só vale para cenas sem pessoas reconhecíveis (um objeto, um ambiente), quando o usuário aceitar e nenhuma foto do catálogo servir. Não apresente a imagem gerada como registro real de cliente, produto ou case, não deixe placeholder quadriculado e informe na entrega que a imagem foi gerada com Figma AI e consumiu créditos da conta.
- Distribua o texto aprovado em títulos, subtítulos e blocos conforme a composição. Ajuste quebras de linha e hierarquia sem mudar o sentido nem omitir trechos.
- Preserve o CTA contextual aprovado. Uma seta, assinatura ou frase genérica para seguir não substitui o convite ligado ao conteúdo. Quando `## Notas de produção` indicar o convite para seguir na legenda, o Fechamento usa só o texto aprovado do último slide, sem acrescentar CTA.
- Se for necessário cortar, reescrever, fundir ou mudar a ordem ou quantidade de slides para obter boa leitura, apresente a proposta editorial concreta para validação antes de aplicá-la.

**Nos modelos que permitem variação, use o template escolhido como base e adapte a área de conteúdo quando a composição ajudar a entender a mensagem.** Leia a função de cada slide ou post. Uma comparação pode ganhar dois blocos empilhados, uma sequência pode virar passos numerados e uma citação pode ganhar destaque tipográfico. Use o arranjo mais simples que torne a relação entre as ideias evidente na leitura pelo celular.

**Use um destaque tipográfico leve para guiar a leitura ao trecho que carrega a ideia.** Na capa e nos demais slides ou posts, selecione uma palavra ou expressão curta quando ela ajudar a localizar a ideia central, o contraste ou a ação. Aplique o sublinhado no próprio texto editável do Figma e vincule a cor do trecho à variável de texto de apoio do brand kit (`Color/Divider/Text/Support`), respeitando o modo de cor. Use um destaque por composição como padrão e confira o contraste e a leitura no celular. Se a hierarquia do layout já apontar para o trecho, o destaque é dispensável. A [capa do carrossel de SaaS](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=26-222) é a referência: “Completo e inovador” recebe a cor de apoio e o sublinhado.

Na prévia aprovada do CRM, “Organize sua operação” ficou em um bloco menor, com cor de apoio. A mensagem concreta sobre vendas pelo WhatsApp ganhou mais espaço e destaque, com um divisor discreto entre os blocos. Use essa lógica quando houver um contraste real no conteúdo.

**Elementos visuais** (ícones, ilustrações em linha e diagramas) seguem a página Elementos visuais do [Brand Kit no Claude Design](https://claude.ai/artifact/3rjExY97iHpq4SxLJbHzUU) e a seção 5A do [brand kit em texto](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Brand-kit-mateus-ritter.md). Use apenas o elemento indicado em `## Visual` para cada slide. Leia o `<svg>` do item no brand kit (`project/ElementosVisuais.dc.html`, `project/Ilustracoes.dc.html` ou `project/Diagramas.dc.html`) e importe-o no Figma como vetor (`createNodeFromSvg`), trocando as cores fixas pelas variáveis do modo escolhido: `#252F25` → `Color/Divider/Text/Primary`, `#667266` → `Color/Divider/Text/Support`, `#E4E4D2` → superfície de ilustração (`#E4E4D2` Light, `#3A4A3A` Dark). Posicione o elemento como nos templates Conteúdo com ícone, com ilustração ou com diagrama do Claude Design. Não use ícones de outras bibliotecas, como Phosphor, para não misturar estilos de traço.

Na cópia de produção, você pode redistribuir blocos, ajustar tamanhos dentro da hierarquia da marca e usar rótulos que identifiquem o que já está no texto, como “GENÉRICA” e “CONCRETA”. Faça esses ajustes visuais durante a montagem, sem nova aprovação, preservando o template base, o modo de cor, as fontes, as variáveis e os componentes da marca. Se a composição pedir outro template ou modo de cor, confirme essa escolha com o usuário.

## 4. Produza no Figma

Use o plugin oficial do Figma. Antes de executar código, carregue as skills disponíveis **figma:figma-use** e **figma:figma-generate-design** e siga seus contratos de sessão, fontes, escrita e verificação. Esta skill fornece o fluxo de conteúdo e não substitui a documentação técnica dessas ferramentas.

1. Abra uma sessão de trabalho no arquivo indicado no brand kit, ou reutilize a sessão da mesma produção, e inspecione os nós escolhidos. Se o usuário indicar outro destino, respeite-o.
2. Duplique os templates escolhidos em uma área livre do arquivo, agrupados e nomeados pelo tema. Numere os frames na ordem do carrossel. Preserve os modelos originais.
3. Mantenha dimensões, fontes, componentes, vínculos com variáveis e modo de cor. Reutilize o Badge e os assets do modelo. No Tweet textual, mantenha a estrutura padrão. Nos modelos flexíveis, adapte os blocos de conteúdo na cópia conforme a composição definida.
4. Carregue as fontes utilizadas antes de editar texto. Substitua os placeholders e remova subtítulos opcionais sem uso. Ajuste a posição dos blocos que crescerem para preservar margens, respiro e distância do rodapé.
5. Quando houver foto (do catálogo ou gerada), aplique-a à área de imagem do slide ou post correspondente e confira o recorte no layout final. Preserve camadas de texto e imagens editáveis. Não entregue um print da composição como substituto das camadas.
6. Retorne e mantenha os IDs criados. Em caso de erro ou retomada, inspecione o que já existe e continue a produção correspondente, evitando duplicar a peça inteira novamente.

Se o modelo não estiver mais acessível, procure sua versão atual no arquivo ou no brand kit. Se não for possível identificá-lo com segurança, peça a referência atual; não substitua silenciosamente a escolha do usuário por outro layout.

## 5. Confira e entregue

Confira o conteúdo da arte contra a versão aprovada: todos os slides, ordem correta, textos completos, CTA contextual e ausência de placeholders. Verifique fontes, modo de cor, imagens e vínculo das instâncias. Observe a composição renderizada na escala de celular para conferir se a hierarquia revela a ideia principal e encontrar cortes, sobreposições, texto pequeno, quebras ruins e contraste insuficiente. Corrija problemas visuais e confira novamente apenas os resultados afetados.

Entregue um link direto para a seção ou peça produzida, com o número de slides e o modelo utilizado, e grave-o em `link_arte` no `conteudo.md`. Informe qualquer pendência real que impeça considerar a peça pronta. A criação no Figma não publica o conteúdo nas redes. Em seguida, sincronize o [Calendário de conteúdos](https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ) conforme a seção [Sincronize o calendário](../skave-ideias-ritter/SKILL.md#sincronize-o-calendário) da skill editorial.

**Depois que o usuário aprovar a arte**, exporte cada frame em PNG de 1080 × 1350 px, na ordem do conteúdo, para a pasta `arte/` da publicação (`01.png`, `02.png`...; estático em `arte.png`). Se a exportação não for possível pelas ferramentas disponíveis, peça ao usuário para exportar e salvar os arquivos nessa pasta. Com os PNGs na pasta, mude o `status` para `arte pronta` e atualize a linha da publicação em `_semana.md`. Em seguida, sincronize o [Calendário de conteúdos](https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ) conforme a seção [Sincronize o calendário](../skave-ideias-ritter/SKILL.md#sincronize-o-calendário) da skill editorial.

Para ajustes posteriores, preserve o modelo e o conteúdo já aprovados, alterando o que o usuário solicitou. Volte à escolha de template apenas se ele pedir outra direção visual ou se o modelo escolhido deixar de atender à mudança solicitada.
