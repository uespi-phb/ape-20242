from random import randint
from dice_combat import DiceCombat


def main():
    players_count = randint(2, 5)

    game = DiceCombat(players_count)
    game.start()

    while len(game.deads()) == 0:
        game.attack()

    print('JGDR|SAÙDE|VENCEU|')
    for player in game.get_players():
        winner = ''
        print(f'{player.get_number():^4}|{player.get_health()}|{winner:^6}|')

'''
JGDR|SAÚDE|VENCEU|
 J1 | 74  | Sim  |
 J2 |  0  | Não  |
'''


if __name__ == '__main__':
    main()
