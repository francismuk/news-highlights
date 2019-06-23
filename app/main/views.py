from flask import render_template,request,redirect,url_for
from app import app
from ..requests import get_sources
from ..models import Sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    category_general = get_sources('general')
    category_business = get_sources('business')
    category_entertainment = get_sources('entertainment')
    category_sports = get_sources('sports')
    category_technology = get_sources('technology')
    category_science = get_sources('science')
    title = 'Welcome to the best News service'
    return render_template('index.html', title=title, general=category_general, business=category_business, entertainment=category_entertainment, sports=category_sports, technology=category_technology, science=category_science)

@app.route('/articles/<source_title>')
def articles(source_title):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('articles.html',title = source_title)