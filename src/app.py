from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_CONNECTION_URI
from utils.db import db
from routes import tweet_service
app = Flask(__name__)


def page_not_found(error):
    return '<h1>not found</h1>', 404
# settings
print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_error_handler(404, page_not_found)
app.register_blueprint(tweet_service.main, url_prefix='/BluePy')
SQLAlchemy(app)



