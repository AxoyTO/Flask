import datetime
from zoneinfo import ZoneInfo

from flask import current_app
from flaskblog import db, login_manager, app
from flask_login import UserMixin
import jwt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        reset_token = jwt.encode(
            {
                "user_id": self.id,
                "exp": datetime.datetime.now(tz=ZoneInfo('localtime')) + datetime.timedelta(seconds=expires_sec)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )
        return reset_token

    @staticmethod
    def verify_reset_token(token, leeway=10):
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                leeway=leeway,
                algorithms="HS256"
            )
            print(data, data.get('user_id'), type(data.get('user_id')))
        except Exception as e:
            print(e, "was error.")
            return None
        return User.query.get(data.get('user_id', None))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    date_posted = db.Column(db.DateTime, nullable=False,
                            default=lambda: datetime.datetime.now(tz=ZoneInfo('localtime')))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
