# Na estrutura de comprehension
# esquerda => dado que queremos (retorno/append)
# meio => iteração (for _ in qqc)
# direito => condições de inclusão

# LIST COMPREHENSION

# processando uma lista de listas

def processa_itens(itens: list) -> list:
    return [p*2 for p in itens]


minha_lista_de_listas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
resultado = [processa_itens(l) for l in minha_lista_de_listas]
print(resultado)

# exemplo de valores condicionais

sao_valores_pares = [True if n % 2 == 0 else False for n in range(11)]
print(list(range(11)))
print(sao_valores_pares)



# SET COMPREHENSION
# a partir de uma lista de produtos, selecione apenas os produtos que tenham mais de 6 letras, sem repetí-los
produdos_comprados = ['pão', 'salsicha', 'mortadela', 'bolacha', 'biscoito', 'pão', 'bolacha', 'chiclete', 'mortadela']
produtos = {p for p in produdos_comprados if len(p) > 6}

print(produtos)

# DICT COMPREHENSION
# processando um dicionário e modificando chaves e valores

lista_de_compras = {
    '01/01': 'pão',
    '02/01': 'salsicha',
    '03/01': 'mortadela',
    '04/01': 'bolacha',
    '05/02': 'biscoito',
    '06/02': 'pão',
    '07/02': 'bolacha',
    '08/02': 'chiclete', 
    '09/02': 'mortadela',
    '10/02': 'coca-cola zero'
}

lista_padronizada = { f'{k}/2020': v.upper() for k, v in lista_de_compras.items() if k.endswith('02') }

lista_padronizada_bad = {}
for k, v in lista_padronizada.items():
    if k.endswith('02'):
        lista_padronizada_bad.update({
            f'{k}/2020': v.upper()
        })


print(lista_padronizada)

