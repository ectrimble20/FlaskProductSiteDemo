from datetime import datetime
from productsite import app_login_manager
from productsite.database import app_db
from flask_login import UserMixin


@app_login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

uac = app_db.Table('user_access_control',
                   app_db.Column('user_id', app_db.Integer, app_db.ForeignKey('user.id'), primary_key=True),
                   app_db.Column('user_access_routes_id', app_db.Integer, app_db.ForeignKey('user_access_routes.id'),
                                 primary_key=True)
                   )


class User(app_db.Model, UserMixin):
    """
    User account model
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    email = app_db.Column(app_db.String(120), unique=True, nullable=False)
    first_name = app_db.Column(app_db.String(120), unique=True, nullable=False)
    last_name = app_db.Column(app_db.String(120), unique=True, nullable=False)
    password = app_db.Column(app_db.String(60), nullable=False)
    verified_email = app_db.Column(app_db.Boolean, nullable=False, default=False)
    create_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
    flag_admin = app_db.Column(app_db.Boolean, nullable=False, default=False)
    flag_cs = app_db.Column(app_db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<User('{}','{}','{}','{}')>".format(self.id, self.email, self.first_name, self.last_name)


class UserAccessRoutes(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    route = app_db.Column(app_db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<UserAccessRoutes('{}', '{}')>".format(self.id, self.route)
