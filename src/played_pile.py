from game_constants import Color

class PlayedPile:
    def __init__(self):
        # Create played pile
        print("Creating played pile...")
        self.playedPile = {}

        for color in Color:
            self.playedPile[color] = 0

        print("Created played pile. Played pile = " + repr(self.playedPile))

    # Use this to check is a particular card is playable on the played pile.
    def isPlayable(self, card):

        if card.number == self.playedPile[card.color] + 1:
            return True
        else:
            return False

    # Plays the provided card onto the played pile, is possible.
    def play(self, card):
        print("PlayedPile.play() called with card = " + repr(card))
        if card.number == self.playedPile[card.color] + 1:
            self.playedPile[card.color] += 1
            return True
        else:
            return False

    def getCurrScore(self):
        currScore = 0
        for key, value in self.playedPile.items():
            currScore += value

        return currScore


