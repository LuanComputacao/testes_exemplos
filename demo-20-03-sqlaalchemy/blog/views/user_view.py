from flask import Blueprint, request, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http import HTTPStatus
from datetime import timedelta

from blog.models.user_model import UserModel
from blog.models.profile_model import ProfileModel


bp_user = Blueprint("user_view", __name__, url_prefix="/users")


@bp_user.route("/signup", methods=["POST"])
def signup():
    session = current_app.db.session

    body = request.get_json()
    nickname = body.get("nickname")
    email = body.get("email")
    password = body.get("password")

    new_user = UserModel(nickname=nickname, email=email)
    new_user.password = password
    session.add(new_user)
    session.commit()

    access_token = create_access_token(
        identity=new_user.id, expires_delta=timedelta(days=7)
    )
    fresh_token = create_access_token(
        identity=new_user.id, expires_delta=timedelta(days=14), fresh=True
    )

    return {
        "user": {
            "access_token": access_token,
            "fresh_token": fresh_token,
            "nickname": new_user.nickname,
            "email": new_user.email,
        }
    }, HTTPStatus.CREATED


@bp_user.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")

    found_user: UserModel = UserModel.query.filter_by(email=email).first()

    if not found_user or not found_user.check_password(password):
        return {"msg": "User not found"}, HTTPStatus.BAD_REQUEST

    access_token = create_access_token(
        identity=found_user.id, expires_delta=timedelta(days=7)
    )
    fresh_token = create_access_token(
        identity=found_user.id, fresh=True, expires_delta=timedelta(days=14)
    )

    return {"access_token": access_token, "fresh_token": fresh_token}


@bp_user.route("/refresh", methods=["GET"])
@jwt_required(fresh=True)
def refresh():
    user_id = get_jwt_identity()

    access_token = create_refresh_token(
        identity=user_id, expires_delta=timedelta(days=7)
    )

    return {"access_token": access_token}


@bp_user.route("/", methods=["GET"])
@jwt_required()
def list_users():
    session = current_app.db.session

    email_filter = request.args.get("email_filter")
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))

    list_of_users = (
        session.query(
            UserModel.nickname, UserModel.email, ProfileModel.age, ProfileModel.bio
        )
        .join(ProfileModel)
        .filter(UserModel.email.like(email_filter))
        .paginate(page=page, per_page=per_page, error_out=False)
        .items
    )

    return {
        "users": [
            {"nickname": nickname, "email": email, "age": age, "bio": bio}
            for nickname, email, age, bio in list_of_users
        ]
    }, HTTPStatus.OK

    # if username_filter:
    #     list_of_users = (
    #         UserModel.query.filter(UserModel.nickname.like(f"{username_filter}"))
    #         .order_by(UserModel.nickname)
    #         .all()
    #     )
    #     # list_of_users = UserModel.query.filter_by(city=...).all()
    # else:
    #     list_of_users = UserModel.query.all()

    # return {
    #     "users": [
    #         {"id": user.id, "nickname": user.nickname, "email": user.email}
    #         for user in list_of_users
    #     ]
    # }


@bp_user.route("/get/", methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    found_user: UserModel = UserModel.query.get(user_id)

    if not found_user:
        return {"msg": "User not found"}, HTTPStatus.NOT_FOUND

    return {
        "user": {"nickname": found_user.nickname, "email": found_user.email},
    }


@bp_user.route("/", methods=["PATCH", "PUT"])
@jwt_required()
def update_user():
    try:
        session = current_app.db.session
        body = request.get_json()
        user_id = get_jwt_identity()

        email = body["email"]
        nickname = body["nickname"]

        found_user: UserModel = UserModel.query.get(user_id)
        found_user.email = email
        found_user.nickname = nickname

        session.add(found_user)
        session.commit()

        return {
            "user": {
                "id": found_user.id,
                "nickname": found_user.nickname,
                "email": found_user.email,
            }
        }, HTTPStatus.OK
    except KeyError:
        return {"msg": "Verify the request body"}, HTTPStatus.BAD_REQUEST
