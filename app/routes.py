from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    products = [
        {
            'id': 1001,
            'title': 'Twitter Bot',
            'price': 150,
            'desc': 'This twitter bot will destroy your enemies!'
        },
        {
            'id': 1002,
            'title': 'Twitter T-Shirt',
            'price': 15,
            'desc': 'You\'ll look pretty okay in this.'
        },
        {
            'id': 1003,
            'title': 'Twitter Stickers',
            'price': 5,
            'desc': 'Be a rebel, put them on stop signs!'
        },
        {
            'id': 1004,
            'title': '100k Follower Account',
            'price': 5000,
            'desc': 'Be an influencer today! Christiano Ronaldo gets paid $950,000 for every post he makes.'
        }
    ]
    return render_template('index.html', title='Home', products=products)

@app.route('/title')
def title():
    return render_template('form.html')
