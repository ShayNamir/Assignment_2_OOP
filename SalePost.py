from Post import Post


class SalePost(Post):
    def __init__(self, user, content, price, location):
        super().__init__(user, content)
        self.__price = price
        self.__location = location
        self.__is_av = True

    def sold(self, password):
        # Mast provide a password to do it
        if not self.get_publisher().check_pass(password):
            return
        self.__is_av = False
        print("{0} product is sold:".format(self.get_publisher().get_name))

    def discount(self, percent, password):
        # Mast provide a password to do it
        if not self.get_publisher().check_pass(password):
            return
        d = percent/100
        d -= 1
        d = abs(d)
        self.__price *= d
        print("Discount on {0} product! the new price is: {1}\n".format(self.get_publisher().get_name, self.__price))

    def get_publisher(self):
        return super().get_publisher()

    def __str__(self):
        ans = "{0} posted a product for sale:'n".format(self.get_publisher().get_name())
        if self.__is_av:
            ans += "For sale! "
        else:
            ans += "Sold! "
        ans += super().__str__()
        ans += ", price: {0}, pickup from: {1}\n".format(self.__price, self.__location)
        return ans
