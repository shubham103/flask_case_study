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
		address		= request.form['address_line_1'] + request.form['address_line_2']
		address		+= request.form['city']
		address		+= request.form['state']
		
		if db.isCustomerSsndExist(ssnid):
			flash("customer already exist")
			return redirect(url_for("createCustomer"))

		response=db.createCustomer(ssnid,name,age, address)

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
			if db.isCustomerIdExist(cid):
				customer_data = getCustomerIdDetils(cid)

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


	response =  db.updateCustomer(ssnid,updateFields)

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





@app.route('/delete_customer', methods=['POST'])
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
				return redirect(url_for("preDeleteCustomer"))

		
	



@app.route('/customer_status', methods=['GET'])
@login_required
def customerStatus():
	customer_data = db.getCustomerDetails()
	if customer_data[0] :
		return render_template('customerStatus.html', customerData=customer_data[1])
	else:
		flash(customer_data[1])
	return redirect(url_for('index'))


#--------------------------------------------------------   account related


@app.route('/create_account', methods=['GET','POST'])
@login_required
def createAccount():

	if request.method == 'POST':
			
		cid      	= request.form['cid']
		aType		= request.form['aType']
		deposit 	= request.form['deposit']

		response=db.createAccount(cid, aType, deposit)

		if respose[0]:
			flash("Account creation initiated successfully")
			return redirect(url_for("index"))
		else:
			flash(response[1])
			return redirect(url_for("createAccount"))
		
	else: 
		return render_template('createAccount.html')


@app.route('/pre_delete_account', methods=['GET','POST'])
@login_required
def preDeleteAccount():

	if request.method == 'POST':
		
		if 'aid' in request.form:
			ssnid = request.form['aid']
			if db.isAccountIdExist(aid):
				account_data = getAccountIdDetils(aid)
				return render_template('DeleteAccount.html', account_data)
			else:
				flash("acount does not exist !!!!!!!!")
				return redirect(url_for('preDeleteAccount'))
						

	elif request.method == 'GET':

		return render_template('preDeleteAccount.html')



@app.route('/delete_account', methods=['POST'])
@login_required
def deleteAccount():

	if request.method == 'POST':
		
		if 'ssnid' in request.form:
			ssnid = request.form['ssnid']

			response = db.deleteCustomer(ssnid)

			if respose[0]:
				flash("Customer deleted successfully")
				return redirect(url_for("index"))
			else:
				flash(response[1])
				return redirect(url_for("preDeleteAccount"))


@app.route('/account_status', methods=['GET'])
@login_required
def accountStatus():
	return render_template('index.html')


# searchAccount.html
# accountlist.html
# accountdetails.html ---- its ha three options withdraw, deposit and transfer

@app.route('/search_account', methods=['GET','POST'])
@login_required
def searchAccount():

	if request.method == 'POST':
		
		if 'aid' in request.form:
			aid =  request.form['aid']

		if 'ssnid' in request.form:
			ssnid =  request.form['aid']

		if len(aid)>0:
			if db.isAccountIdExist(aid):
				account_data = db.getAccountIdDetils(aid)
				session['aid']=aid
				return render_template('accountdetails.html', account_data)

			else:
				flash("account does not exist")
				return redirect(url_for('searchAccount'))

		else:
			if db.isCustomerSsnidExist(ssnid):
				accounts = db.getSsnidAccounts(ssnid)
				return render_template('accountlist.html',accounts)
			else:
				flash("customer  does not exist")
				return redirect(url_for('searchAccount'))

	else:
		return render_template('searchAccount.html')


#--------------------------------------------------------  transactoins

@app.route('/deposit', methods=['GET','POST'])
@login_required
def deposit():

	if request.method == 'POST':
		
		
		aid  = request.form['aid']
		damt = request.form['amount']

		response = db.deposit(aid,damt)

		if respose[0]:
			flash("Amount deposited successfully")
			return redirect(url_for("index"))
		else:
			flash(response[1])
			return redirect(url_for("searchAccount"))


		
	else:
		if 'aid' in session:
			return render_template('deposit.html', aid = session.pop('aid'))
		else:
			return render_template('searchAccount.html')




@app.route('/withdraw', methods=['GET','POST'])
@login_required
def withdraw():

	if request.method == 'POST':

		
		aid  = request.form['aid']
		wamt = request.form['amount']

		response = db.withdraw(aid,wamt)

		if respose[0]:
			flash("Amount withdrawn successfully")
			return redirect(url_for("index"))
		else:
			flash(response[1])
			return redirect(url_for("searchAccount"))
		
		
		
	else:
		if 'aid' in session:
			return render_template('withdraw.html', aid = session.pop('aid'))
		else:
			return render_template('searchAccount.html')


@app.route('/transfer', methods=['GET','POST'])
@login_required
def transfer():

	if request.method == 'POST':
		
		amount   =  request.form['amount']
		SrcAid   =  request.form['source']
		TgtAid   =  request.form['target']

		if db.isAccountIdExist(SrcAid) and db.isAccountIdExist(TgtAid):

			response = db.transfer(amount, SrcAid, TgtAid)

			if respose[0]:
				flash("Amount transfer completed successfully")
				return redirect(url_for("index"))
			else:
				flash(response[1])
				return render_template('transfer.html')
		else:
			flah("please check the account number.. something is wrong!!!!!")
			render_template('transfer.html')

		
	else:
		return render_template('transfer.html')

#--------------------------------------------------------- transaction history


@app.route('/statement', methods=['GET'])
@login_required
def statement():
	return render_template('statement.html')



@app.route('/statement_by_number', methods=['POST'])
@login_required
def statementByNumber():

	if request.method == 'POST':
		
		aid = request.form['aid']
		n   = request.form['number']

		if db.isAccountIdExist(aid):
			
			response = db.statementByNumber(aid,n)

			if respose[0]:
				return render_template("showStatements.html",response)
			else:
				flash(response[1])
				return render_template('statement.html')
		else:
			flash("please check account number")
			return redirect(url_for('statement'))


@app.route('/statement_by_date', methods=['POST'])
@login_required
def statementByDate():

	if request.method == 'POST':
		
		aid    = request.form['aid']
		sdate  = request.form['startDate']
		edate  = request.form['endDate']

		if db.isAccountIdExist(aid):
			
			response = db.statementByDate(aid,sdate,edate)

			if respose[0]:
				return render_template("showStatements.html",response)
			else:
				flash(response[1])
				return render_template('statement.html')
		else:
			flash("please check account number")
			return redirect(url_for('statement'))
