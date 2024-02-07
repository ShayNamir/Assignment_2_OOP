from Comment import Comment


class Post:
    def __init__(self, user, content):
        self.__publisher = user
        self.__content = content
        self.__likes = set()  # Initial the like set
        self.__comments = []  # Initial the comment set

    def __str__(self):
        return "hello"

    def comment(self, user, text):
        c = Comment(self, text, user)
        self.__comments.append(c)

    def get_publisher(self):
        return self.__publisher
