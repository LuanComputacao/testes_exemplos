from csv import DictWriter, DictReader
from os import stat


class EstoqueModel:
    def __init__(self, filename) -> None:
        self.filename = filename

    def estocar(self, **kwargs):
        cabecalho = ['id', *kwargs.keys()]
        with open(self.filename, 'a') as file:
            writer = DictWriter(file, fieldnames=cabecalho)
            if not stat(self.filename).st_size:
                writer.writeheader()
            novo_id = self._obter_id()
            writer.writerow({'id': novo_id, **kwargs})

    def listar_livros(self):
        with open(self.filename) as file:
            reader = DictReader(file)
            registros_lista = list(reader)
            return registros_lista

    def obter_livro(self, livro_id):
        with open(self.filename) as file:
            reader = DictReader(file)
            buscador = (registro for registro in reader if registro.get('id') == livro_id)
            try:
                buscado = next(buscador)
                return buscado
            except StopIteration:
                raise StopIteration('Nao foi encontrado')

    def _obter_id(self):
        with open(self.filename) as file:
            reader = DictReader(file)
            if not list(reader):
                return 1
            ultimo_registro = list(reader)[-1]
            return int(ultimo_registro.get('id')) + 1
