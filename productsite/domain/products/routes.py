from flask import Blueprint
from flask_login import login_required, current_user, login_user, logout_user

products = Blueprint('products', __name__)


# view product, edit product, product images, product

@products.route("/product/<int:product_id>", methods=["GET"])
def show_product(product_id):
    pass


@products.route("/product/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
def admin_product(product_id):
    pass


@products.route("/product/<int:product_id>/remove", methods=["POST"])
@login_required
def admin_remove_product(product_id):
    pass


@products.route("/product/new", methods=["GET", "POST"])
@login_required
def admin_create_new_product():
    pass
