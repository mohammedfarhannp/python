from random import choice

class randGen:
    def __init__(self, charset):
        self.charset = charset

    def randStr(self, length):
        return "".join([choice(self.charset) for _ in range(length)])

    def randFileName(self, length, extension):
        return ".".join([self.randStr(length), extension])
