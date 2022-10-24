from requests import session
import tweepy
from models.entities.tweet import Tweet
from utils.db import db
import re


class Tweet_model():
    @classmethod
    def add_tweet(self, tweets, topic):
        try:
            for tweet in tweets:
                newTweet = Tweet(tweet.id, tweet.full_text, tweet.user.id_str,
                                 tweet.user.name, tweet.created_at, topic)
                db.session.add(newTweet)
                db.session.commit()
            return True
        except Exception as e:
            print(e)
            return Exception(e)

    def clean_text(tweets):
        try:
            for tweet in tweets:
                text = re.sub(r'@[A-Za-z09]+', '', text)
                text = re.sub(r'#', '', text)
                text = re.sub(r'https?:\/\/?', '', text)
            return text
        except Exception as e:
            return e

    def get_tweet_list(topic):
        try:
            tweets = db.session.query(Tweet).filter(Tweet.topic == topic)
            return tweets
        except Exception as e:
            return e
