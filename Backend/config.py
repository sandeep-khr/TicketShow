import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 9000)
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG", False)
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION=["headers", "cookies", "json", "query_string"]
    JWT_COOKIE_SECURE=False
    # JWT_TOKEN_LOCATION = ["headers"]
    # JWT_IDENTITY_CLAIM = "user_id"  # default == sub
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=5)

    CELERY_BROKER_URL = 'redis://localhost:6379/1'
    RESULT_BACKEND = 'redis://localhost:6379/2'

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")

   
