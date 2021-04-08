from . import ma
from app.models.track_model import TrackModel


class TrackSchema(ma.Schema):
    class Meta:
        model = TrackModel

    id = ma.Integer()
    name = ma.String()
    album = ma.String()


track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)
