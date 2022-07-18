from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    announcement = BooleanField('Announcement')

    submit = SubmitField('Post')


class SortPostsForm(FlaskForm):
    options = [('date_posted_new', 'Date posted (Newest first)'),
               ('date_posted_old', 'Date posted (Oldest first)'),
               ('title', 'Title'),
               ('user', 'User'),
               ('priority', 'Priority')]
    sort_by = SelectField('Sort posts by:', choices=options)
    submit = SubmitField('Sort')
