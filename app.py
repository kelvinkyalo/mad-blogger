from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6f591923c71c2caa782aea56e8625a54'

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
def index():
    title = 'BlogHub'
    return render_template('index.html', title=title, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=posts)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)