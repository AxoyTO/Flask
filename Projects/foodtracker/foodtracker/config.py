import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///food_log.db"
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True