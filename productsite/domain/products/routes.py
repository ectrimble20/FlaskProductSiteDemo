from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from flask_login import login_required, current_user, login_user, logout_user
from productsite import app_crypt
from productsite.database import app_db
from productsite.domain.products.forms import ProductAdminAddProduct, ProductAdminUpdateProduct
from productsite.domain.products.models import Product, ProductCategory

products = Blueprint('products', __name__)


# view product, edit product, product images, product

@products.route("/product", methods=["GET"])
def list_product():
    current_app.logger.debug("{} called".format(__name__))
    page = request.args.get('page', 1, type=int)
    c = request.args.get('c', None, type=int)
    if c:
        category = ProductCategory.query.get(c)
        ps = Product.query.filter_by(category=category).paginate(page=page, per_page=10)
    else:
        ps = Product.query.order_by(Product.title).paginate(page=page, per_page=10)
    return render_template('product/list.html', products=ps)


@products.route("/product/<int:product_id>", methods=["GET"])
def show_product(product_id):
    current_app.logger.debug("{} called".format(__name__))
    pd = Product.query.get(product_id)
    return render_template('product/view.html', product=pd)


@products.route("/product/search/<string:search_by>", methods=["GET", "POST"])
def search_product(search_by):
    current_app.logger.debug("{} called".format(__name__))
    pass


@products.route("/product/<int:product_id>/cart/add", methods=["POST"])
@login_required
def add_product_to_cart(product_id):
    current_app.logger.debug("{} called".format(__name__))
    pass
