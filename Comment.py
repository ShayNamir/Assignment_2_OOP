class Comment:
    def __init__(self, post, author_user_name, content):
        self.__post = post
        self.__content = content
        self.__author_name = author_user_name

    def get_content(self):
        return self.__content


