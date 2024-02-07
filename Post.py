class Post:
    def __init__(self, user, content):
        self.publisher = user
        self.content = content
        self.likes = set()  # Initial the like set
        self.comments = set()  # Initial the comment set

    def __str__(self):
        return "hello"

