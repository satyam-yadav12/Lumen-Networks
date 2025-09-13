from flask import jsonify, Blueprint, request
from marshmallow import ValidationError
from flask_jwt_extended import  unset_jwt_cookies, get_jwt_identity, jwt_required

from ..services.authorization_helpers import validate_user_data, create_user_data, generate_and_set_tokens, check_password_and_user_email
from ..utils.db import insert_user_data, search_by_email
from ..services.cloudinary_functions import upload_profile_image

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=['POST'])
def register():
    data = request.form
    img = request.files['Profile_picture']
    username = str(data.get('Full_name'))+str(data.get('Mobile')[2:7])
    

    try:
        validate_data = validate_user_data(data)
        profile_img_url = "None"
        if(img):
            profile_picture = upload_profile_image(img, username)
            if(profile_picture):
                profile_img_url = profile_picture['Url']
        
        if(validate_data):
            user_details = create_user_data(data, username, profile_img_url)
            insertion = insert_user_data(user_details)

 
            if(insertion):
                return jsonify({"msg": "user registered success fully", "insertion id": insertion, 'validation result': validate_data, "profile": profile_img_url, "cloudinary_function": profile_picture['Url']}), 200
            else:
                raise Exception("error inserting user data")

    except ValidationError as error:
        return jsonify({'msg': "some error occured", "errors" : error.messages}), 400
    except ValueError as e: 
        return jsonify({"unexpected error occured": str(e)}),400
    except Exception as e:
        return jsonify({"unexpected error occured": str(e)}),400



@auth_bp.route("/login", methods=['POST'])
def login():
    details = request.json
 
    try:
        user_details, check_password = check_password_and_user_email(details)
        if(check_password and user_details):
            additional = {
                "username": user_details['Username'],
            }

            return generate_and_set_tokens(user_details, additional)
        else:
            raise Exception("incorrect user email or password")
        
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
   

@auth_bp.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    resp = jsonify({"msg": "logout Successful"})
    unset_jwt_cookies(resp)
    return resp


#route to check user details test in thunderclients, remove it after work
#unnecessary stuff

@auth_bp.route("/user/<id>", methods=['GET'])
def get_user(id):
    details = search_by_email(id)
    return jsonify({'details': details})

    
@auth_bp.route("/")
def get_Home():
    return jsonify({"msg":"app is running"})

@auth_bp.route("/me", methods=['GET'])
@jwt_required()
def get_me():
    id = get_jwt_identity()
    return jsonify({"msg": f"welcome {id}!"})
