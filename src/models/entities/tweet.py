
from encodings import utf_8
from numpy import character
from utils.db import db


class Tweet(db.Model):

    id = db.Column(db.String(50), primary_key=True, unique=True)
    text = db.Column(db.Text(600), nullable=False)
    author_id = db.Column(db.String(200), nullable=False)
    author_name = db.Column(db.String(200), nullable=False)
    topic = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, text=None, author_id=None, author_name=None, created_date=None, topic=None) -> None:
        self.id = id
        self.text = text
        self.author_id = author_id
        self.author_name = author_name
        self.created_date = created_date
        self.topic = topic
