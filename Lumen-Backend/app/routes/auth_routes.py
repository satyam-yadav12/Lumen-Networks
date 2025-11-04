from flask import Flask, Blueprint
from flask_jwt_extended import jwt_required
from ..controllers.auth_controllers import register, login, logout, get_me
from ..controllers.google_auth import google_login, authorize_by_google

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register_user():
    return register()


@auth_bp.route("/login", methods=["POST"])
def login_user():
    return login()


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout_user():
    return logout()


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    return get_me()


@auth_bp.route("/google/login")
def login_with_google():
    return google_login()


@auth_bp.route("/google/login/callack")
def get_details_from_google():
    return authorize_by_google()
