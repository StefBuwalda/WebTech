from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager  # type: ignore
import os

# App Config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///services.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Wat is dit?
app.config["SECRET_KEY"] = "bvjchsygvduycgsyugc"  # Andere secret key
app.config["UPLOAD_FOLDER"] = r"application\static\icons"

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)  # type: ignore

# Object Relational Management
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

# bp import
from application.auth.views import auth_blueprint
from application.dash.views import dash_blueprint

# Login manager
from application.auth.models import User

login_manager = LoginManager()
login_manager.init_app(app)  # type: ignore
login_manager.login_view = "auth.login"  # type: ignore


@login_manager.user_loader  # type: ignore
def load_user(user_id):  # type: ignore
    return User.query.get(int(user_id))  # type: ignore


# Blueprint magic

app.register_blueprint(dash_blueprint, url_prefix="/dash")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
