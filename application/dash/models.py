from application import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
