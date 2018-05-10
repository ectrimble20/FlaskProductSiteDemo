from datetime import datetime
from productsite import app_login_manager
from productsite.database import app_db
from flask_login import UserMixin
#  from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#  from flask import current_app


@app_login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    # relationships we'll need, want to build their Models first
    # Orders, Reviews, Ratings, CustomerServiceTickets

    def __repr__(self):
        return "User('{}','{}','{}','{}')".format(self.id, self.email, self.first_name, self.last_name)


class UserType(app_db.Model):
    """
    Used to differentiate between user account types, e.g Customer, Admin, CustomerSupport, etc
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    type = app_db.Column(app_db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return "UserType('{}', '{}')".format(self.id, self.type)


class UserAccessControl(app_db.Model):
    """
    Model used to control access on certain pages which might have an admin check on them.  If the user
    has the appropriate "allow" string for the page, they can access it, otherwise fail with a 403
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    user_id = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)
    allow = app_db.Column(app_db.String(20), nullable=False)
    added_by = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)
    date_added = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "UserAccessControl('{}', '{}', '{}', '{}', '{}')".format(self.id, self.user_id, self.allow,
                                                                        self.added_by, self.date_added)
