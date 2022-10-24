from settings import API_KEY, API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
import tweepy

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)
