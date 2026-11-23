---
name: skave-prospeccao
description: "Encontra e qualifica no Instagram donos e lideranças de empresas SaaS (B2B ou B2C) ativos na rede, para prospecção ativa do Posicionamento de Marca da Skave. Usa o Chrome logado do usuário (Claude in Chrome), confirma cargo, empresa, atividade recente e necessidade visível de posicionamento, e grava a lista em VENDAS - Proposta Comercial/Prospecção. Use quando o usuário pedir leads, prospecção, lista de empresários ou rodar a prospecção da semana."
---

# Prospecção de leads no Instagram · Skave

Rode **somente quando o usuário pedir**; nunca por iniciativa própria nem como sugestão ao fim de outra tarefa. Entregue **10 leads por rodada**, salvo se o usuário pedir outro número: donos e lideranças de SaaS, B2B ou B2C (decisão de 23 de Novembro, 2026), que estão **ativos no Instagram** e cuja empresa mostra **necessidade visível de posicionamento**. Qualidade vem antes de volume: é melhor entregar 8 leads sólidos e dizer isso do que completar a lista com perfis duvidosos.

A busca roda no Chrome do usuário, já logado no Instagram, pelas ferramentas `mcp__claude-in-chrome__*`. Se elas não estiverem disponíveis, peça ao usuário para rodar `/chrome` ou abrir a sessão com `claude --chrome`, e pare até que ele conecte.

## Antes de começar

1. `git pull origin main`.
2. Leia [_leads.md](../../../VENDAS%20-%20Proposta%20Comercial/Prospecção/_leads.md): quem já está na lista ou foi descartado **não entra de novo**.
3. Leia o [guia de identificação de leads](../../../VENDAS%20-%20Proposta%20Comercial/como-identificar-lead.md) e o [cliente ideal](../../../SKAVE%20-%20Posicionamento/possivel-cliente-ideal.md). Esta skill aplica o guia ao Instagram; onde houver diferença, valem os critérios abaixo.

## Os quatro filtros do perfil

Um perfil só vira lead se passar nos **quatro**. Na dúvida em qualquer um, descarte e siga. Não acrescente filtros além destes: filtrar demais trava a busca.

1. **Seguidores: até 50 mil.** O número não importa abaixo disso. Acima de 50 mil, descarte: esse tipo de empresário raramente responde.
2. **Vínculo de liderança no perfil.** Vale qualquer um destes:
   - cargo explícito na bio ou no nome: CEO, fundador, founder, cofundador, sócio, CTO, CMO, CPO ou outra liderança;
   - frase que mostra que a empresa é dela: "Building @empresa", "criando o @empresa", "fundei a…", "meu SaaS @empresa", "@empresa" ao lado de "fundador" ou "founder" sem o cargo completo;
   - **um ou mais @ de empresa na bio, mesmo sem cargo explícito.** Basta que ao menos um desses @ seja de um SaaS.

   A empresa precisa ser **atual**. Cargo só no LinkedIn ou na imprensa não basta.
3. **Empresa identificável no perfil.** O @ da empresa ou o link do site dela na bio. Se houver só o nome da empresa (sem @ nem link), aceite quando o cargo estiver explícito. Confira que a empresa é de software (SaaS ou app, B2B ou B2C) pela bio do @ ou pelo site; agência, consultoria, software sob encomenda e serviço por mensalidade ficam de fora. Não precisa analisar o feed.
4. **Ativo nos últimos dias.** Story ativo no momento da checagem (anel colorido na foto) **ou** post no feed nos últimos 7 dias. Até 14 dias pode entrar se os outros filtros forem fortes; registre a data. Perfil privado ou parado: descarte.

Depois dos quatro filtros do perfil, confira a empresa:

- **Não precisa estar lançado.** SaaS em pré-lançamento ou lista de espera também entra (status C); registre o momento do produto na ficha.
- **Necessidade visível:** abra o site da empresa e procure ao menos um sinal concreto de clareza, diferenciação, coerência, percepção de valor ou desatualização, como descreve o guia (por exemplo: título genérico, vários públicos ao mesmo tempo, números que não batem, posicionamento antigo misturado ao novo, marca em domínios diferentes). Anote o trecho exato. Se o site estiver muito bem resolvido, a prioridade é baixa; só inclua se faltar volume e diga isso.

## Onde procurar

Comece sempre pelo Instagram, não pela empresa. Use, nesta ordem de rendimento:

