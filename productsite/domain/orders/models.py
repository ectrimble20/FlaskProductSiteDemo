from datetime import datetime
from productsite.database import app_db


order_part = app_db.Table('order_part',
                          app_db.Column('product_id', app_db.Integer, app_db.ForeignKey('product.id'),
                                        primary_key=True),
                          app_db.Column('order_id', app_db.Integer, app_db.ForeignKey('customer_order.id'),
                                        primary_key=True),
                          app_db.Column('quantity', app_db.Integer, nullable=False, default=1)
                          )


class CustomerOrder(app_db.Model):
    """
    status can be: open, reviewing, working, shipped, closed
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    user_id = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)
    create_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
    status = app_db.Column(app_db.String(10), nullable=False, default="open")
    last_status_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
    full_filled_date = app_db.Column(app_db.DateTime, nullable=True)
    shipped_date = app_db.Column(app_db.DateTime, nullable=True)
