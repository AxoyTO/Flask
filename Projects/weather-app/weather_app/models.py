from enum import unique
from weather_app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    name = db.Column(db.String(50), nullable=False, unique=True)
    tz = db.Column(db.String(60))
    date = db.Column(db.String)
    tempmax = db.Column(db.Float)
    tempmin = db.Column(db.Float)
    temperature = db.Column(db.Float)
    feelslike = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    sunrise = db.Column(db.String(10))
    sunset = db.Column(db.String(10))
    lastcheck = db.Column(db.String(10))
    description = db.Column(db.String(200))
    icon = db.Column(db.String(50))
