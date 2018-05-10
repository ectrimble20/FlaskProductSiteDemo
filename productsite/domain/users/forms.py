from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from productsite.domain.users.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('Password', validators=[DataRequired(), Length(min=2, max=35)])
    last_name = StringField('Password', validators=[DataRequired(), Length(min=2, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password_confirm = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email address is already in use, please use a different email address.")


class CloseAccountForm(FlaskForm):
    confirm = StringField('Confirm Delete', validators=[DataRequired(), Length(min=6, max=6)])
    submit = SubmitField('Confirm')


class EditAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('Password', validators=[DataRequired()])
    last_name = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        # only check validation if the email address changed
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email address is already in use, please use a different email address.")


class PasswordResetForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
