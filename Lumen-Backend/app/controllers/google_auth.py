from flask import Flask, jsonify, Blueprint, url_for, make_response
from ..extensions import oauth
from ..extensions import mongo
from ..services.authorization_helpers import generate_new_username
from ..services.cloudinary_functions import upload_profile_image
from ..utils.db import insert_user_data, search_by_email
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, decode_token
from dotenv import load_dotenv
import os


google_auth_bp = Blueprint("google_auth", __name__)
load_dotenv()
google = oauth.create_client("google")


@google_auth_bp.route("/login")
def google_login():
    redirect_url  = url_for("google_auth.authorize_by_google", _external = True)
    print(redirect_url)
    return google.authorize_redirect(redirect_url)

@google_auth_bp.route("/login/callback") #change the route name and register it in google cloud
def authorize_by_google():
    token  = google.authorize_access_token()
    id_info = token.get('userinfo')

    if not id_info:
        return jsonify({"msg": "google login fail", "status": 401})
    
    return generate_token_by_google_info(id_info)


def generate_token_by_google_info(data):
    Full_name = data.get('name')
    profile_picture = data.get('picture')
    email = data.get('email')
    try:
        user_registered = search_by_email(email)

        

        if not user_registered:
                # generate_new_and_unique_Username write function here
                username  = generate_new_username(Full_name)

                profile_img_url = "None"
                if(profile_picture):
                    upload_profile_img = upload_profile_image(profile_picture, username)
                    profile_img_url = upload_profile_img['Url']


                user_details ={
                    "Full_name": Full_name,
                    "Email": email,
                    "Username": username,
                    "Agree":True,
                    'Profile_picture': profile_img_url,
                    'Last_login': "None",
                    'Contribution_count': "None"
                }

                insert_user_data(user_details)
    
        #generate token
        additional = {
            "username" :username
        }

        access_token = create_access_token(identity=email, additional_claims=additional)
        refresh_token = create_refresh_token(identity=email, additional_claims=additional)

        jti = decode_token(refresh_token)['jti']
        jti_id = mongo.db.jti_validation.insert_one({"jti":jti, "valid": True}).inserted_id

        # resp = jsonify({'msg': 'login successful', 'user name': user_details['Username'], "access_toke": access_token, "refresh_token": refresh_token, "jti": jti, "jti id": jti_id})
        redirect_uri = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
        resp = make_response(f"""
            <html>
            <body>
            <div><p>Login Success</p>
            <br/>
            <a href="{redirect_uri}">Click here</a><span> to go to Home page</span>
            </body>
            <script>
            window.location.href = "{redirect_uri}";
            </script>
            </html>
            """)

        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        return resp
    except Exception as e:
        return jsonify({"error": {e}}), 500

        

