
# Players use this class to
class Inspector:

    def __init__(self, game):
        print("Creating inspector.")
        self.game = game


    # Gets a card, but only if it is legal for the current player to do so
    def getCard(self, cardUid):

        # Check to make sure card is in a players hand, BUT
        # not in the current players hand

        isLegal = False
        for player in self.game.registeredPlayers:

            if player == self.game.currPlayer:
                continue

            if player.hand.isInHand(cardUid):
                isLegal = True

        if isLegal == False:
            raise RuntimeError("Player tried to ask for card info that was not in any other players hand.")

        return self.game.deck.getCard(cardUid)

    def getPlayableCardUids(self, hand):

        if hand == self.game.currPlayer.hand:
            raise RuntimeError("Player tried to ask for playable card UID's in his/her own hand.")

        playableCardUids = []

        for cardUid in hand.cardUids:

            if self.game.playedPile.isPlayable(cardUid, self.game.deck):
                playableCardUids.append(cardUid)

        return playableCardUids

    def getCardsUidsOfNumber(self, number, hand):
        # Make sure player is not asking for info about their own hand
        if hand == self.game.currPlayer.hand:
            raise RuntimeError("Player tried to ask about numbers in his/her own hand.")

        count = 0;
        for cardUidInHand in hand.cardUids:
            cardInHand = self.game.deck.getCard(cardUidInHand)
            if number == cardInHand.number:
                count += 1

        return count


    def getCardsUidsOfColor(self, color, hand):
        # Make sure player is not asking for info about their own hand
        if hand == self.game.currPlayer.hand:
            raise RuntimeError("Player tried to ask about colors in his/her own hand.")

        colorCount = 0;
        for cardUidInHand in hand.cardUids:
            cardInHand = self.game.deck.getCard(cardUidInHand)
            if color == cardInHand.color:
                colorCount += 1

        return colorCount



