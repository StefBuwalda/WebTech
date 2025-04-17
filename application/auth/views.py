from flask import Blueprint, render_template, redirect, url_for, flash

from application import db
from application.auth.models import User
from application.auth.forms import LoginForm
from flask_login import (  # type: ignore
    login_user,  # type: ignore
    logout_user,
    current_user,
)
from werkzeug.security import check_password_hash, generate_password_hash
from application.decorators import admin_required, login_required
from application.auth.forms import RegisterForm, UpdateForm

auth_blueprint = Blueprint("auth", __name__, template_folder="templates")


# Add user
@auth_blueprint.route("/register_user", methods=["GET", "POST"])
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
                "register_user.html",
                form=register_form,
                feedback="Passwords don't match, please try again",
                active_page="register",
            )
        if User.query.filter_by(username=username).first():
            return render_template(
                "register_user.html",
                form=register_form,
                feedback="Username is already taken",
                active_page="register",
            )
        new_user = User(
            username=username,  # type: ignore
            password=generate_password_hash(password),  # type: ignore
            is_admin=is_admin,
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template(
            "register_user.html",
            form=RegisterForm(formdata=None),
            feedback="User succesfully added",
            active_page="register",
        )
    return render_template(
        "register_user.html", form=register_form, active_page="register"
    )


# Update user (specifically password)
@auth_blueprint.route("/update_user", methods=["GET", "POST"])
@login_required
def update():
    form = UpdateForm(username=current_user.username)
    if form.validate_on_submit():  # type: ignore
        if not check_password_hash(
            current_user.password, form.current_password.data  # type: ignore
        ):
            return render_template(
                "update_user.html",
                form=form,
                feedback="Current password incorrect",
                active_page="update",
            )
        if form.password.data != form.confirm_password.data:
            return render_template(
                "update_user.html",
                form=form,
                feedback="New password mismatched",
                active_page="update",
            )
        current_user.password = generate_password_hash(
            form.password.data  # type: ignore
        )
        db.session.commit()
        logout_user()
        flash("Password changed succesfully, please log back in")
        return redirect(url_for("auth.login"))
    return render_template("update_user.html", form=form, active_page="update")


# Login as user or admin
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
            flash("Logged in succesfully")
            return redirect("/")
        else:
            feedback = "Username or password is incorrect"

    return render_template("login.html", form=login_form, feedback=feedback)


# Logout
@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out succesfully")
    return redirect(url_for("index"))
