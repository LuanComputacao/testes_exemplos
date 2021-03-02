from functools import reduce
from models import Produto
from handlers import VendasHandler


def imprime_produtos(lista_de_produtos):
    print('\n\n- - - - - - PRODUTOS - - - - - -')
    for p in lista_de_produtos:
        print(p)
        print(p.__dict__)
        print('- - - -\n')
    print('- - - - - - - - - - - -')


def main():
    produto1 = Produto(1, 'Pão francês', 0.35, 80)
    produto2 = Produto(2, 'Pão de batata', -0.80)
    produto3 = Produto(3, 'Rosquinha de canela', 0.80)
    produto4 = Produto(4, 'Rosquinha de Romeu e Julieta', 0.80)

    print(produto3)

    produto1.vendedor = 'Bruno p.'
    produto1.tipo = 'morno'

    produto2.atualizar('Pão potato', 1.20)

    # mudando atributo de classe
    Produto.tipo = 'morno'

    lista_de_produtos = [produto1, produto2, produto3, produto4]
    imprime_produtos(lista_de_produtos)

    nomes_dos_produtos = [produto2.nome, produto1.nome]

    lista_de_produtos, valor_da_venda = VendasHandler.vender(
        lista_de_produtos,
        nomes_dos_produtos
    )

    imprime_produtos(lista_de_produtos)
    print(valor_da_venda)


# lista com os atributos "nome" das instancias de classe produto

if __name__ == '__main__':
    main()
