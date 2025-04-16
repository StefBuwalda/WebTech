from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class defaultForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(defaultForm):
    pass


class RegisterForm(defaultForm):
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()]
    )
    is_admin = BooleanField("Admin")


class UpdateForm(defaultForm):
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()]
    )
    current_password = PasswordField(
        "Current Password", validators=[DataRequired()]
    )
