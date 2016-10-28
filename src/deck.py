import random

from game_constants import Color
from game_constants import numberFreq
from card import Card

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