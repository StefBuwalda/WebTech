from typing import Callable, Any
from flask_login import current_user  # type: ignore
from functools import wraps
from flask import redirect, url_for


def admin_required(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    def decorated_function(*args: ..., **kwargs: ...):
        if not current_user.is_authenticated:
            return redirect(url_for("login"))
        if not current_user.is_admin:
            return redirect(url_for("index"))
        return f(*args, **kwargs)

    return decorated_function
