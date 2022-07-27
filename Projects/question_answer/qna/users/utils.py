from flask import session
from qna.db import get_db


def get_current_user():
    user = None
    if 'user' in session:
        user = session['username']

        db = get_db
        db.execute('SELECT * FROM users WHERE username=%s', (user,))
        user = db.fetchone()

    return user
