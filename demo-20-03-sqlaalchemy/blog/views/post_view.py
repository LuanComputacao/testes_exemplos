from flask import Blueprint

bp_post = Blueprint('post_view', __name__)


@bp_post.route('/posts/', methods=['POST'])
def create_post():
    ...

@bp_post.route('/posts/', methods=['GET'])
def list_user_posts():
    ...
