from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '6f591923c71c2caa782aea56e8625a54'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


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

if __name__ == '__main__':
    app.run(debug=True)