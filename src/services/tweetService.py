import re
from flask import Blueprint, jsonify, request
from textblob import TextBlob
from data.tweetRepository import TweetRepository
from utils.db import db
from utils.tweetpy import api


class TweetService():
    @classmethod
    def save_tweets(self, topic):
        try:
            tweets = api.search_tweets(
                q=topic + " " + "-is_retweet -RT", count=100, lang="en", tweet_mode='extended')  # search_tweets
            tweets_save = TweetRepository.add_tweet(
                tweets, request.json['topic'])
            return tweets_save
        except Exception as e:
            return e

    # get tweet list and send to repository

    @classmethod
    def get_tweet_list(self, topic):
        try:
            tweets = TweetRepository.get_tweet_list(topic)
            if(len(tweets) <= 0):
                tweets = TweetService.save_tweets(topic)
            return tweets
        except Exception as e:
            return e

    @classmethod
    def clean_tweet_list(self, tweets):
        try:
            tweets_clean_text = TweetRepository.clean_text(tweets)
            return tweets_clean_text
        except Exception as e:
            return e

    @classmethod
    def get_follower_list(self, username):
        try:
            followers = []
            followers_user = api.get_followers(screen_name=username)
            for follower in followers_user:
                followers.append(follower.name)
            return followers
        except Exception as e:
            return e

    @classmethod
    def get_following_list(self, username):
        try:
            following = []
            following_user = api.get_friends(screen_name=username)
            for friend in following_user:
                following.append(friend.name)
            return following
        except Exception as e:
            return e

    @classmethod
    def analytics_sentiment(self, clean_tweets):
        try:
            polarity = []
            for tweet in clean_tweets:
                text = TextBlob(tweet['text'])
                sentiment = text.sentiment.polarity
                polarity.append(TweetService.x_range(sentiment))
            return TweetService.calculate_polarity(polarity)
        except Exception as e:
            return e

    @staticmethod
    def calculate_polarity(polarity):
        good = 0
        bad = 0
        neutral = 0
        for i in polarity:
            if(i > 0):
                good = good + 1
            elif (i < 0):
                bad = bad + 1
            elif(i == 0):
                neutral = neutral + 1
        return (good, bad, neutral)

    @staticmethod
    def x_range(x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1
