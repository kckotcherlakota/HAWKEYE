from flask import Flask, render_template
from flask import send_file
from flask import send_from_directory
import pandas as pd
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash,g
from functools import wraps
import sqlite3
import os


from flask import request,redirect, url_for
app = Flask(__name__)

# config
app.secret_key = 'my precious'
app.database = "sample.db"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    g.db = connect_db()
    
    g.db.close()
    return render_template('index.html')  # render a template

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] != 'admin') \
                or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

def connect_db():
    return sqlite3.connect(app.database)

@app.route("/downn")
def process():
#    df=pd.read_excel("/home/krishna/Desktop/fa1/attta.xlsx")
    df=pd.read_excel("Don.xlsx")
    return df.to_html()
@app.route("/refresh")
def proces():
    import delete
    return render_template('index.html',name=name)
    
    
    
@app.route('/exec')
def parse(name=None):
    import test
    
    return render_template('index.html',name=name) 


@app.route('/exec2')
def parse1(name=None):
	import videostab
	
	return render_template('index.html',name=name)

if __name__ == '__main__':
    app.run()
   