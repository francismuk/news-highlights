from flask import render_template,request,redirect,url_for
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/articles/<int:title>')
def movie(articles_title):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('articles.html',id = articles_title)