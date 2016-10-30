class Hand:
    # Create a new hand, populating it with 5 cards from the deck
    def __init__(self, deck, game):
        # print("New hand being created.")
        self.cardUids = []
        self.game = game

        # Populate this hand with 5 cards from the deck
        for num in range(0, 5):
            self.cardUids.append(deck.takeCard())

    def __repr__(self):
        return "{ cardUids = %s }" % (self.cardUids)

    def isInHand(self, cardUid):

        foundCard = False
        for cardUidInHand in self.cardUids:
            if cardUidInHand == cardUid:
                foundCard = True
                break

        return foundCard

    # Removes the provided card from this hand and replaces it
    # with a fresh card from the deck
    def removeCardAndTopupFromDeck(self, cardUidToRemove, remainingDeck):
        self.cardUids.remove(cardUidToRemove)

        # Insert a new card from the deck at position 0
        # (only if there are still cards left in the deck)
        if len(remainingDeck.cards) != 0:
            self.cardUids.insert(0, remainingDeck.takeCard())

        print("Removed a card and took a new one from deck (if possible). self.cardUids now = " + repr(self.cardUids))
