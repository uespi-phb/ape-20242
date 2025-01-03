
from random import shuffle, randint
from domino_tile import DominoTile


class DominoSet:

    def __init__(self, tiles=[]):
        if tiles:
            if not all(isinstance(tile, DominoTile) for tile in tiles):
                raise TypeError(f'Argument tiles must be a list of DominoTile')
            self.__tiles = tiles
        else:
            self.__tiles = []


    def clear(self):
        self.__tiles.clear()


    def generate_tiles(self):
        self.__tiles = []
        for n1 in range(0,7):
            for n2 in range(n1,7):
                self.__tiles.append(DominoTile(n1, n2))

    
    def shuffle_tiles(self):
        shuffle(self.__tiles)


    def show_tiles(self):
        for tile in self.__tiles:
            print(tile, end=' ')
        print()


    def pick_tiles(self, n):
        picked_tiles = DominoSet()
        picked_tiles.clear()
        for _ in range(n):
            index = randint(0, len(self.__tiles) - 1)
            tile = self.__tiles.pop(index)
            picked_tiles.__tiles.append(tile)
        return picked_tiles

