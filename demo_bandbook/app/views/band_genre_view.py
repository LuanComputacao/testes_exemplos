from flask import Blueprint, request, current_app
from http import HTTPStatus

from app.models.band_genre_model import BandGenreModel
from app.models.band_model import BandModel
from app.models.genre_model import GenreModel


bp_band_genre = Blueprint('bp_band_genre', __name__, url_prefix='/api')


@bp_band_genre.route('/band_genre', methods=['POST'])
def band_genre():
    session = current_app.db.session

    data = request.get_json()
    band_genre = BandGenreModel(
        band_id=data['band_id'], genre_id=data['genre_id'])

    session.add(band_genre)
    session.commit()

    band = BandModel.query.filter_by(id=band_genre.band_id).first()
    genre = GenreModel.query.get(band_genre.genre_id)

    return {
        'id': band_genre.id,
        'band': band.name,
        'genre': genre.name
    }, HTTPStatus.CREATED
