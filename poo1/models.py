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

    def usando_args(self, *args):
        print(args)

    def __str__(self):
        return f'{self.nome}: R${self.preco}'

    def __add__(self, other):
        return self.preco + other.preco

    def __len__(self):
        return int(self.peso)
