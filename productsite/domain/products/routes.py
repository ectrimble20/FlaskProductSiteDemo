from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from flask_login import login_required, current_user, login_user, logout_user
from productsite import app_crypt
from productsite.database import app_db
from productsite.domain.products.forms import ProductAdminAddProduct, ProductAdminUpdateProduct
from productsite.domain.products.models import Product

products = Blueprint('products', __name__)


# view product, edit product, product images, product

@products.route("/product", methods=["GET"])
def list_product():
    current_app.logger.debug("{} called".format(__name__))
    page = request.args.get('page', 1, type=int)
    ps = Product.query.order_by(Product.title).paginate(page=page, per_page=10)
    return render_template('product/list.html', products=ps)


@products.route("/product/<int:product_id>", methods=["GET"])
def show_product(product_id):
    current_app.logger.debug("{} called".format(__name__))
    pd = Product.query.get(product_id)
    return render_template('product/list.html', products=[pd], single=True)


@products.route("/product/search/<string:search_by>", methods=["GET", "POST"])
def search_product(search_by):
    current_app.logger.debug("{} called".format(__name__))
    pass


@products.route("/product/<int:product_id>/cart/add", methods=["POST"])
@login_required
def add_product_to_cart(product_id):
    current_app.logger.debug("{} called".format(__name__))
    pass


@products.route("/admin/product/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
def product_admin_edit(product_id):
    current_app.logger.debug("{} called".format(__name__))
    form = ProductAdminUpdateProduct()
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
    current_app.logger.debug("{} called".format(__name__))
    pass


@products.route("/admin/product/new", methods=["GET", "POST"])
@login_required
def product_admin_create():
    current_app.logger.debug("{} called".format(__name__))
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
        current_app.logger.debug("new product entry inserted into DB successfully")
        new_product = Product.query.filter_by(title=form.title.data).first()
        flash("Product Created", "success")
        return redirect(url_for('products.product_admin_edit', product_id=new_product.id))
    else:
        return render_template('product/create.html', title="Administration - Create Product", form=form)
