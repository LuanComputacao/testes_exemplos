from flask import Blueprint, request, current_app
from http import HTTPStatus

from app.models.band_model import BandModel
from app.serializers.band_serializer import BandSchema

bp_band = Blueprint("bp_band", __name__, url_prefix="/api")


@bp_band.route('/band', methods=["POST"])
def band():
    session = current_app.db.session

    data = request.get_json()
    band = BandModel(name=data["name"])
    session.add(band)
    session.commit()

    serialized = BandSchema().dump(band)

    return serialized, HTTPStatus.CREATED
