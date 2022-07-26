from flask import Flask
from qna.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from qna.main.routes import main_bp
    from qna.users.routes import users_bp
    from qna.questions.routes import questions_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(questions_bp)

    return app
