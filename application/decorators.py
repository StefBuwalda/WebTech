from flask_login import current_user
from functools import wraps
from flask import redirect, url_for, flash


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("login"))
        if not current_user.is_admin:
            flash("Admins only!")
            return redirect(url_for("index"))
        return f(*args, **kwargs)

    return decorated_function
