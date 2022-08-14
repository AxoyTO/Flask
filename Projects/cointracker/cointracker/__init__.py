from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cointracker.config import Config
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)

    from cointracker.main.routes import main_bp
    from cointracker.exchanges.routes import exchanges_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(exchanges_bp)

    return app
