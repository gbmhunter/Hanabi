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

        self.hands = []


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
        for players in self.registeredPlayers:
            hand = Hand(self.deck)

            self.hands.append(hand)

            print("Created hand. hand = " + repr(hand))

        while self.numTurns < 10:


            # NOTE: We need to provide hands for all players EXCEPT his own
            # Make copy of hands array before modifying
            allHandsPutCurrPlayers = self.hands[:]

            # Create map that will re-organise the players hands
            handMap = []
            tempIndex = currPlayerIndex + 1
            for players in self.registeredPlayers:
                if(tempIndex > len(self.registeredPlayers) - 1):
                    tempIndex = 0

                if tempIndex == currPlayerIndex:
                    continue

                handMap.append(tempIndex)
                tempIndex += 1

            # Map created, now re-organise the players hands
            allHandsPutCurrPlayers = [allHandsPutCurrPlayers[i] for i in handMap]

            print("Re-organised allHandsPutCurrPlayers = " + repr(allHandsPutCurrPlayers))

            # Make the current player take his/her turn, and record the move returned
            move = self.registeredPlayers[currPlayerIndex].takeTurn(self.hands, self.playedPile, self.discardPile)

            # ============================================== #
            # ================= HANDLE MOVE ================ #
            # ============================================== #

            if move is None:
                raise RuntimeError("takeTurn() did not return a move!")

            if isinstance(move, PlayCard):
                print("Player has taken turn. Returned move is a PlayCard. playCard = " + repr(move))

            # ============================================== #
            # =================== TIDY UP ================== #
            # ============================================== #

            currPlayerIndex += 1

            # Cycle through all the players in a continuous loop
            if currPlayerIndex == len(self.registeredPlayers):
                currPlayerIndex = 0

            # Keep track of how many turns have been played this game
            self.numTurns += 1


