from flask import (render_template, request, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import login_required, current_user
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts_bp = Blueprint('posts', __name__)


@posts_bp.route("/post/new", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
            is_announcement=form.announcement.data
        )
        db.session.add(post)
        db.session.commit()
        flash("Successfully created a new post!", "success")
        return redirect(url_for("main.home"))

    return render_template(
        "create_post.html", title="New Post", form=form, legend="Create a new post"
    )


@posts_bp.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title="Update Post", post=post)


@posts_bp.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and current_user.is_admin == False:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.is_announcement = form.announcement.data
        print(form.announcement.data, post.is_announcement)
        db.session.commit()
        flash("Successfully updated the post!", "success")
        return redirect(url_for("posts.post", post_id=post.id))

    form.title.data = post.title
    form.content.data = post.content
    form.announcement.data = post.is_announcement
    return render_template(
        "create_post.html",
        title="Update Post",
        form=form,
        post=post,
        legend="Update post",
    )


@posts_bp.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and current_user.is_admin == False:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Successfully deleted the post!", "success")
    return redirect(url_for("main.home"))


@posts_bp.route('/announcements')
def announcements():
    posts = Post.query.filter_by(is_announcement=True).paginate(per_page=5)
    return render_template('announcements.html', posts=posts)
