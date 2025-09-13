from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from ..services.user_content_helpers import generate_img_id, create_img_data_to_upload
from ..services.cloudinary_functions import upload_user_images, delete_cloudinary_img_by_user
from ..utils.db import insert_img_data, update_image_details_in_db, search_for_user_uploads, delete_image_details

user_content_bp = Blueprint("user_content", __name__)

@user_content_bp.route("/upload-new", methods=['POST'])
@jwt_required()
def upload_new_img():
    img_data = request.form
    img = request.files['picture']
    id = get_jwt()
    username = id['username']

    try:
        if username and img and img_data:
            
            img_id = generate_img_id(img_data['title'])
            if(img_id):
                cloudinary_response = upload_user_images(img, img_id, username)
                Uri, folder = cloudinary_response['Url'], cloudinary_response['folder']

            if(Uri, folder):
                img_collection_data = create_img_data_to_upload(img_data, Uri, folder, username, img_id)
            
            if(img_collection_data):
                insert_id = insert_img_data(img_collection_data)

            return jsonify({"msg": "image uploaded successfull", "insert_id": insert_id}), 200
    except Exception as e:
        return jsonify({"unexpected error occured": str(e)})

@user_content_bp.route("/uploads", methods=['GET'])
@jwt_required()
def get_user_uploads():
    id = get_jwt()['username']

    if(id):
        user_uploads = search_for_user_uploads(id)
    return jsonify({"msg": "user uploaded images are fetched", "data": user_uploads})



@user_content_bp.route("/uploads/<id>/update", methods=['PUT', 'PATCH'])
@jwt_required()
def update_img_details(id):
    data = request.json

    updated_img ={
        "title" :data['title'],
        "description" :data['description'],
        "tags": data['tags']
    }
    if(updated_img):
            update_image_details_in_db(id, updated_img)
    return jsonify({"msg": "image updated"})

@user_content_bp.route("/uploads/<id>/delete",  methods=['DELETE'])
@jwt_required()
def delete_user_img(id):
    user= get_jwt()['username']
    delete_cloudinary_img_by_user(id, user, "user_uploaded_img")
    delete_image_details(id)
    return jsonify({"msg": "image deleted successfull"}), 200

