from flask import Flask, Blueprint, g, jsonify, request
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity,
    decode_token,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    jwt_required,
    get_jwt,
)
from werkzeug.exceptions import Unauthorized
from ..utils.db import token_is_not_revoked, revoke_refresh_token, save_new_jti

refresh_token_bp = Blueprint("refresh", __name__)


# NOTE: refresh token rotation can be performed only with front-end
@refresh_token_bp.route("/action", methods=["POST"])
@jwt_required(refresh=True)
def refresh_old_token():
    try:

        decoded_refresh = get_jwt()

        id = decoded_refresh["sub"]
        jti = decoded_refresh["jti"]

        check_revokation = token_is_not_revoked(jti)

        if not check_revokation:
            raise Unauthorized("Invalid or reused refresh token")

        revoke_refresh_token(jti)

        access_token = create_access_token(identity=id)
        refresh_token = create_refresh_token(identity=id)

        new_jti = decode_token(refresh_token)["jti"]

        save_new_jti(new_jti)

        response = jsonify({"msg": "token refreshed successfully"})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response

    except Exception:
        raise Unauthorized("Session expired, please login again")
