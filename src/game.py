from deck import Deck
from played_pile import PlayedPile
from discard_pile import DiscardPile

class Game:

    def __init__(self):
        self.deck = Deck()
        self.playedPile = PlayedPile()
        self.discardPile = DiscardPile()

        self.registeredPlayers = []
        self.currPlayerIndex = 0

        self.numTurns = 0

    def registerPlayer(self, player):
        print("registerPlayer() called.")

        # Add this player to the list
        self.registeredPlayers.append(player)

    def go(self):
        print("go() called.")

        # The game doesn't make sense if there are not 2 or more players...
        if len(self.registeredPlayers) < 2:
            print("ERROR: 2 or more players must be registered before go() can be called.")
            return

        while self.numTurns < 10:
            self.registeredPlayers[self.currPlayerIndex].takeTurn()
            self.currPlayerIndex += 1

            if self.currPlayerIndex == len(self.registeredPlayers):
                self.currPlayerIndex = 0

            self.numTurns += 1


