from functools import reduce
from models import Produto

def nomes_dos_produtos(*args):
    return [p.nome for p in args]


def main():
    produto1 = Produto(1, 'Pão francês', 0.35, 80)
    produto2 = Produto(1, 'Pão de batata', -0.80)
    produto3 = Produto(1, 'Rosquinha de canela', 0.80)

    produto3.atualizar(produto3.nome, -0.1)
    print(produto1)
    print(produto2)
    print(produto3)

    resultado = produto1 + produto2
    print(resultado)
    print(len(produto1))

    produto3.usando_args('a', 'b', 'c')
    
    nomes = nomes_dos_produtos(produto1, produto2, produto3)
    print(nomes )

# lista com os atributos "nome" das instancias de classe produto

if __name__ == '__main__':
    main()
