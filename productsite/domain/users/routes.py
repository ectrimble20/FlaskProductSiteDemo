from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user, login_user, logout_user
from productsite import app_crypt
from productsite.database import app_db
from productsite.domain.users.models import User
from productsite.domain.users.forms import (LoginForm, RegisterUserForm, CloseAccountForm,
                                            PasswordResetForm, EditAccountForm)

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
            return redirect(next_page) if next_page else redirect(url_for('index.index_page'))
        else:
            flash('Login Failed!', 'danger')
    return render_template('user/login.html', title='Login', form=form)


@users.route("/user/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('index.index_page'))


@users.route("/user/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index.index_page'))
    form = RegisterUserForm()
    if form.validate_on_submit():
        hashed_password = app_crypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=hashed_password
        )
        app_db.session.add(user)
        app_db.session.commit()
        flash('Thank you for registering, please sign-in to continue!')
        return redirect(url_for('users.login'))
    return render_template('user/register.html', title="Account Registration", form=form)


@users.route("/user/close", methods=["GET", "POST"])
@login_required
def close_account():
    form = CloseAccountForm()
    if form.validate_on_submit():
        check_string = form.confirm.data
        check_string.upper()
        if check_string == 'DELETE':
            app_db.session.delete(current_user)
            app_db.session.commit()
            logout_user()
            flash("Your account has been deleted", 'info')
            return redirect(url_for('index.index_page'))
    return render_template('user/close_account.html', title="Account Deletion", form=form)


@users.route("/user/account", methods=["GET", "POST"])
@login_required
def view_account():
    form = EditAccountForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        app_db.commit()
        flash("Account Information Updated", "success")
        return redirect(url_for('users.view_account'))
    else:
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        return render_template('user/edit_account.html', title="Account Information", form=form)


@users.route("/user/password_reset", methods=["GET", "POST"])
@users.route("/user/reset_password", methods=["GET", "POST"])
@users.route("/user/edit/password", methods=["GET", "POST"])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        hashed_password = app_crypt.generate_password_hash(form.password.data).decode('utf-8')
        current_user.password = hashed_password
        app_db.session.commit()
        flash("Your password has been updated, please login to verify", "info")
        logout_user()
        return redirect(url_for('user.login'))
    return render_template('user/reset_password.html', title="Reset Password", form=form)
