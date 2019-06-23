import urllib.request,json
from .models import Sources, Articles
from config import DevConfig

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
#Getting the articles url
articles_url =None

def configure_request(app):
    global api_key,base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)


    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        url = sources_item.get('url')
        name = sources_item.get('name')
        description = sources_item.get('description')
        
        if url:
            sources_object = Sources(id, name, description, url, category, language, country)
            sources_results.append(sources_object)
        
    return sources_results

def get_articles(source_id, limit):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id, limit, api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])

    return articles_location_results


def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')

        if url:
            article_source_object = Articles(author, title, description, url, urlToImage)
            article_location_list.append(article_source_object)

    return article_location_list
