from flask import Flask


def init_app(app: Flask):
    from app.views.band_view import bp_band
    app.register_blueprint(bp_band)

    from app.views.band_profile_view import bp_band_profile
    app.register_blueprint(bp_band_profile)