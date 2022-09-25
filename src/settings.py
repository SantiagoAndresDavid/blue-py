from os import getenv
from dotenv import load_dotenv, find_dotenv
from decouple import config

load_dotenv(find_dotenv())
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
BEARER_TOKEN = getenv('BEARER_TOKEN')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')

class DevelopmentConfig():
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
