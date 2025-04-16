from flask import Blueprint, render_template, redirect, url_for

from application import db
from application.auth.models import User
from application.auth.forms import LoginForm
from flask_login import login_required, login_user, logout_user  # type: ignore
from werkzeug.security import check_password_hash, generate_password_hash
from application.decorators import admin_required
from application.auth.forms import RegisterForm

auth_blueprint = Blueprint("auth", __name__, template_folder="templates")


# Routes
@auth_blueprint.route("/register", methods=["GET", "POST"])
@admin_required
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():  # type: ignore
        username = register_form.username.data
        password = register_form.password.data
        confirm_password = register_form.confirm_password.data
        is_admin = register_form.is_admin.data
        if confirm_password != password:
            return render_template(
                "admin.html",
                form=register_form,
                feedback="Passwords don't match, please try again",
            )
        if User.query.filter_by(username=username).first():
            return render_template(
                "admin.html",
                form=register_form,
                feedback="Username is already taken",
            )
        new_user = User(
            username=username,  # type: ignore
            password=generate_password_hash(password),  # type: ignore
            is_admin=is_admin,
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template(
            "admin.html",
            form=RegisterForm(formdata=None),
            feedback="User succesfully added",
        )
    return render_template("admin.html", form=register_form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    feedback = None

    if login_form.validate_on_submit():  # type: ignore
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()  # type: ignore

        if user and check_password_hash(
            user.password, password  # type: ignore
        ):
            login_user(user)  # type: ignore
            return redirect("/")
        else:
            feedback = "Username or password is incorrect"

    return render_template("login.html", form=login_form, feedback=feedback)


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
