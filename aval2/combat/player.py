
from random import randint

class Player:

    def __init__(self, number, health = 100):
        self.__number = number
        self.__health = health
        self.__attack_power = randint(5, 20)


    def __str__(self):
        return f'J{self.__number}({self.__health, self.__attack_power})'
    
    
    def get_number(self):
        return self.__number
    

    def get_health(self):
        return self.__health
    

    def attack(self, player):
        player.health -= min(self.__attack_power, player.health)


    def dead(self):
        return self.__health == 0


    def alive(self):
        return self.__health > 0