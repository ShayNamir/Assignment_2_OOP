from Post import Post


class SalePost(Post):
    def __init__(self, user, content, price, location):
        super().__init__(user, content)
        self.__price = price
        self.__location = location
        self.__is_av = True

    def set_to_sold(self):
        self.__is_av = False

    def discount(self, percent, password):
        # Mast provide a password to do it
        if not self.get_publisher().check_pass(password):
            return
        d = percent/100
        d -= 1
        self.__price *= d

    def get_publisher(self):
        return super().get_publisher()
