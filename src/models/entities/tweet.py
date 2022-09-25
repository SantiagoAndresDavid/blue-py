
class Tweet():
    def __init__(self, id, author_id=None, text=None) -> None:
        self.id = id
        self.author_id = author_id
        self.text = text


    def to_JSON(self):
        return {
            'id': self.id,
            'autor_id': self.place,
            'text': self.color,
        }
