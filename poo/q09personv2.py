
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.__name},{self.__age})'

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @name.setter
    def name(self, name: str):
        self.__name = name

    @age.setter
    def age(self, age: str):
        if age <= 0:
            raise Exception(f'Invalid age: {age}')
        self.__age = age


p1 = Person('Maria Callas', 78)
p2 = Person('Allan Turing', 106)
p3 = Person('Bebê', 1)

print(p1.name)
print(p1.age)

print(p2)
p2.age = 26
print(p2)
