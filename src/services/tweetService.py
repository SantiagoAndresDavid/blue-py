from flask import Blueprint, jsonify, request
from importlib_metadata import NullFinder
from data.tweetRepository import TweetRepository
from utils.db import db
from utils.tweetpy import api

class TweetService():
    @classmethod
    def save_tweets(self, topic, config):
        try:
            tweets = api.search_tweets(
                q=topic + " " + config, count=100, lang="en", tweet_mode='extended')  # search_tweets
            tweets_save = TweetRepository.add_tweet(tweets, request.json['topic'])
            return tweets_save
        except Exception as e:
            return e

    @classmethod
    def get_tweet_list(self,topic):       
