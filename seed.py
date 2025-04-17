from application import db, app
from application.dash.models import Service
from application.auth.models import User
from werkzeug.security import generate_password_hash

# User acounts to add
new_users = [
    User(
        username="admin",
        password=generate_password_hash("admin"),
        is_admin=True,
    ),
    User(
        username="Daan",
        password=generate_password_hash("pass"),
        is_admin=True,
    ),
    User(
        username="stef",
        password=generate_password_hash("stef123"),
        is_admin=False,
    ),
]

# Services to add
new_services = [
    Service(name="test123", url="http://google.com", user_id=1),
    # Daan services
    Service(name="Google", url="https://google.com", user_id=2),
    Service(name="Netflix", url="https://www.netflix.com", user_id=2),
    # Stef services
    Service(name="Plex", url="https://plex.local", user_id=3),
    Service(name="TrueNAS", url="https://truenas.local", user_id=3),
    Service(name="Transmission", url="https://transmission.local", user_id=3),
    Service(name="Tautulli", url="https://tautulli.local", user_id=3),
    Service(name="Overseerr", url="https://overseerr.local", user_id=3),
    Service(name="Plex", url="https://plex.local", user_id=3),
]

with app.app_context():
    # Remove all existing
    Service.query.delete()
    User.query.delete()
    db.session.commit()
    # Then add new
    db.session.add_all(new_services)
    db.session.add_all(new_users)
    # Commit
    db.session.commit()
