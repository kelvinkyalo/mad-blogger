import requests
from flask import render_template, request, Blueprint
from blog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    title = 'Mad-Blogger'
    return render_template('home.html', title=title, posts=posts)

@main.route('/quotes')
def quotes():
    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    author = 'Jeff'
    quote = 'I just wanted to let you know that the second episode of Doctor Who season, titled "The Shakespeare Code'

    r = requests.get(url.format(author, quote)).json()
    
    quotes = {
        'author' : r['author'],
        'quote' : r['quote'],
    }
    print(quotes)
    return render_template('quotes.html', title='Random Quotes', quotes=quotes)


@main.route('/about')
def about():
    return render_template('about.html')