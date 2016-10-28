# Represents a single card in the Hanabi game.
class Card(object):
    def __init__(self, color, number):
        self.color = color
        self.number = number


if __name__ == "__main__":
    print("Hanabi simulator started.")

    card1 = Card("red", 2)
