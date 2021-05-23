# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash , session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from . import db
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.route('/login/', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    msg = ''
    # Check if "mail" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'mail' in request.form and 'password' in request.form:
        # Create variables for easy access
        mail = request.form['mail']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM utilisateur WHERE mail = %s AND Password = %s', (mail, password))
        # Fetch one record and return result
        account = cursor.fetchone()
                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['mail'] = account['mail']
            # Redirect to menu page
            return redirect(url_for('menu'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect mail/password!'
    return render_template('index.html', msg='')