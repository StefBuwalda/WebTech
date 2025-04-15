from application import db
from flask import Blueprint, render_template
from application.dash.forms import RegisterForm, ServiceForm
from flask_login import login_required  # type: ignore
from application.dash.models import Service
from application.auth.models import User
from application.decorators import admin_required
from werkzeug.security import generate_password_hash

dash_blueprint = Blueprint("dash", __name__, template_folder="templates")

# Routes


@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    services = Service.query.all()  # type: ignore
    return render_template("dashboard.html", services=services)


@dash_blueprint.route("/admin", methods=["GET", "POST"])
@admin_required
def admin():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        username = register_form.username.data
        password = register_form.password.data
        confirm_password = register_form.confirm_password.data
        is_admin = register_form.is_admin.data
        if confirm_password != password:
            return render_template(
                "admin.html",
                form=register_form,
                feedback="Passwords don't match, please try again",
            )
        if User.query.filter_by(username=username).first():
            return render_template(
                "admin.html",
                form=register_form,
                feedback="Username is already taken",
            )
        new_user = User(
            username=username,
            password=generate_password_hash(password),
            is_admin=is_admin,
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template(
            "admin.html",
            form=RegisterForm(formdata=None),
            feedback="Account succesvol toegevoegd",
        )
    return render_template("admin.html", form=register_form)

@dash_blueprint.route("/service", methods=["GET", "POST"])
@login_required
def service():
    return render_template("add_service.html")
