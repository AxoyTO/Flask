import os
from configparser import ConfigParser


def config(filename='../database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///questions.db"
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
