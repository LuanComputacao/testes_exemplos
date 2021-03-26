from flask import Blueprint, request, current_app
from http import HTTPStatus

from blog.models.user_model import UserModel


bp_user = Blueprint('user_view', __name__, url_prefix='/users')


@bp_user.route('/', methods=['POST'])
def create_user():
    session = current_app.db.session

    body = request.get_json()
    nickname = body.get('nickname')
    email = body.get('email')
    password = body.get('password')

    new_user = UserModel(nickname=nickname, email=email)
    new_user.password = password
    session.add(new_user)
    session.commit()

    return {
        'user': {
            'nickname': new_user.nickname,
            'email': new_user.email
    }}, HTTPStatus.CREATED


@bp_user.route('/', methods=['GET'])
def list_users():
    ...
