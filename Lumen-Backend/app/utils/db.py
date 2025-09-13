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


#database name user_imgs
def search_for_img_name(public_name):
    img_details  = mongo.db.user_imgs.find({"img_id": public_name})
    return img_details

def insert_img_data(data):
    insertion_id = mongo.db.user_imgs.insert_one(data).inserted_id
    return insertion_id

def update_image_details_in_db(img_id, update_data):
    mongo.db.user_imgs.update_one({"img_id": img_id}, {"$set": update_data })
    return {"msg": "success"}

def search_for_user_uploads(user):
    details = mongo.db.user_imgs.find({"owner": user})
    return details

def delete_image_details(img_id):
    mongo.db.user_imgs.delete_one({"img_id": img_id})
    return {"msg": "success"}
    