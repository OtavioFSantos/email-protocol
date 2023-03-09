class Response:
    def __init__(self, type, message, data=False):
        self.type = type
        self.message = message
        self.data = data

    def __convert(self):
        if self.type == 'Error':
            self.message = '\033[;1m\033[1;31m' + self.message + '\033[m' 
        else:
            self.message = '\033[1;32m' + self.message + '\033[m'

    def value(self):
        self.__convert()
        return self.message