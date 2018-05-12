from datetime import datetime
from productsite.database import app_db


class Review(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    title = app_db.Column(app_db.String(120), nullable=False)
    content = app_db.Column(app_db.Text, nullable=False)
    user_id = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)
    author = app_db.relationship('User', backref=app_db.backref('user', lazy=True))
    approved = app_db.Column(app_db.Boolean, nullable=False, default=False)
    create_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
