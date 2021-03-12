from flask import Flask
from pytest import fixture
from json import loads

from app import create_app


@fixture
def app():
    return create_app()


@fixture
def client(app: Flask):
    return app.test_client()


def test_estocar_status(client):
    given={
        'name': 'Pedro Augusto',
        'address': 'Rua Sem Nome'
    }
    response = client.post('/estoque', json=given)
    assert response.status_code == 201


def test_estocar(client):
    given={
        'name': 'Pedro Augusto',
        'address': 'Rua Sem Nome'
    }
    response = client.post('/estoque', json=given)

    assert given == loads(response.get_data(as_text=True))


def test_listar_livros(client):
    response = client.get('/estoque')
    assert response.status_code == 200
