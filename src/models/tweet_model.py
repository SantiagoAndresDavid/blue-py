import tweepy
from models.entities.tweet import Tweet
from utils.db import db


class Tweet_model():
    @classmethod
    def add_tweet(self, tweets):
        try:
            for tweet in tweets:
                newTweet = Tweet(tweet.id, tweet.text, tweet.user.id_str, tweet.user.name)
                db.session.add(newTweet)
                db.session.commit()
            return True
        except Exception as e:
            print(e)
            return Exception(e)
