from src.handlers import ProdutosHandler
from src.models import Carrinho, Cliente
import inspect


def imprime_produtos(lista_de_produtos):
    print('\n\n- - - - - - PRODUTOS - - - - - -')
    for p in lista_de_produtos:
        print(p)
        print(p.__dict__)
        print('- - - -\n')

    print('- - - - - - - - - - - -')


def main():
    produtos = ProdutosHandler.retrieve_products()

    cliente = Cliente('Eduardo')
    carrinho = Carrinho(123456, cliente)

    attributes = get_init_params()
    print(attributes)

    carrinho.incluir_produtos(produtos)

    carrinho.save()

    print(carrinho)


def get_init_params(class):
    attributes = list(inspect.signature(Cliente.__init__).parameters.keys())
    attributes.remove('self')
    return attributes


# lista com os atributos "nome" das instancias de classe produto

if __name__ == '__main__':
    main()
