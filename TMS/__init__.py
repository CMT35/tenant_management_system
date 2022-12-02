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
login_manager.login_view = 'login'  # Tells extension where our login route is located
login_manager.login_message_category = 'info'  # Bootstrap class to make 'login required message' colorful

from .routes import *
from .models import User, Post

with app.app_context():
    db.create_all()