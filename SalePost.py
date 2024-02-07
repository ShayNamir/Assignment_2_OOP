class SalePost:
    def __init__(self, price, location):
        super().__init__()
        self.price = price
        self.location = location
        self.is_av = True

    def set_to_sold(self):
        self.is_av = False
