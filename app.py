from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Welcome'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'Welcome'
    return render_template('about.html', title=title)

@app.route('/post')
def post():
    title = 'Welcome'
    return render_template('post.html', title=title)

@app.route('/contact')
def contact():
    title = 'Welcome'
    return render_template('contact.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)