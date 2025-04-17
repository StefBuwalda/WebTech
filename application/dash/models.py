from application import db


# Service class for dashboard
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    icon = db.Column(db.String, default="google.png")

    # Foreign key to connect to User table
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Initialize the service (prevents ugly red lines)
    def __init__(
        self, name: str, url: str, user_id: int, icon: str = "google.png"
    ):
        self.name = name
        self.url = url
        self.user_id = user_id
        self.icon = icon
