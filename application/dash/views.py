from flask import Blueprint, render_template
from flask_login import login_required  # type: ignore
from application.dash.models import Service
from application.decorators import admin_required

dash_blueprint = Blueprint("dash", __name__, template_folder="templates")

# Routes


@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    services = Service.query.all()  # type: ignore
    return render_template("dashboard.html", services=services)


@dash_blueprint.route("/admin", methods=["GET", "POST"])
# @admin_required
def admin():
    return render_template("admin.html")
