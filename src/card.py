# Represents a single card in the Hanabi game.
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return "{ num = %s, color = %s }" % (self.number, self.color)