from application import app
from flask import render_template


# home route
@app.route("/")
def index():
    return render_template("home.html")


# App deployment
if __name__ == "__main__":
    app.run(debug=True, port=5000)
