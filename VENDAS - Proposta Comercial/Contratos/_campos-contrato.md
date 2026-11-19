# Campos do contrato

Cada campo do modelo de contrato vira uma etiqueta `{{NOME}}`. A automação troca cada etiqueta pelo campo personalizado de mesmo nome no card do ClickUp. Se faltar um campo obrigatório, a automação para e avisa, em vez de gerar o contrato com a etiqueta aparecendo.

- Modelo em texto: `modelo-brand-launch.md`. A fonte da redação é o artefato "Contrato · Posicionamento de Marca · Brand Launch" (https://claude.ai/artifact/2hCULFh1neEocjUBcfHiKZ).
- Modelo no Google Docs: "Modelo - Posicionamento de Marca - Brand Lauch", na pasta Novos Clientes/2026 do Drive (id `1lhUp7-7jJA5fvWPpmI2LkePdWJrRGKaplCoz3gaR5Ec`). Esse arquivo nunca é preenchido: ele é duplicado para a pasta de cada cliente.

## Etiquetas

| Etiqueta | O que vai | Quem preenche | Onde aparece |
|---|---|---|---|
| `{{RAZAO_SOCIAL}}` | Razão social da contratante | Cliente (formulário) | Partes, assinaturas |
| `{{CNPJ}}` | CNPJ da contratante | Cliente | Partes, assinaturas |
| `{{ENDERECO_SEDE}}` | Rua, número, bairro, cidade/UF, CEP | Cliente | Partes, 14.1.1 |
| `{{EMAIL_EMPRESA}}` | E-mail da empresa | Cliente | Partes |
| `{{TELEFONE_EMPRESA}}` | Telefone da empresa | Cliente | Partes |
| `{{REPRESENTANTE_NOME}}` | Nome do representante legal que assina | Cliente | Partes, assinaturas |
| `{{REPRESENTANTE_NACIONALIDADE}}` | Nacionalidade | Cliente | Partes |
| `{{REPRESENTANTE_ESTADO_CIVIL}}` | Estado civil | Cliente | Partes |
| `{{REPRESENTANTE_PROFISSAO}}` | Profissão | Cliente | Partes |
| `{{REPRESENTANTE_CPF}}` | CPF do representante | Cliente | Partes, assinaturas |
| `{{REPRESENTANTE_EMAIL}}` | E-mail do representante (recebe o envelope de assinatura) | Cliente | Assinaturas |
| `{{RESPONSAVEL_NOME}}` | Ponto focal que recebe as comunicações formais | Cliente | 14.1.1 |
| `{{RESPONSAVEL_EMAIL}}` | E-mail do ponto focal | Cliente | 14.1.1 |
| `{{RESPONSAVEL_TELEFONE}}` | Telefone do ponto focal | Cliente | 14.1.1 |
| `{{DECISORES}}` | Nome, cargo e e-mail de cada Decisor, separados por ponto e vírgula | Cliente | 14.1.1 |
| `{{TESTEMUNHA_NOME}}` | Testemunha da contratante | Cliente | Assinaturas |
| `{{TESTEMUNHA_CPF}}` | CPF da testemunha | Cliente | Assinaturas |
| `{{TESTEMUNHA_EMAIL}}` | E-mail da testemunha | Cliente | Assinaturas |
| `{{CANAL_ADICIONAL}}` | Canal além do Instagram nas Primeiras Ativações (ex.: LinkedIn) | Skave | 4.1.1 |
| `{{VALOR_AVISTA}}` | Valor à vista, ex.: 11.500,00 | Skave | 8.1 |
| `{{VALOR_AVISTA_EXTENSO}}` | Valor à vista por extenso, ex.: onze mil e quinhentos reais | Skave (a automação pode gerar) | 8.1 |
| `{{VALOR_PARCELADO_TOTAL}}` | Total no cartão em 12x, ex.: 13.099,92 | Skave | 8.1 |
| `{{VALOR_PARCELA}}` | Valor de cada parcela, ex.: 1.091,66 | Skave | 8.1 |
| `{{CONDICAO_PAGAMENTO}}` | A opção escolhida, com parcelas, valores e vencimentos | Skave | 8.1 |
| `{{DATA_CONTRATO}}` | Data por extenso, ex.: 19 de novembro de 2026 | Automação (data da geração) | Local e data |

O endereço para notificações (14.1.1) usa o mesmo `{{ENDERECO_SEDE}}`. Se algum cliente pedir endereço diferente, criar `{{ENDERECO_NOTIFICACOES}}`.
