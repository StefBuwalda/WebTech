from application import app
from flask import redirect, url_for
from flask_login import current_user, login_required


# home route
@app.route("/")
@login_required
def index():
    if current_user.is_authenticated:
        return redirect(url_for("application.dash"))
    else:
        return redirect(url_for("application.auth"))


# App deployment
if __name__ == "__main__":
    app.run(debug=True, port=5000)
