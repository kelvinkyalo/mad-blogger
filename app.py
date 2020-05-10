from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    title = '<h1>Hello Basic Bitches!! Fuck y\'all!! hahahahaha!!!!!!</h1>'
    return title

if __name__ == '__main__':
    app.run(debug=True)