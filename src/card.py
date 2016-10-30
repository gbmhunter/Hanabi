# Represents a single card in the Hanabi game.
class Card:
    def __init__(self, uniqueId, color, number):
        self.uniqueId = uniqueId
        self.color = color
        self.number = number

    def __repr__(self):
        return "{ uniqueId = %s, num = %s, color = %s }" % (self.uniqueId, self.number, self.color)