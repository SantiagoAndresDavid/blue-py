from flask import Flask, jsonify
from settings import config



app = Flask(__name__)


def page_not_found(error):
    return '<h1>not found</h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    #BLueprints

    #error handler
    app.register_error_handler(404, page_not_found)
    app.run()
