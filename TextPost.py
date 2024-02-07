from Post import Post


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)
    
    def __str__(self):
        ans = "{0} published a post:\n".format(self.get_publisher().get_name())
        ans += '"{0}"\n'.format(super().__str__())
        return ans
