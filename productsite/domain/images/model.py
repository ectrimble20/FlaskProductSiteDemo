from datetime import datetime
from productsite.database import app_db


class ProductImage(app_db.Model):
    """
    Represents a single stored image, names are hashed
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    file_name = app_db.Column(app_db.String(120), unique=True, nullable=False)
    date_added = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "ProductImage('{}', '{}', '{}')".format(self.id, self.file_name, self.date_added)


class ProductImages(app_db.Model):
    """
    Used to add a group of images to a product display.  A couple notes, the order_weight can be any number,
    the higher the number, the higher it is in the selection, so an image with a weight on 100 is selected
    before an image with a weight of 10 in the ordering.
    Also, the is_primary_image flag is used for the "primary" product display, e.g this is the image shown
    outside of the product page and as the main product display.  IF, because this can be done, multiple images
    have this flag set to true for a single product, it's sorted by order_weight and .first() to resolve the
    conflict silently.
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    product_image_id = app_db.Column(app_db.Integer, app_db.ForeignKey('productimage.id'), nullable=False)
    product_id = app_db.Column(app_db.Integer, app_db.ForeignKey('product.id'), nullable=False)
    is_primary_image = app_db.Column(app_db.Boolean, nullable=False, default=False)
    order_weight = app_db.Column(app_db.Integer, nullable=False, default=0)
