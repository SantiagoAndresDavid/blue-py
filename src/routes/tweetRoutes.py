
from flask import Blueprint, jsonify, request
from importlib_metadata import NullFinder
from data.tweetRepository import TweetRepository
from models.tweet import Tweet
from services.tweetService import TweetService
from utils.db import db
from utils.tweetpy import api


# models
from data import tweetRepository

main = Blueprint('tweet_Routes_blueprint', __name__)


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
        tweets_save = TweetService.save_tweets(request.json['topic'],request.json['config'])
        return jsonify(tweets_save)  ##graficar dede donde fue tweeteado
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# search tweets for database and analytics
@main.route('/search-tweets', methods=['GET'])
def get_tweets_database():
    try:
        tweets = TweetService.get_tweet_list(request.json['topic'])
        return jsonify(tweets)  # retornar la lista.
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
