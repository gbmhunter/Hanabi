import copy

from deck import Deck
from played_pile import PlayedPile
from discard_pile import DiscardPile
from hand import Hand
from moves import *
from inspector import Inspector
from game_constants import *

class Game:

    def __init__(self):

        self.deck = Deck()

        self.remainingDeck = copy.deepcopy(self.deck)
        self.playedPile = PlayedPile()
        self.discardPile = DiscardPile()

        self.registeredPlayers = []
        self.currPlayer = None

        self.numCluesAvailable = 8
        self.livesRemaining = 3

        self.moveHistory = []

        self.numTurns = 0

        self.inspector = Inspector(self)

    def registerPlayer(self, player):
        # print("registerPlayer() called.")

        # Add this player to the list
        self.registeredPlayers.append(player)

    def go(self):
        # print("go() called.")

        currPlayerIndex = 0

        # The game doesn't make sense if there are not 2 or more players...
        if len(self.registeredPlayers) < 2:
            print("ERROR: 2 or more players must be registered before go() can be called.")
            return

        # Create a hand for each player
        for player in self.registeredPlayers:
            #hand = Hand(self.deck)
            player.hand = Hand(self.remainingDeck, self)

            ##self.hands[player] = hand

            # print("Created hand. hand = " + repr(player.hand))

        # Main loop. Each iteration of this loop handles a single move.
        while True:

            self.currPlayer = self.registeredPlayers[currPlayerIndex]

            if self.checkForNoMoveAvailable():
                # print("No move available for current player!. Game over. Score = " + str(self.playedPile.getCurrScore()))
                return

            # Make the current player take his/her turn, and record the move returned
            move = self.registeredPlayers[currPlayerIndex].takeTurn(
                self.registeredPlayers,
                self.playedPile,
                self.discardPile,
                self.moveHistory,
                self.numCluesAvailable,
                self.inspector)

            # ============================================== #
            # ================= HANDLE MOVE ================ #
            # ============================================== #

            if move is None:
                raise RuntimeError("takeTurn() did not return a move!")

            if isinstance(move, GiveClueMove):
                self.handeGiveClue(self.currPlayer, move)
                if self.checkForEndOfGame() == True:
                    return

            elif isinstance(move, PlayCardMove):

                self.handlePlayCard(self.currPlayer, move)
                if self.checkForEndOfGame() == True:
                    return

            elif isinstance(move, DiscardMove):
                # print("Player has taken turn. Returned move is a Discard. move = " + repr(move))

                self.handleDiscard(self.currPlayer, move)



            # ============================================== #
            # =================== TIDY UP ================== #
            # ============================================== #

            currPlayerIndex += 1

            # Cycle through all the players in a continuous loop
            if currPlayerIndex == len(self.registeredPlayers):
                currPlayerIndex = 0

            # Keep track of how many turns have been played this game
            self.numTurns += 1

            if self.numTurns == 1000:
                raise RuntimeError("Players took 1000 turns and game has not finished.")


    def handeGiveClue(self, currPlayer, giveClueMove):
        # print("Player has taken turn. Returned move is a GiveClueMove. playCard = " + repr(giveClueMove))

        # We need to:
        # 1. Validate legality of move
        # 2. Add the number of cards includes in the clue
        # 3. Decrement the number of clues available
        # 4. Add move to move history

        # VALIDATE LEGALITY
        if self.numCluesAvailable == 0:
            raise RuntimeError("Player tried to give clue when no more clues were available.")

            # Find all card UIDs of this color in target players hand
            cardUids = self.getCardUidsOfNumber(giveClueMove.numOrColor, giveClueMove.targetPlayer.hand, self.deck)

            # print("Searched for cards with particular color in target players hand. cardUids = " + repr(cardUids))

            giveClueMove.cardUids = cardUids


        # FIND NUMBER OF APPLICABLE CARDS
        if isinstance(giveClueMove.numOrColor, int):
            # print("Clue was about a number. number = " + repr(giveClueMove.numOrColor))

            # Find all card UIDs of this color in target players hand
            cardUids = self.getCardUidsOfNumber(giveClueMove.numOrColor, giveClueMove.targetPlayer.hand, self.deck)

            # print("Searched for cards with particular color in target players hand. cardUids = " + repr(cardUids))

            giveClueMove.cardUids = cardUids

        elif isinstance(giveClueMove.numOrColor, Color):
            # print("Clue was about color. color = " + repr(giveClueMove.numOrColor))

            # Find all card UIDs of this color in target players hand
            cardUids = self.getCardUidsOfColor(giveClueMove.numOrColor, giveClueMove.targetPlayer.hand, self.deck)

            # print("Searched for cards with particular color in target players hand. cardUids = " + repr(cardUids))

            giveClueMove.cardUids = cardUids
        else:
            raise RuntimeError("Clue type was not recognised.")

        self.numCluesAvailable -= 1
        self.moveHistory.append(giveClueMove)


    def handlePlayCard(self, currPlayer, playCardMove):
        # print("Player has taken turn. Returned move is a PlayCard. playCard = " + repr(playCardMove))

        # Validate legality
        if not currPlayer.hand.isInHand(playCardMove.cardUid):
            raise RuntimeError("Player tried to play card that was not in his/her hand.")

        # Try and play card
        ableToBePlayed, completedPile = self.playedPile.play(playCardMove.cardUid, self.deck)

        if ableToBePlayed is True:
            # print("Card was played successfully!")
            # Card was played successfully
            currPlayer.hand.removeCardAndTopupFromDeck(playCardMove.cardUid, self.remainingDeck)

            # If playing this card completed a pile (i.e. a 5 was played),
            # then give a clue back
            if completedPile and self.numCluesAvailable < 8:
                self.numCluesAvailable += 1

        else:
            # print("Card was not able to be played.")

            # Card was not able to be played! We need to:
            # 1. Remove the card from the current players hand
            # 2. Add it to the discard pile
            # 3. Decrement the number of lives remaining
            currPlayer.hand.removeCardAndTopupFromDeck(playCardMove.cardUid, self.remainingDeck)
            self.discardPile.addCard(playCardMove.cardUid)
            self.livesRemaining -= 1


    def handleDiscard(self, currPlayer, discardMove):
        # We need to
        # 1. Check card is in current players hand
        # 1. Remove card from current players hand
        # 2. Add it to the discard pile
        # 4. Increase the number of clues available

        # Validate legality
        if not currPlayer.hand.isInHand(discardMove.cardUid):
            raise RuntimeError("Player tried to discard a card that was not in his/her hand.")

        currPlayer.hand.removeCardAndTopupFromDeck(discardMove.cardUid, self.remainingDeck)
        self.discardPile.addCard(discardMove.cardUid)

        if self.numCluesAvailable < 8:
            self.numCluesAvailable += 1


    def getCardUidsOfColor(self, color, hand, deck):

        cardUids = []
        for cardUid in hand.cardUids:
            card = deck.getCard(cardUid)

            if card.color == color:
                cardUids.append(cardUid)

        return cardUids

    def getCardUidsOfNumber(self, number, hand, deck):

        cardUids = []
        for cardUid in hand.cardUids:
            card = deck.getCard(cardUid)

            if card.number == number:
                cardUids.append(cardUid)

        return cardUids

    def checkForEndOfGame(self):

        gameIsOver = False
        if self.livesRemaining == 0:
            # print("No lives remaining!")
            gameIsOver = True

        # Check for completion of played pile
        if self.playedPile.getCurrScore == 25:
            # print("Your bots scored 25 points!")
            gameIsOver = True

        # if gameIsOver == True:
            # print("Game is over. Your bots scored " + str(self.playedPile.getCurrScore()) + " points.")

        return gameIsOver

    def checkForNoMoveAvailable(self):

        if len(self.currPlayer.hand.cardUids) == 0 and self.numCluesAvailable == 0:
            return True
        else:
            return False

    def getScore(self):

        return self.playedPile.getCurrScore()






