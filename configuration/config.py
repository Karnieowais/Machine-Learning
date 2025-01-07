class Configuration:
    def __init__(self):
        return self

    def conf(self, *args, **kwargs):
        for val in kwargs:
            return self.val
        return "Out of conf"


Conf = Configuration()