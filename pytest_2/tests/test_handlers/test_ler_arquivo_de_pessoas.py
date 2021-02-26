import csv
import os

from src.handlers import ler_arquivo_de_pessoas


def test_deve_ler_um_arquivo_com_dados_de_pessoas(arquivo_de_dados_de_pessoas, pessoa_filename, pessoas_fieldnames,
                                                  pessoa_fake):
    filename = pessoa_filename

    with open(filename, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=pessoas_fieldnames)
        dicionario_de_uma_pessoa = dict(zip(pessoas_fieldnames, pessoa_fake))
        writer.writerow(dicionario_de_uma_pessoa)

    result = ler_arquivo_de_pessoas(filename)

    assert os.path.isfile(pessoa_filename) == True
    assert len(result) == 1
    assert result[0] == dicionario_de_uma_pessoa
