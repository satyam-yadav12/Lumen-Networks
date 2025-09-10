from flask import Flask, jsonify, Blueprint, request
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, unset_jwt_cookies
from ..Schema.user_validation import user_registration_schema
from ..utils.db import search_by_email, update_user_data, update_without_search
from marshmallow import ValidationError
from ..services.cloudinary_functions import upload_profile_image
user_profile_bp = Blueprint("user", __name__)

@user_profile_bp.route("profile", methods= ['GET'])
@jwt_required()
def get_profile():
    id = get_jwt_identity()
    user_details = search_by_email(id)
    filtered_user_data = filter_userdata(user_details, ["Password", "Agree"])
    return jsonify({"user details": filtered_user_data, "response_code": 201}), 201


@user_profile_bp.route("editprofile", methods=['PUT', "PATCH"])
@jwt_required()
def edit_profile():
    data = request.json
    id  = get_jwt_identity()
    Schema = user_registration_schema(partial=True)
    try:
        validate_data = Schema.load(data)
        if(validate_data):
            update_user_data(id, data)
        
        return jsonify({"msg": "profile update successfully"}), 201
        


    except ValidationError as err:
        return jsonify({"error": err.messages})
    except ValueError as e:
        return jsonify({"error": str(e)}), 401



@user_profile_bp.route("changepassword", methods=['PUT'])
@jwt_required()
def edit_password():
    id = get_jwt_identity()
    data = request.json
    Schema = user_registration_schema(partial=True)
    try:
        validate_data = Schema.load(data)
        hash_password =generate_password_hash(data.get("Password"))
        update_param = {"Password": hash_password}
        if(validate_data):
            update_user_data(id, update_param)
        
        resp = jsonify({"msg": "password updated successfully"})
        unset_jwt_cookies(resp)
        return resp
        

    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    except ValidationError as err:
        return jsonify({"error": err.messages})

@user_profile_bp.route("change-profile-picture", methods=["PUT", "PATCH"])
@jwt_required()
def change_profile_picture():
    id = get_jwt_identity()
    img= request.files["Profile_picture"]
    try:
        user_details = search_by_email(id)
        username = user_details['Username']
        update_param = {"Profile_picture":"None"}
        if(img):
            New_secure_uri= upload_profile_image(img, username)
            update_param = {"Profile_picture": New_secure_uri["Url"]}
        
        update_without_search(id, update_param)
        return jsonify({"msg": "profile image updated successfully", "secure_url": update_param}) , 201
    except ValueError as e:
        return jsonify({"error": str(e)}),  400



def filter_userdata(data, exclude_keys):
    filtered_data = {}
    for key, val in data.items():
        if(key not in exclude_keys):
            filtered_data[key] = val

    return filtered_data


