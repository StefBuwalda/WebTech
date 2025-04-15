from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password")
    submit = SubmitField("Login")
