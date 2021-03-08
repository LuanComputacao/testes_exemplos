from functools import reduce
from models import Produto, Frio, Bebidas, Pacote, Quente, Carrinho, Cliente
from handlers import VendasHandler, Matematica


def imprime_produtos(lista_de_produtos):
    print('\n\n- - - - - - PRODUTOS - - - - - -')
    for p in lista_de_produtos:
        print(p)
        print(p.__dict__)
        print('- - - -\n')
    print('- - - - - - - - - - - -')


def main():
    
    r = Matematica.soma(2,3)
    print(r)
    
    
    produto1 = Produto(1, 'Pão francês', 0.35, 13234, 80)
    produto2 = Produto(2, 'Pão de batata', -0.80, 43215)
    produto3 = Produto(3, 'Rosquinha de canela', 0.80, 654324)

    produto4 = Frio(4, 'Salame', -13, 6543)

    produto5 = Bebidas(5, 'Coca-cola', 5.6, 903543)
    produto6 = Bebidas(6, 'Vinho', -5.6, 987643, 600, True)
    produto8 = Quente(8, 'Dogão', -5.6, 987643, 600)

    produto1.vendedor = 'Bruno p.'
    produto2.atualizar('Pão potato', 1.20)

    cliente = Cliente('Eduardo')
    carrinho = Carrinho(123456, cliente)

    carrinho.incluir_produto(produto1)
    carrinho.incluir_produto(produto2)
    carrinho.incluir_produto(produto3)
    carrinho.incluir_produto(produto4)
    carrinho.incluir_produto(produto5)
    carrinho.incluir_produto(produto6)
    carrinho.incluir_produto(produto8)

    print(carrinho)


# lista com os atributos "nome" das instancias de classe produto


def dobro(limite):
    limite+=1
    for n in range(limite):
        yield n*2
    


if __name__ == '__main__':
    #main()
    
    reduzido = reduce(lambda a, i : a+i, range(5))

    if reduzido < 10:
        print('menor do que 10')
    elif reduzido <40:
        print('menor do que 40; maior que 10;')
    else:
        print('igual ou maior que 40')
    

