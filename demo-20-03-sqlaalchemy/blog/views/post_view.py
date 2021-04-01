from flask import request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from flask import Blueprint

from blog.models.post_model import PostModel
from blog.models.user_model import UserModel

bp_post = Blueprint("post_view", __name__, url_prefix="/posts")


@bp_post.route("/", methods=["POST"])
@jwt_required()
def create_post():
    session = current_app.db.session
    user_id = get_jwt_identity()

    body = request.get_json()
    title = body.get("title")
    content = body.get("content")

    found_user: UserModel = UserModel.query.get(user_id)
    if not found_user:
        return {"msg": "User not found"}, HTTPStatus.NOT_FOUND

    new_post = PostModel(title=title, content=content)

    found_user.post_list.append(new_post)
    session.add(found_user)
    session.commit()

    return {
        "post": {
            "id": new_post.id,
            "title": new_post.title,
            "content": new_post.content,
        }
    }


@bp_post.route("/", methods=["GET"])
def list_user_posts():
    try:
        session = current_app.db.session
        user_id = get_jwt_identity()

        page = int(request.args.get("page"))
        per_page = int(request.args.get("per_page"))

        posts_list = (
            session.query(PostModel, UserModel)
            .join(UserModel)
            .filter(UserModel.id == user_id)
            .paginate(page=page, per_page=per_page, error_out=False)
            .items
        )

        if not posts_list:
            return {"msg": "This page does not exist"}, HTTPStatus.NOT_FOUND

        return {
            "posts": [
                {
                    "nickname": user.nickname,
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                }
                for post, user in posts_list
            ]
        }, HTTPStatus.OK

    except ValueError:
        return {
            "msg": "Values in query parametters are not in integer format"
        }, HTTPStatus.BAD_REQUEST

    # found_user = UserModel.query.get(user_id)

    # user_posts = found_user.post_list

    # return {
    #     "posts": [
    #         {"id": post.id, "title": post.title, "content": post.content}
    #         for post in user_posts
    #     ]
    # }


@bp_post.route("/<int:post_id>", methods=["DELETE"])
@jwt_required(refresh=True)
def delete_post(post_id):
    session = current_app.db.session
    found_post = PostModel.query.get(post_id)
    session.delete(found_post)
    session.commit()

    return {"msg": "Post deleted"}, HTTPStatus.OK
