# SocialNetwork.py
from User import User


class SocialNetwork:
    def __init__(self, name):
        # Initialize the SocialNetwork class
        self.name = name
        self.users = set()  # Set that's contained all the user that's in the network

    # Methods
    def __get_user_by_name__(self, name):
        for user in self.users:
            if name==user.get_name():
                return user

    '''
    This function will get a name and a password and register the user to this network
    '''
    def sign_up(self, name, passw):
        user = User(name, passw, True)  # The user will be logged in
        self.users.add(user)  # Add the user to this network

    def log_out(self,name):
        user = self.__get_user_by_name__(name)
        user.user_log_out()

    def log_in(self, name, password):
        user = self.__get_user_by_name__(name)  # Get the user

        if user.check_pass(password):  # Check the password
            user.user_log_in()  # If correct-> log in
