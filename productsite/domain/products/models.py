from datetime import datetime
from productsite.database import app_db
#  from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#  from flask import current_app

cart = app_db.Table('cart',
                    app_db.Column('product_id', app_db.Integer, app_db.ForeignKey('product.id'), primary_key=True),
                    app_db.Column('user_id', app_db.Integer, app_db.ForeignKey('user.id'), primary_key=True),
                    app_db.Column('quantity', app_db.Integer, nullable=False, default=1)
                    )

rating = app_db.Table('rating',
                      app_db.Column('user_id', app_db.Integer, app_db.ForeignKey('user.id'), primary_key=True),
                      app_db.Column('product_id', app_db.Integer, app_db.ForeignKey('product.id'), primary_key=True),
                      app_db.Column('rating', app_db.Integer, nullable=False, default=3),
                      )


class Product(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    title = app_db.Column(app_db.String(120), nullable=False)
    description = app_db.Column(app_db.Text, nullable=False, default="No Description")
    quantity = app_db.Column(app_db.Integer, nullable=False, default=0)
    price = app_db.Column(app_db.Float, nullable=False, default=0.0)
    expect_stock_quantity = app_db.Column(app_db.Integer, nullable=False, default=0)
    flag_out_of_stock = app_db.Column(app_db.Boolean, nullable=False, default=False)
    expect_restock_date = app_db.Column(app_db.DateTime, nullable=True)
    category_id = app_db.Column(app_db.Integer, app_db.ForeignKey('product_category.id'), nullable=False)
    category = app_db.relationship('Category', backref=app_db.backref('product', lazy=True))

    def __repr__(self):
        return "<Product('{}', '{}', '{}')>".format(self.id, self.title, self.quantity)


class ProductCategory(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    description = app_db.Column(app_db.String(45), unique=True, nullable=False)

    def __repr__(self):
        return "<ProductCategory('{}', '{}')>".format(self.id, self.description)
