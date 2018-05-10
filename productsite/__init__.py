from flask import Flask
from productsite.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# initialize some of our support classes
app_db = SQLAlchemy()
app_crypt = Bcrypt()
app_login_manager = LoginManager()
app_mailer = Mail()


def create_flask_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app_db.init_app(app)
    app_crypt.init_app(app)
    app_login_manager.init_app(app)
    app_mailer.init_app(app)
    # we'll need to load in our routes in here
    from productsite.domain.index.routes import index
    # and register our blueprints
    app.register_blueprint(index)
    return app
