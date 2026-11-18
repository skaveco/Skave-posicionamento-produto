---
name: skave-prospeccao
description: "Encontra e qualifica no Instagram donos e lideranças de empresas SaaS B2B ativos na rede, para prospecção ativa do Posicionamento de Marca da Skave. Usa o Chrome logado do usuário (Claude in Chrome), confirma cargo, empresa, atividade recente e necessidade visível de posicionamento, e grava a lista em VENDAS - Proposta Comercial/Prospecção. Use quando o usuário pedir leads, prospecção, lista de empresários ou rodar a prospecção da semana."
---

# Prospecção de leads no Instagram · Skave

Entregue **15 leads por rodada** (ou o número que o usuário pedir): donos e lideranças de SaaS B2B que estão **ativos no Instagram** e cuja empresa mostra **necessidade visível de posicionamento**. Qualidade vem antes de volume: é melhor entregar 12 leads sólidos e dizer isso do que completar a lista com perfis duvidosos.

A busca roda no Chrome do usuário, já logado no Instagram, pelas ferramentas `mcp__claude-in-chrome__*`. Se elas não estiverem disponíveis, peça ao usuário para rodar `/chrome` ou abrir a sessão com `claude --chrome`, e pare até que ele conecte.

## Antes de começar

1. `git pull origin main`.
2. Leia [_leads.md](../../../VENDAS%20-%20Proposta%20Comercial/Prospecção/_leads.md): quem já está na lista ou foi descartado **não entra de novo**.
3. Leia o [guia de identificação de leads](../../../VENDAS%20-%20Proposta%20Comercial/como-identificar-lead.md) e o [cliente ideal](../../../SKAVE%20-%20Posicionamento/possivel-cliente-ideal.md). Esta skill aplica o guia ao Instagram; onde houver diferença, valem os critérios abaixo.

## Os cinco filtros do perfil

Um perfil só vira lead se passar nos **cinco**. Na dúvida em qualquer um, descarte e siga.

1. **Seguidores: até 50 mil.** O número não importa abaixo disso. Acima de 50 mil, descarte: esse tipo de empresário raramente responde.
2. **Cargo comprovado no perfil.** A bio, o nome do perfil ou os destaques precisam mostrar que a pessoa é CEO, fundador, cofundador, sócio, CTO, CMO, CPO ou outro cargo de liderança **de uma empresa atual**. Cargo só no LinkedIn ou na imprensa não basta.
3. **@ da empresa no perfil.** Um @ da empresa na bio (ou o link do site da empresa) é praticamente a confirmação do vínculo. Abra o @ para conferir que é a empresa certa e que ela é um SaaS.
4. **O feed confirma que é dono ou líder de SaaS.** Olhe os últimos posts e destaques: bastidores do produto, time, clientes, eventos, lançamentos, métricas, conteúdo sobre o mercado do software. Se o feed for só vida pessoal, coach, infoproduto, agência ou serviço sob encomenda, descarte.
5. **Ativo nos últimos dias.** Story ativo no momento da checagem (anel colorido na foto) **ou** post no feed nos últimos 7 dias. Até 14 dias pode entrar se os outros filtros forem fortes; registre a data. Perfil privado ou parado: descarte.

Depois dos cinco filtros do perfil, confira a empresa:

- **É SaaS B2B lançado:** software como produto para empresas, já vendendo ou disponível. Agência, consultoria, software sob encomenda, serviço por mensalidade e produto só em lista de espera ficam de fora.
- **Necessidade visível:** abra o site da empresa e procure ao menos um sinal concreto de clareza, diferenciação, coerência, percepção de valor ou desatualização, como descreve o guia (por exemplo: título genérico, vários públicos ao mesmo tempo, números que não batem, posicionamento antigo misturado ao novo, marca em domínios diferentes). Anote o trecho exato. Se o site estiver muito bem resolvido, a prioridade é baixa; só inclua se faltar volume e diga isso.

## Onde procurar

Comece sempre pelo Instagram, não pela empresa. Use, nesta ordem de rendimento:

1. **Sugestões de perfis parecidos.** No perfil de um lead já confirmado (veja `_leads.md`), abra as sugestões ("Sugestões para você" / seta ao lado de Seguir). Cada lead bom traz outros.
2. **Seguidos dos perfis da área.** Perfis que leads confirmados seguem, e perfis de eventos, comunidades, fundos e podcasts de SaaS (por exemplo RD Summit, Web Summit Rio, Startup Summit, ABSeed). Procure nomes com "CEO", "founder" ou "@empresa" na bio.
3. **Busca por palavra-chave** (`instagram.com/explore/search/keyword/?q=...`): "fundador saas", "ceo saas", "meu saas", "MRR", "B2B". Quem posta sobre isso costuma estar ativo; confira se o SaaS já está lançado.
4. **Busca por nome**, quando você já tem o nome do fundador ou do CMO por outra fonte (imprensa, site da empresa). Confirme pela bio; homônimos são comuns.

Ritmo: no máximo 80 a 100 perfis visitados por sessão, sem pressa artificial e sem rolagem infinita. **Nunca** siga, curta, comente, responda story nem mande mensagem: a abordagem é sempre do usuário.

## Como trabalhar no navegador

- Comece com `tabs_context_mcp` e abra uma aba nova; feche as abas que abriu ao terminar.
- Use `browser_batch` para encadear navegação, espera curta e captura.
- Para ler um perfil, capture só o cabeçalho (`zoom` na região da bio) e, se precisar, o início do feed. Para confirmar a data do último post, abra o post mais recente que não esteja fixado.
- Se o Instagram pedir login, mostrar bloqueio temporário ou limitar ações, pare e avise o usuário. Não tente contornar.
- Dê um retorno curto ao usuário a cada 5 leads confirmados.

## O que gravar

Ao final, grave `VENDAS - Proposta Comercial/Prospecção/leads-AAAA-MM-DD.md` (data da rodada), no mesmo formato de [leads-2026-11-18.md](../../../VENDAS%20-%20Proposta%20Comercial/Prospecção/leads-2026-11-18.md): tabela de resumo, uma ficha por lead e a lista de descartados com o motivo.

Cada ficha traz:

- **Pessoa e cargo**, como aparecem no perfil.
- **Instagram:** link, número de seguidores e o trecho da bio que comprova cargo e empresa.
- **Atividade:** data do último post e se havia story ativo, com a data da checagem.
- **Feed:** uma linha sobre o que os posts mostram de SaaS.
- **Empresa e produto:** @ da empresa, site e o que o software faz.
- **Status A ou B** pelo guia (com ou sem evidência pública de clientes).
- **Necessidade observada:** os sinais, com o trecho do site.
- **Prioridade:** alta (necessidade clara e perfil muito ativo) ou média.
- **Gancho:** uma observação concreta e uma pergunta para abrir a conversa. Não diagnosticar perda de vendas nem afirmar fatos sobre receita.
- Faturamento: **não confirmado**, salvo evidência pública.

Depois, atualize [_leads.md](../../../VENDAS%20-%20Proposta%20Comercial/Prospecção/_leads.md): acrescente os novos leads com status `encontrado` e os descartados relevantes (para não revisitar). Status de abordagem: `encontrado` → `abordado` → `respondeu` → `call marcada` → `descartado`. Quando o usuário contar que abordou ou recebeu resposta, atualize o status ali.

Por fim, faça commit e push no `main` (`git pull --rebase origin main` antes do push) e entregue no chat a tabela de resumo, o caminho do arquivo e quantos perfis foram descartados por qual filtro.
