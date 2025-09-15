from marshmallow import fields, Schema

class feedback_validation(Schema):
    "Email" = fields.Email(
        required=True,
        error_messages={"invalid Email": "Enter a valid Email"}
    )
    "Name" = fields.String(
        required=True,
        error_messages={"required":"name is required"}
    )
    "Title"= fields.String(
        required=True,
        error_messages={"required":"name is required"}
    )
    "Description" = fields.String(
        required=True,
        error_messages={"required":"name is required"}
    )