from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app.extensions import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Route for user login.

    If the user is already authenticated, redirects to the chat page.
    If the form is submitted and valid, checks the credentials and logs in the user.
    Displays errors if authentication fails.

    Returns:
        redirect or render_template: Redirects to the chat page upon successful login,
        or renders the login page with the login form.
    """
    if current_user.is_authenticated:
        return redirect(url_for("chat.chat_users"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("chat.chat_users"))
        else:
            flash("Please check username and password", category="error")
    return render_template(
        "auth/login_register.html", title="Login", form=form, errors=form.errors
    )


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    Route for user registration.

    If the user is already authenticated, redirects to the chat page.
    If the form is submitted and valid, checks if the username already exists.
    Creates a new user and logs them in upon successful registration.
    Displays errors if registration fails.

    Returns:
        redirect or render_template: Redirects to the chat page upon successful registration,
        or renders the registration page with the registration form.
    """
    if current_user.is_authenticated:
        return redirect(url_for("chat.chat_users"))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash(
                "Username already exists. Please choose a different one.",
                category="error",
            )
        else:
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("chat.chat_users"))
    return render_template(
        "auth/login_register.html", title="Register", form=form, errors=form.errors
    )


@auth.route("/logout")
@login_required
def logout():
    """
    Route for user logout.

    Logs out the current user and redirects to the chat page.

    Returns:
        redirect: Redirects to the chat page upon successful logout.
    """
    logout_user()
    return redirect(url_for("chat.chat_users"))
