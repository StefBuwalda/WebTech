from application import app
from flask import redirect, url_for
from flask_login import current_user  # type: ignore


# home route
@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dash.index"))
    else:
        return redirect(url_for("auth.login"))


# App deployment
if __name__ == "__main__":
    app.run(debug=True, port=5000)
