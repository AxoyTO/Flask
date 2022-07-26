from flask import session
from qna.db import get_db


def get_current_user():
    user = None
    if 'user' in session:
        user = session['username']

        db = get_db
        user = db.execute(
            'SELECT * FROM users WHERE username=?', [user]).fetchone()

    return user
