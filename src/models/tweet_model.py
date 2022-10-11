import tweepy
import settings
from utils.db import db

class Tweet_model():
    @classmethod         
    def add_tweet(self,tweet):
        try:
            db.session.add(tweet)
            db.session.commit()
            return True
        except Exception as e:
            return Exception(e)
