from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.band_profile_model import BandProfileModel
from app.serializers.band_profile_serializer import BandProfileSerializer

bp_band_profile = Blueprint("bp_band_profile", __name__, url_prefix="/api")


@bp_band_profile.route('/band_profile', methods=['POST'])
def band_profile():
    session = current_app.db.session

    data = request.get_json()
    profile = BandProfileModel(
        state=data["state"],
        country=data["country"],
        ein=data["ein"],
        band_id=data["band_id"],
    )

    session.add(profile)
    session.commit()

    serializer = BandProfileSerializer(data['band_id'])

    return serializer, HTTPStatus.CREATED
