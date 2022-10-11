from os import getenv
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
BEARER_TOKEN = getenv('BEARER_TOKEN')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')

user = getenv('PGSQL_USER')
password = getenv('PGSQL_PASSWORD')
host = getenv('PGSQL_HOST')
database = getenv('PGSQL_DATABASE')



class DevelopmentConfig():
    DEBUG = True


config = {
    'development': DevelopmentConfig
}


DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)
