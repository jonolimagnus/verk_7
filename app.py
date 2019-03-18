from flask import Flask, flash, redirect, request, session, url_for, escape, make_response
from flask import json
from datetime import datetime
from flask import render_template
import pymysql.cursors
import os
import urllib.request

conn = pymysql.connect(user='kennitala',password='mypassword',host='tsutst.tskoli.is',database='')

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userDetais = request.form
        user = userDetails['user']
        email = userDetails['email']
        name = userDetails['name']
        cur = conn.cursor()
        cur.execute('INSERT INTO database.user(user, email, name), VALUES(%s,%s,%s)',(user,name,email))
        cur.commit()
        cur.close()
        return redirect('/users')

    elif request.method == 'POST':
        conn.rollback()
        return redirect('/error')
    return render_template("index.html")

@app.route('/users')
def users():
    cur == conn.cursor()
    resultValue = cur.execute("select * from database.users")
    if resultValue > 0
        userDetails = cur.fetchall()
        return render_template('/users.html'userDetails=userDetails)


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

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) 
               VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

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