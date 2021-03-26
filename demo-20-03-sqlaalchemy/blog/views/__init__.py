from flask import Flask


def init_app(app: Flask):
    from blog.views.user_view import bp_user
    app.register_blueprint(bp_user)

    from blog.views.post_view import bp_post
    app.register_blueprint(bp_post)
