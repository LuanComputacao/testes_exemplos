from marshmallow import fields
from . import ma
from flask_marshmallow import fields

from app.models.music_model import MusicModel
from app.serializers.band_serializer import BandSchema

class MusicBandSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MusicModel

    id = ma.auto_field()
    name = ma.auto_field()

    band = ma.HyperlinkRelated('band')
    # band_name = fields.Nested(BandSchema, required=True)
