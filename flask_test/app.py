from flask import Flask, render_template, request
from main import soma

app = Flask(__name__)


@app.route('/')
@app.route('/<nome>')
def home(nome: str = None):
    return render_template('index.html', nome=nome)


@app.route('/soma/', methods=['POST'])
def faz_soma():
    numeros = request.get_json()
    r = soma(
        numeros.get('n1', 0),
        numeros.get('n2', 0)
    )

    return {
        'status': 'ok',
        'resultado': r
    }
