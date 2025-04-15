from application import app
from flask import redirect, url_for
from flask_login import login_required  # type: ignore


# home route
@app.route("/")
@login_required
def index():
    return redirect(url_for("dash.index"))


# App deployment
if __name__ == "__main__":
    app.run(debug=True, port=5000)
