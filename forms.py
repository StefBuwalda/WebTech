from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    name = StringField("Service name:", validators=[DataRequired()])
    url = URLField("Service URL:", validators=[DataRequired()])
    submit = SubmitField("Add")


class LoginForm(FlaskForm):
    pass
