
class BloodType:
    def __init__(self, data):
        if isinstance(data, BloodType):
            self.type = data.type
            self.rh_factor = data.rh_factor
        elif isinstance(data, str):
            self.type, self.rh_factor = self.__validate_str(data)
        else:
            raise TypeError('invalid data type')


    def __validate_str(self, data):
        if (len(data) < 2) or (len(data) > 3):
            raise ValueError(f'invalid string format: {data}')

        rh_factors = ('+', '-')
        blood_types = ('A', 'B', 'AB', 'O')
        type, rh = data[0:-1], data[-1]
        if rh not in rh_factors:
            raise ValueError(f'invalid RH factor: {rh}')
        if type not in blood_types:
            raise ValueError(f'invalid blood type: {type}')
        return (type, rh)


    def __str__(self):
        return f'{self.type}{self.rh_factor}'


    def __repr__(self):
        return f'BloodType({self.type}{self.rh_factor})'


    def can_donate_to(self, other):
        if not isinstance(other, BloodType):
            raise TypeError(f'not instance of BloodType: {other}')
        
        if (self.rh_factor == '+') and (other.rh_factor == '-'):
            return False
        
        if self.type == 'O':
            return True
        elif self.type in other.type:
            return True
        
        return False 


    def can_receive_from(self, other):
        pass

