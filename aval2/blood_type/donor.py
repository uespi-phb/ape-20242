
from blood_type import BloodType


class Donor:

    def __init__(self, name, age, blood_type):
        self.name = name
        self.age = age
        self.blood_type = BloodType(blood_type)


    def __str__(self):
        return f'{self.name}({self.age},{self.blood_type})'


    def __repr__(self):
        return f'Donor({self.name},{self.age},{self.blood_type})'


    def can_donate_to(self, other):
        return self.blood_type.can_donate_to(other.blood_type)


    def can_receive_from(self, other):
        return self.blood_type.can_receive_from(other)