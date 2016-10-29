class Hand:

    # Create a new hand, populating it with 5 cards from the deck
    def __init__(self, deck):
        print("New hand being created.")

        self.deck = deck
        self.cards = []

        # Populate this hand with 5 cards from the deck
        for num in range(0, 5):
            self.cards.append(deck.takeCard())

    # Removes the provided card from this hand and replaces it
    # with a fresh card from the deck
    def removeCardAndTopupFromDeck(self, cardToRemove):
        self.cards.remove(cardToRemove)

        print("Removed a card. self.cards now = " + repr(self.cards))

        # Insert a new card from the deck at position 0
        # (only if there are still cards left in the deck)
        if len(self.deck.cards) != 0:
            self.cards.insert(0, self.deck.takeCard())


    def __repr__(self):
        return "{ cards = %s }" % (self.cards)