
class DominoTile:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2


    def __str__(self):
        return f'({self.number1},{self.number2})'


    def __repr__(self):
        return str(self)


    def flip(self):
        self.number1, self.number2 = self.number2, self.number1


    def is_double(self):
        return self.number1 == self.number2
