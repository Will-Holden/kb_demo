class Book:
    def __init__(self, name="", pubishTime="", publisher="", description=""):
        self.name = name
        self.publishTime = pubishTime
        self.publisher = publisher
        self.description = description
    def __getitem__(self, item):
        return self.__dict__[item]