# Campos do contrato

Cada campo do modelo de contrato vira uma etiqueta `{{NOME}}`. A automação lê o card do cliente no ClickUp, monta o valor de cada etiqueta a partir dos campos personalizados e troca no contrato. Se faltar um campo obrigatório, a automação para e avisa, em vez de gerar o contrato com a etiqueta aparecendo.

## Onde fica cada coisa

- **Modelo em texto:** `modelo-brand-launch.md`. A redação vem do artefato "Contrato · Posicionamento de Marca · Brand Launch" (https://claude.ai/artifact/2hCULFh1neEocjUBcfHiKZ).
- **Modelo no Google Docs (Brand Launch):** "Modelo - Posicionamento de Marca - Brand Lauch", id `1lhUp7-7jJA5fvWPpmI2LkePdWJrRGKaplCoz3gaR5Ec`. Aprovado em 19/11/2026. Nunca é preenchido: é duplicado para a pasta de cada cliente.
- **Modelo do Brand Evolution:** ainda não existe.
- **Lista do ClickUp:** workspace da Skave (`9011515818`), espaço Jurídico, lista "Contratos em andamento" (`901110364224`). O formulário do cliente cai nela.
- **Pasta-mãe no Drive:** "POSICIONAMENTO DE MARCA" (`1b_pNii0BJjAoGojyaYynMgyYDWyNSATo`). A pasta de cada cliente é criada dentro dela.
- **Nome da pasta do cliente:** `<nome do card no ClickUp> LAUNCH` ou `<nome do card no ClickUp> EVOLUTION`, conforme o produto.

## Campos personalizados do ClickUp

Status: **existe** = já está na lista; **criar** = ainda não existe; **ajustar** = existe, mas precisa de mudança.

### Preenchidos pelo cliente (formulário)

| Campo no ClickUp | Tipo | Status | Etiqueta | Observação |
|---|---|---|---|---|
| Razão Social | texto curto | existe | `{{RAZAO_SOCIAL}}` | |
| CNPJ | texto curto | existe | `{{CNPJ}}` | |
| Endereço | texto curto | existe | `{{ENDERECO_SEDE}}` | Rua. Junto com os quatro campos abaixo forma o endereço completo |
| Número | número | existe | `{{ENDERECO_SEDE}}` | Trocar para texto curto, para aceitar "s/n" e complemento |
| Bairro | texto curto | existe | `{{ENDERECO_SEDE}}` | |
| Cidade | texto curto | existe | `{{ENDERECO_SEDE}}` | |
| Estado (UF) | texto curto | criar | `{{ENDERECO_SEDE}}` | |
| CEP | texto curto | existe | `{{ENDERECO_SEDE}}` | |
| Email | e-mail | existe | `{{EMAIL_EMPRESA}}` | E-mail da empresa |
| Telefone/Whatsapp | telefone | existe | `{{TELEFONE_EMPRESA}}` | Telefone da empresa |
| Representante | texto curto | existe | `{{REPRESENTANTE_NOME}}` | Quem assina |
| Nacionalidade | texto curto | criar | `{{REPRESENTANTE_NACIONALIDADE}}` | |
| Estado Civil | lista suspensa | ajustar | `{{REPRESENTANTE_ESTADO_CIVIL}}` | Hoje só tem Casado e Solteiro. Acrescentar Divorciado, Viúvo e União estável |
| Profissão | texto curto | existe | `{{REPRESENTANTE_PROFISSAO}}` | |
| CPF do representante | texto curto | existe | `{{REPRESENTANTE_CPF}}` | |
| Email do representante | e-mail | criar | `{{REPRESENTANTE_EMAIL}}` | Recebe o envelope de assinatura |
| Ponto focal: nome | texto curto | criar | `{{RESPONSAVEL_NOME}}` | Recebe as comunicações formais (cláusula 14.1.1) |
| Ponto focal: email | e-mail | criar | `{{RESPONSAVEL_EMAIL}}` | |
| Ponto focal: telefone | telefone | criar | `{{RESPONSAVEL_TELEFONE}}` | |
| Decisores | texto longo | criar | `{{DECISORES}}` | Nome, cargo e e-mail de cada um |
| Testemunha | texto curto | existe | `{{TESTEMUNHA_NOME}}` | |
| CPF da testemunha | texto curto | existe | `{{TESTEMUNHA_CPF}}` | |
| Email da testemunha | e-mail | existe | `{{TESTEMUNHA_EMAIL}}` | |

### Preenchidos pela Skave

| Campo no ClickUp | Tipo | Status | Etiqueta | Observação |
|---|---|---|---|---|
| Contrato | lista suspensa | ajustar | (escolhe o modelo e o sufixo da pasta) | Acrescentar as opções "Posicionamento · Brand Launch" e "Posicionamento · Brand Evolution" |
| Canal adicional | texto curto | criar | `{{CANAL_ADICIONAL}}` | Canal além do Instagram, ex.: LinkedIn |
| Valor | texto curto | existe | `{{VALOR_AVISTA}}` | Valor à vista, ex.: 11.500,00 |
| Valor parcelado total | texto curto | criar | `{{VALOR_PARCELADO_TOTAL}}` | Total em 12x no cartão, ex.: 13.099,92 |
| Valor da parcela | texto curto | criar | `{{VALOR_PARCELA}}` | Ex.: 1.091,66 |
| Condições de pagamento | texto longo | existe | `{{CONDICAO_PAGAMENTO}}` | A opção escolhida, com parcelas e vencimentos |

### Gerados pela automação, sem campo no ClickUp

| Etiqueta | Como é gerada |
|---|---|
| `{{VALOR_AVISTA_EXTENSO}}` | Escrita por extenso a partir do campo Valor |
| `{{DATA_CONTRATO}}` | Data da geração por extenso, ex.: 19 de novembro de 2026 |
| `{{ENDERECO_SEDE}}` | "Endereço, Número, Bairro, Cidade/UF, CEP" |

O endereço para notificações (14.1.1) usa o mesmo `{{ENDERECO_SEDE}}`.

### Campos da lista que o contrato de Posicionamento não usa

Itens de entrega, Serviço, Etapas, Setor Operacional, Itens de desenvolvimento, Objeto, Prazo e Prazo por extenso servem aos outros contratos da lista e ficam como estão.
