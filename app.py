from flask import Flask, flash, redirect, request, session, url_for, escape, make_response
from flask import json
from datetime import datetime
from flask import render_template
import pymysql.cursors
import pymysql
import os
import urllib.request

conn = pymysql.connect(user='2611982589',port=3306,password='mypassword',host='tsuts.tskoli.is',database='2611982589_verk7_user')

app = Flask(__name__)
app.secret_key= os.urandom(16)
print(os.urandom(16))

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        userID = userDetails['userID']
        email = userDetails['email']
        name = userDetails['name']
        cur = conn.cursor()
        cur.execute("INSERT INTO 2611982589_verk7_user.users(userID, nafn, email, lykil) VALUES(%s,%s,%s,%s)",(userID,nafn,email,lykil))
        conn.commit()
        cur.close()
        return redirect('/users')

    elif request.method == 'POST':
        conn.rollback()
        return redirect('/error')
    return render_template("index.html")

@app.route('/nyskra',methods=['GET','POST'])
def nyr():
    error = None
    if request.method == 'POST':
        userDetails = request.form
        userID = userDetails['userID']
        nafn = userDetails['nafn']
        email = userDetails['email']
        lykil = userDetails['lykil']
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO 2611982589_verk7_user.users(userID, nafn, email, lykil) VALUES(%s,%s,%s,%s)",(userID,nafn,email,lykil))
            conn.commit()
            cur.close()
            flash('þú hefur verið skráður inn')
            return redirect(url_for('users'))
        except pymysql.IntegrityError:
            error = 'Notandi er þegar skráður með þessu nafni og/eða lykilorði'
        
    return render_template('index.html', error=error)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        userID = request.form.get('userID')
        lykil = request.form.get('lykil')
         
        conn = pymysql.connect(user='2611982589',password='mypassword',host='tsuts.tskoli.is',database='2611982589_verk7_user')
        cur = conn.cursor()

        cur.execute("select count(*) from 2611982589_verk7_user.users where userID=%s and lykil=%s",(userID,lykil))
        result = cur.fetchone()
        print(result)
        if result[0] == 1:
            cur.close()
            conn.close()
            flash('you were successfully logged in')
            return render_template('users.tpl',user=user)
        else:
            error = 'innskráning mistókst - reyndu aftur'
    return render_template('index.html', error=error)
        
@app.route('/users')
def users():
    cur = conn.cursor()
    resultValue = cur.execute("select * from 2611982589_verk7_user.users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('/users.tpl',userDetails=userDetails)

@app.route("admin")
def admin():
    if not session,get('logged_in'):
        return render_template('index.html')
    else:
        try:
            cur =conn.cursor()
            resultValue = cur.execute("select * from 2611982589_verk7_user.users")
            if resultValue > 0:
                userDetails = cur.fetchall()
                flash('velkomin')
                return render_template('/users.tpl',userDetails=userDetails)
        except pymysql.IntegrityError:
            error = 'þú hefur ekki aðgang að þessari síðu'
        return render_template('index.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return render_template('index.html')
        
#kóði fyrir verk_7
"""
conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Table created successfully";
conn.close()

@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/test/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

"""

if __name__ == '__main__':
    app.run(debug=True)