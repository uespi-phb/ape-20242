
from random import sample
from player import Player

class DiceCombat:

    def __init__(self, n):
        if n < 2:
            raise ValueError('Game should have at least 2 players')
        self.__players_count = n
        self.__players = []


    def get_players(self):
        self.__players


    def start(self):
        self.__players = [ Player(p + 1) for p in range(self.__players_count) ]


    def attack(self):
        attacker, attacked = sample(self.__players, 2)
        attacker.attack(attacked)
        return (attacker, attacked)


    def deads(self):
        return [ player for player in self.__players if player.dead() ]
    
