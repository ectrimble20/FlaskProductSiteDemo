from datetime import datetime
from productsite.database import app_db
#  from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#  from flask import current_app


class Product(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    code = app_db.Column(app_db.String(120), unique=True, nullable=False)
    description = app_db.Column(app_db.Text, nullable=False)
    quantity_in_stock = app_db.Column(app_db.Integer, nullable=False, default=0)
    quantity_sold_since_last_restock = app_db.Column(app_db.Integer, nullable=False, default=0)
    create_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
    restocked_date = app_db.Column(app_db.DateTime, nullable=True)
    category_id = app_db.Column(app_db.Integer, app_db.ForeignKey('productcategory.id'), nullable=False)
    # relationships: Images, Orders
    # my plan is to have the orders be smart, if a customer
    # selects buy 1 of N, N's inventory will be reduced by 1
    # but the order will only be valid for X amount of time before
    # the order is removed from the DB and the inventory and reset

    def __repr__(self):
        return "User('{}','{}','{}')".format(self.id, self.code, self.quantity_in_stock)


class ProductCategory(app_db.Model):
    """
    Model used to group products together
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    description = app_db.Column(app_db.String(45), unique=True, nullable=False)

    def __repr__(self):
        return "ProductCategory('{}', '{}')".format(self.id, self.description)
