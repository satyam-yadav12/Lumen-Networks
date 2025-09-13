from .cloudinary_functions import upload_image
import re, uuid
from ..utils.db import search_for_img_name



def generate_img_id(title):
    
    check = True
    while check:
        public_id = generate_unique_name_for_img(title)
        mongo_search = search_for_img_name(public_id)
        if not mongo_search:
            check = False
            return public_id
        
def generate_unique_name_for_img(title):
    safe  = re.sub(r'[^a-zA-Z0-9]', "", title)
    safe = safe[:10].lower()
    unique_suffix  = str(uuid.uuid4())[:8]
    public_id = f"{safe}_{unique_suffix}"

    return public_id

def create_img_data_to_upload(data, Url, folder, user, img_id):
    img_data ={
        "img_id" : img_id,
        "owner": user,
        "title": data['title'],
        "description": data['description'], 
        "tags": data["tags"], 
        "secure_url": Url,
        "cloudinary_details":{
            "folder": folder,
            "public_id": img_id,
            "secure_url": Url
        },
        "count_of_likes": "none",
        "created_at": "none",
        "download_count": "none"
    }
    return img_data
        