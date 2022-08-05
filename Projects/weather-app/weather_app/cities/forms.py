from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp


class CityForm(FlaskForm):
    city = StringField(
        'City', validators=[DataRequired(), Regexp(r'^[a-zA-Z ]+$', message='Only letters and space allowed')])
    submit = SubmitField('Add City')
