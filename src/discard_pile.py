class DiscardPile:
    def __init__(self):
        print("Creating discard pile...")
        self.cardUids = []

    def addCard(self, cardUid):
        print("DiscardPile.addCard() called with cardUid = " + repr(cardUid))
        self.cardUids.append(cardUid)