from application import db
from flask import Blueprint, render_template
from application.dash.forms import RegisterForm, ServiceForm
from flask_login import login_required, current_user  # type: ignore
from application.dash.models import Service
from application.auth.models import User
from application.decorators import admin_required
from werkzeug.security import generate_password_hash

dash_blueprint = Blueprint("dash", __name__, template_folder="templates")

# Routes


@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    services = current_user.services  # type: ignore
    return render_template("dashboard.html", services=services)


@dash_blueprint.route("/admin", methods=["GET", "POST"])
@admin_required
def admin():
    register_form = RegisterForm()

    if register_form.validate_on_submit():  # type: ignore
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
            username=username,  # type: ignore
            password=generate_password_hash(password),  # type: ignore
            is_admin=is_admin,
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template(
            "admin.html",
            form=RegisterForm(formdata=None),
            feedback="User succesfully added",
        )
    return render_template("admin.html", form=register_form)


@dash_blueprint.route("/service", methods=["GET", "POST"])
@login_required
def service():
    service_form = ServiceForm()

    if service_form.validate_on_submit():  # type: ignore
        name = service_form.name.data
        url = service_form.url.data
        new_service = Service(
            name=name,  # type: ignore
            url=url,  # type: ignore
            user_id=current_user.id,
        )
        db.session.add(new_service)
        db.session.commit()
        return render_template(
            "add_service.html",
            form=ServiceForm(formdata=None),
            feedback="Service succesfully added",
        )
    return render_template("add_service.html", form=service_form)
