from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user, login_user, logout_user
from productsite import app_crypt
from productsite.domain.users.models import User
from productsite.domain.users.forms import LoginForm

users = Blueprint('users', __name__)


@users.route("/user/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.index_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and app_crypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Failed!', 'danger')
    return render_template('user/login.html', title='Login', form=form)


@users.route("/user/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index_page'))


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
