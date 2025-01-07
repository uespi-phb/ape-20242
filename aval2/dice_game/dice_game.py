
from die import Die


class DiceGame:
    die = None

    def __init__(self, players, dice_sides=6):
        if not isinstance(players, int):
            raise TypeError(f'Argument players must be an integer: {players}')
        if players < 2:
            raise ValueError(f'Dice game must have at least 2 players')
        self.players = players
        self.dice_sides = dice_sides

        DiceGame.die = Die(dice_sides)

        self.__reset()

    def __reset(self):
        self.scores = None
        self.state = None

    def start(self):
        self.scores = [0] * self.players
        self.state = [None] * self.players

    def finish(self):
        print('RESULTADO FINAL:')
        self.show_scores()
        self.__reset()

    def play(self):
        for player in range(self.players):
            self.state[player] = DiceGame.die.roll()

        max_side = max(self.state)
        for player in range(self.players):
            if self.state[player] == max_side:
                self.scores[player] += 1

    def show_dices(self):
        for player in range(self.players):
            print(f'J{player + 1}: {self.state[player]}\t', end='')
        print()

    def show_scores(self):
        for player in range(self.players):
            print(f'J{player + 1}: {self.scores[player]}\t', end='')
        print()
