from game import Game
from player_interface import PlayerInterface
from moves import *

class ExamplePlayer(PlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        print("Creating a Geo player.")

    def __repr__(self):
        return "{ name = %s, hand = %s}" % (self.name, self.hand)

    def takeTurn(self, players, playedPile, discardPile, moveHistory, numCluesAvailable, inspector):
        print(self.name + " taking turn.")

        # First see if there is anything playable
        for move in moveHistory:

            if not isinstance(move, GiveClueMove):
                continue

            if len(move.cardUids) == 0:
                # Detected GiveClueMove but there were 0 cards assigned to the clue
                continue

            if self.hand.isInHand(move.cardUids[0]):
                return PlayCardMove(move.cardUids[0])


        print(self.name, " decided there was no card he could play.")

        if numCluesAvailable == 0:
            return DiscardMove(self.hand.cardUids[len(self.hand.cardUids) - 1])

        for player in players:

            # Don't do anything if we are looking at ourselves
            if player == self:
                continue

            playableCardUids = inspector.getPlayableCardUids(player.hand)

            print("playableCardUids = " + repr(playableCardUids))

            # if len(playableCardUids) == 0:
            #     return DiscardMove(self.hand.cardUids[len(self.hand.cardUids) - 1])

            for playableCardUid in playableCardUids:
                # Get the actual card
                playableCard = inspector.getCard(playableCardUid)

                if inspector.getCardsUidsOfNumber(playableCard.number, player.hand) == 1:
                    return GiveClueMove(player, playableCard.number)

                if inspector.getCardsUidsOfColor(playableCard.color, player.hand) == 1:
                    return GiveClueMove(player, playableCard.color)

        if(len(self.hand.cardUids) == 0):
            # We can't discard (we have no cards left), we have to give a clue!
            print("I have no cards left, I have to give a clue!")

            for player in players:

                # Don't do anything if we are looking at ourselves
                if player == self:
                    continue

                # Give a bogus clue
                return GiveClueMove(player, 1)


        return DiscardMove(self.hand.cardUids[len(self.hand.cardUids) - 1])




if __name__ == "__main__":
    print("Hanabi simulator started.")

    game = Game()

    # Create and register custom players
    examplePlayer1 = ExamplePlayer("examplePlayer1")
    examplePlayer2 = ExamplePlayer("examplePlayer2")

    game.registerPlayer(examplePlayer1)
    game.registerPlayer(examplePlayer2)

    game.go()




