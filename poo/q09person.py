
class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def __repr__(self):
        return f'Person({self.__name},{self.__age})'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age <= 0:
            raise Exception(f'Invalid age: {age}')
        self.__age = age


p1 = Person('Maria Callas', 78)
p2 = Person('Allan Turing', 106)
p3 = Person('Bebê', 1)
