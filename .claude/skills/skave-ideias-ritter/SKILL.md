---
name: skave-ideias-ritter
description: "Propõe e desenvolve pautas para o perfil de Mateus Ritter a partir das dores atendidas pelo Posicionamento de Marca da Skave. Use quando o usuário pedir ideias, trouxer pautas ou chamar Planejar a semana. Após a seleção, grava cada publicação em Markdown na pasta Conteúdos de posts, organizada por mês e semana; artes são produzidas apenas quando solicitadas, no Claude Design ou no Figma."
---

# Ideias de conteúdo — Ritter

Gere conteúdos específicos, variados e executáveis para o perfil pessoal de Mateus Ritter, conforme os documentos atuais da estratégia. Cada conteúdo deve partir de uma dor que o produto Posicionamento de Marca resolve e terminar com uma chamada explícita para seguir o perfil. Apresente as pautas no chat para o usuário selecionar. Depois da seleção, escreva o texto de execução completo no arquivo `conteudo.md` de cada publicação, conforme a seção [Organização dos arquivos](#organização-dos-arquivos): falas por take nos reels, textos por slide nos carrosséis e texto final nos demais formatos. Se o usuário pedir expressamente apenas títulos ou pautas, respeite esse recorte até que ele selecione o que deseja desenvolver.

## Fluxo de pautas, arquivos e produção

Esta skill é responsável pelas ideias, pelos textos e pelas revisões editoriais. Comece quando o usuário trouxer pautas ou pedir sugestões no chat; não dependa de um dia da semana nem de acionamento automático. Apresente as pautas com as informações necessárias para a escolha. Se o usuário já indicar exatamente as pautas escolhidas, avance sem uma seleção redundante. A seleção das pautas autoriza a redação e a criação dos arquivos correspondentes; não equivale à aprovação dos textos finais nem autoriza produzir artes.

Para cada pauta selecionada, crie **uma pasta por publicação** com o arquivo `conteudo.md`, conforme a seção [Organização dos arquivos](#organização-dos-arquivos). Antes de gravar, confira a pasta da semana para não duplicar publicações. Não invente uma data se ela não foi definida; combine o período de publicação antes de criar as pastas, porque a data define onde a publicação fica. Grave com `status: rascunho`; não marque a publicação como aprovada nem como arte pronta. Confira os arquivos gravados e peça ao usuário para conferir os textos, informando o caminho da pasta da semana. Se ele pedir ajustes, edite os arquivos correspondentes e peça nova conferência apenas do que mudou. Quando ele aprovar um texto, mude o `status` daquele arquivo para `aprovado`; aprovação de uma peça não aprova o lote inteiro. Em retomadas, atualize os arquivos existentes em vez de duplicá-los.

**Somente quando o usuário pedir uma arte**, pergunte se quer produzir no **Claude Design** ou no **Figma**, salvo se já tiver escolhido o meio para a peça ou lote. Depois da resposta, leia e siga a [skave-producao-claude-design](../skave-producao-claude-design/SKILL.md) ou a [skave-producao-figma](../skave-producao-figma/SKILL.md), respectivamente. Encaminhe apenas publicações com `status: aprovado`, indicando o caminho de cada `conteudo.md`; a skill de produção escolhe o template pelo conteúdo e pergunta apenas o modo de cor. Aproveite escolhas já informadas e não peça a mesma aprovação novamente. Reels e stories não entram automaticamente no fluxo de produção de estáticos e carrosséis.

## Organização dos arquivos

As publicações ficam em [Conteúdos de posts](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Conteúdos%20de%20posts/), dois níveis acima desta skill, organizadas por **mês > semana > publicação**. Use datas por extenso, com o mês em maiúscula, para que qualquer pessoa encontre o post sem decifrar códigos:

```
Conteúdos de posts/
  11 · Novembro, 2026/
    _calendario.md
    17 a 23 de Novembro, 2026/
      _semana.md
      17 de Novembro · Carrossel · Se o cliente só entende seu SaaS na demo/
        conteudo.md
        arte/
      17 de Novembro · Reels · <título>/
        conteudo.md
```

- **Mês:** `<número do mês com dois dígitos> · <Mês>, <ano>`, por exemplo `11 · Novembro, 2026`. O número mantém os meses em ordem no Finder.
- **Semana:** o intervalo do lote, que começa na data do pedido e não necessariamente numa segunda-feira: `17 a 23 de Novembro, 2026`. Se cruzar meses, `28 de Novembro a 4 de Dezembro, 2026`; se cruzar anos, `29 de Dezembro, 2026 a 4 de Janeiro, 2027`. A semana fica dentro do mês da **data inicial**. Pautas avulsas entram na semana que contém a data de publicação; se não houver pasta para ela, crie a semana de sete dias começando na data de publicação mais cedo do pedido.
- **Publicação:** `<dia> de <Mês> · <Formato> · <título>`. Formatos: `Carrossel`, `Reels`, `TWICH`, `Estático`, `Stories`. Use o título selecionado, removendo os caracteres `/ \ : * ? " < > |` e encurtando para cerca de 70 caracteres sem cortar palavras.
- **`arte/`:** criada apenas pela skill de produção, quando houver arte aprovada.
- **`_semana.md`:** grade da semana em tabela (data, formato, título com link relativo para a pasta, funil, pilar, status). Atualize a cada criação ou mudança de status.
- **`_calendario.md`:** lista das semanas do mês com links e totais por status. Atualize junto com `_semana.md`.
- **`_claude-design.md`:** link do canvas de produção do mês no Claude Design e assets copiados. É criado e mantido pela [skave-producao-claude-design](../skave-producao-claude-design/SKILL.md); esta skill não o altera.

### Modelo do `conteudo.md`

```markdown
---
titulo: Se o cliente só entende seu SaaS na demo, a explicação chegou tarde
data: 17 de Novembro, 2026
rede: Instagram
formato: Carrossel
funil: Topo
pilar: <pilar do documento 09>
dor: <dor principal> (documento 04)
status: rascunho
producao:
template:
modo_cor:
link_arte:
---

## Texto publicável

### Slide 1
...

## Visual

- Slide 1: nenhum
- Slide 2: ilustração `comparacao`
- Slide 3: diagrama A · Comparação
- Slide 4: nenhum

## Legenda

## Notas de produção

## Base e dependências
```

- **`status`:** `rascunho` → `aprovado` → `em produção` → `arte pronta` → `publicado`. Esta skill grava `rascunho` e muda para `aprovado` quando o usuário aprovar o texto. As skills de produção mudam para `em produção` e `arte pronta`. Marque `publicado` somente quando o usuário informar.
- **`producao`, `template`, `modo_cor` e `link_arte`:** ficam vazios até a produção; a skill de produção os preenche.
- **Texto publicável:** reels em `### Take 1`, `### Take 2`...; carrosséis em `### Slide 1`, `### Slide 2`...; estáticos e TWICH em `### Arte`; stories em `### Quadro 1`... Notas de produção, imagem sugerida e classificações ficam fora do texto publicável.
- **`## Visual`** (somente carrosséis): uma linha por slide indicando o elemento visual, conforme a seção [Elementos visuais nos carrosséis](#elementos-visuais-nos-carrosséis). Fica fora do texto publicável.
- Inclua `## Legenda` quando a legenda fizer parte do pedido; caso contrário, omita a seção.

### Sincronize o calendário

O [Calendário de conteúdos](https://claude.ai/artifact/T3DQXBTVPCYaDKvso5y7xJ) mostra os posts por dia e status. Ele não lê as pastas: os dados ficam no banco do artifact (coleção `posts`) e são atualizados por esta skill e pelas skills de produção. Os `conteudo.md` continuam sendo a fonte oficial; o calendário é só visualização.

**Sempre que criar, editar, mudar o status ou apagar uma publicação, sincronize no fim da etapa** (uma vez por lote, não a cada arquivo):

1. Rode o script, com saída numa pasta nova do scratchpad:
   ```bash
   python3 -I "<esta skill>/scripts/sync_calendario.py" "<Conteúdos de posts>" "<scratchpad>/sync-<data-hora>"
   ```
   Ele gera um JSON por publicação (`<doc_id>.json`) e o `manifest.json`. O `doc_id` é `<data ISO>-<formato>-<título resumido>`. Se o script listar erros (data fora do padrão `16 de Novembro, 2026`, frontmatter ausente), corrija o `conteudo.md` e rode de novo.
2. Leia a coleção atual com `ArtifactData` `list` (`collection: "posts"`, `query.limit: 1000`) para ter a `version` de cada documento.
3. Envie tudo com `ArtifactData` `batch` (até 50 por chamada): `set` com `file_path` para cada JSON do manifest, com `if_version` quando o documento já existir; `delete` com `if_version` para documentos do banco que não estão mais no manifest (publicação apagada ou com título/data alterados, que muda o `doc_id`).
4. Informe numa linha que o calendário foi atualizado.

O banco só aceita escrita do dono do artifact; quem recebe o link compartilhado apenas visualiza.

## Planejar a semana

Ao receber **“Planejar a semana”** ou um pedido pelos conteúdos da semana, trabalhe no período indicado pelo usuário. Sem período explícito, planeje **os próximos sete dias consecutivos, começando na data da chamada e terminando seis dias depois**, no fuso do usuário. Identifique as sete datas no chat para que o usuário selecione as pautas e ajuste o intervalo antes da criação dos arquivos. A skill só é acionada quando o usuário chamar, sem dia fixo. A grade semanal completa tem **21 conteúdos para Instagram: três por dia, sendo um TWICH textual, um reel e um carrossel em cada uma das sete datas**. Use o [documento 11](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/11-distribuicao-formatos-e-rotina.md) e o [documento 09](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/09-pilares-de-comunicacao.md) como fontes das proporções. Calcule as quantidades inteiras de cada eixo para o lote e distribua as etapas ao longo dos dias. As duas análises de caso previstas na estratégia ocupam vagas de reel ou carrossel, com fonte verificável. Stories ficam fora dos três posts diários.

Consulte as pastas de semana que cobrem o período para identificar o que já existe pelas datas e evitar duplicatas. Entregue a grade no chat com data, título da pauta, formato, etapa do funil e pilar de cada publicação. Confira **sete datas e três formatos em cada data**, mostre o total de 21 conteúdos e indique as pautas que dependem de material ou fonte. Aguarde o usuário selecionar as pautas. Depois, crie a pasta da semana, grave os conteúdos completos **nos `conteudo.md` de cada publicação**, atualize `_semana.md` e `_calendario.md` e peça a conferência, conforme o fluxo acima. Não produza carrosséis ou TWICH automaticamente após criar os arquivos.

## Leia a estratégia atual antes de gerar

A pasta da estratégia está ao lado da pasta de criação de conteúdo, **três níveis acima deste arquivo**. Comece pelo [índice e decisões](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/00-visao-geral-e-decisoes.md), liste os Markdown na raiz dessa pasta e leia integralmente os documentos de estratégia numerados, incluindo novos tópicos que tenham sido adicionados. Faça essa leitura em cada novo pedido de geração ou revisão; não use somente a memória de uma conversa anterior. Se uma leitura vier truncada, complete-a antes de afirmar que conferiu as diretrizes.

**Consulte sempre [Ganchos de conteúdos](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Ganchos-de-conteúdos.md) antes de criar ou revisar as aberturas.** Use os exemplos para inspirar ganchos chamativos, variados e adequados à dor de cada conteúdo; não é necessário reproduzir as frases nem seguir a ordem da lista.

O próprio índice contém a ordem de precedência das definições. Siga os links para documentos comerciais e de produto vigentes quando uma ideia depender de público, qualificação, promessa, método ou entrega. Para preço, prazo e escopo, confira também o documento específico da condição citada. O PDF original é contexto de origem; as decisões reconciliadas nos Markdown orientam o trabalho.

Mantenha a estratégia nos arquivos de origem: esta skill não guarda uma cópia de preços, prazos, percentuais ou escopos. Os links são relativos à localização desta skill, não ao diretório de execução. Se ela for movida, localize o índice no projeto antes de continuar. Se um documento necessário estiver ausente, informe o que faltou e não apresente as ideias dependentes dele como verificadas.

Se houver conflito não resolvido pela precedência documentada, explicite o ponto e prossiga com as ideias que não dependem dele. Não escolha silenciosamente uma regra nem altere a documentação durante a geração. Uma mudança estratégica expressa pelo usuário tem precedência; um pedido de quantidade ou formato não altera automaticamente público, oferta ou promessa.

## Interprete o pedido

Use quantidade, formatos, canal, etapa do funil e restrições informadas. Não pergunte de novo por dados que já estão nos documentos ou na conversa.

Em pedidos avulsos de ideias sem quantidade especificada, gere **12 ideias para Instagram**, distribuídas entre reels com Ritter falando, carrosséis pessoais e textos curtos em arte estática. Essa regra não se aplica ao pedido de conteúdos da semana, cuja grade padrão tem 21 publicações. Stories, análises de caso e outros canais entram conforme o pedido ou a adequação do assunto; análise de caso é uma abordagem que pode usar reels ou carrossel, não um formato que duplique a contagem.

Considere os materiais realmente disponíveis. As fotos reais de Ritter estão no [catálogo do ensaio](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Ensaio%20Fotogáfico%20Ritter/_catalogo.md): quando uma peça pedir foto, escolha ali o arquivo cujo tom e uso combinam com a pauta. Só indique uma foto nova como dependência quando a pauta exigir uma cena que o catálogo não tem (um cliente, um evento específico, um bastidor datado); não presuma que ela existe. Para bastidores, fatos pessoais ou provas de cliente, indique a dependência específica sem inventar uma cena ou um relato.

## Monte o lote

1. Consulte os pilares e proporções em [09](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/09-pilares-de-comunicacao.md) e o funil em [11](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/11-distribuicao-formatos-e-rotina.md). Trate pilar, etapa e formato como dimensões diferentes: um reels não é automaticamente topo, e “Marca que vende” não é automaticamente fundo.
2. Aplique as proporções ao conjunto editorial, com aproximação razoável no lote. Em pedidos pequenos ou focados em um formato, tema ou etapa, respeite o recorte e informe a composição real; não force todos os pilares nem venda em todo pedido para atingir percentuais.
3. Escolha uma dor principal em [04](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/04-dores-e-desejos.md) e use o [banco de temas](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/12-banco-de-temas.md) para encontrar um ângulo. Construa a situação concreta, o raciocínio e a orientação em torno dessa dor. História pessoal, disciplina, networking e IA podem ilustrá-la, mas não sustentam uma pauta isolada sem essa ligação. Evite só reescrever os títulos do banco.
4. Consulte o histórico em [Conteúdos de posts](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Conteúdos%20de%20posts/): leia os `_semana.md` das últimas quatro semanas e abra os `conteudo.md` cujo tema se aproxime da pauta. Considere também ideias trazidas na conversa. Compare premissa, gancho e desenvolvimento, não apenas título. Trocar o formato ou sinônimos não torna uma ideia nova. Reaproveitamento deve ser identificado como variação e ter um ângulo diferente.
5. Use o `status` de cada arquivo para saber o que foi aprovado ou publicado; não presuma além do que está registrado. Se a pasta estiver vazia ou não cobrir o período, evite repetições dentro do lote e não alegue originalidade em relação a conteúdos anteriores.

## Crie o gancho de abertura

Use o repertório do arquivo de ganchos para explorar perguntas, identificação com uma dificuldade, curiosidade, descoberta, contraste entre duas situações reais (nunca o “não é X, é Y” da seção [Vícios de linguagem proibidos](#vícios-de-linguagem-proibidos)), listas e outros caminhos adequados à pauta. Crie uma redação própria, na voz de Ritter, que apresente a situação **e já revele uma tensão, consequência ou descoberta**. O público deve perceber, na própria abertura, por que vale continuar. Uma pergunta que apenas nomeia a dor não basta; não deixe o motivo para seguir só para o segundo slide ou take. Varie a estrutura entre os conteúdos do lote e considere o histórico disponível; não repita a mesma fórmula apenas trocando o assunto.

**Referência de gancho fornecida pelo usuário:** “Seu SaaS só fica fácil de entender quando entra na call?” identifica uma situação, mas não dá motivo suficiente para passar para o lado. Para um carrossel, a direção é: **“Se o seu produto só fica fácil de entender quando você entra na call, você tem um problema.”** Subtítulo possível: **“Não entendeu? Vem comigo.”** A frase principal traz a consequência; a continuação abre espaço para explicar o problema. Use essa lógica para criar ganchos próprios, sem repetir “você tem um problema” ou o subtítulo em todas as peças.

O gancho deve aparecer na primeira fala do primeiro take, no primeiro slide, na primeira linha da arte estática ou no primeiro quadro de stories. Conecte-o à dor principal desde a abertura e entregue no desenvolvimento aquilo que ele desperta ou promete. Evite introduções genéricas antes do gancho.

Os exemplos são referências criativas, não fatos sobre Ritter nem promessas aprovadas. Aberturas sobre ganhos, prazos, experimentos ou histórias pessoais exigem base real; quando ela não existir, adapte a estrutura para uma pergunta ou observação sustentada pelo conteúdo. Não invente uma experiência para encaixar uma frase da lista.

## Escreva como uma conversa real

O texto publicável deve soar como Ritter conversando com um dono de SaaS: próximo, direto e espontâneo, com menos formalidade. Ser sério sobre o negócio não exige uma fala fria, corporativa ou professoral. Essa orientação vale para ganchos, falas, slides, legendas e chamadas finais.

- Use palavras comuns, situações reconhecíveis e frases que alguém diria em voz alta. Quando uma expressão estratégica ficar abstrata, mostre como ela aparece na conversa com o cliente, no site ou na rotina do comercial.
- Preserve o raciocínio entre as frases. Não encurte tanto que o público precise decifrar uma metáfora, nem monte uma sequência de frases de efeito desconectadas. Varie o ritmo e use transições de conversa quando ajudarem.
- Fale diretamente com a pessoa, usando “você”, “seu cliente” e “seu produto” quando couber. Formas como “pra”, “tá” e “a gente” podem aparecer naturalmente, sem virar obrigação ou caricatura. Mantenha a ortografia correta e evite intimidade, gírias ou bordões forçados.
- Troque o vocabulário de apresentação institucional por explicações concretas. Por exemplo, “seu cliente não entendeu por que escolher você” costuma comunicar melhor do que “existe uma lacuna de percepção da diferenciação”. Use termos técnicos apenas quando ajudarem o público a entender a ideia.
- Faça a curiosidade nascer da situação e da consequência para o empresário. Não dependa sempre de suspense, pergunta retórica ou da mesma expressão no fim da frase.

### A linguagem do próprio Ritter

O jeito real de Ritter falar está registrado na [Linguagem do Ritter](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Linguagem-do-Ritter.md): expressões que ele usa, trocas que já fez nos textos e o que ele não fala. **Leia esse arquivo antes de cada geração ou revisão** e escreva a partir dele. Ele vale mais que qualquer referência genérica de tom, porque as pessoas percebem quando o texto não é de quem assina. Use as expressões dele com naturalidade, sem transformar nenhuma em bordão repetido no lote.

O arquivo cresce com o uso. Mantenha-o assim:

- **Correção no chat:** quando Ritter reescrever uma frase, trocar uma palavra ou disser que não falaria de um jeito, registre na seção de trocas o antes e o depois, a data, o post de origem e o **padrão** que a troca revela (não só a frase). Se a correção mostrar uma expressão que ele usa ou evita, registre também na seção correspondente.
- **Edição direta nos arquivos:** antes de gerar ou revisar, confira com `git log -p --since=<data do último registro> -- "VENDAS - Proposta Comercial/Criação de conteúdo/Conteúdos de posts"` se alguém editou o texto publicável de algum `conteudo.md` depois que esta skill o gravou. Compare a versão gravada com a editada e registre os padrões das mudanças feitas por Ritter. Ajustes de status, frontmatter ou produção não contam.
- Atualize a data de "Último registro" no topo do arquivo e inclua o arquivo no commit da etapa.
- Registre padrões, não cópias. Se uma troca contradisser outra anterior, mantenha a mais recente e anote a mudança.

## Vícios de linguagem proibidos

Estes vícios deixam o texto com cara de IA e de copy genérica. Não use em nenhum texto publicável, legenda ou CTA, e corrija quando aparecerem em revisões:

1. **Contraste artificial.** “Não é sobre X, é sobre Y”, “Não é só A, é B” e a versão em duas frases, “Isso não é X. É Y.” Diga diretamente o que é. Em vez de “Isso não é equipe insegura. É equipe sem direção escrita”, prefira “A equipe pergunta tudo pra você porque ninguém escreveu qual é a mensagem”. Comparar duas coisas reais continua permitido (antes e depois, site e proposta, dois concorrentes); o que fica fora é negar uma ideia que ninguém defendeu só para dar peso à outra.
2. **Pergunta retórica de efeito.** “A verdade? Mudou tudo.”, “O segredo? Diversificar.”, “O resultado?” Faça a frase inteira. Pergunta só entra quando é uma pergunta de verdade para o leitor, e nunca em sequência (“Dá pra saber…? Dá pra entender…?”); se precisar de várias, transforme em uma frase só.
3. **Vocabulário robótico e adjetivos vazios.** Não use: crucial, fundamental, essencial, vital, revolucionário, inspirador, mergulhar, navegar, jornada, ecossistema. Evite também sinônimos pomposos do mesmo tipo. Troque por uma palavra comum ou pelo fato concreto.
4. **Transições repetitivas.** Nada de “É importante lembrar que…”, “É fundamental ressaltar…”. Evite empilhar “além disso”, “por outro lado”, “portanto”, “dessa forma”; numa conversa, a ligação vem de “aí”, “e”, “só que”, “então” ou simplesmente da ordem das frases.
5. **Lista onde cabia conversa.** Não transforme uma explicação em itens verticais. Em reels, legendas e TWICH, escreva em frases corridas. Nos carrosséis, os diagramas de passos ou checklist da biblioteca continuam valendo quando o argumento é de fato uma sequência ou uma lista.
6. **Pontuação engessada.** Não use travessão como respiro (prefira vírgula, ponto ou parênteses), nem ponto e vírgula fora de contexto. Depois de dois-pontos, use minúscula, salvo nome próprio ou citação.
7. **“Sem X. Sem Y. Só Z.”** Ex.: “Sem dicas milagrosas. Sem enrolação. Só estratégia.” Não use essa fórmula nem variações com três frases curtas em série.

## Critérios editoriais

- **Público:** a ideia deve interessar a donos ou sócios de SaaS B2B e ter uma ligação explicável com suas decisões, operação ou comunicação. Evite conteúdo genérico de empreendedorismo, tutorial para designers ou pauta feita para atrair outros estrategistas. A ligação pode existir sem escrever “SaaS” no gancho de toda peça.
- **Dor central obrigatória:** o conteúdo inteiro deve desenvolver uma dor documentada e atendida pelo produto, como valor difícil de explicar, comunicação incoerente, comparação por preço ou funcionalidades, marca aquém da operação ou dependência do fundador. A ligação precisa aparecer no texto, não apenas na classificação da pauta ou no CTA. Não atribua ao posicionamento a solução de problemas gerais de gestão, distribuição ou desempenho técnico do software.
- **Voz:** preserve o estrategista direto, provocativo, sério, bem-humorado e parceiro descrito em [01](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/01-posicionamento-pessoal.md) e [08](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/08-narrativa-pessoal.md), com linguagem de conversa e pouca formalidade. A provocação precisa sustentar uma ideia; não depende de ataque pessoal, humilhação ou frase absoluta sem fundamento.
- **Funil:** topo gera identificação com a dor; meio mostra como pensar ou enfrentar essa dor; fundo apresenta provas, responde objeções e pode convidar para uma conversa sobre a oferta vigente. Todas as etapas terminam com uma chamada para seguir o perfil. Um convite comercial no fundo pode aparecer antes desse fechamento.
- **Chamada final obrigatória e contextual:** escreva a frase exata como um convite feito pelo próprio Ritter, em primeira pessoa, continuando o raciocínio do post. Retome a situação, a dor ou o aprendizado específico desenvolvido e diga por que vale acompanhá-lo naquele assunto. Prefira construções naturais como “me acompanha por aqui” ou “me acompanhe por aqui”; o @mateusritter pode identificar o perfil, mas não deve substituir a voz de quem fala. Não use “siga @mateusritter”, que soa como uma recomendação de terceiros, nem frases genéricas como “Me siga para mais conteúdos” ou “Me acompanha para mais dicas”. Acrescentar “sobre SaaS” ou “sobre branding” a uma frase genérica não basta: o motivo para acompanhar precisa estar ligado ao argumento daquela peça. Varie a redação com naturalidade, sem transformar o exemplo em fórmula nem prometer resultados comerciais. Perguntas, pedidos de comentário, salvamento, compartilhamento ou convite para call não substituem a chamada para acompanhar. Coloque-a na última fala do último take, no último slide, no final da arte estática ou no último quadro da sequência de stories. Se produzir legenda, termine também com um convite contextual em primeira pessoa. Referências e notas de produção ficam fora do texto publicável.
- **Oferta:** siga a hierarquia vigente de produto, planos e downsell. Não promova Start como alternativa pública equivalente, workshops ou mentorias como ofertas ativas do perfil, nem planos de continuidade ainda indefinidos.
- **Promessa:** preserve clareza e percepção de valor. Não transforme “parar de ser comparado por preço”, “vale mais” ou metas internas em garantia de venda, faturamento, margem ou conversão.
- **IA:** mantenha a coerência da narrativa: uma pessoa pensa a direção; a ferramenta apoia sua aplicação. Não trate as Skills como substitutas da estratégia nem transforme a tese de momento em prova de que todo SaaS tem o mesmo problema.
- **Temas e exposição:** siga os limites de [08](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/08-narrativa-pessoal.md). Política, religião e vida de famosos ficam fora. Casos e tendências precisam ter relação concreta com negócios, marca ou tecnologia. Referência pessoal e familiar documentada pode inspirar uma pauta, mas o trecho a expor deve respeitar a escolha de Ritter. Não invente episódios, diálogos ou detalhes biográficos.

### Exemplos de CTA ligado ao conteúdo

- **Post sobre depender do fundador para explicar o produto:** “Se você quer que seu time explique o valor do SaaS sem chamar você em toda conversa, me acompanha por aqui. Eu falo sobre como construir uma mensagem que a equipe consiga usar.”
- **Post sobre mensagens diferentes no site e na proposta:** “Se o seu site promete uma coisa e a proposta destaca outra, me acompanha por aqui. Eu falo sobre como colocar esses pontos na mesma direção.”

Esses exemplos mostram a ligação com o assunto; não são fechamentos fixos. Escreva o CTA a partir do conteúdo efetivamente desenvolvido, sem introduzir uma nova dor no encerramento nem transformar toda chamada em pergunta.

## Fatos, notícias e provas

Use a distinção de [13](../../../VENDAS%20-%20Proposta%20Comercial/Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/13-provas-e-medicao.md) entre fatos, hipóteses, resultados observados e causalidade. Não invente depoimentos, métricas, clientes, eventos, autorizações ou resultados. Uma hipótese de dor não é um relato real de cliente. Dados datados de diagnóstico não descrevem automaticamente a situação atual.

Ao usar notícia, caso público ou informação atual, pesquise e confira fonte e data antes de apoiar uma ideia nesse fato. Cite a página que o sustenta, preferindo a fonte original. Separe o ocorrido da interpretação de Ritter e da ação que ele sugeriria. Não atribua decisões internas ou perda de vendas a uma empresa com base apenas em seu site.

Sem verificação disponível, transforme o assunto em uma pauta geral ou indique claramente o fato que precisa ser confirmado. Para resultados e materiais de clientes, registre a fonte e a necessidade de autorização quando ela ainda não estiver comprovada. A ausência de case numérico não impede ideias de fundo sobre objeções, método e entregas verificadas.

## Apresentação das pautas e conteúdo dos arquivos

Abra a seleção no chat com uma frase sobre quantidade e composição. Apresente as pautas numeradas, agrupadas por formato quando facilitar a escolha. Identifique **título, formato, pilar, etapa e dor principal**, com referência ao documento que sustenta essa dor e uma frase que mostre por que a situação importa para quem vende software. **Desenvolva o conteúdo completo apenas para as pautas selecionadas e grave-o no `conteudo.md` de cada publicação.** Se o usuário pedir o texto no chat também, apresente-o ali sem dispensar o arquivo.

### Reels

No `conteudo.md`, escreva o roteiro completo em takes numerados (`### Take 1`, `### Take 2`...), com uma fala curta e exata em cada take. **A primeira frase falada deve capturar a atenção nos primeiros três segundos:** entre direto na situação com tensão, consequência ou surpresa compreensível. A abertura precisa funcionar ao ser ouvida sozinha, sem depender do texto de tela, de uma saudação ou de uma segunda frase para ficar interessante. Os takes seguintes desenvolvem a dor, o raciocínio e uma orientação concreta; a última fala convida a seguir o perfil. Inclua texto de tela e indicação visual apenas quando ajudarem a execução. Não substitua as falas por instruções vagas como “explique a dor” ou “fale sobre o método”. Mantenha transições claras para que Ritter consiga gravar sem completar o argumento por conta própria.

Organize os takes em unidades naturais de fala. A divisão ajuda a gravar, mas a leitura do roteiro inteiro deve soar como uma conversa contínua, sem um corte artificial a cada frase ou tom de texto decorado.

### Carrosséis

No `conteudo.md`, organize os textos finais em **Slide 1, Slide 2...** (`### Slide 1`...), incluindo títulos e corpo quando necessários. **Limite cada carrossel a cinco slides no total, incluindo capa e fechamento.** Use menos slides quando o raciocínio couber. **O Slide 1 precisa dar um motivo concreto para passar para o lado:** o título traz a tensão, consequência ou descoberta, e um subtítulo curto pode convidar à explicação. Não use como gancho apenas uma pergunta diagnóstica que o leitor possa responder mentalmente e encerrar ali. Os slides seguintes cumprem a curiosidade aberta, desenvolvem a dor e o raciocínio, e o último encerra com a chamada para seguir o perfil. Use uma ideia principal por slide e texto que caiba em leitura rápida. Indique o elemento visual de cada slide na seção `## Visual`, conforme a subseção abaixo; uma foto sugerida também entra ali. Para caber no limite, recorte o argumento e elimine repetições; não comprima vários assuntos nem reduza a legibilidade. Se a pauta exigir mais espaço, proponha outro recorte ou outra peça em vez de acrescentar slides.

#### Elementos visuais nos carrosséis

Os slides de carrossel não precisam ser só texto. A página **Elementos visuais** do [Brand Kit no Claude Design](https://claude.ai/artifact/3rjExY97iHpq4SxLJbHzUU) (e a seção 5A do [brand kit em texto](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Brand-kit-mateus-ritter.md)) define 16 ícones, 12 ilustrações em linha e 6 padrões de diagrama. Ao escrever cada carrossel, escolha o visual de cada slide junto com o argumento e registre em `## Visual`:

- **Formato da linha:** `Slide N: nenhum`, `Slide N: ícone <nome>`, `Slide N: ilustração <nome>`, `Slide N: diagrama <letra> · <nome>` ou `Slide N: foto <descrição ou arquivo>`. Use os nomes de referência da biblioteca (`comparacao`, `preco`, `fundador`...).
- **Padrão: slides de desenvolvimento com elemento visual.** Sempre que houver espaço sem reduzir o texto, dê ao slide um ícone, uma ilustração ou um diagrama, para o carrossel ficar dinâmico. Texto puro (`nenhum`) é a exceção: use só quando o texto ocupa a área inteira ou quando nenhum item da biblioteca tem relação com a ideia do slide.
- **Nunca sem contexto.** O elemento precisa ter relação direta com o que o slide diz: nomear a situação (ícone ou ilustração) ou mostrar uma relação do argumento (diagrama). Um elemento genérico só para preencher espaço não entra; nesse caso, prefira outro item da biblioteca ou `nenhum`.
- **Um elemento por slide, no máximo.**
- **Capa:** no máximo um ícone, e só quando ele reforça o gancho. **Nunca ilustração, diagrama ou foto na capa.**
- **Fechamento:** `nenhum` por padrão; no máximo um ícone discreto quando reforçar o CTA.
- **Diagramas reorganizam o texto aprovado** (comparação, antes e depois, passos, checklist, citação, espectro). Escreva o texto do slide já na estrutura do diagrama, com os rótulos (por exemplo `GENÉRICA` e `CLARA`) dentro do próprio texto publicável.
- **Variedade no lote:** alterne entre ícone, ilustração e diagrama ao longo dos slides e dos carrosséis da semana; não repita o mesmo elemento em slides seguidos nem use o mesmo item em todos os carrosséis.
- **Não use** em TWICH, reels nem stories. Nunca crie gráfico com números sem fonte verificável.
- **Foto:** registre o nome exato do arquivo do [catálogo do ensaio](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Ensaio%20Fotogáfico%20Ritter/_catalogo.md) (`Slide N: foto ritter_estudio-escuro_camiseta-verde_mao-no-queixo.png`), escolhido pelo tom do slide e pelo modo de cor previsto. Vale o mesmo para TWICH com foto e estático de Imagem de fundo, numa linha `Arte: foto <arquivo>`. Não repita uma foto usada nas últimas quatro semanas (confira os `## Visual` dos `_semana.md` lidos no histórico) nem a mesma foto em duas peças do lote. Siga os cuidados de recorte da coluna "Cuidados" do catálogo.
- Se nenhum item da biblioteca servir para uma ideia importante, registre `Slide N: nenhum` e, em Notas de produção, sugira o elemento que faltou para o usuário decidir se entra na biblioteca.

### Textos curtos e stories

No `conteudo.md` de arte estática ou TWICH, escreva o texto final em `### Arte` e a chamada para seguir ao final da peça. Em stories, organize o texto ou a fala por quadro e termine a sequência com a chamada para seguir. Quando o pedido incluir legenda, registre o texto completo e o mesmo objetivo de fechamento.

### Base e dependências

Após o texto publicável, indique fontes externas usadas e qualquer material, fato ou autorização que ainda seja necessário. Não preencha lacunas de um case com números inventados: reformule para uma orientação geral ou identifique a dependência concreta.

Ao fim do lote, compartilhe links para a pasta da semana e para cada `conteudo.md` criado e mostre a composição efetiva por etapa e pilar em uma linha ou tabela breve. Peça ao usuário para conferir os textos nos arquivos. Roteiro escrito não comprova que todos os materiais ou autorizações de publicação estejam disponíveis.

## Revise antes de entregar

Faça esta revisão antes de gravar cada `conteudo.md`. A conferência posterior do usuário pode gerar ajustes, mas a primeira versão do arquivo já deve estar completa e coerente.

Confira o lote inteiro e corrija conteúdos que falhem em aderência ao ICP, voz, etapa, variedade, factualidade ou condição comercial. Verifique a quantidade pedida e a adequação real dos formatos. Em cada peça, confirme que a dor documentada orienta todo o desenvolvimento e que a última fala ou texto chama explicitamente para seguir o perfil. Reels precisam de falas completas por take; carrosséis, de textos completos por slide e **no máximo cinco slides, contando capa e fechamento**. Confirme a consulta ao arquivo de ganchos e teste a abertura isoladamente: **o Slide 1 faz querer passar para o lado? A primeira frase do reels prende a atenção em até três segundos?** Se a resposta depender do conteúdo que vem depois para surgir interesse, reescreva o gancho. Confira também se o desenvolvimento cumpre a expectativa criada. Remova ganchos repetidos e variações que só troquem palavras. Se faltar evidência para uma premissa essencial, substitua o conteúdo por outro verificável ou exponha a dependência concreta.

Revise também a especificidade e a voz do CTA: **ele poderia ser usado sem alteração em posts sobre dores diferentes? Soa como Ritter convidando a pessoa a acompanhá-lo, em primeira pessoa?** Se o convite for genérico ou soar como recomendação de terceiros, reescreva para retomar a situação ou o aprendizado daquela peça e dar um motivo concreto para acompanhá-lo. A conexão deve estar no próprio convite, inclusive quando houver legenda.

Faça essa revisão internamente. Na resposta, relate apenas dependências e conflitos que afetem a escolha do usuário. Não declare conformidade de 100% quando alguma fonte necessária não tiver sido lida ou houver uma divergência em aberto.

Faça também uma revisão de oralidade: leia o texto como se Ritter estivesse falando com uma pessoa. Reescreva trechos que soem como relatório, anúncio genérico, sequência de slogans ou frase que exige releitura para fazer sentido. Confira se o gancho, o desenvolvimento e o convite para seguir mantêm a mesma voz próxima. A naturalidade deve vir da clareza e do ritmo, não da adição automática de gírias.

Por último, passe o texto pela lista de [vícios de linguagem proibidos](#vícios-de-linguagem-proibidos) e compare com a [Linguagem do Ritter](../../../VENDAS%20-%20Proposta%20Comercial/Criação%20de%20conteúdo/Linguagem-do-Ritter.md). Além da leitura, faça uma busca textual nos arquivos gravados, por exemplo:

```bash
grep -niE "não é (sobre|só)|não é [^.]*\. é |crucial|fundamental|essencial|vital|revolucion|inspirador|mergulh|naveg|jornada|ecossistema|é importante (lembrar|ressaltar)|além disso|por outro lado|portanto|dessa forma|—|;|\b(sem [^.]+\. ){2}" <conteudo.md>
```

Cada ocorrência no texto publicável precisa ser reescrita ou ter um motivo claro para ficar (por exemplo, “vital” dentro de uma citação). Também confira à mão perguntas retóricas seguidas de resposta curta, que a busca não pega bem.
