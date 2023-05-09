from flask import Flask
from qna.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)

    from qna.main.routes import main_bp
    from qna.users.routes import users_bp
    from qna.questions.routes import questions_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(questions_bp)

    return app
