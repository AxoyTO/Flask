from flaskblog.models import Post
from flask import render_template, request, Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
@main_bp.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main_bp.route("/about", endpoint="about")
def about():
    return render_template("about.html")
