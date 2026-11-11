# Brand kit — Mateus Ritter

Atualizado em **9 de novembro de 2026**, a partir das variáveis, propriedades de texto, componentes e templates do [Figma — Mateus Ritter](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=0-1).

Este documento registra o sistema visual atual e orienta sua aplicação nos conteúdos. As especificações foram lidas diretamente no arquivo; as orientações de composição indicam como usá-las. Para produção, duplicar o template correspondente no Figma, preservando seus componentes e vínculos com variáveis. Se o Figma evoluir, conferir a mudança e atualizar este registro antes de reutilizar valores antigos.

## 1. Identidade e expressão

- **Nome:** Mateus Ritter.
- **Perfil:** @mateusritter.
- **Descritor:** Posicionamento para SaaS B2B.
- **Lema:** Posicione-se ou será posicionado.
- **Papel da marca pessoal:** atrair donos e sócios de SaaS B2B para conversas sobre clareza, diferenciação e coerência de marca.
- **Expressão desejada:** direta, séria, próxima e com personalidade. A linguagem visual usa espaço livre, hierarquia tipográfica clara, verdes sóbrios, fundos claros e fotografia pessoal.

A orientação editorial e comercial segue os [documentos de estratégia](../Estratégia%20de%20marca%20pessoal%20e%20conteúdo%20-%20Ritter/00-visao-geral-e-decisoes.md). Este kit descreve a identidade visual e sua aplicação.

## 2. Paleta atual e modos

O Figma possui uma coleção de variáveis com os modos **Light** e **Dark**. Os nomes abaixo são os nomes exatos das variáveis. Os HEX são a conversão dos valores RGB para oito bits por canal; ao trabalhar no Figma, preferir a variável vinculada.

| Variável no Figma | Light | Dark | Aplicação observada |
| --- | --- | --- | --- |
| `Color/Divider/Background/Primary` | `#F8F8F6` | `#252F25` | Fundo dos estáticos “TWICH”. |
| `Color/Divider/Background/Secondary` | `#F3F3E7` | `#2F3B2F` | Fundo dos slides de carrossel. |
| `Color/Divider/Text/Primary` | `#252F25` | `#F8F8F6` | Títulos e nome da assinatura. |
| `Color/Divider/Text/Support` | `#667266` | `#ABB9AB` | Corpo, subtítulos, descritor e informações de apoio. |
| `Color/Divider/Primary` | `#D7D7C9` | `#445644` | Cor disponível para divisores e contornos discretos. |
| `Color/Divider/Detail/Blue` | `#4193EF` | `#4193EF` | Azul do selo de verificação. |

### Regras de cor

- Escolher um modo por peça e manter a combinação de fundo, texto principal e apoio desse modo.
- Usar o verde escuro como base de reconhecimento da marca; os fundos claros dão respiro à composição.
- Reservar o azul ao selo presente na assinatura. Sua existência como variável não o torna uma cor de destaque para títulos ou CTAs.
- Manter as cores vinculadas às variáveis ao duplicar os modelos. Não substituir os vínculos por valores avulsos apenas para trocar o modo.
- A paleta anterior, que incluía creme `#F3F0E8`, verde claro `#D9DBBD` e oliva `#585744`, não descreve os tokens atuais destes templates. Para reproduzir os modelos vigentes, usar a tabela acima.

### Combinações de leitura

| Texto | Fundo | Contraste aproximado |
| --- | --- | ---: |
| Principal Light `#252F25` | Primário Light `#F8F8F6` | 13,1:1 |
| Apoio Light `#667266` | Secundário Light `#F3F3E7` | 4,5:1 |
| Principal Dark `#F8F8F6` | Secundário Dark `#2F3B2F` | 11,0:1 |
| Apoio Dark `#ABB9AB` | Secundário Dark `#2F3B2F` | 5,7:1 |

Esses valores são aproximações calculadas com os HEX documentados, em fundos sólidos. Fotografias e transparências exigem nova conferência visual. O contraste não compensa texto pequeno demais para leitura no celular.

