from flask import g
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
