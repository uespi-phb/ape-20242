import random


class Lamp:
    def __init__(self, power, color, initial_state=False):
        if initial_state:
            self.state = 'on'
        else:
            self.state = 'off'
        self.power = power
        self.color = color

    def __str__(self):
        return f'Lamp({self.power}W,{self.color},{self.state})'

    def turn_on(self):
        self.state = 'on'

    def turn_off(self):
        self.state = 'off'

    def print_state(self):
        print('Lamp is', self.state)


def lamp_test():
    lamps = []
    lamps_count = random.randint(5, 20)

    for _ in range(lamps_count):
        state = random.randint(0, 1)
        power = random.randint(1, 20) * 5
        color = random.choice(('white', 'yellow'))
        lamps.append(Lamp(power, color, state))

    print('My', lamps_count, 'lamps:')
    for lamp in lamps:
        print(lamp)


if __name__ == '__main__':
    lamp_test()
