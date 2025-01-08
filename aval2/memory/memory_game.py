
from random import shuffle, sample
from memory_card import MemoryCard


class MemoryGame:
    def __init__(self):
        self.cards = []
    
    def start(self, quantity):
        self.cards = []
        for number in range(quantity):
            self.cards.append(MemoryCard(number + 1))
            self.cards.append(MemoryCard(number + 1))
        shuffle(self.cards)

    def play(self, index1, index2):
        card1 = self.cards[index1]
        card2 = self.cards[index2]

        if card1.is_matched() or card1.is_matched():
            return False

        if card1.get_value() == card2.get_value():
            card1.match()
            card2.match()
            return True
        
        return None
    
    def random_pair(self):
        unmatched_indexes = [ index for index, card in enumerate(self.cards) if not card.is_matched() ]

        return tuple(sample(unmatched_indexes, 2))

    def is_game_over(self):
        for card in self.cards:
            if not card.is_matched():
                return False
        return True
    
    def show_cards(self):
        for card in self.cards:
            print(f'{str(card):^5}', end='')
        print()
