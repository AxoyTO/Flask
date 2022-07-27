from flask import g
import psycopg2
from psycopg2.extras import DictCursor


def connect_db():
    conn = psycopg2.connect(
        'postgres://zdlhwhjfwbjwhs:a4a9c1101e446e31a4411c509459d764c661bdef9716601064ac7644bad1752a@ec2-100-26-39-41.compute-1.amazonaws.com:5432/d1tgd5386cmf45', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql


def get_db():
    db = connect_db()
    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur


def init_db():
    db = connect_db()
    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()
