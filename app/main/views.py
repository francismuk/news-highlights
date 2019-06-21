from flask import render_template,request,redirect,url_for
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/articles/<source_title>')
def articles(source_title):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('articles.html',title = source_title)