class Sources:
    '''
    Source class that define News objects
    '''
    def __init__(self, name, author, title, description, url, publishedAt, content):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content
    
    