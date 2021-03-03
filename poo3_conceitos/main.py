from functools import reduce
from models import Produto, Frio, Bebidas, Pacote
from handlers import VendasHandler


def imprime_produtos(lista_de_produtos):
    print('\n\n- - - - - - PRODUTOS - - - - - -')
    for p in lista_de_produtos:
        print(p)
        print(p.__dict__)
        print('- - - -\n')
    print('- - - - - - - - - - - -')


def main():
    produto1 = Produto(1, 'Pão francês', 0.35, 13234, 80)
    produto2 = Produto(2, 'Pão de batata', -0.80, 43215)
    produto3 = Produto(3, 'Rosquinha de canela', 0.80, 654324)

    produto4 = Frio(4, 'Salame', -13, 6543)

    produto5 = Bebidas(5, 'Coca-cola', 5.6, 903543)
    produto6 = Bebidas(6, 'Vinho', -5.6, 987643, 600, True)

    print(produto4.tipo)

    produto1.vendedor = 'Bruno p.'

    produto2.atualizar('Pão potato', 1.20)

    pacote1 = Pacote(produto6)

    print(pacote1)

    lista_de_produtos = [produto1, produto2, produto3, produto4, produto5, produto6]
    imprime_produtos(lista_de_produtos)


# lista com os atributos "nome" das instancias de classe produto

if __name__ == '__main__':
    main()
