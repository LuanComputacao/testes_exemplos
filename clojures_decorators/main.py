import csv
import json
def cria_outra_funcao(b): # função enclausuradora
    def funcao_interna(a): # função enclausurada
        return a + b
    
    return funcao_interna

# - - - - - -

funcao_criada = cria_outra_funcao(10)

r1 = funcao_criada(6)
r2 = funcao_criada(5)
r3 = funcao_criada(7)

"""
FUNÇÃO DECORATOR
"""
LISTA_DE_USUARIOS = ['Rámon', 'Luiz']

def funcao_decoradora(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user not in LISTA_DE_USUARIOS:
            return 'Usuário não existente'
        
        with open('log.log', 'a') as f:
            f.write(*args)
            f.write('\n')

        return func(args[0])

    return wrapper



@funcao_decoradora
def retorna_nome(nome):
    with open('produtos.csv') as f:
        reader = csv.DictReader(f)
        return [notas for notas in reader]


def converte_para_json(*args,**kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            r = func(*args)
            with open('log_produtos.csv', 'a') as f:
                w = csv.DictWriter(f, fieldnames=['produto', 'preco'])
                w.writerow(r)            
            return r
        
        return wrapper
    
    return decorator

@converte_para_json('olá')
def retorna_dict(produto, preco):
    return {
        'produto': produto,
        'preco': preco
        }

p1 = retorna_dict('maçã', 1.56)
p2 = retorna_dict('pão', 1.56)
print(p1)
print(p2)