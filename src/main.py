from enum import Enum
import random

# Enumerates the allowed card colors in the Hanabi game
class Color(Enum):
    blue = 1
    green = 2
    red = 3
    white = 4
    yellow = 5

numberFreq = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]


# Represents a single card in the Hanabi game.
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return "{ num = %s, color = %s }" % (self.number, self.color)


class Deck:
    def __init__(self):
        # Create a deck of cards in random order
        print("Creating deck...")
        self.cards = []

        for number in numberFreq:
            for color in Color:
                self.cards.append(Card(color, number))

        random.shuffle(self.cards)

        print("Shuffled cards. self.cards = " + repr(self.cards))




class Game:

    def __init__(self):
        self.deck = Deck()


if __name__ == "__main__":
    print("Hanabi simulator started.")

    game = Game()

