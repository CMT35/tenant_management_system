from . import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
from .models import User, Post
from flask_login import login_user

posts = [
    {
        'author': 'Chris Thuo',
        'title': 'Property Management 1',
        'content': 'First post content',
        'date posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Property Management 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home_page.html', posts=posts)


@app.route('/about')
def about():  # put application's code here
    return render_template('about_page.html', title='About')


# noinspection PyArgumentList
@app.route('/register', methods=['GET', 'POST'])
def register():  # put application's code here
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        users = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(users)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