1. **Sugestões de perfis parecidos.** No perfil de um lead já confirmado (veja `_leads.md`), clique no botão "Contas semelhantes" ao lado de Seguir e leia a lista com `get_page_text`, sem captura. Funciona melhor a partir de **fundadores e de perfis sobre SaaS** (como @vivendodesaas); a partir de quem trabalha com marketing, as sugestões trazem sobretudo agências e criadores. Perfil privado não mostra o botão.
2. **Seguidos dos perfis da área.** Abra a lista "seguindo" de um perfil sobre SaaS e use a caixa de busca dentro da lista (por exemplo "saas", "ceo", "founder") para filtrar. Também valem os perfis que leads confirmados seguem, e perfis de eventos, comunidades, fundos e podcasts de SaaS (por exemplo RD Summit, Web Summit Rio, Startup Summit, ABSeed). Procure nomes com "CEO", "founder" ou "@empresa" na bio.
3. **Busca por palavra-chave** (`instagram.com/explore/search/keyword/?q=...`): "fundador saas", "ceo saas", "meu saas", "MRR", "B2B", "meu app". Quem posta sobre isso costuma estar ativo.
4. **Busca por nome**, quando você já tem o nome do fundador ou do CMO por outra fonte (imprensa, site da empresa). Confirme pela bio; homônimos são comuns.

Ritmo: no máximo 80 a 100 perfis visitados por sessão, sem pressa artificial e sem rolagem infinita. **Nunca** siga, curta, comente, responda story nem mande mensagem: a abordagem é sempre do usuário.

## Como trabalhar no navegador, gastando pouco

Imagens são o que mais consome tokens e tempo. Siga esta ordem para cada perfil:

1. **Uma captura só do cabeçalho:** `zoom` na região da foto e da bio, com `scale` 0.4 a 0.5. Ela já mostra seguidores, bio, @ da empresa e se há story ativo (anel colorido na foto).
2. Se falhar o filtro 1, 2 ou 3, descarte ali mesmo, sem abrir mais nada.
3. Só se não houver story ativo, confira a data dos posts sem nova captura: um `find` por "posts do feed com data" costuma devolver "Photo by ... on <data>". Se o post do topo não trouxer data, abra-o e leia a data com `javascript_tool` (`Array.from(document.querySelectorAll('time')).map(t=>t.getAttribute('datetime')).slice(0,3)`).
4. Nunca capture a tela inteira quando um `zoom` resolve, e não role o feed.

Outras regras:

- Comece com `tabs_context_mcp` e abra uma aba nova; feche as abas que abriu ao terminar.
- Encadeie vários perfis num mesmo `browser_batch` (navegar, esperar 2 s, zoom no cabeçalho), de 3 a 5 por lote.
- **Análise dos sites no fim, de uma vez:** depois de fechar a lista de perfis aprovados, mande todos os sites num único agente `web-fetch` (em segundo plano, se houver outra coisa a fazer), pedindo só o título, o subtítulo e os sinais de necessidade de cada um. Não leia site por site no navegador.
- Pare quando chegar ao número pedido de leads; não continue buscando "por garantia".
- Se o Instagram pedir login, mostrar bloqueio temporário ou limitar ações, pare e avise o usuário. Não tente contornar.
- Dê um retorno curto ao usuário a cada 5 leads confirmados.

## O que gravar

Ao final, grave `VENDAS - Proposta Comercial/Prospecção/leads-AAAA-MM-DD.md` (data da rodada), no mesmo formato de [leads-2026-11-18.md](../../../VENDAS%20-%20Proposta%20Comercial/Prospecção/leads-2026-11-18.md): tabela de resumo, uma ficha por lead e a lista de descartados com o motivo.

Cada ficha traz:

- **Pessoa e cargo**, como aparecem no perfil.
- **Instagram:** link, número de seguidores e o trecho da bio que comprova cargo e empresa.
- **Atividade:** data do último post e se havia story ativo, com a data da checagem.
- **Empresa e produto:** @ da empresa, site e o que o software faz.
- **Status A, B ou C** pelo guia (com clientes, lançado sem clientes visíveis, ou pré-lançamento). Nesta skill, C também é abordável.
- **Necessidade observada:** os sinais, com o trecho do site.
- **Prioridade:** alta (necessidade clara e perfil muito ativo) ou média.
- **Gancho:** uma observação concreta e uma pergunta para abrir a conversa. Não diagnosticar perda de vendas nem afirmar fatos sobre receita.
- Faturamento: **não confirmado**, salvo evidência pública.

Depois, atualize [_leads.md](../../../VENDAS%20-%20Proposta%20Comercial/Prospecção/_leads.md): acrescente os novos leads com status `encontrado` e os descartados relevantes (para não revisitar). Status de abordagem: `encontrado` → `abordado` → `respondeu` → `call marcada` → `descartado`. Quando o usuário contar que abordou ou recebeu resposta, atualize o status ali.

Por fim, faça commit e push no `main` (`git pull --rebase origin main` antes do push) e entregue no chat a tabela de resumo, o caminho do arquivo e quantos perfis foram descartados por qual filtro.
