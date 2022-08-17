from flask import Flask, render_template, request
from passlib.hash import sha256_crypt
import mysql.connector as database
app = Flask(__name__)
database_connection = database.connect(user='carsAdmin', password='carsAdmin', database='Login')
@app.route('/')
def index():
  password = sha256_crypt.encrypt("newPassword")
  email = "what@ever.com"
  username = email

  cur = database_connection.cursor()
  cur.execute('INSERT INTO Login (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
  database_connection.commit()
  cur.close()

  return "New user added"
if __name__ == '__main__':
  app.run(debug=True, host='localhost', port='3306')