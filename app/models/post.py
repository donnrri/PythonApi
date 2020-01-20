class Post(object):
    def __init__(self, blog_id, title, content, author, post_id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author= author
        self.post_id = post_id
        self.created_date = date

    def save_post(self, db):
        db.insert('posts', self.json())

    def json(self):
        return {
            'id': self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'created_date': self.created_date
        }

