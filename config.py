class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?api_key=29cfe31df9fb475ebd6767b6b8ef74b4'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

















# import os

# class Config:
#     """
#     General configuration parent class
#     """
#     NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v1/sources?language=en&category={}&apiKey={}'
#     EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'

#     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')

# class ProdConfig(Config):
#     """
#     Production configuration child class
#     Args:
#         Config: The parent configuration class with general configuration settings
#     """
#     pass

# class DevConfig(Config):
#     """
#     Development configuration child class
#     Args:
#         Config: The parent configuration class with general configuration settings
#     """
#     DEBUG = True

# configer = {
#     'development':DevConfig,
#     'production':ProdConfig
# }