#  WARNING: This file contains an incomplete JWT auto-refresh implementation. The token refresh happens after route execution, causing the first request to fail with "token expired" before new tokens are set. Do not use or copy these routes in production.

from flask import Flask, blueprints, g, jsonify, request
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity,
    decode_token,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
)
from werkzeug.exceptions import Unauthorized
from ..utils.db import token_is_not_revoked, revoke_refresh_token, save_new_jti


def verify_and_refresh_token(app):

    @app.before_request
    def check_access_refresh_token():
        if request.path in ["/login", "/register", "/static"]:
            return None
        try:

            verify_jwt_in_request()
            g.user = get_jwt_identity()
            return None
        except Exception as e:

            # refresh_token = None (use it if name error occurs)
            if "expired" in str(e).lower():
                old_refresh_token = request.cookies.get("refresh_token_cookie")
            if not old_refresh_token:
                raise Unauthorized("Missing refresh token")

            try:
                decoded_refresh = decode_token(old_refresh_token)
                id = decoded_refresh["sub"]
                jti = decoded_refresh["jti"]

                check_revokation = token_is_not_revoked(
                    jti
                )  # BUG: do not works all the time, code breaks from here often

                if not check_revokation:  # create function in utils
                    raise Unauthorized("Invalid or reused refresh token")

                revoke_refresh_token(jti)

                access_token = create_access_token(identity=id)
                refresh_token = create_refresh_token(identity=id)

                new_jti = decode_token(refresh_token)["jti"]

                save_new_jti(new_jti)  # create function in utils
                g.refresh = refresh_token
                g.access = access_token

                # BUG: refresh token or access token does not attached in cookies so in first try the request always returns "Token has expired"
                return None

            except Exception:
                raise Unauthorized("Session expired, please login again")

    @app.after_request  # FIXME: token are always attached after ongoing request returns 401
    def attach_token(response):
        if hasattr(g, "refresh") and hasattr(g, "access"):
            set_access_cookies(response, g.access)
            set_refresh_cookies(response, g.refresh)
        return response
