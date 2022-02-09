from quiz import Quiz
import random

# Dunder main to start the game
if __name__ == '__main__':
    random.seed(2)
    game = Quiz()
    game.start()
