import os


class Config(object):
    SECRET_KEY = os.environ.get('SITE_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SITE_DB_URI')
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('SITE_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('SITE_EMAIL_PASS')
