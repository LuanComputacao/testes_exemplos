import csv
from random import randint

from faker import Faker
from pytest import fixture


@fixture(scope='function')
def pessoa_filename():
    return 'test_dados_de_pessoas.csv'


@fixture(scope='function')
def pessoas_fieldnames():
    return ['Nome', 'CPF', 'Inadimplencia']


@fixture(scope='function')
def pessoa_fake():
    faker = Faker(['pt_BR'])
    return [faker.name(), faker.cpf(), randint(0, 1)]


@fixture(scope='function')
def arquivo_de_dados_de_pessoas(pessoas_fieldnames, pessoa_filename):
    with open(pessoa_filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=pessoas_fieldnames)
        writer.writeheader()
    print('\nsetup')

    yield None

    print('\n tear down')