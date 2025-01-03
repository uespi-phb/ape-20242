
from domino_set import DominoSet

domino = DominoSet()
domino.generate_tiles()
domino.shuffle_tiles()

print('PEÇAS RETIRADAS:')
picked_tiles = domino.pick_tiles(5)
picked_tiles.show_tiles()

print('PEÇAS RESTANTES:')
domino.show_tiles()
