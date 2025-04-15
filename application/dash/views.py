from flask import Blueprint, render_template
from application.dash.forms import RegisterForm
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
    register_form = RegisterForm()

    if register_form.validate_on_submit:
        username = register_form.username.data
        password = register_form.password.data
        check_admin = register_form.admin.data


    return render_template("admin.html")
