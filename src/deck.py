import random

from game_constants import Color
from game_constants import numberFreq
from card import Card

class Deck:
    def __init__(self):
        # Create a deck of cards in random order
        # print("Creating deck...")
        self.cards = []

        uniqueId = 0
        for number in numberFreq:
            for color in Color:
                self.cards.append(Card(uniqueId, color, number))
                uniqueId += 1

        random.shuffle(self.cards)

        # print("Shuffled cards. self.cards = " + repr(self.cards))

    # Removes and returns the top card from the deck
    def takeCard(self):

        # "Pop" the first card
        return self.cards.pop(0).uniqueId

    def getCard(self, cardUid):

        foundCard = None
        for card in self.cards:
            if card.uniqueId == cardUid:
                foundCard = card

        if foundCard is None:
            raise RuntimeError("Specified card UID did not exist in deck.")

        return foundCard