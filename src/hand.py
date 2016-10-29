class Hand:

    # Create a new hand, populating it with 5 cards from the deck
    def __init__(self, deck):
        print("New hand being created.")

        self.cards = []

        # Populate this hand with 5 cards from the deck
        for num in range(0, 5):
            self.cards.append(deck.takeCard())

    def __repr__(self):
        return "{ cards = %s }" % (self.cards)