## 3. Tipografia

**Instrument Sans** conduz a mensagem. O peso predominante dos templates atuais é **Medium 500**. **SemiBold 600** aparece no nome da assinatura e **Regular 400** no descritor. **Courier Prime Regular e Bold** ficam nas pequenas informações do cabeçalho.

| Elemento | Família e peso | Tamanho | Entrelinha | Espaçamento de letras |
| --- | --- | ---: | ---: | ---: |
| Título de capa | Instrument Sans Medium 500 | 80 px | 105% | −4% |
| Chamada principal de fechamento | Instrument Sans Medium 500 | 80 px | 105% | −4% |
| Subtítulo de capa ou fechamento | Instrument Sans Medium 500 | 32 px | 130% | 0% |
| Corpo do carrossel textual | Instrument Sans Medium 500 | 44 px | 110% | 0% |
| Corpo do carrossel com foto | Instrument Sans Medium 500 | 35 px | 110% | 0% |
| Texto dos estáticos “TWICH” | Instrument Sans Medium 500 | 40 px | 130% | 0% |
| Nome “Mateus Ritter” | Instrument Sans SemiBold 600 | 32 px | Automática | 0% |
| Descritor da assinatura | Instrument Sans Regular 400 | 26 px | Automática | 0% |
| Categoria do cabeçalho | Courier Prime Bold 700 | 16 px | Automática | 0% |
| Lema do cabeçalho | Courier Prime Regular 400 e Bold 700 | 16 px | Automática | 0% |

Os tamanhos correspondem às pranchetas de **1080 × 1350 px**. Não há estilos locais de texto cadastrados na leitura atual; as configurações estão aplicadas diretamente às camadas dos templates. Por isso, duplicar os modelos ajuda a preservar a hierarquia.

### Regras de texto

- Manter o título curto o suficiente para funcionar como abertura. O subtítulo é opcional e pode ser removido quando não acrescentar informação.
- Preservar uma ideia principal por slide. Quando o texto ficar excessivo, editar a redação ou dividir o desenvolvimento antes de reduzir a fonte.
- Conferir as quebras de linha após cada troca de conteúdo. As caixas com altura automática crescem; isso não garante que continuem centralizadas ou afastadas do rodapé.
- Usar as etiquetas de 16 px como informação complementar. A mensagem essencial deve estar no título ou corpo.
- O corpo de 35 px do modelo com foto exige concisão e revisão em tamanho de celular.
- Não substituir as famílias silenciosamente em outro software. Carregar Instrument Sans e Courier Prime antes de produzir ou exportar.

## 4. Composição e assinatura

Todos os **13 templates** atuais têm proporção **4:5**, com **1080 × 1350 px**. São oito modelos de carrossel, quatro estáticos “TWICH” e um modelo de imagem de fundo.

### Carrosséis

- Cabeçalho com categoria à esquerda, avatar central e lema à direita.
- Margens laterais próximas de **100–107 px** e área principal de texto de **864 px** de largura.
- Subtítulo de capa e fechamento com **646 px** de largura.
- Cabeçalho dos modelos inspecionados em **y = 82 px**, com **92 px** de altura.
- Rodapé com assinatura e indicador de passagem, próximo de **y = 1158 px**.
- No modelo com foto, a área de imagem tem **856 × 508 px**, seguida pelo comentário textual.
- Título e subtítulo são agrupados verticalmente. Ajustar a posição do conjunto conforme a quantidade final de linhas, respeitando o respiro do modelo.

### Badge

O [componente Badge](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-62) reúne avatar, nome, selo e descritor. As instâncias nos templates podem ocultar o avatar quando já existe um retrato no cabeçalho.

Usar a instância correspondente e preservar sua ligação com o componente. O texto atual no componente principal é **“Posicionamento para SaaS B2B”**; conferir se instâncias antigas não mantêm uma substituição local da grafia anterior.

### Fotografia

