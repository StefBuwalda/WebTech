from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager  # type: ignore

# App Config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///services.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Wat is dit?
app.config["SECRET_KEY"] = "bvjchsygvduycgsyugc"  # Andere secret key

# Object Relational Management
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

# bp import
from application.auth.views import auth_blueprint

# from application.strike.views import strike_blueprint

# Login manager
from application.auth.models import User

login_manager = LoginManager()
login_manager.init_app(app)  # type: ignore
login_manager.login_view = "auth.login"  # type: ignore


@login_manager.user_loader  # type: ignore
def load_user(user_id):  # type: ignore
    return User.query.get(int(user_id))  # type: ignore


# Blueprint magic

# app.register_blueprint(strike_blueprint, url_prefix="/staking")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
