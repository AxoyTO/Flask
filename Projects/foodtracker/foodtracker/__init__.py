from flask import Flask
from foodtracker.config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from foodtracker.main.route import main_bp
    from foodtracker.foods.route import foods_bp
    from foodtracker.dates.route import dates_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(foods_bp)
    app.register_blueprint(dates_bp)
    
    return app