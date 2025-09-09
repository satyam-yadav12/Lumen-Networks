import cloudinary
import cloudinary.uploader
from flask import Flask, jsonify

def upload_profile_image(img, username):
    try:
        upload_results = cloudinary.uploader.upload(img, public_id = username, folder="/Profile_pictures", overwrite = True)
        return jsonify({'msg': "profile image updated successfuly", "Url": upload_results['secure_url'], "status": 201})
    except Exception as e:
        return jsonify({"Unexpected error occurred": {e}, "status": 401})



