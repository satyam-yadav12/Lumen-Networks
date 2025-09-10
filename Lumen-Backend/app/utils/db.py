from ..extensions import mongo


#database name auth_student
def search_by_email(email):
    user_details = mongo.db.auth_student.find_one({"Email": email})

    return user_details

def search_by_username(username):
    user_details = mongo.db.auth_student.find_one({"Username": username})

    return user_details

def insert_user_data(data):
    insertion_id = mongo.db.auth_student.insert_one(data).inserted_id
    return insertion_id

def update_user_data(email, data):
    user_details  = search_by_email(email)
    if not user_details:
        raise ValueError("email not registered")
    mongo.db.auth_student.update_one({"Email": email}, {"$set": data})

def update_without_search(email, data):
    mongo.db.auth_student.update_one({"Email": email}, {"$set": data})