A fonte principal de fotos de Ritter é o [catálogo do ensaio fotográfico](Ensaio%20Fotogáfico%20Ritter/_catalogo.md): 14 fotos originais em PNG, sem compressão, com tom, modo de cor indicado, usos sugeridos e cuidados de recorte de cada uma. A página [02 · Fotografias](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=1-23) do Figma e os assets dos modelos são complementares. Imagens geradas nunca representam Ritter. Fotos de palco, rotina ou bastidores devem sustentar o assunto do post.

No modelo de imagem de fundo, preservar o degradê escuro que ajuda a leitura e revisar o contraste após trocar a foto. Evitar que título ou subtítulo prejudiquem a leitura do rosto ou de um detalhe importante da imagem. Os espaços quadriculados dos modelos com foto são placeholders e precisam receber a imagem final.

## 5. Biblioteca de templates

Os nomes “TWICH” abaixo preservam a identificação usada no Figma; são composições de postagem textual para o feed, sem implicar uma publicação na plataforma Twitch.

| Família e função | Modelo claro | Modelo escuro |
| --- | --- | --- |
| **Capa:** gancho e subtítulo opcional | [CAPA · 9:66](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=9-66) | [CAPA · 17:228](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-228) |
| **Conteúdo:** desenvolvimento textual | [CONTEÚDO · 9:112](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=9-112) | [CONTEÚDO · 17:245](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-245) |
| **Conteúdo com foto:** exemplo visual e comentário | [CONTEÚDO COM FOTO · 13:185](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=13-185) | [CONTEÚDO COM FOTO · 17:260](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-260) |
| **Fechamento:** conclusão e CTA contextual | [FECHAMENTO · 17:394](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-394) | [FECHAMENTO · 17:422](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-422) |
| **Estático textual:** opinião ou reflexão curta | [TWICH · 13:210](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=13-210) | [TWICH · 17:131](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-131) |
| **Estático com foto:** comentário com imagem | [TWICH COM FOTO · 13:256](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=13-256) | [TWICH COM FOTO · 17:106](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-106) |

O [modelo IMAGEM · 17:316](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=17-316) usa fotografia de fundo, degradê, título e subtítulo opcional. Pode funcionar como capa ou estático conforme o conteúdo. Para publicação isolada, adaptar os indicadores que pressupõem um próximo slide.

O arquivo inspecionado não contém um template próprio de Stories em 1080 × 1920 px. Uma adaptação para 9:16 exige revisão de composição e áreas de leitura.

## 5A. Elementos visuais

