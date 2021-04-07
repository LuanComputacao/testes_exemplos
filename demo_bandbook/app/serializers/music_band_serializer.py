from . import ma

from app.models.music_model import MusicModel
from app.serializers.band_serializer import BandSchema

class MusicBandSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MusicModel

    id = ma.auto_field()
    name = ma.auto_field()

    band = ma.Nested(BandSchema(exclude=['id']), required=True)
