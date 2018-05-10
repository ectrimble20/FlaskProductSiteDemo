from productsite import create_flask_app
from productsite.database import app_db

if __name__ == '__main__':
    app = create_flask_app()
    with app.app_context():
        from productsite.domain.users.models import User
        app_db.create_all()
        app_db.session.commit()
