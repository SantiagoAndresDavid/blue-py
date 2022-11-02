import re
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
        try:
            tweets = TweetRepository.get_tweet_list(topic)
            tweets_clean_text = TweetRepository.clean_text(tweets)
            return tweets_clean_text
        except Exception as e:
            return e           

    @classmethod
    def get_follower_list(self,username):
        try:
            followers = []
            followers_user = api.get_followers(screen_name=username)
            for follower in followers_user:
                followers.append(follower.name)
            return followers    
        except Exception as e:
            return e

    @classmethod
    def get_following_list(self,username):
        try:
            following = []
            following_user = api.get_friends(screen_name=username)
            for friend in following_user:
                following.append(friend.name)
            return following    
        except Exception as e:
            return e    
            