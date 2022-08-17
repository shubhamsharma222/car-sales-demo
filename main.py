from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from flask import flash, redirect, render_template, request, session, abort
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zpnokcisfqwwmx:1c4aa86ddbf81e37f083153ab930f2bf4b81a95955cb05ca515ae8142a595e5b@ec2-52-207-15-147.compute-1.amazonaws.com:5432/d36o315crg5okl'
db = SQLAlchemy(app)


class Login(db.Model):
    __tablename__ = 'login'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = sha256_crypt.encrypt(request.form['password'])
        username = email
        # password = sha256_crypt.encrypt("newPassword")
        # email = "what@ever.com"
        # username = email
        if db.session.query(Login).filter(Login.username == username).count() == 0:
            data = Login(username, password, email)
            db.session.add(data)
            db.session.commit()
            return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = email
        # password = sha256_crypt.encrypt("newPassword")
        # email = "what@ever.com"
        # username = email
        users = db.session.query(Login).filter(Login.username == username)
        if users:
            for user in users:
                if sha256_crypt.verify(password, user.password):
                    account = True
                else:
                    flash('wrong password!')
                return login()
        else:
            return login()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=5000)
