from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed  # type: ignore


# Form for service on dashboard, connected to database through ORM
class ServiceForm(FlaskForm):
    name = StringField(
        "Service name:",
        validators=[DataRequired()],
        render_kw={"placeholder": "Service Name"},
    )
    url = URLField(
        "Service URL:",
        validators=[DataRequired()],
        render_kw={"placeholder": "https://example.com"},
    )
    # File field that only allows jpg, jpeg or png
    image = FileField(
        "Icon:",
        validators=[
            FileAllowed(["jpg", "jpeg", "png"], "Unsupported file format"),
        ],
    )
    submit = SubmitField("Submit")
