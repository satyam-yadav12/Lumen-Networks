from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from ..services.collection_helpers import create_collection_data
from ..utils.db import insert_collection_data, delete_collection_data, search_collection_of_user, check_if_like_exist

collection_bp = Blueprint("collection", __name__)

@collection_bp.route("/save/<img_id>", methods=['POST'])
@jwt_required()
def save_to_collection(img_id):
    user_name = get_jwt()['username']
    try:
        liked = check_if_like_exist(img_id, user_name)
        if not liked:
            data = create_collection_data(img_id, user_name)
            insertion = insert_collection_data(data)
            return jsonify({'msg': "success", "insert id": insertion}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@collection_bp.route("/unsave/<img_id>", methods =['DELETE'])
@jwt_required()
def unsave_from_collection(img_id):
    user_name = get_jwt()['username']
    delete_collection_data(user_name, img_id)
    return jsonify({'msg': "success"}), 200

@collection_bp.route("/collection", methods =['GET'])
@jwt_required()
def get_collection_of_user():
    user_name = get_jwt()['username']
    collection = search_collection_of_user(user_name)
    return jsonify({"msg": "success", "collection":collection}), 200