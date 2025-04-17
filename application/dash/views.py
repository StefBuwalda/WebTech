from application import db
from flask import Blueprint, render_template, redirect, url_for
from application.dash.forms import ServiceForm
from flask_login import login_required, current_user  # type: ignore
from application.dash.models import Service
from application.utils import saveImage

# Dashboard blueprint
dash_blueprint = Blueprint("dash", __name__, template_folder="templates")


# index
@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    services = current_user.services  # type: ignore
    return render_template(
        "dashboard.html", services=services, active_page="dashboard"
    )


# Deleting a service
@dash_blueprint.route("/delete_service/<int:service_id>", methods=["POST"])
@login_required
def delete_service(service_id: int):
    service = Service.query.get_or_404(service_id)

    # Check ownership
    if service.user_id != current_user.id:
        return redirect(url_for("dash.index"))

    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("dash.index"))


# Add a service
@dash_blueprint.route("/add_service", methods=["GET", "POST"])
@login_required
def add_service():
    service_form = ServiceForm()

    if service_form.validate_on_submit():  # type: ignore
        image = service_form.image.data
        name = service_form.name.data
        url = service_form.url.data
        filename2 = "google.png"
        if image:
            filename2 = saveImage(image)

        new_service = Service(
            name=name,  # type: ignore
            url=url,  # type: ignore
            user_id=current_user.id,
            icon=filename2,
        )  # type: ignore
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


# Edit service
@dash_blueprint.route(
    "/edit_service/<int:service_id>", methods=["GET", "POST"]
)
@login_required
def edit_service(service_id: int):
    service = Service.query.get_or_404(service_id)

    if current_user.id != service.user_id:
        redirect(url_for("dash.index"))

    # Correcte gebruiker
    form = ServiceForm()
    if form.validate_on_submit():  # type: ignore
        commit = False
        if service.name != form.name.data:
            service.name = form.name.data
            commit = True
        if service.url != form.url.data:
            service.url = form.url.data
            commit = True
        if form.image.data:
            service.icon = saveImage(form.image.data)
            commit = True
        if commit:
            db.session.commit()
        return redirect(url_for("dash.index"))
    # Fill in correct data
    form = ServiceForm(name=service.name, url=service.url)
    return render_template("edit_service.html", form=form)
