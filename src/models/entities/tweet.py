
from utils.db import db

class Tweet(db.Model):
        
    id = db.Column(db.String(50), primary_key=True, unique=True)
    author_id = db.Column(db.String(200), nullable=False)
    text = db.Column(db.String(200), nullable=False)


    def __init__(self, id, author_id=None, text=None) -> None:
        self.id = id
        self.author_id = author_id
        self.text = text

