from qna import create_app
from flask import g

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
