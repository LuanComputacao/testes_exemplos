# Cancelador de CPF

Um software que lê um arquivo CSV com dados de pessoas e, depois, faz o cancelamento de CPFs conforme algumas regras.

## Estórias de usuário

__Como__ um agente da receita federal

__Quero__ fornecer um CSV com dados de pessoas e processá-los

__Porque__ preciso aplicar uma regra para cancelamento de CPF de pessoas inadimplente


## Critérios de aceitação

| Dado | Quando | Espero |
|------|------|------|
|Um CSV com os dados de pessoas| Processado | que seja identificado as pessoas inadimplentes|
|Dados de uma pessoa|estiver com a flag de inadimplente com valor 1|marcar o CPF dela como cancelado|
|Dados de uma pessoa com CPF cancelado|ela for identificada|salvar em um arquivo `pessoas_com_cpf_cancelado.csv`
