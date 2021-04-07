from . import ma
from app.models.band_model import BandModel


class BandSchema(ma.SQLAlchemySchema):
    class Meta:
        model = BandModel

    id = ma.auto_field()
    name = ma.auto_field()

