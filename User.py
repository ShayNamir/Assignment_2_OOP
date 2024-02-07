"""
Do we need to check for existing username before adding?
"""
from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class User:
    def __init__(self, name, password, is_in):
        self.__name = name
        self.__password = password
        self.__followers = set()  # Initialize an empty set for followers
        self.__is_log_in = is_in
        self.__posts_num = 0
        self.__notifications = []

    '''
    This function will get a user and follow him
    '''

    def follow(self, user):
        if self.__is_log_in:  # Check if the user is logged in
            initial_length = len(self.__followers)
            self.__followers.add(user)
            if len(self.__followers) > initial_length:  # Check if the new user is added
                self.__notifications.append("{0} started following {1}".format(self.get_name(), user.get_name()))
                self.print_last_not()

    def print_last_not(self):
        print(self.__notifications[len(self.__notifications)-1])

    '''
    This function will get a user and remove the follow from him, if exist 
    '''

    def unfollow(self, user):
        if self.__is_log_in:  # Check if the user is logged in
            self.__followers.remove(user)

    def user_log_in(self):
        self.__is_log_in = True
        print("{0} connected".format(self.__name))

    def user_log_out(self):
        self.__is_log_in = False
        print("{0} disconnected".format(self.__name))

    def get_name(self):
        return self.__name

    def check_pass(self, password):
        if self.__password == password:
            return True
        return False

    def publish_post(self, typ, content, price=None, loc=None):
        if typ == "Text":
            post = TextPost(self, content)
        elif typ == "Image":
            post = ImagePost(self, content)
        elif typ == "Sale":
            post = SalePost(self, content, price, loc)
        else:
            return None  # Error
        self.__posts_num += 1
        print(post)  # Print the post-details
        return post

    def print_notifications(self):
        print("FILL")

    def __str__(self):
        ans = "User name: {0}, Number of posts: {1}, Number of followers: {2}".format(self.__name, self.__posts_num, len(self.__followers))
        return ans





