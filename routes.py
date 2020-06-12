from main import app
from flask import render_template,request,url_for,redirect,flash
import os
import json
from functools import wraps
from data import db_functions as db


@app.route('/')
def index():
	return render_template('index.html')

#------------------------------------------------------------ login & logout
 
def login_required(f):
	@wraps(f)
	def wraps(*args,**kwargs):
		if 'userId' in session:
			return f(*args,**kwargs)
		else:
			flash(" You need to login first.. ")
			return redirect(url_for("login"))





@app.route('/login', methods=['GET','POST'])
def login():

	if request.method == 'POST':
		
		userId   = request.form('userId')
		password = request.form('password')

		if db.isUserExist(userId,password) :

			flash('success fully logged in.')
			session['userId']= userId
			return redirect(url_for('index'))

		else:

			flash('Some thing is wrong.. please try again !!')
			return redirect(url_for('login'))

	else:
		return render_template('/login')



@app.route('/logout', methods=['GET'])
@login_required
def logout():

	session.clear()
	return render_template('index.html')

#---------------------------------------------------------  customer related

@app.route('/create_customer', methods=['GET','POST'])
@login_required
def createCustomer():

	if request.method == 'POST':
		
		ssnid 			= request.form['ssnid']
		name 			= request.form['name']
		age 			= request.form['age']
		address			= request.form['address_line_1'] + request.form['address_line_2']
		city 			= request.form['city']
		state 			= request.form['state']
		
		if db.isCustomerSsndExist(ssnid):
			flash("customer already exist")
			return redirect(url_for("createCustomer"))

		response=db.createCustomer(ssnid,name,age, address, city, state)

		if respose[0]:
			flash("Customer creation initiated successfully")
			 return redirect(url_for("index"))
		else:
			flash(response[1])
			return redirect(url_for("createCustomer"))

		
	elif request.method == 'GET':

		return render_template('createCustomer.html')



@app.route('/pre_update_customer', methods=['GET','POST'])
@login_required
def preUpdateCustomer():

	if request.method == 'POST':
		
		if 'ssnid' in request.form:
			ssnid = request.form['ssnid']
			if db.isCustomerSsiddExist(ssnid):
				customer_data = getCustomerSSnidDetils(ssnid)

				return render_template("updateCustomer.html", customer_data)

		elif 'cid' in request.form:
			cid = request.form['cid']
			if db.isCustomerIddExist(cid):
				customer_data = getCustomerSSnidDetils(cid)

				return render_template('updateCustomer.html', customer_data)
						

	elif request.method == 'GET':

		return render_template('preUpdateCustomer.html')


@app.route('/update_customer', methods=['POST'])
@login_required
def updateCustomer():

	ssnid 		= request.form['ssnid']
	name 		= request.form['name']
	address 	= request.form['address']
	age 		= request.form['age']

	# customerOldData = db.getCustomerSSnidDetils(ssnid)
	
	updateFields={}
	if len(name) >0:
		updateFields['name']= name
	if len(address) >0:
		updateFields['address']= address
	if len(age) > 0:
		updateFields['age'] = age


	response =  db.updateCustomer(updateFields)

	if respose[0]:
		flash("Customer updated successfully")
		return redirect(url_for("index"))
	else:
		flash(response[1])
		return redirect(url_for("preUpdateCustomer"))


@app.route('/pre_delete_customer', methods=['GET','POST'])
@login_required
def preDeleteCustomer():

	if request.method == 'POST':
		
		if 'ssnid' in request.form:
			ssnid = request.form['ssnid']
			if db.isCustomerSsiddExist(ssnid):
				customer_data = getCustomerSSnidDetils(ssnid)
				return render_template('DeleteCustomer.html', customer_data)
			else:
				return redirect(url_for('preDeleteCustomer'))
						

	elif request.method == 'GET':

		return render_template('preDeleteCustomer.html')





@app.route('/delete_customer', methods=['GET','POST'])
@login_required
def deleteCustomer():

	if request.method == 'POST':
		
		if 'ssnid' in request.form:
			ssnid = request.form['ssnid']

			response = db.deleteCustomer(ssnid)

			if respose[0]:
				flash("Customer deleted successfully")
				return redirect(url_for("index"))
			else:
				flash(response[1])
				return redirect(url_for("preUpdateCustomer"))

		
	



@app.route('/customer_status', methods=['GET'])
@login_required
def customerStatus():
	return render_template('index.html')






# @app.route('/search_customer', methods=['GET','POST'])
# @login_required
# def searchCustomer():

# 	if request.method == 'POST':
		
		
		
# 	else:

# 		return render_template('searchCustomer.html')


#--------------------------------------------------------   account related


@app.route('/create_account', methods=['GET','POST'])
@login_required
def createAccount():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/delete_account', methods=['GET','POST'])
@login_required
def deleteAccount():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/account_status', methods=['GET'])
@login_required
def accountStatus():
	return render_template('index.html')


# @app.route('/search_account', methods=['GET','POST'])
# @login_required
# def searchAccount():

# 	if request.method == 'POST':
		
# 		pass
		
# 	else:

# 		pass

# 	return render_template('index.html')


#--------------------------------------------------------  transactoins

@app.route('/deposit', methods=['GET','POST'])
@login_required
def deposit():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/withdraw', methods=['GET','POST'])
@login_required
def withdraw():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/transfer', methods=['GET','POST'])
@login_required
def transfer():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')

#--------------------------------------------------------- transaction history



@app.route('/statement_by_number', methods=['GET','POST'])
@login_required
def statementByNumber():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/statement_by_date', methods=['GET','POST'])
@login_required
def statementByDate():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')

