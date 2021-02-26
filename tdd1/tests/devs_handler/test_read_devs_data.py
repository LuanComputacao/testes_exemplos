import csv

from src.devs_handler import read_devs_data
from os.path import isfile
from os import remove
from faker import Faker
from pytest import fixture


@fixture(scope='function')
def dev_fielnames():
    return ['First Name', 'Last Name', 'email cadastrado no canvas']


@fixture(scope='function')
def devs_data_filename():
    return 'test_devs_data.csv'


@fixture(scope='function')
def fake_user(dev_fielnames):
    fake = Faker()
    fake_data = [fake.first_name(), fake.first_name(), fake.email()]
    return dict(zip(dev_fielnames, fake_data))


@fixture(scope='function')
def devs_data_file(devs_data_filename, fake_user, dev_fielnames):
    # antes de executar a função de testes
    with open(devs_data_filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=dev_fielnames)
        writer.writeheader()
        writer.writerow(fake_user)

    yield None  # aqui executa a função de teste

    # depois de executar a função de testes
    remove(devs_data_filename)


def test_deve_fazer_a_leitura_de_uma_arquivo_com_os_dados_dos_devs(devs_data_file, devs_data_filename, fake_user):
    given = devs_data_filename
    result = read_devs_data(given)
    expected = fake_user

    assert isfile(given) == True
    assert result[0] == expected
