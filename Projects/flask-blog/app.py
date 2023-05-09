from venv import create
from flaskblog import create_app
import os

app = create_app()

if __name__ == "__main__":
    if not "SECRET_KEY" in os.environ:
        from secrets import token_hex
        os.environ["SECRET_KEY"] = token_hex(16)
    app.run(debug=True, host="0.0.0.0")  # debug=True for development
