import csv


def ler_arquivo_de_pessoas(filename):
    with open(filename, 'r') as f:
        return [
            {
                'CPF': pessoa['CPF'],
                'Nome': pessoa['Nome'],
                'Inadimplencia': int(pessoa['Inadimplencia'])
            }
            for pessoa in csv.DictReader(f)
        ]
