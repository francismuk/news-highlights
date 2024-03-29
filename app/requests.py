import urllib.request
import json  # urllib.request will help us create a connection to the API URL and send a request.
from .models import Source, Articles


# Getting the api key
api_key = None

# Getting the news base url
base_url = None

# Getting the articles
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']

def get_sources(category):
    """
    Function that gets the json response to the url request
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response["sources"]:
            source_results_list = get_sources_response["sources"]
            source_results = process_results(source_results_list)

    return source_results

def process_results(sources_list):
    """
    function that processes the json and returns a list of objects
    Args:
        source_list: a list of dictionaries that contain source details
    Returns:
        sources_results: a list of source objects
    """
    source_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        if url:
            source_object = Source(id, name, description, url, category, language, country)
            source_results.append(source_object)

    return source_results


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
        publishedAt = article.get('publishedAt')

        if urlToImage:
            article_source_object = Articles(author, title, description, url, urlToImage, publishedAt)
            article_location_list.append(article_source_object)

    return article_location_list
