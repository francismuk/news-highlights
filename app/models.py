class Sources:
    '''
    Source class that define News objects
    '''
    def __init__(self,id, sources, category, language, country, url, name, title, description,urlToImage, publishedAt):
        self.id = id
        self.sources = name
        self.category = name
        self.language = name
        self.country = name
        self.url = url
        self.name = name
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    
class Articles:
    '''
    Class that defines articles
    '''
    def __init__(self, title, author, url, content):
        self.title = title        
        self.author = author
        self.url = url
        self.content = content
