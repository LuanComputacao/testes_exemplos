from flask import Flask


def init_app(app: Flask):
    from app.views.band_view import bp_band
    app.register_blueprint(bp_band)

    from app.views.band_profile_view import bp_band_profile
    app.register_blueprint(bp_band_profile)

    from app.views.music_view import bp_music
    app.register_blueprint(bp_music)

    from app.views.genre_view import bp_genre
    app.register_blueprint(bp_genre)

    from app.views.band_genre_view import bp_band_genre
    app.register_blueprint(bp_band_genre)