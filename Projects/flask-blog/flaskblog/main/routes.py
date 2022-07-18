from flaskblog.models import Post
from flask import render_template, request, Blueprint
from flaskblog.posts.forms import SortPostsForm

main_bp = Blueprint('main', __name__)


@main_bp.route("/", methods=['GET', 'POST'])
@main_bp.route("/home", methods=['GET', 'POST'])
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    form = SortPostsForm()
    if form.sort_by.data == "date_posted_new":
        posts = Post.query.order_by(
            Post.date_posted.desc()).paginate(page=page, per_page=5)
    elif form.sort_by.data == "date_posted_old":
        posts = Post.query.order_by(
            Post.date_posted.asc()).paginate(page=page, per_page=5)
    elif form.sort_by.data == "title":
        posts = Post.query.order_by(
            Post.title.asc()).paginate(page=page, per_page=5)
    elif form.sort_by.data == "user":
        posts = Post.query.order_by(
            Post.user_id.asc()).paginate(page=page, per_page=5)
    elif form.sort_by.data == "priority":
        posts = Post.query.order_by(
            Post.is_announcement.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts, form=form)


@main_bp.route("/about", endpoint="about")
def about():
    return render_template("about.html")
