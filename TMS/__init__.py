from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask Instance
app = Flask(__name__)
# Secret Key!
app.config['SECRET_KEY'] = 'hjfyui896rghj896r56'
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Initialize the Database
db = SQLAlchemy(app)

from .routes import *

