from flask_restful import Resource, reqparse, current_app
from http import HTTPStatus

from app.models.track_model import TrackModel
from app.schemas.track_schema import track_schema, tracks_schema


class AllTracks(Resource):
    def get(self):
        all_tracks = TrackModel.query.all()
        serializer = tracks_schema.dump(all_tracks)
        return {"data": serializer}, HTTPStatus.OK


class Track(Resource):
    def get(self, req_id):
        track = TrackModel.query.get(req_id)
        serializer = track_schema.dump(track)
        return {"data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()

        parse.add_argument("name", type=str, required=True)
        parse.add_argument("album", type=str, required=True)

        args = parse.parse_args()

        new_track = TrackModel(**args)
        session = current_app.db.session
        session.add(new_track)
        session.commit()

        serializer = track_schema.dump(new_track)
        return {"data": serializer}, HTTPStatus.CREATED

    def patch(self, req_id):
        parse = reqparse.RequestParser()

        parse.add_argument("name", type=str)
        parse.add_argument("album", type=str)

        args = parse.parse_args()

        track = TrackModel.query.get_or_404(req_id)

        for key, value in args.items():
            if value:
                setattr(track, key, value)

        session = current_app.db.session
        session.add(track)
        session.commit()

        serializer = track_schema.dump(track)
        return {"data": serializer}, HTTPStatus.OK

    def delete(self, req_id):
        track = TrackModel.query.get_or_404(req_id)
        session = current_app.db.session
        session.delete(track)
        session.commit()

        return {"data": "NO CONTENT"}, HTTPStatus.NO_CONTENT
