from application import db, app
from application.dash.models import Service
from application.auth.models import User
from werkzeug.security import generate_password_hash

"""
new_strikers = [
    se(name="Erik", strike="y", age=44),
    Striker(name="Henk", strike="n", age=88),
]

"""

new_user = User(username="admin", password=generate_password_hash("admin"))

with app.app_context():
    # Remove all existing
    # Service.query.delete()
    User.query.delete()
    db.session.commit()
    # Then add new
    # db.session.add_all(new_strikers)
    db.session.add(new_user)
    db.session.commit()
