from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config) # Configuration from config.py
db = SQLAlchemy(app) # DB object connected to app

from app import routes