import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLAlchemy_DATABASE_URI = os.environ.get('DATABASE_URL')
    EMAIL_USER = os.environ.get('EMAIL_USER')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')
