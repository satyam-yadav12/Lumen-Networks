from ..controllers.auth_controllers import register, login, logout
from ..controllers.google_auth import google_login, authorize_by_google
from ..controllers.user_profile import get_profile, edit_profile, edit_password, change_profile_picture
from ..controllers.user_content import upload_new_img, get_user_uploads, update_img_details, delete_user_img
from ..controllers.collection_controller import save_to_collection, unsave_from_collection, get_collection_of_user 


#replace all routes inside of this folder in future