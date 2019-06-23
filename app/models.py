class Sources:
    '''
    Source class that define News objects
    '''
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
    
class Articles:
    '''
    Class that defines articles
    '''
    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
