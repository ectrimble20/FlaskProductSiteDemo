from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user, login_user, logout_user
from productsite import app_crypt
from productsite.database import app_db
from productsite.domain.products.forms import ProductAdminAddProduct
from productsite.domain.products.models import Product

products = Blueprint('products', __name__)


# view product, edit product, product images, product

@products.route("/product/<int:product_id>", methods=["GET"])
def show_product(product_id):
    pass


@products.route("/product/search/<string:search_by>", methods=["GET", "POST"])
def search_product(search_by):
    pass


@products.route("/product/<int:product_id>/cart/add", methods=["POST"])
@login_required
def add_product_to_cart(product_id):
    pass


@products.route("/admin/product/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
def product_admin_edit(product_id):
    form = ProductAdminAddProduct()
    if form.validate_on_submit():
        p = Product(
            title=form.title.data,
            description=form.description.data,
            quantity=form.quantity.data,
            price=form.price.data,
            expect_stock_quantity=form.expect_stock_quantity.data,
            flag_out_of_stock=form.flag_out_of_stock.data,
            expect_restock_date=form.expect_restock_date.data
        )
        app_db.session.add(p)
        app_db.session.commit()
        flash("Product Created", "success")
        return redirect(url_for('products.product_admin_edit', product_id=p.id))
    else:
        p = Product.query.get(product_id)
        form.title.data = p.title
        form.description.data = p.description
        form.quantity.data = p.quantity
        form.price.data = p.price
        form.expect_stock_quantity.data = p.expect_stock_quantity
        form.flag_out_of_stock.data = p.flag_out_of_stock
        form.expect_restock_date.data = p.expect_restock_date
        return render_template('product/edit.html', title="Administration - Edit Product", form=form)


@products.route("/admin/product/<int:product_id>/delete", methods=["GET", "POST"])
@login_required
def product_admin_remove(product_id):
    pass


@products.route("/admin/product/new", methods=["GET", "POST"])
@login_required
def product_admin_create():
    form = ProductAdminAddProduct()
    if form.validate_on_submit():
        p = Product(
            title=form.title.data,
            description=form.description.data,
            quantity=form.quantity.data,
            price=form.price.data,
            expect_stock_quantity=form.expect_stock_quantity.data,
            flag_out_of_stock=form.flag_out_of_stock.data,
            expect_restock_date=form.expect_restock_date.data
        )
        app_db.session.add(p)
        app_db.session.commit()
        flash("Product Created", "success")
        return redirect(url_for('products.product_admin_edit', product_id=p.id))
    return render_template('product/create.html', title="Administration - Create Product", form=form)
