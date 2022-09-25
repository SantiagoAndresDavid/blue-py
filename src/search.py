<<<<<<< HEAD
import tweepy
import settings   

client = tweepy.Client(bearer_token=settings.BEARER_TOKEN)
=======
from tweepy import Client
import tweetpyConfig

client = Client(bearer_token=tweetpyConfig.BEARER_TOKEN)
>>>>>>> 6f9ef366c31ce58f84b6b2c7aa42f5d20cd3524b

def search():
    query = 'covid -is:retweet'
    response = client.search_recent_tweets(query=query, max_results=10)
    print(response)
