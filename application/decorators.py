from typing import Callable, Any
from flask_login import current_user  # type: ignore
from functools import wraps
from flask import redirect, url_for


# Decorator that checks if the current user is logged in and an admin
# Could be shortened by adding the login_required decorator
# and removing the logic here
def admin_required(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    def decorated_function(*args: ..., **kwargs: ...):
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        if not current_user.is_admin:
            return redirect(url_for("index"))
        return f(*args, **kwargs)

    return decorated_function


def login_required(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    def decorated_function(*args: ..., **kwargs: ...):
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function
