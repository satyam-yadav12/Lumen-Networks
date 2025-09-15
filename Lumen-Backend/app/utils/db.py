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

def delete_user(email):
    exist = search_by_email(email)
    if exist:
        mongo.db.auth_student.delete_one({"Email": email})
    return 


#database name user_imgs
def search_for_img_name(public_name):
    img_details  = mongo.db.user_imgs.find_one({"img_id": public_name})
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

def update_Like_counts_in_img(img_id):
    mongo.db.user_imgs.update_one({"img_id": img_id}, {"$inc": {"count_of_likes": 1}})
    return True
def decrement_Like_count_in_img(img_id):
    mongo.db.user_imgs.update_one({"img_id": img_id}, {"$inc": {"count_of_likes": -1}})
    return True

def delete_image_details(img_id):
    mongo.db.user_imgs.delete_one({"img_id": img_id})
    return {"msg": "success"}

#search related queries

def find_search_results_title(keyword, skip, limit):
    result =mongo.db.user_imgs.find({"title":{"$regex": keyword, "$options": "i"}}).skip(skip).limit(limit)
    return result

def find_search_results_tags(keyword, skip, limit):
    result =mongo.db.user_imgs.find({"tags":{"$regex": keyword, "$options": "i"}}).skip(skip).limit(limit)
    return result
    

def find_total_count_of_results_title(keyword):
    result =mongo.db.user_imgs.count_documents({"title":{"$regex": keyword, "$options": "i"}})
    return result
    

def find_total_count_of_results_tag(keyword):
    result =mongo.db.user_imgs.count_documents({"title":{"$regex": keyword, "$options": "i"}})
    return result
    

#database name user_collection
def insert_collection_data(data):
    insert_id = mongo.db.user_collection.insert_one(data).inserted_id
    return insert_id

def delete_collection_data(user, img):
    mongo.db.user_collection.delete_one({"username": user, "img_id": img})
    return {"msg": "success"}

def search_collection_of_user(user):
    data = mongo.db.user_collection.find({"username": user})
    return data

def check_if_like_exist(id, user):
    result = mongo.db.user_collection.find_one({"img_id": id, "username": user})
    if result:
        raise Exception("like exist")
    return False


#database name counters
def increment_counter(name):
    counter = mongo.db.counters.find_one_and_update({"counter_id": name}, {"$inc": {"sequence_value": 1}}, return_document = True, upsert = True)
    return counter["sequence_value"]

#database name user_feedback
def insert_feedback_data(data):
    insertion = mongo.db.user_feedback.insert_one(data).insertion_id
    return insertion

#database name content_report
def insert_content_report(data):
    insertion = mongo.db.content_report.insert_one(data).insertion_id
    return insertion