import cloudinary
import cloudinary.uploader


def upload_profile_image(img, username):
        upload_results = cloudinary.uploader.upload(img, public_id = username, folder="/Profile_pictures", overwrite = True)
        return ({'msg': "profile image updated successfuly", "Url": upload_results['secure_url'], "response_code": 201})




