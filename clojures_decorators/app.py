from flask import Flask
from main import retorna_dict
app = Flask(__name__)

@app.route('/')
def home():
    p1 = retorna_dict('maçã', 1.56)
    return p1