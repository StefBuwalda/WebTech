from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    get_flashed_messages,
)
from application import db
from application.dash.models import Service
from application.dash.forms import ServiceForm
from flask_login import login_required, current_user

dash_blueprint = Blueprint("dash", __name__, template_folder="templates")

# Routes

"""
@strike_blueprint.route("/bedankt", methods=["GET"])
def thanks():
    return render_template("bedankt.html")
"""


@dash_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    """
    session["_flashes"] = []
    my_form = ServiceForm()

    if request.method == "POST":
        if my_form.validate_on_submit():
            flash("Het formulier is succesvol gePOST")

            session["naam"] = my_form.name.data
            session["url"] = my_form.url.data
            flash("De gegevens zijn in de sessie opgeslagen")

            new_service = Service(name=my_form.name.data, url=my_form.url.data)
            db.session.add(new_service)
            db.session.commit()
            flash("De gegevens zijn in de database opgeslagen")

            return redirect(url_for("application.dash"))
        else:
            flash("Het formulier is niet goed ingevuld")
    """
    # return render_template("dashboard.html", form=my_form)
    return render_template("dashboard.html")


"""
@strike_blueprint.route("/stakers")
@login_required
def strikers():
    rows = Striker.query.all()
    return render_template(
        "strikers.html", rows=rows, user=current_user.username
    )
"""
