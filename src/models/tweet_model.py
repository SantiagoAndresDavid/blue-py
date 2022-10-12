import tweepy
from models.entities.tweet import Tweet
from utils.db import db

class Tweet_model():
    @classmethod         
    def add_tweet(self,tweets):
        try:
            for tweet in tweets:
                newTweet = Tweet(tweet.id,"a","a")
                db.session.add(newTweet)
                db.session.commit()   
            return True
        except Exception as e:
            return Exception(e)
