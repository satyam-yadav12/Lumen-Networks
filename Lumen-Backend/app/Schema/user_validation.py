from marshmallow import Schema, validate, ValidationError, validates_schema, fields


class user_registration_schema(Schema):
    
    Full_name = fields.String(
        required = True, 
        error_messages = {"required": "Full Name of the user is required"},
        validate = validate.Length(min=3, max=20, error="Name of the user should be atleast 3 character long")
    )

    Email = fields.Email(
        required=True, 
        error_messages = {'Email Error': 'Enter a valid Email'}
        )
    Mobile = fields.String(
        required= True,
        error_messages={"required": "phone number required"},
        validate=validate.Regexp(r"^[6-9]\d{9}$", error="invalid mobile number")
    )
    Password = fields.String(
        required=True,
            validate=validate.Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,12}$",
            error="Password must be 8 – 12 character long with uppercase, lowercase, digit, and special character."
        )
    )
    
    ConfirmPassword = fields.String(
        required=True,
        error_messages={"required": "confirm password field should not be empty"}
    )

    City= fields.String(
        error_messages={"type error": 'city should be a string'}
    )

    Gender = fields.String(
        required=True,
        validate=validate.OneOf(['Male', 'Female', 'Other'], error="invalid gender value")
    )

    Agree = fields.Boolean(
        required=True,
        error_messages = {"required" :"True or false required"}
    )

    Profile_picture = fields.String(
        error_messages={"must be string": True}
    )
    Last_login = fields.String(

    )
    Contribution_count = fields.String(

    )

    @validates_schema
    def match_confirmPassword(self, data, **kwargs):
        if(data.get('Password') != data.get('ConfirmPassword')):
            raise ValidationError("Password and confirm password must match", field_name="ConfirmPassword")

        if(data.get("Agree") != True):
            raise ValidationError("you must accept terms and condtion", field_name="Agree")