from crypt import methods
from json import dump
from flask import Blueprint, jsonify, request
from importlib_metadata import NullFinder
from data.tweetRepository import TweetRepository
from utils.db import db
from utils.tweetpy import api


# models
from data import tweetRepository
main = Blueprint('tweet_service_blueprint', __name__)


@main.route('/')
def get_main():
    try:
        return jsonify({'message': "si"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# search_tweets about topic


@main.route('/save-tweets', methods=['POST'])
def save_tweets():
    try:
        tweets = api.search_tweets(
            q=request.json['topic'] + " " + request.json['config'], count=100, lang="es ", tweet_mode='extended')  # search_tweets
        affected_rows = TweetRepository.add_tweet(
            tweets, request.json['topic'])

        if affected_rows == True:
            # retornar la lista de tweets guardados en la base de datos
            return jsonify({'message': 'se guardo con exito'})
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# search tweets for database and analytics
@main.route('/search-tweets', methods=['GET'])
def get_tweets_database():
    try:
        tweets = TweetRepository.get_tweet_list(request.json['topic'])
        tweets_clean_text = TweetRepository.clean_text(tweets)
        return jsonify(tweets_clean_text)  # retornar la lista.
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# search follower list
@main.route('/search-follower-list', methods=['POST'])
def get_follower_list():
    try:
        user = api.get_user(screen_name=request.json['user'])
        for follower in user.followers():
            print(follower.name)
        return jsonify({'message': 'se encontro'})  # retornar la base de datos
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# search list of followers
@main.route('/search-list-of-following', methods=['POST'])
def get_following_list():
    try:
        user = api.get_user(screen_name=request.json['user'])
        for follower in user.friends:
            print(follower.name)

        return jsonify({'message': 'se encontro'})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
