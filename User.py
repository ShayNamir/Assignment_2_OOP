

from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class User:
    def __init__(self, name, password, is_in):
        self.__name = name
        self.__password = password
        self.__followers = set()  # this is the observer set
        self.__is_log_in = is_in
        self.__posts_num = 0
        self.__notifications = []

    '''
    This function will get a user and follow him
    '''

    def __add_observer(self, user):
        self.__followers.add(user)

    def __remove_observer(self, user):
        user.__followers.discard(self)  # If self doesn't exist in user.__followers -> do nothing

    def notify_observers(self):
        # Send a notification to all followers
        for observer in self.__followers:
            observer.update("{0} has a new post".format(self.get_name()))

    def update(self, notification):
        self.__notifications.append(notification)

    def __get_followers(self):
        return self.__followers

    def add_notification(self, text):
        self.__notifications.append(text)

    def follow(self, user):
        if self.__is_log_in:  # Check if the user is logged in
            if self != user:  # Can't follow yourself
                initial_length = len(user.__get_followers())
                user.__add_observer(self)
                if len(user.__get_followers()) > initial_length:  # Check if the new user is added
                    print("{0} started following {1}".format(self.get_name(), user.get_name()))

    def get_last_not(self):
        return self.__notifications[len(self.__notifications) - 1]

    '''
    This function will get a user and remove the follow from him, if exist 
    '''

    def unfollow(self, user):
        if self.__is_log_in:  # Check if the user is logged in.
            initial_length = len(user.__get_followers())
            user.__remove_observer(self)  # If self doesn't exist in user.__followers -> do nothing
            if len(user.__get_followers()) < initial_length:  # Check if the new user is added
                print("{0} unfollowed {1}".format(self.get_name(), user.get_name()))

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
        post = PostFactory.create_post(self, typ, content, price, loc)  # Create a post using a factory design pattern
        if post:
            self.__posts_num += 1

            # Send a notification to all followers using the observer pattern
            self.notify_observers()

            # Print the post-details
            print(post)
            return post
        else:
            return None  # Error

    def print_notifications(self):
        print("{0}'s notifications:".format(self.get_name()))
        for notification in self.__notifications:
            print(notification)

    def __str__(self):
        ans = "User name: {0}, Number of posts: {1}, Number of followers: {2}".format(self.__name, self.__posts_num,
                                                                                      len(self.__followers))
        return ans

    def __eq__(self, other) -> bool:
        if isinstance(other, User):
            return self.get_name() == other.get_name()  # Can't be two users with the same name
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__name)


# This class using the Factory Design pattern to create a post
class PostFactory:
    @staticmethod
    def create_post(user, typ, content, price=None, loc=None):
        if typ == "Text":
            return TextPost(user, content)
        elif typ == "Image":
            return ImagePost(user, content)
        elif typ == "Sale":
            return SalePost(user, content, price, loc)
        else:
            return None  # Error



