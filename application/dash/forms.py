from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, PasswordField, SubmitField, URLField, BooleanField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    name = StringField("Service name:", validators=[DataRequired()])
    url = URLField("Service URL:", validators=[DataRequired()])
    submit = SubmitField("Add")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    admin = BooleanField("Admin")
    submit = SubmitField("Add")