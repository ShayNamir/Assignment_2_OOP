from Post import Post


class ImagePost(Post):
    def __init__(self, user, path):
        super().__init__(user, path)


    def display(self):
        return  # Fill

    def __str__(self):
        return "{0} posted a picture:\n".format(self.get_publisher().get_name())
