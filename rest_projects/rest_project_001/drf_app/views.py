from datetime import datetime


class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

class BlogPost(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

blogpost = BlogPost(title="This is a New Era", content="Pandemic Changed the way of life")
