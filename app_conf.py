from flask import Flask

from distance_app.app import distance_app


def create_app():
    app = Flask(__name__)

    app.register_blueprint(distance_app)

    return app
