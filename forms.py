from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    naam = StringField("Service naam:", validators=[DataRequired()])
    url = URLField("Service URL:", validators=[DataRequired()])
    submit = SubmitField("Toevoegen")


class LoginForm(FlaskForm):
    pass
