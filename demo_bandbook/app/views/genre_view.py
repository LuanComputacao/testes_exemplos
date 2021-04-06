from flask import Blueprint, request, current_app
from http import HTTPStatus

from app.models.genre_model import GenreModel

bp_genre = Blueprint('bp_genre', __name__, url_prefix='/api')

@bp_genre.route('/genre', methods=['POST'])
def genre():
    session = current_app.db.session
    data = request.get_json()
    if not data.get('name'):
        return {'detail': 'Missing key name'}, HTTPStatus.BAD_REQUEST

    try:
        genre = GenreModel(name=data['name'])
        session.add(genre)
        session.commit()

    except:
        return {'detail': 'BAD REQUEST'}, HTTPStatus.BAD_REQUEST


    return {
        'id': genre.id,
        'genre_name': genre.name
    }, HTTPStatus.CREATED