<div id="beginning"><h1>Tutorial</h1></div>

<b>Table Of Contents</b> |
------------ | 
[Project Layout](#project-layout)
[Application Factory](#app-factory)
[Database Access](#db-access)
[Views and Blueprints](#views)
[Templates](#templates)
[Static Files](#statics)
[Making the Project Installable](#install)
[Test Coverage](#tests)
[Deploy to Production](#deploy)

<div id="project-layout"></div>
    <h2>Project Layout</h2>

As a project gets bigger, it becomes a need to keep the code in separate files. Python projects use packages to organize code into multiple modules that can be imported where needed.

The project directory will contain:

- `flaskr/`, a Python package containing our app code and files
- `tests/`, a directory containing test modules
- `venv/`, a Python virtual environment where Flask and other dependencies are installed.  
- Installation files, telling Python how to install the project in another machine.

By the end, our project will look like:

```
/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

</div>

<div id="app-factory">
    <h2>Application Factory</h2>

A Flask application is an instance of the Flask class. Everything about the application, such as configuration and URLs, will be registered with this class.

The most straightforward way to create a Flask application is to create a global Flask instance directly at the top of your code. While this is simple and useful in some cases, it can cause some tricky issues as the project grows.

Instead of creating a Flask instance globally, we will create it inside a function. This function is known as the application factory. Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.

<h3>The Application Factory</h3>

Let's create the `flaskr` dir and add the `__init__.py` file. The `__init__.py` serves double duty: it will contain the application factory, and it tells Python that the `flaskr` directory should be treated as a package.

```sh
$ mkdir flaskr
```

`flaskr/__init__.py :`
```py
import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

`create_app()` is the application factory function. 

1. `app = Flask(__name__, instance_relative_config=True)` creates the Flask instance.

   - `__name__` is the name of the current Python module. The app needs to know where it’s located to set up some paths, and `__name__` is a convenient way to tell it that.

    - `instance_relative_config=True` tells the app that configuration files are relative to the instance folder. The instance folder is located outside the flaskr package and can hold local data that shouldn’t be committed to version control, such as configuration secrets and the database file.

2. `app.config.from_mapping()` sets some default configuration that the app will use:

    - `SECRET_KEY` is used by Flask and extensions to keep data safe. It’s set to **'dev'** to provide a convenient value during development, but it should be overridden with a random value when deploying.

    - `DATABASE` is the path where the SQLite database file will be saved. It’s under **app.instance_path**, which is the path that Flask has chosen for the instance folder. You’ll learn more about the database in the next section.

3. `app.config.from_pyfile()` overrides the default configuration with values taken from the `config.py` file in the instance folder if it exists. For example, when deploying, this can be used to set a real **SECRET_KEY**.

    - `test_config` can also be passed to the factory, and will be used instead of the instance configuration. This is so the tests you’ll write later in the tutorial can be configured independently of any development values you have configured.

4. `os.makedirs()` ensures that app.instance_path exists. Flask doesn’t create the instance folder automatically, but it needs to be created because our project will create the SQLite database file there.

5. `@app.route()` creates a simple route so you can see the application working before getting into the rest of the tutorial. It creates a connection between the URL **/hello** and a function that returns a response, the string **'Hello, World!'** in this case.

<h3>Running the Application</h3>

Now we can run our app using the `flask` command. From the terminal, we tell Flask where to find our app, then run it in dev mode. While doing this, we should still be in the top-level `flask-tutorial` dir, not the `flaskr` package.

Dev mode shows an interactive debugger when whenever a page raises an exception, and restarts the server whenever you make changes to the code. We can leave it running and just reload the browser page after we make changes in our app as Flask has the hot-reloading feature.

```sh
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
``` 

We should see an output similar to this:
![Flask Run Output](img/readme-flask_run.png)

Also, <a href="http://localhost:5000/hello">http://localhost:5000/hello</a> should show us the 'Hello, World!' output.

**Note:** If another program is already using port 5000, you'll see **OSError: [Errno 98] or OSError: [WinError 10013]** when the server tries to start.

</div>

<div id="db-access">
    <h2>Database Access</h2>

The app will use a `SQLite` DB to store users and posts. Python comes in with built-in support for SQLite in `sqlite3` module.

SQLite is convenient because it doesn’t require setting up a separate database server and is built-in to Python. However, if concurrent requests try to write to the database at the same time, they will slow down as each write happens sequentially. Small applications won’t notice this. Once you become big, you may want to switch to a different database.

<h2>Connecting to the DB</h2>

The first thing to do when working with a SQLite database (and most other Python database libraries) is to create a connection to it. Any queries and operations are performed using the connection, which is closed after the work is finished.

In web applications this connection is typically tied to the request. It is created at some point when handling a request, and closed before the response is sent.

`flaskr/db.py`

```py
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

**g** is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. The connection is stored and reused instead of creating a new connection if `get_db()` is called a second time in the same request.

`current_app` is another special object that points to the Flask application handling the request. Since we used an application factory, there is no application object when writing the rest of your code. `get_db()` will be called when the application has been created and is handling a request, so **current_app** can be used.

`sqlite3.connect()` establishes a connection to the file pointed at by the DATABASE configuration key. This file doesn’t have to exist yet, and won’t until you initialize the database later.

`sqlite3.Row` tells the connection to return rows that behave like dicts. This allows accessing the columns by name.

`close_db()` checks if a connection was created by checking if g.db was set. If the connection exists, it is closed. Further down we will tell the application about the `close_db()` function in the application factory so that it is called after each request.

<h3>Creating the Tables</h3>

In `SQLite`, data is stored in tables and columns. These need to be created before you can store and retrieve data. Flaskr will store users in the **user** table, and posts in the **post** table. Create a file with the SQL commands needed to create empty tables:

`flaskr/schema.sql:`
```sql
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

Let's add the Python functions that will run these SQL commands to the db.py file:

```py
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```

`open_resource()` opens a file relative to the flaskr package, which is useful since you we don't need to know where that location is when deploying the application later. `get_db()` returns a database connection, which is used to execute the commands read from the file.

`click.command()` defines a command line command called **init-db** that calls the init_db function and shows a success message to the user.

The `close_db()` and `init_db_command()` functions need to be registered with the application instance; otherwise, they won’t be used by the application. However, since we’re using a factory function, that instance isn’t available when writing the functions. Instead, let's write a function in `db.py` that takes an application and does the registration.

```py
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

`app.teardown_appcontext()` tells Flask to call that function when cleaning up after returning the response.

`app.cli.add_command()` adds a new command that can be called with the flask command.

Now let's import and call this function from the factory and then, place the new code at the end of the factory function before returning the app.

```py
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

<h3>Initializing the DB File</h3>

Now that `init-db` has been registered with the app, it can be called using the flask command, similar to the run command.

```sh
$ flask init-db
Initialized the database.
```

There should now appear a flaskr.sqlite file in the instance folder in your project.

</div>

<div id="views">
    <h2>Views and Blueprints</h2>

A view function is the code to respond to requests. Flask uses patterns to match the incoming request URL to the view that should handle it. The view returns data that Flask turns into an outgoing response. Flask can also go the other direction and generate a URL to a view based on its name and arguments.

<h3>Creating a Blueprint</h3>

A **Blueprint** is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.

in `flaskr/auth.py`:

```py
import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix = "/auth")
```

This creates a **Blueprint** named `'auth'`. Like the application object, the blueprint needs to know where it’s defined, so `__name__` is passed as the second argument. The `url_prefix` will be prepended to all the URLs associated with the blueprint.

Let's import and register the blueprint from the factory using app.register_blueprint() in `__init__.py` and place the new code at the end of the factory function before returning the app.

```py
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
``` 

The authentication blueprint will have views to register new users and to log in and log out.

<h3>Register View</h3>

When the user visits the `/auth/register` URL, the register view will return HTML with a form for them to fill out. When they submit the form, it will validate their input and either show the form again with an error message or create the new user and go to the login page.

in `auth.py`:

```py
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```

Here’s what the register view function is doing:

1. `@bp.route` associates the URL `/register` with the `register()` view function. When Flask receives a request to `/auth/register`, it will call the register view and use the return value as the response.

2. If the user submitted the form, `request.method` will be **'POST'**. In this case, start validating the input.

3. `request.form` is a special type of dict mapping submitted form keys and values. The user will input their **username** and **password**.

4. Validate that **username** and **password** are not empty.

5. If validation succeeds, insert the new user data into the database.

    - **db.execute** takes a SQL query with `?` placeholders for any user input, and a tuple of values to replace the placeholders with. The database library will take care of escaping the values so you are not vulnerable to a *SQL injection attack*.

    - For security, passwords should never be stored in the database directly. Instead, `generate_password_hash()` is used to securely hash the password, and that hash is stored. Since this query modifies data,` db.commit()` needs to be called afterwards to save the changes.

    - An `sqlite3.IntegrityError` will occur if the username already exists, which should be shown to the user as another validation error.

6. After storing the user, they are redirected to the login page. `url_for()` generates the URL for the login view based on its name. This is preferable to writing the URL directly as it allows you to change the URL later without changing all code that links to it. `redirect()` generates a redirect response to the generated URL.

7. If validation fails, the error is shown to the user. `flash()` stores messages that can be retrieved when rendering the template.

8. When the user initially navigates to `auth/register`, or there was a validation error, an HTML page with the registration form should be shown. `render_template()` will render a template containing the HTML, which we'll write in a moment.


<h3>Login View</h3>

This view follows the same pattern as the register view.

```py
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

There are a few differences from the register view:

1. The user is queried first and stored in a variable for later use.

    - `fetchone()` returns one row from the query. If the query returned no results, it returns None. Later, `fetchall()` will be used, which returns a list of all results.

2. `check_password_hash()` hashes the submitted password in the same way as the stored hash and securely compares them. If they match, the password is valid.

3. `session` is a **dict** that stores data across requests. When validation succeeds, the user’s id is stored in a new session. The data is stored in a cookie that is sent to the browser, and the browser then sends it back with subsequent requests. Flask securely signs the data so that it can’t be tampered with.

Now that the user’s id is stored in the session, it will be available on subsequent requests. At the beginning of each request, if a user is logged in their information should be loaded and made available to other views.

```py
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```

`bp.before_app_request()` registers a function that runs before the view function, no matter what URL is requested. `load_logged_in_user()` checks if a user id is stored in the session and gets that user’s data from the database, storing it on `g.user`, which lasts for the length of the request. If there is no user id, or if the id doesn’t exist, g.user will be None.


<h3>Logout View</h3>

To log out, we need to remove the user id from the session. Then `load_logged_in_user()` won’t load a user on subsequent requests.

```py
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

<h3>Requiring Authentication in Other Views</h3>

Creating, editing, and deleting blog posts will require a user to be logged in. A *decorator* can be used to check this for each view it’s applied to.

in `flaskr/auth.py`:

```py
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    return wrapped_view
```

This decorator returns a new view function that wraps the original view it’s applied to. The new function checks if a user is loaded and redirects to the login page otherwise. If a user is loaded the original view is called and continues normally. We’ll use this decorator when writing the blog views.

<h3>Endpoints and URLs</h3>

The `url_for()` function generates the URL to a view based on a name and arguments. The name associated with a view is also called the endpoint, and by default it’s the same as the name of the view function.

When using a blueprint, the name of the blueprint is prepended to the name of the function, so the endpoint for the login function we wrote above is `'auth.login'` because we added it to the `'auth'` blueprint.

<div id="blog">
    <h3>Blog Blueprint</h3>

The blog should list all posts, allow logged in users to create posts, and allow the author of a post to edit or delete it.

Inside `flaskr/blog.py`:

```py
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```

Inside `flaskr/__init__.py`:

```py
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

Unlike the auth blueprint, the blog blueprint does not have a `url_prefix`. So the index view will be at /, the create view at /create, and so on. The blog is the main feature of Flaskr, so it makes sense that the blog index will be the main index.

However, the endpoint for the index view defined below will be `blog.index`. Some of the authentication views referred to a plain index endpoint. `app.add_url_rule()` associates the endpoint name 'index' with the `/` url so that `url_for('index')` or `url_for('blog.index')` will both work, generating the same `/` URL either way.

<h3>Index</h3>

The index will show all of the posts, most recent first. A `JOIN` is used so that the author information from the `user` table is available in the result.

Inside `flaskr/blog.py`:

```py
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

See <a href="templates/blog/index.html">`flaskr/templates/blog/index.html`</a> for index layout of our project.

When a user is logged in, the **header** block adds a link to the `create` view. When the user is the author of a post, they’ll see an “Edit” link to the `update` view for that post. `loop.last` is a special variable available inside Jinja for loops. It’s used to display a line after each post except the last one, to visually separate them.


</div>

<div id="templates">
    <h2>Templates</h2>

The template files will be stored in the `templates directory` inside the flaskr package.

Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the `Jinja` template library to render templates.

In our application, we will use templates to render HTML which will display in the user’s browser. **In Flask, Jinja is configured to autoescape any data that is rendered in HTML templates.** This means that it’s safe to render user input; any characters they’ve entered that could mess with the HTML, such as `<` and `>` will be escaped with safe values that look the same in the browser but don’t cause unwanted effects.

Jinja looks and behaves mostly like Python. Special delimiters are used to distinguish Jinja syntax from the static data in the template. **Anything between {{ and }} is an expression that will be output to the final document. {% and %} denotes a control flow statement like if and for.** Unlike Python, blocks are denoted by start and end tags rather than indentation since static text within a block could change indentation.

<h3>The Base Layout</h3>

Each page in the application will have the same basic layout around a different body. Instead of writing the entire HTML structure in each template, each template will **extend** a base template and override specific sections.

in `flaskr/templates/base.html`:

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

**g** is automatically available in templates. Based on if **g.user** is set (from `load_logged_in_user()`), either the username and a log out link are displayed, or links to register and log in are displayed. `url_for()` is also automatically available, and is used to generate URLs to views instead of writing them out manually.

After the page title, and before the content, the template loops over each message returned by `get_flashed_messages()`. We used `flash()` in the views to show error messages, and this is the code that will display them.

There are three blocks defined here that will be overridden in the other templates:

1. `{% block title %}` will change the title displayed in the browser’s tab and window title.

2. `{% block header %}` is similar to title but will change the title displayed on the page.

3. `{% block content %}` is where the content of each page goes, such as the login form or a blog post.

The base template is directly in the `templates` directory. To keep the others organized, the templates for a blueprint will be placed in a directory with the same name as the blueprint.

<h3>Register Layout</h3>

in `flaskr/templates/auth/register.html`:
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

`{% extends 'base.html' %}` tells Jinja that this template should replace the blocks from the base template. All the rendered content must appear inside `{% block %}` tags that override blocks from the base template.

A useful pattern used here is to place `{% block title %}` inside `{% block header %}`. This will set the title block and then output the value of it into the header block, so that both the window and page share the same title without writing it twice.

The `input` tags are using the `required` attribute here. This tells the browser not to submit the form until those fields are filled in. If the user is using an older browser that doesn’t support that attribute, or if they are using something besides a browser to make requests, we still want to validate the data in the Flask view. It’s important to always fully validate the data on the server, even if the client does some validation as well.

<h3>Log In Layout</h3>

This is identical to the register template except for the title and submit button.

Inside `flaskr/templates/auth/login.html`: 

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

<h3>Registering a User</h3>

Now that the authentication templates are written, we can register a user by going to <a href="http://127.0.0.1:5000/auth/register">http://127.0.0.1:5000/auth/register</a>.


</div>

<div id="statics">
    <h2>Static Files</h2>

CSS can be added to add style to the HTML layout we constructed. The style won’t change, so it’s a static file rather than a template.

Flask automatically adds a static view that takes a path relative to the `flaskr/static` directory and serves it. The base.html template already has a link to the style.css file:
`{{ url_for('static', filename='style.css') }}`

Besides CSS, other types of static files might be files with JavaScript functions, or a logo image. They are all placed under the `flaskr/static` directory and referenced with `url_for('static', filename='...')`.

<a href="static/style.css">Check the styling in `flaskr/static/style.css`.</a>

After styling, the page should look like:
<img src="img/readme-styled-register.png" alt="Styled Register & Login">

</div>

</div>

<div id="install">
    <h2>Making the Project Installable</h2>
</div>

<div id="tests">
    <h2>Test Coverage</h2>
</div>

<div id="deploy">
    <h2>Deploying to Production</h2>
</div>

[Go to the beginning of the page](#beginning)