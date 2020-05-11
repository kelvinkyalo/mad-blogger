from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


posts = [
    {
        'author' : 'Joan',
        'title' : 'Blog Post 1',
        'content' : 'First post',
        'date_posted' : 'May 7 2020'
    },
    {
        'author' : 'Simon',
        'title' : 'Blog Post 2',
        'content' : 'Second post',
        'date_posted' : 'May 10 2020'
    }
]

@app.route('/')
def home():
    title = 'BlogHub'
    return render_template('home.html', title=title, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'wamuyujoan4@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)