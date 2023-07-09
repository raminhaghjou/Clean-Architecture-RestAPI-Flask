""" Flask config class """
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.flaskenv')

DB_USER = os.getenv("DATABASE_USER")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_DRIVER = "mysql+mysqlconnector"

DB_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class BaseConfig:
    """ Base config vars."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_secret_key'
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maximum file size: 16 MB


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
