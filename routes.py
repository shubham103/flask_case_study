from main import app,LoginForm,RegistrationForm,CreateAccountForm,DepositForm,TransferForm,StatementDateForm,StatementNumberForm
from flask import render_template,request,url_for,redirect,flash,session
import os
import json
from functools import wraps
from db import db_service as db

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
	return render_template('index.html')

#------------------------------------------------------------ login & logout
 
def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'userId' in session:
			return f(*args,**kwargs)
		else:
			flash(" You need to login first.. ",'danger')
			return redirect(url_for("login"))
	return wrap





@app.route('/login', methods=['GET','POST'])
def login():

	if request.method == 'POST':
		
		
		userId   = request.form['userId']
		password = request.form['password']

		if db.isUserExist(userId,password) :

			session['userId'] = userId

			flash('success fully logged in.','success')
			return redirect(url_for('index'))

		else:

			flash('please enter correct Id or Password.. and try again !!','danger')
			return redirect(url_for('login'))

	else:
	
		form = LoginForm()
		return render_template('login.html',form=form)



@app.route('/logout', methods=['GET'])
@login_required
def logout():

	session.clear()
	return redirect(url_for('index'))

#---------------------------------------------------------  customer related

@app.route('/create_customer', methods=['GET','POST'])
@login_required
def createCustomer():

	if request.method == 'POST':
		
		ssnid 			= request.form['ssnid']
		name 			= request.form['name']
		age 			= request.form['age']
		address		= request.form['address']
		city		= request.form['city']
		state		= request.form['state']
		
		if db.isCustomerSsnidExist(ssnid):
			flash("customer already exist",'danger')
			return redirect(url_for("createCustomer"))

		response=db.createCustomer(ssnid,name,age, address, city, state)

		if response[0]:
			flash("Customer creation initiated successfully",'success')
			return redirect(url_for("index"))
		else:
			flash(response[1],'danger')
			return redirect(url_for("createCustomer"))

		
	elif request.method == 'GET':
		form = RegistrationForm()
		return render_template('createCustomer.html',form=form)



@app.route('/pre_update_customer', methods=['GET','POST'])
@login_required
def preUpdateCustomer():

	if request.method == 'POST':
		
		if 'ssnid' in request.form:
			ssnid = request.form['ssnid']
			if db.isCustomerSsnidExist(ssnid):
				customer_data = db.getCustomerSsnidDetails(ssnid)
				form=RegistrationForm()
				return render_template("updateCustomer.html", cd = customer_data[0], form=form)
			else:
				flash("customer does not exist",'danger')
				return redirect(url_for('preUpdateCustomer'))

		elif 'cid' in request.form:
			cid = request.form['cid']
			if db.isCustomerIdExist(cid):
				customer_data = db.getCustomerIdDetails(cid)
				form=RegistrationForm()
				return render_template('updateCustomer.html', cd = customer_data[0], form=form)
			else:

				flash("customer does not exist",'danger')
				return redirect(url_for('preUpdateCustomer'))
						

	elif request.method == 'GET':

		return render_template('preUpdateCustomer.html')


@app.route('/update_customer', methods=['POST','GET'])
@login_required
def updateCustomer():
	if request.method == 'POST':

		ssnid 		= request.form['ssnid']
		name 		= request.form['name']
		address 	= request.form['address']
		age 		= request.form['age']

		#customerOldData = db.getCustomerSsnidDetils(ssnid)
		# paste the old data in value parameter of form inputs and  make these fields as mandatory in form 
		# accountant should update the input field or let the old data written.

		response =  db.updateCustomer(ssnid,name,address,age)

		if response[0]:
			flash("Customer updated successfully",'success')
			return redirect(url_for("index"))
		else:
			flash(response[1],'danger')
			return redirect(url_for("preUpdateCustomer"))
	else:

		return render_template('UpdateCustomer.html')

@app.route('/pre_delete_customer', methods=['GET','POST'])
@login_required
def preDeleteCustomer():

	if request.method == 'POST':
		
		if 'ssnid' in request.form:
			ssnid = request.form['ssnid']
			if db.isCustomerSsnidExist(ssnid):
				customer_data = db.getCustomerSsnidDetails(ssnid)
				
				return render_template('deleteCustomer.html', cd=customer_data[0])
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

			if response[0]:
				flash("Customer deleted successfully",'success')
				return redirect(url_for("index"))
			else:
				flash(response[1],'danger')
				return redirect(url_for("preDeleteCustomer"))

		
	



@app.route('/customer_status', methods=['GET'])
@login_required
def customerStatus():
	customer_data = db.getCustomerStatus()
	if customer_data[0] :
		return render_template('customerstatus.html', customerData=customer_data[1])
	else:
		flash(customer_data[1],'danger')
	return redirect(url_for('index'))


#--------------------------------------------------------   account related


