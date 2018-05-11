from productsite import create_flask_app
from productsite.database import app_db

if __name__ == '__main__':
    app = create_flask_app()
    with app.app_context():
        # load the models we need to build here
        from productsite.domain.users.models import User
        from productsite.domain.products.models import Product, cart
        app_db.create_all()
        app_db.session.commit()
