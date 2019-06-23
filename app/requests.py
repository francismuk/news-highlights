from app import app
import urllib.request,json
from models import Sources, Articles
from config import DevConfig



# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

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
        sources = sources_item.get('sources')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        name = sources_item.get('name')
        title = sources_item.get('title')
        description = sources_item.get('description')
        urlToImage = sources_item.get('urlToImage')
        publishedAt = sources_item.get('publishedAt')
        
        sources_object = Sources(id, sources, category, language, country, name, title, description, urlToImage, publishedAt)
        sources_results.append(sources_object)
        
    return sources_results