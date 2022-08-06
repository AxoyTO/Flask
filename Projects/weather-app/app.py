from weather_app import create_app, db

app = create_app()


@app.before_first_request
def before():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
