from src.handlers import ProdutosHandler
from src.models import Carrinho, Cliente
import pandas as pd


def imprime_produtos(lista_de_produtos):
    print('\n\n- - - - - - PRODUTOS - - - - - -')
    for p in lista_de_produtos:
        print(p)
        print(p.__dict__)
        print('- - - -\n')

    print('- - - - - - - - - - - -')


def main():
    produtos_df = pd.read_csv('produtos.csv')
    produtos_df.set_index('id', inplace=True)
    print(produtos_df)
    print(produtos_df.loc[1])
    produtos_pesados_df = produtos_df[produtos_df['peso'] > 50]
    print(produtos_pesados_df)


# lista com os atributos "nome" das instancias de classe produto

if __name__ == '__main__':
    main()
