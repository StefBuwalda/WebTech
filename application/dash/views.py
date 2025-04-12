from flask import Blueprint, render_template
from flask_login import login_required  # type: ignore

dash_blueprint = Blueprint("dash", __name__, template_folder="templates")

# Routes


@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template("dashboard.html")
