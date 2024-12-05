import random


class Lamp:
    def __init__(self, initial_state=False):
        if initial_state:
            self.state = 'on'
        else:
            self.state = 'off'

    def turn_on(self):
        self.state = 'on'

    def turn_off(self):
        self.state = 'off'

    def print_state(self):
        print('Lamp is', self.state)


def lamp_test1():
    lamp1 = Lamp(True)
    lamp2 = Lamp()

    print('Lamp States:')
    print('- Lamp #1: ', end='')
    lamp1.print_state()

    print('- Lamp #2: ', end='')
    lamp2.print_state()


def lamp_test2():
    lamps = []
    lamps_count = random.randint(5, 20)

    for _ in range(lamps_count):
        # if random.randint(0, 1) == 0:
        #     state = False
        # else:
        #     state = True

        state = random.randint(0, 1)
        lamps.append(Lamp(state))

    print('My', lamps_count, 'lamps:')
    for lamp in lamps:
        lamp.print_state()


if __name__ == '__main__':
    lamp_test2()
