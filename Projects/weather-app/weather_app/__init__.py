import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from weather_app.config import Config
import geonamescache

db = SQLAlchemy()
csrf = CSRFProtect()
gc = geonamescache.GeonamesCache()

API_KEY = os.environ.get("WEATHER_API_KEY")


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)
    
    from weather_app.cities.routes import cities_bp

    app.register_blueprint(cities_bp)

    return app
