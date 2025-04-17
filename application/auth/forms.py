from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired


# Default Form that inherits from FlaskForm and
# contains a username, password and submit button
class defaultForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# LoginForm, contains exactly the same as defaultForm
class LoginForm(defaultForm):
    pass


# RegisterForm that inherits from the default.
# Adds a password confirmation and if the user is an admin or not.
class RegisterForm(defaultForm):
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()]
    )
    is_admin = BooleanField("Admin")


# Form to update password information.
# Needs a confirmation password and the current password
class UpdateForm(defaultForm):
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()]
    )
    current_password = PasswordField(
        "Current Password", validators=[DataRequired()]
    )
