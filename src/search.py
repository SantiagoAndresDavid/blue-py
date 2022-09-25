import tweepy
import settings   

client = tweepy.Client(bearer_token=settings.BEARER_TOKEN)

query = 'covid -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10)

print(response)
