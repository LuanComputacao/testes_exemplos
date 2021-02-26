import json

pessoas = [ 
        {
        "nome": "Karlos",
        "sobrenome": "Snow",
        "CPF": "07723308879"
        },
        {
        "nome": "Jane",
        "sobrenome": "Doe",
        "CPF": "07703324879"
        },
        {
        "nome": "Abdiel",
        "sobrenome": "Roe",
        "CPF": "07702308879"
        }

        ]

inicio_do_nome = 'JA'.lower()

for pessoa in pessoas:
    cpf_cancelado = pessoa.get('nome', '').lower().startswith(inicio_do_nome)

    pessoa.update({'cpf cancelado': cpf_cancelado})

print(json.dumps(pessoas))


