from application import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, name: str, url: str, user_id: int):
        self.name = name
        self.url = url
        self.user_id = user_id
