from application import db
from flask import Blueprint, render_template, redirect, url_for
from application.dash.forms import ServiceForm
from flask_login import login_required, current_user  # type: ignore
from application.dash.models import Service

dash_blueprint = Blueprint("dash", __name__, template_folder="templates")


@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    services = current_user.services  # type: ignore
    return render_template(
        "dashboard.html", services=services, active_page="dashboard"
    )


@dash_blueprint.route("/delete_item/<int:service_id>", methods=["POST"])
@login_required
def delete_item(service_id: int):
    service = Service.query.get_or_404(service_id)

    # Check ownership
    if service.user_id != current_user.id:
        return redirect(url_for("dash.index"))

    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("dash.index"))


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
            active_page="service",
        )
    return render_template(
        "add_service.html", form=service_form, active_page="service"
    )


@dash_blueprint.route("/edit_service/<int:service_id>", methods=["POST"])
@login_required
def edit_service(service_id: int):
    service = Service.query.get_or_404(service_id)
    if current_user.id != service.user_id:
        redirect(url_for("dash.index"))

    return render_template("edit_service.html")
