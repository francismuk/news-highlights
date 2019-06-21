class Sources:
    '''
    Source class that define News objects
    '''
    def __init__(self,id, name, title, description,urlToImage, publishedAt):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    
class Aricles:
    '''
    Class that defines articles
    '''
    def __init__(self, title, author, url, content):
        self.title = title        
        self.author = author
        self.url = url
        self.content = content
