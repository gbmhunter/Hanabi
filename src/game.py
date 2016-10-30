from deck import Deck
from played_pile import PlayedPile
from discard_pile import DiscardPile
from hand import Hand
from moves import *

class Game:

    def __init__(self):
        self.deck = Deck()
        self.playedPile = PlayedPile()
        self.discardPile = DiscardPile()

        self.registeredPlayers = []

        self.hands = {}

        self.livesRemaining = 3

        self.numTurns = 0

    def registerPlayer(self, player):
        print("registerPlayer() called.")

        # Add this player to the list
        self.registeredPlayers.append(player)

    def go(self):
        print("go() called.")

        currPlayerIndex = 0

        # The game doesn't make sense if there are not 2 or more players...
        if len(self.registeredPlayers) < 2:
            print("ERROR: 2 or more players must be registered before go() can be called.")
            return

        # Create a hand for each player
        for player in self.registeredPlayers:
            hand = Hand(self.deck)

            self.hands[player] = hand

            print("Created hand. hand = " + repr(hand))

        # Main loop. Each iteration of this loop handles a single move.
        while self.numTurns < 10:

            currPlayer = self.registeredPlayers[currPlayerIndex]


            # NOTE: We need to provide hands for all players EXCEPT his own
            # Make copy of hands array before modifying
            # allHandsPutCurrPlayers = self.hands[:]
            #
            # # Create map that will re-organise the players hands
            # handMap = []
            # tempIndex = currPlayerIndex + 1
            # for player in self.registeredPlayers:
            #     if(tempIndex > len(self.registeredPlayers) - 1):
            #         tempIndex = 0
            #
            #     if player == currPlayer:
            #         continue
            #
            #     handMap.append(tempIndex)
            #     tempIndex += 1
            #
            # # Map created, now re-organise the players hands
            # allHandsPutCurrPlayers = [allHandsPutCurrPlayers[i] for i in handMap]
            #
            # print("Re-organised allHandsPutCurrPlayers = " + repr(allHandsPutCurrPlayers))

            allHandsButCurrPlayers = self.hands.copy()
            # Remove current players hand from dictionary
            allHandsButCurrPlayers.pop(currPlayer)

            # Make the current player take his/her turn, and record the move returned
            move = self.registeredPlayers[currPlayerIndex].takeTurn(self.hands, self.playedPile, self.discardPile)

            # ============================================== #
            # ================= HANDLE MOVE ================ #
            # ============================================== #

            if move is None:
                raise RuntimeError("takeTurn() did not return a move!")

            if isinstance(move, PlayCard):
                print("Player has taken turn. Returned move is a PlayCard. playCard = " + repr(move))

                # Try and play card
                cardToPlay = self.hands[currPlayer].cards[move.cardNumber]
                wasAbleToPlay = self.playedPile.play(cardToPlay)

                if wasAbleToPlay is True:
                    print("Card was played successfully!")
                    # We need to remove the card from the current players hand
                    self.hands[currPlayer].removeCardAndTopupFromDeck(cardToPlay)

                else:
                    print("Card was not able to be played.")

                    # Card was not able to be played! We need to:
                    # 1. Remove the card from the current players hand
                    # 2. Add it to the discard pile
                    # 3. Decrement the number of lives remaining
                    self.hands[currPlayer].removeCardAndTopupFromDeck(cardToPlay)
                    self.discardPile.addCard(cardToPlay)
                    self.livesRemaining -= 1

                    if self.livesRemaining == 0:
                        print("No lives remaining! Game is over. Score = " + str(self.playedPile.getCurrScore()))
                        return
            elif isinstance(move, Discard):
                print("Player has taken turn. Returned move is a Discard. move = " + repr(move))

                self.handleDiscard(currPlayer, move)



            # ============================================== #
            # =================== TIDY UP ================== #
            # ============================================== #

            currPlayerIndex += 1

            # Cycle through all the players in a continuous loop
            if currPlayerIndex == len(self.registeredPlayers):
                currPlayerIndex = 0

            # Keep track of how many turns have been played this game
            self.numTurns += 1


    def handleDiscard(self, currPlayer, discardMove):
        # We need to
        # 1. Remove card from current players hand
        # 2. Add it to the discard pile
        discardCard = self.hands[currPlayer].cards[discardMove.cardNumber]
        self.hands[currPlayer].removeCardAndTopupFromDeck(discardCard)
        self.discardPile.addCard(discardCard)

