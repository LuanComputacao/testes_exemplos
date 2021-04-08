from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    from app.views.track_view import AllTracks, Track

    api.add_resource(AllTracks, "/api/track")
    api.add_resource(Track, "/api/track", endpoint="/track", methods=["POST"])
    api.add_resource(
        Track,
        "/api/track/<int:req_id>",
        endpoint="/track/<int:req_id>",
        methods=["GET", "PATCH", "DELETE"],
    )
