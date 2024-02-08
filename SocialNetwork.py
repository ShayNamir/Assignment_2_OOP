# SocialNetwork.py
from User import User


# Static functions
def __is_pass_valid__(password):
    if 4 <= len(password) <= 8:
        return True
    return False


class SocialNetwork:
    def __init__(self, name):
        # Initialize the SocialNetwork class
        self.__name = name
        self.__users = []  # Set that's contained all the user that's in the network
        print("The social network {0} was created!".format(name))

    # Methods
    def __get_user_by_name__(self, name):
        for user in self.__users:
            if name == user.get_name():
                return user
        return None  # Return None if the user is not found

    '''
    This function will get a name and a password and register the user to this network
    '''

    def sign_up(self, name, password):
        # Check username and password validation
        if self.__is_user_exist__(name) or not __is_pass_valid__(
                password):  # If username is taken or password not valid
            return

        # Else add the user to the network
        user = User(name, password, True)  # The user will be logged in
        self.__users.append(user)  # Add the user to this network
        return user

    def log_out(self, name):
        user = self.__get_user_by_name__(name)
        if user is None:  # If the user does not exist
            return
        user.user_log_out()

    def log_in(self, name, password):
        user = self.__get_user_by_name__(name)  # Get the user
        if user is None:  # If the user does not exist
            return
        if user.check_pass(password):  # Check the password correctness
            user.user_log_in()  # If correct-> log in

    def __is_user_exist__(self, user_name):
        for user in self.__users:
            if user_name == user.get_name():
                return True
        return False

    def __str__(self):
        ans = "{0} social network:\n".format(self.__name)
        for user in self.__users:
            ans += str(user) + "\n"
        return ans
