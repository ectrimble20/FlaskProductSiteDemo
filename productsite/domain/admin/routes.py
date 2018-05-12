from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app, abort
from flask_login import login_required, current_user, login_user, logout_user
from productsite.domain.users.models import User, UserAccessRoutes
from productsite.domain.admin.forms import AdminCreateUserForm, AdminEditUserForm
from productsite import app_crypt
from productsite.database import app_db

admin = Blueprint('admin', __name__)


def uac_check(user_id, path_check):
    """
    check = UserAccessControl.query.filter_by(user_id=user_id, allow=path_check).first()
    if not check:
        abort(403)
    """


@admin.route("/admin", methods=["GET"])
@login_required
def admin_index():
    uac_check(current_user.id, 'admin')
    return render_template('admin/admin.html', title="Administrative Home")


@admin.route("/admin/user", methods=["GET"])
@login_required
def admin_user():
    uac_check(current_user.id, 'admin-user')
    user_list = User.query.all()
    return render_template('admin/user.html', users=user_list)


@admin.route("/admin/user/new", methods=["GET", "POST"])
@login_required
def admin_new_user():
    uac_check(current_user.id, 'admin-user')
    form = AdminCreateUserForm()
    if form.validate_on_submit():
        # we need to ensure that either admin or CS is checked
        if not form.is_admin.data and not form.is_cs.data:
            flash("You must select Is Admin or Is Customer Service for an admin created user", "danger")
        else:
            hashed_password = app_crypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=hashed_password,
                flag_admin=form.is_admin.data,
                flag_cs=form.is_cs.data
            )
            app_db.session.add(user)
            app_db.session.commit()
            flash("User Account Created Successfully", "success")
            return redirect(url_for('admin.admin_user'))
    return render_template('admin/user_create.html', form=form)


@admin.route("/admin/user/<int:uid>", methods=["GET", "POST"])
@login_required
def admin_edit_user(uid):
    uac_check(current_user.id, 'admin-user')
    user = User.query.get_or_404(uid)
    form = AdminEditUserForm()
    if form.validate_on_submit():
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.flag_admin = form.is_admin.data
        user.flag_cs = form.is_cs.data
        app_db.session.add(user)
        app_db.session.commit()
        flash("User Account Updated Successfully", "success")
        return redirect(url_for('admin.admin_user'))
    else:
        form.id.data = user.id
        form.email.data = user.email
        form.first_name.data = user.first_name
        form.last_name.data = user.last_name
        form.is_admin.data = user.flag_admin
        form.is_cs.data = user.flag_cs
        return render_template('admin/user_edit.html', form=form)


@admin.route("/admin/user/<int:uid>/ban", methods=["POST"])
@login_required
def admin_ban_user(uid):
    uac_check(current_user.id, 'admin-user-ban')
    return redirect(url_for('admin.admin_user'))


@admin.route("/admin/user/<int:uid>/uac", methods=["GET", "POST"])
@login_required
def admin_uac_user(uid):
    uac_check(current_user.id, 'admin-user-uac')
    user = User.query.get(uid)
    routes = UserAccessRoutes.query.all()
    if request.method == 'GET':
        return render_template('admin/user_uac.html', routes=routes, user=user)
    return redirect(url_for('admin.admin_user'))


@admin.route("/admin/product", methods=["GET", "POST"])
@login_required
def admin_product():
    uac_check(current_user.id, 'admin-product')
    pass


@admin.route("/admin/product/new", methods=["GET", "POST"])
@login_required
def admin_new_product():

    uac_check(current_user.id, 'admin-product-new')
    pass


@admin.route("/admin/product/<int:pid>", methods=["GET", "POST"])
@login_required
def admin_edit_product():
    uac_check(current_user.id, 'admin-product')
    pass


@admin.route("/admin/product/<int:pid>/review", methods=["GET", "POST"])
@login_required
def admin_edit_product_review():
    uac_check(current_user.id, 'admin-product-review')
    pass


@admin.route("/admin/product/<int:pid>/rating", methods=["GET", "POST"])
@login_required
def admin_edit_product_rating():
    uac_check(current_user.id, 'admin-product-rating')
    pass


@admin.route("/admin/cs", methods=["GET", "POST"])
@login_required
def admin_cs():
    uac_check(current_user.id, 'admin-cs')
    pass


@admin.route("/admin/cs/ticket", methods=["GET", "POST"])
@login_required
def admin_cs_ticket():
    uac_check(current_user.id, 'admin-cs-ticket')
    pass


@admin.route("/admin/cs/ticket/<int:tid>", methods=["GET", "POST"])
@login_required
def admin_cs_work_ticket():
    uac_check(current_user.id, 'admin-cs-ticket-work')
    pass


@admin.route("/admin/cs/order", methods=["GET", "POST"])
@login_required
def admin_cs_order():
    uac_check(current_user.id, 'admin-cs-order')
    pass


@admin.route("/admin/cs/order/<int:oid>", methods=["GET", "POST"])
@login_required
def admin_cs_work_order():
    uac_check(current_user.id, 'admin-cs-order-work')
    pass





"""
/admin/user                         - view all users, only admin/CS, option for all
/admin/user/new                     - create a new user, defaults to admin/CS users only
/admin/user/[id]/ban                - place a ban on a specific user
/admin/user/[id]/uac                - set Access control rules for a user, only admin/CS
/admin/product                      - admin view of products
/admin/product/new                  - add a new product
/admin/product/[id]                 - update/view specific product
/admin/product/[id]/review          - edit/remove/approve reviews
/admin/product/[id]/rating          - view rating, can completely reset, but not modify ratings
/admin/cs/ticket                    - view Customer service tickets
/admin/cs/ticket/[id]               - work a specific ticket
/admin/cs/order                     - view orders
/admin/cs/order/[id]                - view/work a specific order
"""