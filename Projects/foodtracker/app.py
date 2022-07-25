from flask import g
from foodtracker import create_app

app = create_app()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db().close()


if __name__ == '__main__':
    app.run(debug=True)
