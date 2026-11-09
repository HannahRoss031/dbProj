from app import app, db
from flask import render_template
from sqlalchemy import text

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/')
@app.route('/test')
def test():
    result = db.session.execute(
        text("SELECT franchID, franchName FROM franchises LIMIT 10")
    )
    rows = result.fetchall()

    output = "<h1>DB Testing!</h1>"
    for row in rows:
        output += f"<p>{row.franchID}: {row.franchName}</p>"
    return output