from ..extensions import mongo

def search_by_email(email):
    user_details = mongo.db.auth_student.find_one({"Email": email})

    return user_details

def search_by_username(username):
    user_details = mongo.db.auth_student.find_one({"Username": username})

    return user_details

def insert_user_data(data):
    insertion_id = mongo.db.auth_student.insert_one(data).inserted_id
    return insertion_id