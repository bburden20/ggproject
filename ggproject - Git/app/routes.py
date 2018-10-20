from flask import render_template, flash, redirect, url_for, request
from app import app2
from app.forms import CreateForm
from app import db
from app.models import Employee
import datetime

@app2.route('/')
@app2.route('/index')
def index():
	employees = Employee.query.all()
	return render_template('index.html', title='Home', employees=employees)
	
@app2.route('/create', methods=['GET', 'POST'])
def create():
	form = CreateForm()
	
	if form.validate_on_submit():
		employee = Employee(first_name=form.first_name.data, 
			last_name=form.last_name.data, 
			salary=form.salary.data, 
			hire_date=form.hired_date.data,
			department=form.department.data)
		db.session.add(employee)
		db.session.commit()
		flash('Employee created for {} {}'.format(form.first_name.data, form.last_name.data))
		return redirect(url_for('index'))
	return render_template('create.html', title='Sign In', form=form)
	
@app2.route('/update', methods=['GET', 'POST'])
def update():	
	form = CreateForm()
	datec = request.args.get('hire_date');
	end_date = datec.split(" ")
	timeless = end_date[0]
	
	if form.validate_on_submit():
		employee = Employee.query.get(request.args.get('id'))
		employee.first_name = form.first_name.data
		employee.last_name = form.last_name.data
		employee.salary = form.salary.data
		employee.hire_date = form.hired_date.data
		employee.department = form.department.data
		db.session.commit()
		flash('Employee updated for {} {}'.format(form.first_name.data, form.last_name.data))
		return redirect(url_for('index'))
	return render_template('update.html', form=form, request=request, timeless=timeless)	

@app2.route('/delete', methods=['GET', 'POST'])	
def delete():
	employee = Employee.query.get(request.args.get('id'))
	db.session.delete(employee)
	db.session.commit()
	flash('Employee deleted for id {}'.format(request.args.get('id')))
	return redirect(url_for('index'))

	