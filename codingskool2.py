from flask import Flask
import sqlite3
import hashlib
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os

app = Flask(__name__)
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()








@app.route('/')
def iin():
    return render_template('login.html')

@app.route('/secret')
def home():
    if not session.get('signup'):
        return render_template('quiz3.html')
    else:
        return render_template('quiz3.html')
def home1():
    if not session.get('completion'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"



@app.route('/signup', methods=['POST'])

def do_admin_signup():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot1(Name TEXT,password Text,level1 REAL,level2 REAL,level3 REAL)")



    pass1 = request.form['password']
    user=request.form['username']
    c.execute("INSERT INTO stuffToPlot1(Name,password ) VALUES (?, ?)",
              (user, pass1))
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot1')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    if request.form['password']=='' and request.form['username']==' ':
        session['logged in']=True
        flash('logged in sussceesfully')
        return(home())
    else:
        session['logged in'] = False
        flash('login unsucessful')
        return home()






@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()




if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()