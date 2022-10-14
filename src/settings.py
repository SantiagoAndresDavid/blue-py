from os import getenv
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
BEARER_TOKEN = getenv('BEARER_TOKEN')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')

user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
host = getenv('MYSQL_HOST')
database = getenv('MYSQL_DATABASE')
port = getenv('MYSQL_PORT')


class DevelopmentConfig():
    DEBUG = True


config = {
    'development': DevelopmentConfig
}


DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4'
print(DATABASE_CONNECTION_URI)
