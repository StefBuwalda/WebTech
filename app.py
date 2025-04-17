from application import app
from flask import redirect, url_for


# home route, place holder in case we want a home page
@app.route("/")
def index():
    return redirect(url_for("dash.index"))


# App deployment
if __name__ == "__main__":
    app.run(debug=True, port=5000)