@app.route('/create_account', methods=['GET','POST'])
@login_required
def createAccount():

	if request.method == 'POST':
			
		cid      	= request.form['cid']
		aType		= request.form['atype']
		deposit 	= request.form['deposit']

		response=db.createAccount(cid, aType, deposit)

		if response[0]:
			flash("Account creation initiated successfully",'success')
			return redirect(url_for("index"))
		else:
			flash(response[1],'danger')
			return redirect(url_for("createAccount"))
		
	else: 
		form = CreateAccountForm()
		return render_template('createAccount.html',form=form)



@app.route('/pre_delete_account', methods=['GET','POST'])
@login_required
def preDeleteAccount():

	if request.method == 'POST':
		
		if 'aid' in request.form:
			aid = request.form['aid']
			
			if db.isAccountIdExist(aid):
				account_data = db.getAccountIdDetails(aid)

				return render_template('deleteAccount.html', account_data=account_data)
			else:
				flash("acount does not exist !!!!!!!!",'success')
				return redirect(url_for('preDeleteAccount'))
						

	elif request.method == 'GET':

		return render_template('preDeleteAccount.html')



@app.route('/delete_account', methods=['POST'])
@login_required
def deleteAccount():

	if request.method == 'POST':
		
		if 'aid' in request.form:
			aid = request.form['aid']

			response = db.deleteAccount(aid)

			if response[0]:
				flash("Customer deleted successfully",'success')
				return redirect(url_for("index"))
			else:
				flash(response[1],'danger')
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
			if db.isAccountIdExist(aid):
				account_data = db.getAccountIdDetails(aid)
				session['aid']=aid
				return render_template('accountdetails.html', accountData=account_data)

			else:
				flash("account does not exist",'danger')
				return redirect(url_for('searchAccount'))

		elif 'ssnid' in request.form:

			ssnid =  request.form['ssnid']
			if db.isCustomerSsnidExist(ssnid):
				accounts = db.getSsnidAccounts(ssnid)
				return render_template('accountlist.html',accountNumbers=accounts)
			else:
				flash("customer  does not exist",'danger')
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

		if response[0]:
			flash("Amount deposited successfully",'success')
			return redirect(url_for("index"))
		else:
			flash(response[1],'danger')
			return redirect(url_for("searchAccount"))


		
	else:
		form =DepositForm()
		return render_template('deposit.html',form=form)




@app.route('/withdraw', methods=['GET','POST'])
@login_required
def withdraw():

	if request.method == 'POST':

		
		aid  = request.form['aid']
		wamt = request.form['amount']

		response = db.withdraw(aid,wamt)

		if response[0]:
			flash("Amount withdrawn successfully",'success')
			return redirect(url_for("index"))
		else:
			flash(response[1],'danger')
			return redirect(url_for("searchAccount"))
		
		
		
	else:
		form =DepositForm()
		return render_template('withdraw.html',form=form)
		
		

@app.route('/transfer', methods=['GET','POST'])
@login_required
def transfer():

	if request.method == 'POST':
		
		amount   =  request.form['amount']
		SrcAid   =  request.form['said']
		TgtAid   =  request.form['taid']

		if db.isAccountIdExist(SrcAid) and db.isAccountIdExist(TgtAid):

			response = db.transfer(amount, SrcAid, TgtAid)

			if response[0]:
				flash("Amount transfer completed successfully",'success')
				return redirect(url_for("index"))
			else:
				flash(response[1],'danger')
				return render_template('transfer.html')
		else:
			flah("please check the account number.. something is wrong!!!!!")
			render_template('transfer.html')

		
	else:
		form= TransferForm()
		return render_template('transfer.html',form=form)

#--------------------------------------------------------- transaction history


@app.route('/statement', methods=['GET'])
@login_required
def statement():
	dateform=StatementDateForm()
	numberform=StatementNumberForm()
	return render_template('statement.html',dateform=dateform,numberform=numberform)



@app.route('/statement_by_number', methods=['POST'])
@login_required
def statementByNumber():

	if request.method == 'POST':
		
		aid = request.form['aid']
		n   = request.form['number']


		if db.isAccountIdExist(aid):
			
			response = db.statementByNumber(aid,n)

			if response[0]:
				return render_template("showStatements.html",response=response)
			else:
				flash(response[1],'success')
				return render_template('statement.html')
		else:
			flash("please check account number",'danger')
			return redirect(url_for('statement'))


@app.route('/statement_by_date', methods=['POST'])
@login_required
def statementByDate():

	if request.method == 'POST':
		
		aid    = request.form['aid']
		sdate  = request.form['start_date']
		edate  = request.form['end_date']

		print(type(sdate))
		print(type(edate))	


		if db.isAccountIdExist(aid):
			
			response = db.statementByDate(aid,sdate,edate)

			if response[0]:
				return render_template("showStatements.html",response=response)
			else:
				flash(response[1],'success')   
				return render_template('statement.html')
		else:
			flash("please check account number",'danger')
			return redirect(url_for('statement'))
