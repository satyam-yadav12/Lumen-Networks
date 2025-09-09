from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from authlib.integrations.flask_client import OAuth

mongo = PyMongo()
cors = CORS()
jwt = JWTManager()
oauth = OAuth()
