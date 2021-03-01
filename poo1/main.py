class Produto:
    def __init__(self, id: int, nome: str, preco: float, peso: int = 1):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.atribui_preco(preco)

    def atribui_preco(self, preco: float):
        self.preco = 0.01 if preco < 0 else preco

    def atualizar(self, nome: str, preco: float):
        self.nome = nome
        self.atribui_preco(preco)

    def __str__(self):
        return f'{self.nome}: R${self.preco}'

    def __add__(self, other):
        return self.preco + other.preco

    def __len__(self):
        return int(self.peso)


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


if __name__ == '__main__':
    main()
