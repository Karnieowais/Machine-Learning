class Configuration:
    def __init__(self):
        return None

    def conf(self, *args, **kwargs):
        for self.key, self.value in kwargs.items():
            print(f"{self.key} : {self.value}")
        return "Conf done"


Conf = Configuration()
Conf.conf('owais', 'shaziah', designation="Software Engineer", location="Kashmir")
