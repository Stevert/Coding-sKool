import sqlite3
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json

from flask import Flask

app = Flask(__name__)

conn = sqlite3.connect('coding.db')
c = conn.cursor()


@app.route('/')

def insert():
    return render_template("quiz3.html")
    '''if not session.get(in_flag):
        return render_template('login.html')
    else:
        print("Values currectly inserted")'''




@app.route('/insert')

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS CODINGKOOL(Name TEXT, password TEXT, level1 REAL,level2 REAL,level3 REAL)")

    Name="Stevert" #dummy
    password="abcd" #dummy
    level2=67;
    level1=55;
    level3=20;

    c.execute("INSERT INTO CODINGKOOL (Name, passsword, level1, level2, level3) VALUES (?, ?, ?, ?)",
              (Name, password, level1, level2))

    conn.commit()
    sqlite3.time.sleep(1)
    return ""


@app.route('/abc', methods=["POST"])
def receive():
    # read json + reply
    data = request.get_json()
    qts=[]
    cans=[]

    for item in data:
        # loop over every row
        qts = qts.append(str(item['question'])) # + '\n'
        cans = cans.append(str(item['correctAnswer']))
    print(qts)
    print(cans)
    return ''







if __name__ == '__main__':
    app.run()

