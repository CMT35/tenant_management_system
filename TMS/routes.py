from . import app
from flask import render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
from .models import User, Post


posts = [
    {
        'author': 'Corey Schafer',
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


@app.route('/register', methods=['GET', 'POST'])
def register():  # put application's code here
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    form = LoginForm('/login')
    if form.validate_on_submit():
        if form.email.data == 'admin@tms.com' and form.password.data == 'test':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

