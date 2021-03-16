from flask import Blueprint
from ..models.character_model import RickAndMortyImage


bp = Blueprint('character_route', __name__)


@bp.route('/character')
def character():
    rnm_image = RickAndMortyImage()

    response = rnm_image.get_images()

    return {'msg': response}
