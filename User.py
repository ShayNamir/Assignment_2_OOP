"""
Do we need to check for existing username before adding?
"""


class User:
    def __init__(self, name, password, is_in):
        self.name = name
        self.password = password
        self.followers = set()  # Initialize an empty set for followers
        self.is_log_in = is_in

    '''
    This function will get a user and follow him
    '''

    def follow(self, user):
        if self.is_log_in:  # Check if the user is logged in
            self.followers.add(user)

    '''
    This function will get a user and remove the follow from him, if exist 
    '''

    def unfollow(self, user):
        if self.is_log_in:  # Check if the user is logged in
            self.followers.remove(user)

    def user_log_in(self):
        self.is_log_in = True

    def user_log_out(self):
        self.is_log_in = False

    def get_name(self):
        return self.name

    def check_pass(self, password):
        if self.password == password:
            return True
        return False
