class DiscardPile:
    def __init__(self):
        print("Creating discard pile...")
        self.cards = []

    def addCard(self, card):
        print("DiscardPile.addCard() called with card = " + repr(card))
        self.cards.append(card)