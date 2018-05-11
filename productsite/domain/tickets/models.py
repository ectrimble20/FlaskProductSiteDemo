from productsite.database import app_db
from datetime import datetime


class Ticket(app_db.Model):
    """
    status can be: open, assigned, reviewing, working, closed
    1->N relationship with TicketMessages represented by the ticket back reference
    close_date should be assigned when the status is set to closed
    last_status_date should be assigned immediate with the initial status of open
    submitted_by and assigned_to both represent User.ID fields
    """
    id = app_db.Column(app_db.Integer, primary_key=True)
    title = app_db.Column(app_db.String(75), nullable=False)
    summary = app_db.Column(app_db.Text, nullable=False)
    submitted_by = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)
    assigned_to = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=True)
    status = app_db.Column(app_db.String(10), nullable=False, default="open")
    create_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
    last_status_date = app_db.Column(app_db.DateTime, nullable=False, default=datetime.utcnow)
    close_date = app_db.Column(app_db.DateTime, nullable=True)
    messages = app_db.relationship('TicketMessage', backref=app_db.backref('ticket', lazy=True))


class TicketMessage(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    message = app_db.Column(app_db.Text, nullable=False)
    user_id = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)
    ticket_id = app_db.Column(app_db.Integer, app_db.ForeignKey('ticket.id'), nullable=True)
