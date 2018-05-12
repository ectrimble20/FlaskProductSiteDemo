from productsite import create_flask_app
from productsite.database import app_db

"""
NOTE THIS WILL DROP THE EXISTING DATABASE AND ALL DATA IN IT

This is designed to completely rebuild the data structure and should be considered
only useful for TESTING purposes.  This is kept up-to-date with the current model.

I plan to add in an UPDATE model at some point, but until I finish this product, this
is what we've got to work with.
"""
if __name__ == '__main__':
    app = create_flask_app()
    with app.app_context():
        app_db.drop_all()
        # load the models we need to build here
        from productsite.domain.users.models import User, UserAccessControl, UserType
        from productsite.domain.products.models import Product, ProductCategory, cart
        from productsite.domain.reviews.models import Review
        from productsite.domain.tickets.models import Ticket, TicketMessage
        from productsite.domain.orders.models import CustomerOrder, order_part
        app_db.create_all()
        # generate placeholders
        t1 = UserType(
            type="Customer"
        )
        t2 = UserType(
            type="Admin"
        )
        t3 = UserType(
            type="CS Rep"
        )
        app_db.session.add(t1)
        app_db.session.add(t2)
        app_db.session.add(t3)
        pc1 = ProductCategory(
            description="Coding"
        )
        pc2 = ProductCategory(
            description="Administration"
        )
        pc3 = ProductCategory(
            description="Hosting"
        )
        app_db.session.add(pc1)
        app_db.session.add(pc2)
        app_db.session.add(pc3)
        # write changes
        app_db.session.commit()
