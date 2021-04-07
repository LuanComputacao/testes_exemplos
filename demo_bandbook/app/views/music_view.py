from flask import Blueprint, request, current_app
from http import HTTPStatus

from ipdb.__main__ import set_trace

from app.models.music_model import MusicModel
from app.serializers.music_band_serializer import MusicBandSchema

bp_music = Blueprint('bp_music', __name__, url_prefix='/api')

@bp_music.route('/music', methods=['POST'])
def music():
    session = current_app.db.session

    data = request.get_json()
    music = MusicModel(name=data['name'], band_id=data['band_id'])

    session.add(music)
    session.commit()

    serializer = MusicBandSchema()
    serialized = serializer.dump(music)

    set_trace()

    return serialized, HTTPStatus.CREATED