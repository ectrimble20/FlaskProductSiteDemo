from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, IntegerField, DecimalField, DateField
from wtforms.validators import DataRequired


class ProductAdminAll(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    expect_stock_quantity = IntegerField('Expected Stock Quantity', validators=[DataRequired()])
    flag_out_of_stock = BooleanField('Out Of Stock')
    expect_restock_date = DateField('Expected Restock Date')
    submit = SubmitField('Create New Product')


class ProductAdminAddProduct(FlaskForm, ProductAdminAll):
    pass


class ProductAdminUpdateProduct(FlaskForm, ProductAdminAll):
    pass
