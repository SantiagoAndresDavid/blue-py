from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import tweetRoutes
from settings import DATABASE_CONNECTION_URI
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def page_not_found(error):
    return '<h1>not found</h1>', 404
# settings
print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_error_handler(404, page_not_found)
app.register_blueprint(tweetRoutes.main, url_prefix='/blue-py')
SQLAlchemy(app)




