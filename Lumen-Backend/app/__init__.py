from flask import Flask
from .config import Config
from .extensions import oauth, jwt, cors, mongo
import cloudinary


def Create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initializing extensions
    mongo.init_app(app)
    cors.init_app(app, supports_credentials=True, origins=app.config["CORS_ORIGIN"])
    jwt.init_app(app)
    oauth.init_app(app)

    # register google client

    oauth.register(
        name="google",
        client_id=app.config["GOOGLE_CLIENT_ID"],
        client_secret=app.config["GOOGLE_CLIENT_SECRET"],
        server_metadata_url=app.config["GOOGLE_DISCOVERY_URL"],
        client_kwargs={"scope": "openid email profile"},
    )

    cloudinary.config(
        cloud_name=app.config["CLOUDINARY_CLOUD_NAME"],
        api_key=app.config["CLOUDINARY_API_KEY"],
        api_secret=app.config["CLOUDINARY_API_SECRET"],
        secure=True,
    )

    # register bluprints here
    def registerBluprints():

        from .routes.auth_routes import auth_bp
        from .routes.user_content_routes import user_profile_bp
        from .routes.collection_routes import collection_bp
        from .routes.feedback_routes import feedback_bp
        from .routes.search_routes import search_bp
        from .middlewares.refresh_manual import refresh_token_bp

        app.register_blueprint(auth_bp, url_prefix="/")
        app.register_blueprint(user_profile_bp, url_prefix="/user")
        app.register_blueprint(collection_bp, url_prefix="/images")
        app.register_blueprint(feedback_bp, url_prefix="/misc")
        app.register_blueprint(search_bp, url_prefix="/lumen")
        app.register_blueprint(refresh_token_bp, url_prefix="/refresh")

    registerBluprints()

    return app
