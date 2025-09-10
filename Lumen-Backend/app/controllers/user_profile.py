from flask import Flask, jsonify, Blueprint, request
from ..extensions import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.db import search_by_email

user_profile_bp = Blueprint("user", __name__)

@user_profile_bp.route("profile", methods= ['GET'])
@jwt_required()
def get_profile():
    id = get_jwt_identity()
    user_details = search_by_email(id)
    filtered_user_data = filter_userdata(user_details, ["Password", "Agree"])
    return jsonify({"user details": filtered_user_data, "response_code": 201}), 201


@user_profile_bp.route("editprofile", methods=['PUT'])
@jwt_required()
def edit_profile():
    data = request.json()


@user_profile_bp.route("changepassword", methods=['PUT'])
@jwt_required()
def edit_password():
    pass


def filter_userdata(data, exclude_keys):
    filtered_data = {}
    for key, val in data.items():
        if(key not in exclude_keys):
            filtered_data[key] = val

    return filtered_data


