from pytest import fixture
from csv import DictReader
from os.path import isfile
from os import remove

from app.models.estoque_model import EstoqueModel


FILENAME = 'db_teste.csv'


@fixture
def estoque():
    yield EstoqueModel(FILENAME)
    if isfile(FILENAME):
        remove(FILENAME)


@fixture
def novo_livro():
    return {"livro": "HP", "autor": "Um Autor"}


def test_esta_escrevendo_no_csv(estoque: EstoqueModel, novo_livro):
    estoque.estocar(**novo_livro)

    with open(FILENAME) as file:
        reader = DictReader(file)
        assert list(reader)[0] == {'id': '1', **novo_livro}
