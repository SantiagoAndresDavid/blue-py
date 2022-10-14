from crypt import methods
from flask import Blueprint, jsonify, request
from models.entities.tweet import Tweet
from models.tweet_model import Tweet_model
from utils.db import db
from utils.tweetpy import api

# models
from models import tweet_model
main = Blueprint('tweet_service_blueprint', __name__)


@main.route('/')
def get_main():
    try:
        return jsonify({'message': "si"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

## search_tweets about topic 
@main.route('/search-tweets', methods=['POST'])
def get_tweets():
    try:
        tweets = api.search_tweets(
            q=request.json['topic'], count=1000, lang="es")  # search_tweets
        affected_rows = Tweet_model.add_tweet(tweets)
        if affected_rows == True:
            return jsonify({'message': 'se guardo con exito'})
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

## search follower list
@main.route('/search-follower-list', methods=['POST'])
def get_follower_list():
    try:
        user = api.get_user(screen_name=request.json['user'])
        for follower in user.followers():
            print(follower.name)
        return jsonify({'message': 'se encontro'})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500        


## search list of followers