Registrados na página **Elementos visuais** do [Brand Kit no Claude Design](https://claude.ai/artifact/3rjExY97iHpq4SxLJbHzUU) em 10 de Novembro, 2026. Ícones, ilustrações e diagramas explicam o argumento do slide; não são decoração.

### Estilo

- **Traço:** fino, contínuo, pontas e cantos arredondados. Ícones em grid 24 com stroke 1,75; ilustrações em viewBox 240 × 160 com stroke 1,5.
- **Cores:** traço principal em `Text/Primary`, detalhes em `Text/Support` e uma superfície de ilustração (`soft`): `#E4E4D2` no Light e `#3A4A3A` no Dark. Sem outras cores, sombras ou degradês.
- **Origem:** usar apenas os ícones e ilustrações do brand kit. Não misturar com outras bibliotecas, emojis ou ilustrações coloridas.

### Regras de uso

- **Um elemento visual por slide**: um ícone, uma ilustração ou um diagrama.
- **Onde usar:** slides de desenvolvimento do carrossel. Capa e Fechamento priorizam gancho e CTA, com no máximo um ícone discreto.
- **TWICH continua só texto.**
- Não reduzir a fonte do texto para caber o elemento. Se não couber, cortar texto ou dispensar o elemento.
- Diagramas usam o texto aprovado do slide e nunca números sem fonte verificável.

### Biblioteca

| Tipo | Itens (nome de referência) |
| --- | --- |
| **Ícones** | `site`, `demo`, `planilha`, `preço`, `fundador`, `time`, `mensagem`, `funil`, `foco`, `direção`, `diagnóstico`, `proposta`, `certo`, `errado`, `ideia`, `coerência` |
| **Ilustrações** | `site`, `demo`, `comparacao`, `preco`, `fundador`, `time`, `mensagem`, `funil`, `foco`, `direcao`, `diagnostico`, `proposta` |
| **Diagramas** | A · Comparação (genérica × clara), B · Antes e depois, C · Sequência (até 4 passos), D · Checklist, E · Citação, F · Espectro |

Na biblioteca, as ilustrações usam cores fixas do modo Light. Ao aplicar num template, trocar `#252F25` por `{{txt}}`, `#667266` por `{{sup}}` e `#E4E4D2` por `{{soft}}`.

### Templates novos

| Template | Arquivo no Claude Design | Uso |
| --- | --- | --- |
| Carrossel · Conteúdo com ícone | `project/ConteudoIcone.dc.html` | Ícone de 56 px em círculo `soft` acima de dois blocos de 44 px |
| Carrossel · Conteúdo com ilustração | `project/ConteudoIlustracao.dc.html` | Ilustração de 690 × 460 px acima de dois blocos de 40 px |
| Carrossel · Conteúdo com diagrama | `project/ConteudoDiagrama.dc.html` | Diagrama A (comparação) em tamanho real; os demais padrões seguem a mesma área de 864 px |

## 6. Aplicação ao conteúdo

### Sequência de carrossel

1. **Capa:** apresentar a situação e uma tensão, consequência ou descoberta que dê motivo para passar ao próximo slide.
2. **Desenvolvimento:** escolher o modelo textual ou com foto conforme o argumento. A imagem deve contribuir para a explicação.
3. **Fechamento:** concluir o raciocínio e escrever um convite explícito para seguir @mateusritter, ligado ao assunto desenvolvido.

A quantidade de slides acompanha o desenvolvimento necessário. Alternar claro e escuro pode ajudar a marcar mudanças de etapa; manter a hierarquia e os modos consistentes dentro de cada peça.

### CTA contextual

O convite final deve retomar a situação, a dor ou o aprendizado do post. Exemplo para um conteúdo sobre dependência do fundador:

> Quer que seu time consiga explicar o valor do seu SaaS sem chamar você em toda conversa? Siga @mateusritter para aprender a construir uma mensagem que a equipe consiga usar.

Não usar fechamentos genéricos como “Siga meu perfil para mais dicas”. Se o CTA funcionar sem alteração em posts sobre dores diferentes, reescrevê-lo. No template de fechamento, distribuir o texto entre título e subtítulo quando isso favorecer a leitura; o convite para seguir precisa continuar explícito. A seta do modelo não substitui o CTA.

Aplicar a mesma regra nos estáticos, reels, stories e legendas. A [skill skave-ideias-ritter](../../.claude/skills/skave-ideias-ritter/SKILL.md) contém as orientações completas de geração e revisão editorial.

## 7. Conferência antes de exportar

- Confirmar o template e modo de cor escolhidos.
- Substituir textos de exemplo e placeholders de imagem.
- Verificar fontes, quebras de linha, crescimento das caixas e distância do rodapé.
- Conferir assinatura, grafia “SaaS B2B” e recorte das fotografias.
- Revisar contraste sobre imagens e leitura na escala de celular.
- Garantir que o último slide ou texto encerre com um CTA ligado ao conteúdo.
- Exportar cada prancheta individualmente, na ordem do conteúdo, mantendo 1080 × 1350 px para os modelos atuais.

## Fonte e manutenção

Fonte visual: [01 · Identidade Visual no Figma](https://www.figma.com/design/KksVBnHPlxGwzjZSeKLmfv/Mateus-Ritter?node-id=0-1). Este registro incorpora os modos Light/Dark, o uso de Instrument Sans Medium, o componente Badge e os novos templates de fechamento presentes na data da conferência.

Mudanças de estratégia, oferta e linguagem devem ser feitas nos documentos correspondentes e na skill editorial. Mudanças de cor, fonte, assinatura ou template no Figma devem ser refletidas neste kit para manter a produção alinhada.
