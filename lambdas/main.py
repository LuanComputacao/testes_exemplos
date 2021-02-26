from functools import reduce
from faker import Faker
from random import randint
import json


lista = list(range(0,11))

extrair_idade = lambda x: [p['idade'] for p in x] 
soma_da_lista = reduce(lambda a, c: a + c, lista, 0)

extrair_idade = lambda x: [p['idade'] for p in x] 
def fake_people(qtd=1):
    fake = Faker(['pt_BR'])
    for _ in range(qtd):
        yield {
                'nome': fake.name(),
                'idade': randint(1, 110)
                }
lista_de_pessoas = list(fake_people(10))

print(json.dumps(lista_de_pessoas, indent=2))
extrair_idade = lambda x: [p['idade'] for p in x] 

lista_de_pessoas_ordenada_por_idade = sorted(lista_de_pessoas, key=lambda x: x['idade'])

extrair_idade = lambda x: [p['idade'] for p in x] 

def extrair_idade (pessoas: list):
    return [p['idade'] for p in pessoas]

print(extrair_idade(lista_de_pessoas))
print([p['idade'] for p in lista_de_pessoas_ordenada_por_idade])

