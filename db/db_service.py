from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'retailbanking'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def isUserExist(userId,password):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT username,password from userstore where username=%s and password=%s", (userId, password))
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        return True
    else:
        return False

def isCustomerSsnidExist(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from customerstatus where SSN_ID=%s" %ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        return True
    else:
        return False

def isCustomerIdExist(id):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from customerstatus where Customer_ID=%s" %id)
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        return True
    else:
        return False

def isAccountIdExist(aid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from accountstatus where Account_ID=%s" % aid)
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        return True
    else:
        return False

def createCustomer(ssnid,name,age, address, city, state):
    cur = mysql.connection.cursor()
    l=[]
    res1 = cur.execute("SELECT * from customer where SSN_ID=%s" % ssnid)
    if res1 == 1:
        error_msg = "Customer already exist with %s ID" % ssnid
        l.append(False)
        l.append(error_msg)
        return l
    else:
        cur.execute("""INSERT INTO customer(SSN_ID, Name, Address, City, State, Age) VALUES(%s,%s,%s,%s,%s,%s)""",(ssnid, name, address, city, state, age))
        l.append(True)
        l.append("")
        mysql.connection.commit()
        cur.close()
        return l

def createAccount(cid, aType, deposit):
    dur=3
    cur = mysql.connection.cursor()
    l = []
    res1 = cur.execute("SELECT * from account where Customer_ID=%s" % cid)
    if res1 == 1:
        error_msg = "Customer already exist with %s ID" % cid
        l.append(False)
        l.append(error_msg)
        return l
    else:
        cur.execute("""INSERT INTO account(Customer_ID, Account_Type, Balance, CR_date, CR_last_date, Duration) VALUES(%s,%s,%s,%s,%s,%s)""",
                    (cid, aType, deposit, datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d'), dur))
        l.append(True)
        l.append("")
        mysql.connection.commit()
        cur.close()
        return l

def getCustomerSSnidDetils(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from customer where SSN_ID=%s" % ssnid)
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        res2 = cur.fetchall() #res2 = ({'Customer_ID': 1, 'Account_ID': 10, 'Account_Type': 'S', 'Status': 'Activated', 'Message': 'login', 'Last_Updated': datetime.datetime(2020, 6, 13, 18, 43, 38)},)
        return res2[0]
    else:
        return False

def updateCustomer(ssnid, name, address, age):
    cur = mysql.connection.cursor()

    res1 = cur.execute("Update customer SET Name=%s, Address = %s, Age = %s where SSN_ID=%s",(name, address, age, ssnid))
    if res1 == 1:
        l.append(True)
        l.append("")
        return l
    else:
        error_msg = "No Customer exist with %s ID" %ssnid
        l.append(False)
        l.append(error_msg)
        return l


def deleteCustomer(ssnid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("DELETE FROM customer where SSN_ID=%s" % ssnid)
    mysql.connection.commit()
    cur.close()
    l=[]
    if res1 == 1:
        l.append(True)
        l.append("")
        return l
    else:
        error_msg = "No Customer exist with %s ID" %ssnid
        l.append(False)
        l.append(error_msg)
        return l

def getCustomerDetails():
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM customer")
    res2 = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    l = []
    if res1 == 1:
        l.append(True)
        l.append(res2)
        return l
    else:
        error_msg = "No Customer exist"
        l.append(False)
        l.append(error_msg)
        return l

def getAccountIdDetils(aid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from account where Account_ID=%s" % aid)
    mysql.connection.commit()
    cur.close()
    if res1 == 1:
        res2 = cur.fetchall()  # res2 = ({'Customer_ID': 1, 'Account_ID': 10, 'Account_Type': 'S', 'Status': 'Activated', 'Message': 'login', 'Last_Updated': datetime.datetime(2020, 6, 13, 18, 43, 38)},)
        return res2[0]
    else:
        return False

def deleteAccount(aid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("DELETE FROM account where Account_ID=%s" % aid)
    mysql.connection.commit()
    cur.close()
    l = []
    if res1 == 1:
        l.append(True)
        l.append("")
        return l
    else:
        error_msg = "No Customer exist with %s ID" % aid
        l.append(False)
        l.append(error_msg)
        return l

def getSsnidAccounts(ssnid):
    pass

def deposit(aid,damt):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM account where Account_ID=%s" % aid)
    l=[]
    if res1==1:
        cur.execute("Update account SET Balance=Balance+%s where Account_ID=%s", (damt, aid))
        mysql.connection.commit()
        cur.close()
        l.append(True)
        l.append("")
        return l
    else:
        mysql.connection.commit()
        cur.close()
        error_msg = "No Customer exist with %s ID" % aid
        l.append(False)
        l.append(error_msg)
        return l

def withdraw(aid,wamt):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM account where Account_ID=%s" % aid)
    l=[]
    if res1 == 1:
        cur.execute("Update account SET Balance=Balance-%s where Account_ID=%s", (wamt, aid))
        mysql.connection.commit()
        cur.close()
        l.append(True)
        l.append("")
        return l
    else:
        mysql.connection.commit()
        cur.close()
        error_msg = "No Customer exist with %s ID" % aid
        l.append(False)
        l.append(error_msg)
        return l

def transfer(amount, SrcAid, TgtAid):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * FROM account where Account_ID=%s" % SrcAid)
    l=[]
    if res1==1:
        val = cur.fetchall()  # val is a tuple
        for k, v in val[0].items():
            if k == 'Account_Type':
                at1 = v
    else:
        mysql.connection.commit()
        cur.close()
        error_msg = "No Customer exist with %s ID" % SrcAid
        l.append(False)
        l.append(error_msg)
        return l

    res2 = cur.execute("SELECT * FROM account where Account_ID=%s" % TgtAid)
    if res2==1:
        val = cur.fetchall()  # val is a tuple
        for k, v in val[0].items():
            if k == 'Account_Type':
                at2 = v
    else:
        mysql.connection.commit()
        cur.close()
        error_msg = "No Customer exist with %s ID" % TgtAid
        l.append(False)
        l.append(error_msg)
        return l

    if res1 == 1 and res2 == 1:
        #Deduct from Source Account
        cur.execute("Update account SET Balance=Balance-%s where Account_ID=%s", (amount, SrcAid))

        #Add into Target Account
        cur.execute("Update account SET Balance=Balance+%s where Account_ID=%s", (amount, SrcAid))

        #Insert Data into Transaction Table
        cur.execute("""INSERT INTO transaction(Customer_ID, Account_Type, Amount, Transaction_date, Source_Acct_type, Target_Acct_type) VALUES(%s,%s,%s,%s,%s,%s)""",
                    (cid1, at1, amount, datetime.now(), at1, at2))
        mysql.connection.commit()
        cur.close()
        l.append(True)
        l.append("")
        return l
    else:
        mysql.connection.commit()
        cur.close()
        error_msg = "No Customer exist with %s ID" % aid
        l.append(False)
        l.append(error_msg)
        return l

def statementByNumber(aid,n):
    cur = mysql.connection.cursor()
    res1 = cur.execute("SELECT * from transaction where SSN_ID=%s" % ssnid)
    mysql.connection.commit()
    cur.close()

app.run(debug=True)
