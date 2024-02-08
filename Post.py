from Comment import Comment


class Post:
    def __init__(self, user, content):
        self.__publisher = user
        self.__content = content
        self.__likes = set()  # Initial the like set
        self.__comments = []  # Initial the comment set

    def __str__(self):
        return self.__content

    def comment(self, user, text):
        if not user._User__is_log_in:  # Check if the user is logged in
            return
        c = Comment(self, user, text)
        self.__comments.append(c)
        author = self.get_publisher()

        # If isn't me-> Send a notification
        author = self.get_publisher()
        if author != user:
            author.add_notifications("{0} commented on your post".format(user.get_name()))
            print("notification to {0}: {1}: {2}".format(author.get_name(), author.get_last_not(), c.get_content()))  # Print in the same line



    def get_publisher(self):
        return self.__publisher

    def like(self, user):
        if not user._User__is_log_in:  # Check if the user is logged in
            return

        self.__likes.add(user)
        # If isn't me-> Send a notification
        author = self.get_publisher()
        if author != user:
            author.add_notifications("{0} liked your post".format(user.get_name()))
            print("notification to {0}: {1}".format(author.get_name(), author.get_last_not()))  # Print in the same line

