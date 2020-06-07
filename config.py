import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base config vars."""

    DEBUG = False
    TESTING = False
    ENV = "production"
    #FLASK_ENV = "production"
    QUART_ENV = "production"
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(64)  # os.getenv('SECRET_KEY')


class ProdConfig(Config):
    """ Production Configs inheriting from Base Config """

    DEBUG = False
    TESTING = False
    ENV = "production"
    #FLASK_ENV = "production"
    QUART_ENV = "production"


class DevConfig(Config):
    """ Development Configs Inheriting from Base Config """

    DEBUG = True
    TESTING = True
    ENV = "development"
    #FLASK_ENV = "development"
    QUART_ENV = "deployment"
