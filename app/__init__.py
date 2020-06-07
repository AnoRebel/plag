from flask import Flask, redirect, url_for
from flask_cors import CORS


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False
    )
    CORS(app)

    app.config.from_object("config.ProdConfig")

    with app.app_context():
        from . import routes

        return app
