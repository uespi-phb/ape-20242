from random import randint
from dice_game import DiceGame


def main():
    game = DiceGame(4)

    game.start()

    turns_count = randint(10, 20)
    for turn in range(turns_count):
        print(f'RODADA #{turn + 1}:')
        game.play()
        game.show_dices()

    game.finish()


if __name__ == '__main__':
    main()
