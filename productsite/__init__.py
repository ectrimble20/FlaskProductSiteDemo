from flask import Flask
from productsite.config import Config
from productsite.database import app_db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import logging


# initialize some of our support classes
app_crypt = Bcrypt()
app_login_manager = LoginManager()
app_mailer = Mail()


def create_flask_app(config_class=Config):
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app = Flask(__name__)
    app.config.from_object(config_class)
    app_db.init_app(app)
    app_crypt.init_app(app)
    app_login_manager.init_app(app)
    app_mailer.init_app(app)
    # we'll need to load in our routes in here
    from productsite.domain.index.routes import index
    from productsite.domain.users.routes import users
    from productsite.domain.products.routes import products
    from productsite.domain.admin.routes import admin
    # and register our blueprints
    app.register_blueprint(index)
    app.register_blueprint(users)
    app.register_blueprint(products)
    app.register_blueprint(admin)
    return app
