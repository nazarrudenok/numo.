from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   make_response)
from datetime import datetime, date
from pymongo import MongoClient
import hashlib

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://nazarrudenok:nazarkoqweA228rty@main.sbsvi8i.mongodb.net/?retryWrites=true&w=majority&appName=main")
db = cluster['numo']
collection = db['numocoll']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reg')
def reg():
    return ...

if __name__ == '__main__':
    app.run(debug=True, host= '192.168.1.249')