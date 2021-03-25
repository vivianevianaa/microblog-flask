from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vivi'}
    posts = [
        {
            'author': {'username': 'Vivi'},
            'body': 'I tried so hard...'
        },
        {
            'author': {'username': 'Aurora'},
            'body': 'And got so far...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)