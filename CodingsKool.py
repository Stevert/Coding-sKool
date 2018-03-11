import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'coding.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('CODING SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/')
def start():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS entries (id integer primary key autoincrement,username TEXT , password text ,test text , urscore real ,maxscore real ,totalperct real ,prof text )")
    return render_template('login1.html')

@app.route('/signup', methods=['POST'])
def add_signup():
    if request.method !='POST':
        abort(401)
    db = get_db()
    u=request.form['username']
    v= request.form['password']
    db.execute('insert into entries (username, password,test,urscore,maxscore,totalperct,prof) values (?, ?,?,?,?,?,?)',
                 [request.form['username'], request.form['password'],"",0,0,0,""])
    db.commit()
    db = get_db()
    cur = db.execute('select username, password from entries ')
    entry = cur.fetchall();
    print(entry)
    for row in entry:
        print(row)
    session['signup'] = True
    flash('Successfully Signed In')
    return render_template('quiz31.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()

        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login1.html', error=error)

@app.route("/final", methods=["GET",'POST'])
def move():
    #form = InputForm(request.form)
    v = request.get_json().get('mvar')
    print(v)

    return render_template('final.html')


######
'''
conn = sqlite3.connect('coding.db')
c = conn.cursor()


@app.route('/')

def insert():
    return render_template("quiz31.html")
    if not session.get(in_flag):
        return render_template('login.html')
    else:
        print("Values currectly inserted")




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
    qts=['11']
    cans=[]
    print(data)
    for item in data:
        # loop over every row
        qts = qts.append(str(item['question'])) # + '\n'
        cans = cans.append(str(item['correctAnswer']))
    print(qts)
    print(cans)
    return ''



'''



if __name__ == '__main__':
    app.run()

