
from flask import Blueprint, jsonify, request
from data.tweetRepository import TweetRepository
from flask_cors import cross_origin
from services.tweetService import TweetService


main = Blueprint('tweet_Routes_blueprint', __name__)


@main.route('/')
def get_main():
    try:
        return jsonify({'message': "si"})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/save-tweets', methods=['POST'])
def save_tweets():
    try:
        # search for tweets using tweepy returning a list of tweets receiving a topic
        # and saving it to the database
        tweets_save = TweetService.save_tweets(
            request.json['topic'])
        return jsonify(tweets_save)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@cross_origin
@main.route('/search-tweets', methods=['GET'])
def get_tweets_database():
    try:
        # search tweets for database receiving a topic
        tweets = TweetService.get_tweet_list(request.args.get('topic'))
        return jsonify(tweets)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/analytics-sentiments', methods=['GET'])
def analytics_sentiments():
    try:
        # search tweets for database receiving a topic
        tweets = TweetService.get_tweet_list(request.args.get('topic'))
        # clean text using regular expressions
        tweets_clean_text = TweetRepository.clean_text(tweets)
        # returns the sentiment using the sentiment method of the textblob library
        (good, bad, neutral) = TweetService.analytics_sentiment(tweets_clean_text)
        return jsonify({'good': good, 'bad': bad, 'neutral': neutral})
    except Exception as ex:
        jsonify({'message': str(ex)}), 500


@main.route("/analytics-sources", methods=["GET"])
def analytics_sources():
    try:
        sources = TweetService.get_source_list(request.args.get('topic'))
        return jsonify(sources)
    except Exception as ex:
        jsonify({'message': str(ex)}), 500


@main.route('/search-follower-list', methods=['GET'])
def get_follower_list():
    try:
        # search for follower using tweepy returning a list of tweets receiving a
        # user name and saving it to the database
        follwers = TweetService.get_follower_list(request.args.get('topic'))
        return jsonify({'message': str(follwers)})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/search-following-list', methods=['GET'])
def get_following_list():
    try:
        # search for following using tweepy returning a list of tweets receiving a
        # user name and saving it to the database
        following = TweetService.get_following_list(request.args.get('topic'))
        return jsonify({'message': str(following)})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
