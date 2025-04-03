from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, PasswordField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password")
    submit = SubmitField("Login")
