from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')
