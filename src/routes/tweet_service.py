from flask import Blueprint,jsonify,request
from models.entities.tweet import Tweet
from models.tweet_model import Tweet_model
from utils.db import db

#models
from models import tweet_model
main = Blueprint('tweet_service_blueprint', __name__)


@main.route('/')
def get_cars():
    try:

        return jsonify({'message':"si"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



@main.route('/add', methods=['POST'])
def add_car():
    try:
        id = request.json['id']
        author_id = request.json['author_id']
        text = request.json['text']
        tweet = Tweet(id,author_id,text)
        affected_rows = Tweet_model.add_tweet(tweet)

        if affected_rows == True:
            return jsonify({'message': 'se guardo con exito'})
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
