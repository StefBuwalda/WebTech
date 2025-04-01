from flask import Flask, render_template, session
from forms import ServiceForm

# Create Flask instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "mijngeheimesleutel"


# Default app route
@app.route("/")
def index():
    # Return HTML content
    return "<h1>This is the default page</h1>"

@app.route("/dashboard")
def dashboard():
    # Return Dashboard.html
    return render_template("dashboard.html")


@app.route("/forms", methods=["GET", "POST"])
def forms():
    form = ServiceForm()

    if form.validate_on_submit:  # type: ignore
        session["name"] = form.name.data
        session["url"] = form.url.data

    form = ServiceForm(formdata=None)
    return render_template("forms.html", form=form)


# Prevent execution when imported by other script
if __name__ == "__main__":
    # Start the flask server in debug mode for development purposes
    app.run(port=80, debug=True)
