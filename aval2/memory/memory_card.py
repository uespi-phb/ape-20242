
class MemoryCard:
    def __init__(self, value):
        self.__value = value
        self.__is_matched = False

    def __str__(self):
        return str(self.__value) if self.__is_matched else '*'
    
    def __repr__(self):
        return str(self)
    
    def match(self):
        self.__is_matched = True

    def get_value(self):
        return self.__value

    def is_matched(self):
        return self.__is_matched
