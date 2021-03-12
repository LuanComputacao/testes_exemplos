from flask import Blueprint, request

from app.models.estoque_model import EstoqueModel


bp_estoque = Blueprint('bp_estoque', __name__)


@bp_estoque.route('/estoque', methods=['POST'])
def estocar():
    body = request.get_json()
    print(body)
    return body, 201


@bp_estoque.route('/estoque', methods=['GET'])
def listar_livros():
    return 'livros no estoque'


@bp_estoque.route('/estoque/<int:livro_id>')
def obter_livro(livro_id):
    return 'livro especifico'

