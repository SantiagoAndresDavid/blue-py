from tweepy import Client
import tweetpyConfig

client = Client(bearer_token=tweetpyConfig.BEARER_TOKEN)

def search():
    query = 'covid -is:retweet'
    response = client.search_recent_tweets(query=query, max_results=10)
    print(response)
