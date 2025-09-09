from flask import Flask
from .config import Config
from .extensions import oauth, jwt, cors, mongo
import cloudinary

def Create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #initializing extensions
    mongo.init_app(app)
    cors.init_app(app, supports_credentials=True, origins=app.config["CORS_ORIGIN"])
    jwt.init_app(app)
    oauth.init_app(app)

    #register google client
    from authlib.integrations.flask_client import OAuth
    google= oauth.register(
        name="googel",
        client_id=app.config["GOOGLE_CLIENT_ID"],
        client_secret=app.config["GOOGLE_CLIENT_SECRET"],
        server_metadata_url=app.config["GOOGLE_DISCOVERY_URL"],
        client_kwargs={"scope": "openid email profile"},
        
    )

    cloudinary.config(
        cloud_name= app.config["CLOUDINARY_CLOUD_NAME"],
        api_key = app.config["CLOUDINARY_API_KEY"],
        api_secret = app.config["CLOUDINARY_API_SECRET"],
        secure = True
    )

    
    #register bluprints here
    def registerBluprints():
        from .controllers.auth_controllers import auth_bp

        app.register_blueprint(auth_bp, url_prefix="/")


    registerBluprints()
        

    return app


