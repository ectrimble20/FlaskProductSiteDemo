from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, IntegerField, DecimalField, DateField, SelectField
from wtforms.validators import DataRequired


# TODO - This needs to go away in favor of the admin forms
class ProductAdminAddProduct(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    expect_stock_quantity = IntegerField('Expected Stock Quantity', validators=[DataRequired()])
    flag_out_of_stock = BooleanField('Out Of Stock')
    expect_restock_date = DateField('Expected Restock Date', format="%Y-%m-%d")
    categories = SelectField("Category", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create New Product')


class ProductAdminUpdateProduct(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    expect_stock_quantity = IntegerField('Expected Stock Quantity', validators=[DataRequired()])
    flag_out_of_stock = BooleanField('Out Of Stock')
    expect_restock_date = DateField('Expected Restock Date', format="%Y-%m-%d")
    categories = SelectField("Category", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Update Product')
