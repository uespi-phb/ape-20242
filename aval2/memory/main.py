

from memory_game import MemoryGame


def main():
    game = MemoryGame()
    
    game.start(5)
    game.show_cards()
    while not game.is_game_over():
        index1, index2 = game.random_pair()
        game.play(index1, index2)
        game.show_cards()


if __name__ == '__main__':
    main()
