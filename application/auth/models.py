from application import db
from flask_login import UserMixin  # type: ignore


# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Purely a relationship not a column,
    # makes all the services accessible through User.services
    services = db.relationship("Service", backref="user", lazy="joined")

    # Initialize user, prevents red stuff
    def __init__(self, username: str, password: str, is_admin: bool = False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
