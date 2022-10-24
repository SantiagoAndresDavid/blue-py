from crypt import methods
from flask import Blueprint, jsonify, request
from importlib_metadata import NullFinder
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
@main.route('/save-tweets', methods=['POST'])
def save_tweets():
    try:

        tweets = api.search_tweets(
            q=request.json['topic'] + " " + request.json['config'], count=100, lang="es", tweet_mode='extended')  # search_tweets
        affected_rows = Tweet_model.add_tweet(tweets, request.json['topic'])
        
        if affected_rows == True:
            return jsonify({'message': 'se guardo con exito'}) ## retornar la lista de tweets guardados en la base de datos
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



## search tweets for database and analytics
@main.route('/search-tweets', methods=['GET'])
def get_tweets_database():
    try:
        i = 1
        tweets = Tweet_model.get_tweet_list(request.json['topic'])
        tweets.text.apply(Tweet_model.clean_text)
        for tweet in tweets:
            print(str(i) + ') ' + tweet.text + '\n')
            i += 1
        return jsonify({'message': 'se guardo con exito'})
    except Exception as ex:
        return jsonify({'message': str  (ex)}), 500     


## search follower list
@main.route('/search-follower-list', methods=['POST'])
def get_follower_list():
    try:
        user = api.get_user(screen_name=request.json['user'])
        for follower in user.followers():
            print(follower.name)
        return jsonify({'message': 'se encontro'}) ##retornar la base de datos 
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500        


## search list of followers
@main.route('/search-list-of-following', methods=['POST'])
def get_following_list():
    try:
        user = api.get_user(screen_name=request.json['user'])
        for follower in user.friends:
            print(follower.name)
            
        return jsonify({'message': 'se encontro'})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
