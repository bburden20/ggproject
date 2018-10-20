from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class CreateForm(FlaskForm):
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	salary = IntegerField('Salary')
	hired_date = DateField('Hire Date', format='%Y-%m-%d')
	department = StringField('Department')
	submit = SubmitField('Create')
	update = SubmitField('Update')