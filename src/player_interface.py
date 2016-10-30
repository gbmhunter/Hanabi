from hand import Hand

# Describes an interface for a particular player. Designed to be inherited to create actual players.
class PlayerInterface:
    def __init__(self, name):
        # print("New player being created.")

        self.name = name

    def takeTurn(self, playersCards, playedPile, discardPile):
        raise NotImplementedError()

