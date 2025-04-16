from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed  # type: ignore


class ServiceForm(FlaskForm):
    name = StringField("Service name:", validators=[DataRequired()])
    url = URLField("Service URL:", validators=[DataRequired()])
    image = FileField(
        "Icon:",
        validators=[
            FileAllowed(["jpg", "jpeg", "png"], "Unsupported file format"),
        ],
    )
    submit = SubmitField("Submit")
