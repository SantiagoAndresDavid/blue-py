from requests import session
import tweepy
from models.tweet import Tweet
from utils.db import db
import re


class TweetRepository():
    @classmethod
    def add_tweet(self, tweets, topic):
        try:
            tweets_saved = []
            for tweet in tweets:
                new_tweet = Tweet(tweet.id, tweet.full_text, tweet.user.id_str,
                                 tweet.user.name, tweet.created_at, topic,tweet.source)
                db.session.add(new_tweet)
                db.session.commit()
                tweets_saved.append(TweetRepository.to_JSON(new_tweet))
            return tweets_saved
        except Exception as e:
            return Exception(e)

    @classmethod
    def clean_text(self, tweets):
        try:
            for tweet in tweets:
                tweet['text'] = re.sub(r'^RT[\s]+', '', tweet['text'])
                tweet['text'] = re.sub(r'#', '', tweet['text'])
                tweet['text'] = re.sub(r'@[A-Za-z0-9]+', '', tweet['text'])
                tweet['text'] = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ",  tweet['text'])
            return tweets
        except Exception as e:
            return e

    @classmethod
    def get_tweet_list(self, topic):
        try:
            tweets = []
            for tweet in db.session.query(Tweet).filter(Tweet.topic == topic):
                tweets.append(TweetRepository.to_JSON(tweet))
            return tweets
        except Exception as e:
            return e

    @staticmethod
    def to_JSON(tweet):
        return {
            'id': tweet.id,
            'text': tweet.text,
            'author_id': tweet.author_id,
            'author_name': tweet.author_name,
            'created_date': tweet.created_date,
            'topic': tweet.topic,
            'source': tweet.source
        }
