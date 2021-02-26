# Descrição

Enviar emails para todos os DEVs do Q3 entregando o presente de Quarta-Feira!

# Estórias de usuário

* St1
    * Como um instrutor
    * Quero enviar emails para todos os DEVs
    * Porque preciso entregar um código
    
* St2
    * Como um instrutor com uma lista de emails em CSV
    * Quero fornecer esta lista ao software para ser feito o processamento
    * Porque preciso enviá-los rapidamente
    
* St3
    * Como um instrutor
    * Quero obter estes códigos a partir de um arquivo CSV exportado
    * Porque não ter que fornecer código a código para o software
    
# Crítérios de aceitação

Dado | Quando | Então
------ | ------  | ------
Um CSV com os dados dos DEVs | Ler este CSV  | quero que processe apenas os email válidos
Um CSV com os códigos  | Ler este CSV | quero que seja verifica o formato do Código
Um email válido | Enviar este email | o DEV receba este email com o código
Um email da lista de dados dos DEVs | __não__ estiver correto | enviar uma mensagem por slack para este DEV
Um email da lista de dados dos DEVs | estiver correto | prosseguir com o processo de envio do email
Um email da lista de dados dos DEVs | estiver correto | enviar uma mensagem de confirmação por slack para este DEV
