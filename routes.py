from main import app
from flask import render_template,request,url_for,redirect,flash
import os
import json



@app.route('/')
def index():
	return render_template('index.html')

#------------------------------------------------------------ login & logout
 
@app.route('/login', methods=['GET','POST'])
def login():

	if request.method == 'POST':
		
		userId   = request.form('userId')
		password = request.form('password')

		if isUserExist(userId,password) :

			flash('success fully logged in.')
			session['userId']= userId
			return redirect(url_for('index'))

		else:

			flash('Some thing is wrong.. please try again !!')
			return render_template('/login')

	else:
		return render_template('/login')



@app.route('/logout', methods=['GET'])
def logout():

	session['userId']=False
	return render_template('index.html')

#---------------------------------------------------------  customer related

@app.route('/create_customer', methods=['GET','POST'])
def createCustomer():

	if request.method == 'POST':
		
		pass
		
	else:

		pass
	return render_template('index.html')


@app.route('/delete_customer', methods=['GET','POST'])
def deleteCustomer():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/customer_status', methods=['GET'])
def customerStatus():
	return render_template('index.html')


@app.route('/search_customer', methods=['GET','POST'])
def searchCustomer():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


#--------------------------------------------------------   account related


@app.route('/create_account', methods=['GET','POST'])
def createAccount():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/delete_account', methods=['GET','POST'])
def deleteAccount():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/account_status', methods=['GET'])
def accountStatus():
	return render_template('index.html')


@app.route('/search_account', methods=['GET','POST'])
def searchAccount():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


#--------------------------------------------------------  transactoins

@app.route('/deposit', methods=['GET','POST'])
def deposit():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/withdraw', methods=['GET','POST'])
def withdraw():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/transfer', methods=['GET','POST'])
def transfer():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')

#--------------------------------------------------------- transaction history



@app.route('/statement_by_number', methods=['GET','POST'])
def statementByNumber():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')


@app.route('/statement_by_date', methods=['GET','POST'])
def statementByDate():

	if request.method == 'POST':
		
		pass
		
	else:

		pass

	return render_template('index.html')

