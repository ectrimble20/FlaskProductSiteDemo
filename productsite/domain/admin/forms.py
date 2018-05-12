from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField,
                     DecimalField, SelectField, HiddenField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from productsite.domain.users.models import User


class AdminCreateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=35)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField("Is Admin")
    is_cs = BooleanField("Is Customer Service Rep")
    submit = SubmitField('Create User')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email address is already in use, please use a different email address.")


class AdminEditUserForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Update User')

    def validate_email(self, email):
        # validation needs to be different since it's not ALWAYS going to be this user updating it.
        owner = User.query.filter_by(email=email.data).first()
        if owner:   # if the email address is in use it will have an owner
            if int(owner.id) != int(self.id.data):  # if the owner of the email is NOT this user, we cannot allow it
                raise ValidationError("That email address is already in use, please use a different email address.")


class AdminCreateProductForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    expect_stock_quantity = IntegerField('Expected Stock Quantity', validators=[DataRequired()])
    flag_out_of_stock = BooleanField('Out Of Stock')
    expect_restock_date = DateField('Expected Restock Date', format="%Y-%m-%d")
    categories = SelectField("Category", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create New Product')


class AdminEditProductForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    expect_stock_quantity = IntegerField('Expected Stock Quantity', validators=[DataRequired()])
    flag_out_of_stock = BooleanField('Out Of Stock')
    expect_restock_date = DateField('Expected Restock Date', format="%Y-%m-%d")
    categories = SelectField("Category", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Update Product')
