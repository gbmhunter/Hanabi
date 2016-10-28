from deck import Deck

class Game:

    def __init__(self):
        self.deck = Deck()

    def registerPlayer(self, player):
        print("registerPlayer() called.")