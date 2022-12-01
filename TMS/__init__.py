from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create a Flask Instance
app = Flask(__name__)
# Secret Key!
app.config['SECRET_KEY'] = 'hjfyui896rghj896r56'
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Initialize the Database
db = SQLAlchemy(app)
# Hash Passwords in the system
bcrypt = Bcrypt(app)
# Initialize the flask_login
login_manager = LoginManager(app)

from .routes import *
from .models import User, Post

with app.app_context():
    db.create_all()