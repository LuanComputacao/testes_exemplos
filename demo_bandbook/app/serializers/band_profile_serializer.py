from app.models.band_model import BandModel
from app.models.band_profile_model import BandProfileModel

def BandProfileSerializer(band_id: int):
    band = BandModel.query.get(band_id)
    profile = BandProfileModel.query.filter_by(band_id=band_id).first()

    return {
        "id": profile.id,
        "state": profile.state,
        "country": profile.country,
        "ein": profile.ein,
        "band": band.name,
    }
