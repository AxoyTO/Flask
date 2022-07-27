from qna import create_app
from flask import g


app = create_app()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur.close()

    if hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn.close()


if __name__ == '__main__':
    app.run(debug=True)
