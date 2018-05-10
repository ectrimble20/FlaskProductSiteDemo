from flask import Blueprint
from flask_login import login_required, current_user, login_user, logout_user

users = Blueprint('users', __name__)


@users.route("/user/login", methods=["GET", "POST"])
def login():
    pass


@users.route("/user/logout", methods=["GET", "POST"])
@login_required
def logout():
    pass


@users.route("/user/register", methods=["GET", "POST"])
def register():
    pass


@users.route("/user/close", methods=["GET", "POST"])
@login_required
def close_account():
    pass


@users.route("/user/account", methods=["GET", "POST"])
@login_required
def view_account():
    pass


@users.route("/user/password_reset", methods=["GET", "POST"])
def reset_password():
    pass
