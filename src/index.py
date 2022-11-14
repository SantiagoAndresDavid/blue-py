from app import app
from utils.db import db
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from settings import DATABASE_CONNECTION_URI



with app.app_context():
    engine = create_engine(DATABASE_CONNECTION_URI)
    if not database_exists(engine.url):
        create_database(engine.url, encoding='utf8mb4')
    print(database_exists(engine.url))
    db.create_all()


if __name__ == '__main__':
    app.run(debug=False, host="localhost", port=5000)
