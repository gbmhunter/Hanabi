# Describes an interface for a particular player. Designed to be inherited to create actual players.
class PlayerInterface:
    def __init__(self):
        print("New player being created.")

    def takeTurn(self, playersCards, playedPile, discardPile):
        raise NotImplementedError()

