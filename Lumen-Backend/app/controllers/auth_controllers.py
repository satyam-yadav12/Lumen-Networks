from flask import Flask, jsonify, Blueprint, request
from ..extensions import mongo

from marshmallow import Schema, ValidationError
from ..Schema.user_validation import user_registration_schema
from Schema.update_profile_img import upload_profile_image
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, get_jwt_identity, jwt_required, decode_token

auth_bp = Blueprint("auth", __name__)



@auth_bp.route("/register", methods=['POST'])
def register():
    data = request.form
    img = request.files['Profile_picture']

    Schema = user_registration_schema()
    try:
        validate_data = Schema.load(data)
        username = str(data.get('Full_name'))+str(data.get('Mobile')[2:7])
        user_exist = mongo.db.auth_student.find_one({'Username':username})
        user_email = mongo.db.auth_student.find_one({'Email':data.get('Email')})


        try:
            if(user_exist):
                raise ValueError("user already exist")
            if(user_email):
                raise ValueError("Email already registered")
        except ValueError as e:
            return jsonify({'error': str(e)})
        
        if(img):
            profile_picture = upload_profile_image(img, username)
            if(profile_picture.status == 201):
                profile_img_url = profile_picture['Url']
            else:
                profile_img_url = "None"
        
        if(validate_data and not user_exist and not user_email):
            hashed_password = generate_password_hash(data.get("Password"))
            user_details ={
                "Full Name": data.get('Full_name'),
                "Email": data.get('Email'),
                "Phone": data.get('Mobile'),
                "Password": hashed_password,
                "Username": username,
                "City": data.get('City'),
                "Agree": data.get('Agree'),
                'Profile_picture': profile_img_url,
                'Last_login': "None",
                'Contribution_count': "None"
            }

            insertion = mongo.db.auth_student.insert_one(user_details).inserted_id

            return jsonify({"msg": "user registered success fully", "insertion id": insertion, 'validation result': validate_data}), 200


    except ValidationError as error:
        return jsonify({'msg': "some error occured", "errors" : error.messages}), 400
    
@auth_bp.route("/")
def get_Home():
    return jsonify({"msg":"app is running"})

@auth_bp.route("/login", methods=['POST'])
def login():
    data = request.json
    password = data.get('Password')
    user_details = mongo.db.auth_student.find_one({'Email': data.get('Email')})
    check_password = check_password_hash(user_details['Password'], password )

    try:
        if(check_password):
            additional = {
                "username": user_details['Username'], 
            }
            access_token = create_access_token(identity=user_details['Email'], additional_claims=additional)
            refresh_token = create_refresh_token(identity=user_details['Email'], additional_claims=additional)

            jti = decode_token(refresh_token)['jti']
            jti_id = mongo.db.jti_validation.insert_one({"jti":jti, "valid": True}).inserted_id

            resp = jsonify({'msg': 'login successful', 'user name': user_details['Username'], "access_toke": access_token, "refresh_token": refresh_token, "jti": jti, "jti id": jti_id})

            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)

            return resp
        else:
            raise ValueError("incorrect password or username")
    except ValueError as error:
        return jsonify({"error": str(error)})
   


@auth_bp.route("/me", methods=['GET'])
@jwt_required()
def get_me():
    id = get_jwt_identity()
    return jsonify({"msg": f"welcome {id}!"})


@auth_bp.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    unset_jwt_cookies()
    return jsonify({"msg": "logout Successful"})



@auth_bp.route("/user/<id>", methods=['GET'])
def get_user(id):
    details = mongo.db.auth_student.find({'Full Name': id})
    return jsonify({'details': details})

