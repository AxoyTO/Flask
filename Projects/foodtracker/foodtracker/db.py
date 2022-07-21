from flask import g, current_app
import sqlite3
import os

def connect_db():
    sql = sqlite3.connect(os.path.join('food_log.db'))
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if 'db' not in g:
        g.db = connect_db()
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(error):
    db = g.pop('sqlite_db', None)
    
    if db is not None:
        db.close()
        current_app.teardown_appcontext()