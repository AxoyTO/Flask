import os
from redis import StrictRedis
from werkzeug.wrappers import Request, Response
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader


class MovieApp(object):
    """Implements a WSGI application for managing your favorite movies."""

    def __init__(self, config):
        """Initializes the Jinja templating engine to render from the 'templates' folder,
        defines the mapping of URLs to view methods, and initializes the Redis interface."""
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_path), autoescape=True
        )

        self.url_map = Map(
            [
                Rule("/", endpoint="index", methods=["GET"]),
                Rule("/movies", endpoint="movies", methods=["GET"]),
                Rule("/add_movie", endpoint="add_movie", methods=["GET", "POST"]),
            ]
        )

        self.redis = StrictRedis(
            config["redis_host"], config["redis_port"], decode_responses=True
        )

    def dispatch_request(self, request):
        """Dispatches the request."""
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except NotFound:
            return self.error404()
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        """WSGI app that processes requests and returns responses."""
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def render_template(self, template_name, **context):
        """Renders the specified template file using the Jinja templating engine."""
        template = self.jinja_env.get_template(template_name)
        return Response(template.render(context), mimetype="text/html")

    def index(self, request):
        return self.render_template("base.html")

    def movies(self, request):
        return self.render_template("movies.html")

    def add_movie(self, request):
        """Adds a movie to the list of favorite movies."""
        if request.method == "POST":
            movie_title = request.form["title"]
            self.redis.lpush("movies", movie_title)
            return redirect("/movies")
        return self.render_template("add_movie.html")

    def error404(self):
        response = self.render_template("404.html")
        response.status_code = 404
        return response

    def __call__(self, environ, start_response):
        """The WSGI server calls this method as the WSGI application."""
        return self.wsgi_app(environ, start_response)


def create_app():
    """Application factory function that returns an instance of MovieApp."""
    app = MovieApp({"redis_host": "localhost", "redis_port": 6379})
    app.wsgi_app = SharedDataMiddleware(
        app.wsgi_app, {"/static": os.path.join(os.path.dirname(__file__), "static")}
    )
    return app


if __name__ == "__main__":
    # Run the Werkzeug dev server to serve the WSGI app(MovieApp)
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple("127.0.0.1", 5000, app, use_debugger=True, use_reloader=True)
