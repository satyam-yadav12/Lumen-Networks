#feedback controller
from flask import request, Blueprint, jsonify
from marshmallow import ValidationError
from ..Schema.feedback_validation import feedback_validation
from ..utils.db import insert_feedback_data, insert_content_report
from flask_jwt_extended import jwt_required, get_jwt

feedback_bp = Blueprint("feedback", __name__)
@feedback_bp.route("/feedback", methods=['POST'])
def send_feedback():
    data = request.json
    Schema = feedback_validation()
    try:
        validate = Schema.load(data)
        data_to_upload = create_feedback_data(data)
        insertion = insert_feedback_data(data_to_upload)

        return jsonify({"msg": "success", "insertion id": insertion}), 200
    except ValidationError as e:
        return jsonify({"error": e.messages})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@feedback_bp.route("/reportcontent/<id>", methods=['POST'])
@jwt_required()
def send_content_violetion_report(id):
    data = request.json
    user = get_jwt()['username']
    details = {
        "img_id": id,
        "report_by": user,
        "reson": data.get("reason")
    }
    insertion = insert_content_report(details)
    return jsonify({"msg": "success", "insert id": insertion}), 200

    
def create_feedback_data(data):
    details = {
        "Email": data.get("Email"),
        "Name": data.get("Name"),
        "Title": data.get("Title"),
        "Description": data.get("Description")

    }
    return details