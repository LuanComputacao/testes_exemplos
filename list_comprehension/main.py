from functools import reduce
from faker import Faker
from random import randint

"""
1. processamento
2. iteração
3. filtragens
"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dobro_da_lista = [n*2 for n in lista]  # map


def processa(n):
    mult = 2 if n % 2 == 0 else 3
    return n * mult


numeros_pares = [processa(n) for n in lista]


def cria_pessoa():
    fake = Faker()
    return {
        "nome": fake.name(),
        "endereço": fake.address(),
        "idade": randint(1, 80)
    }

def cancela_cpf(pessoa):
    pessoa.update({'cpf cancelado': True})
    return pessoa

pessoas = [cria_pessoa() for _ in range(10)]

pessoas_menor_de_idade = [cancela_cpf(pessoa) for pessoa in pessoas if pessoa['idade'] < 18]

print(pessoas)
print(pessoas_menor_de_idade)
