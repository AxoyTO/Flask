from weather_app import create_app, db

app = create_app()


""" DEPRECATED
@app.before_first_request
def before():
    db.create_all()
"""


if __name__ == '__main__':
    import os
    if not "SECRET_KEY" in os.environ:
        from secrets import token_hex
        os.environ["SECRET_KEY"] = token_hex(16)
    app.run(debug=True, host="0.0.0.0")
