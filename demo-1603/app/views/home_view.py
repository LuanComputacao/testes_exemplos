from flask import Blueprint, render_template
from ..models.character_model import RickAndMortyImage


bp = Blueprint('home_route', __name__)


@bp.route('/')
def home():
    rnm_image = RickAndMortyImage()
    response = rnm_image.get_images()

    return render_template('character.html', characters=response)
