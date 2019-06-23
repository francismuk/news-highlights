from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources

# Views
@main.route('/')
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


@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id, per_page):
    """
    View source page function that returns the news details page in addition to its data.
    """
    news_source = get_articles(source_id, per_page)
    title = f'Welcome to {source_id}'
    return render_template('articles.html', title=title, name = source_id, news = news_source)
