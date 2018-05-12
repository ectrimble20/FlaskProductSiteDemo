from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app, abort
from flask_login import login_required, current_user, login_user, logout_user
from productsite.domain.users.models import UserAccessControl, User, UserType
from productsite.domain.users.forms import RegisterUserForm

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
    pass


@admin.route("/admin/user/<int:id>", methods=["GET", "POST"])
@login_required
def admin_edit_user():
    uac_check(current_user.id, 'admin-user')
    pass


@admin.route("/admin/user/<int:id>/ban", methods=["POST"])
@login_required
def admin_ban_user():
    uac_check(current_user.id, 'admin-user-ban')
    pass


@admin.route("/admin/user/<int:id>/uac", methods=["GET", "POST"])
@login_required
def admin_uac_user():
    uac_check(current_user.id, 'admin-user-uac')
    pass


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


@admin.route("/admin/product/<int:id>", methods=["GET", "POST"])
@login_required
def admin_edit_product():
    uac_check(current_user.id, 'admin-product')
    pass


@admin.route("/admin/product/<int:id>/review", methods=["GET", "POST"])
@login_required
def admin_edit_product_review():
    uac_check(current_user.id, 'admin-product-review')
    pass


@admin.route("/admin/product/<int:id>/rating", methods=["GET", "POST"])
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


@admin.route("/admin/cs/ticket/<int:id>", methods=["GET", "POST"])
@login_required
def admin_cs_work_ticket():
    uac_check(current_user.id, 'admin-cs-ticket-work')
    pass


@admin.route("/admin/cs/order", methods=["GET", "POST"])
@login_required
def admin_cs_order():
    uac_check(current_user.id, 'admin-cs-order')
    pass


@admin.route("/admin/cs/order/<int:id>", methods=["GET", "POST"])
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