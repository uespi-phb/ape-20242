
class Temperature:
    def __init__(self, celsius):
        self.set_celsius(celsius)

    def __str__(self):
        return f'{self.__celsius}ºC'

    def __repr__(self):
        return str(self)

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, celsius):
        if celsius < -273.15:
            raise Exception(f'Invalid temperature: {celsius}')
        self.__celsius = celsius


t1 = Temperature(75)
t2 = Temperature(-200)
