class Etiqueta:
    def __init__(self, codigo: str):
        self.codigo = codigo
        self.etiqueta = self.criar_etiqueta(codigo)

    def criar_etiqueta(self, codigo):
        return str(codigo) + 'ABCD'

    def __repr__(self):
        return f'<Etiqueta {self.codigo} {self.etiqueta} >'


class Produto:

    def __init__(self, id: int, nome: str, preco: float, codigo: int, peso: int = 1, tipo: str = 'prateleira'):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.atribui_preco(preco)
        self.tipo = tipo
        self.etiqueta = Etiqueta(codigo)

    def atribui_preco(self, preco: float):
        self.preco = 0.01 if preco < 0 else preco

    def atualizar(self, nome: str, preco: float):
        self.nome = nome
        self.atribui_preco(preco)

    def __str__(self):
        return f'{self.nome} ({self.tipo}): R${self.preco}'

    def __add__(self, other):
        return self.preco + other.preco

    def __len__(self):
        return int(self.peso)


class Frio(Produto):
    MANTER_CONGELADO = True

    def __init__(self, id: int, nome: str, preco: float, codigo: int, peso: int = 1):
        super().__init__(id, nome, preco, codigo, peso, 'frio')


class Bebidas(Frio):
    MANTER_CONGELADO = False

    def __init__(self, id: int, nome: str, preco: float, codigo: int, peso: int = 1, restricao=False):
        super().__init__(id, nome, preco, codigo, peso)
        self.restricao = restricao

    def atribui_preco(self, preco: float):
        self.preco = 5 if preco < 0 else preco


class Pacote:
    def __init__(self, produto: Produto):
        self.produto = produto

    def __str__(self):
        return f'<Pacote {self.produto} >'
