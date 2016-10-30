from game import Game
from player_interface import PlayerInterface
from moves import *

class GeoPlayer(PlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        print("Creating a Geo player.")

    def __repr__(self):
        return "{ name = %s, hand = %s}" % (self.name, self.hand)

    def takeTurn(self, players, playedPile, discardPile, numCluesAvailable, inspector):
        print(self.name + " taking turn.")

        if numCluesAvailable == 0:
            return DiscardMove(self.hand.cardUids[len(self.hand.cardUids) - 1])

        for player in players:

            # Don't do anything if we are looking at ourselves
            if player == self:
                continue

            playableCardUids = inspector.getPlayableCardUids(player.hand)

            print("playableCardUids = " + repr(playableCardUids))

            if len(playableCardUids) == 0:
                return DiscardMove(self.hand.cardUids[len(self.hand.cardUids) - 1])

            for playableCardUid in playableCardUids:
                # Get the actual card
                playableCard = inspector.getCard(playableCardUid)

                if inspector.getCardsUidsOfNumber(playableCard.number, player.hand) == 1:
                    return GiveClueMove(player, playableCard.number)

                if inspector.getCardsUidsOfColor(playableCard.color, player.hand) == 1:
                    return GiveClueMove(player, playableCard.color)

        return DiscardMove(self.hand.cardUids[len(self.hand.cardUids) - 1])


if __name__ == "__main__":
    print("Hanabi simulator started.")

    game = Game()

    # Create and register custom players
    geoPlayer1 = GeoPlayer("geoPlayer1")
    geoPlayer2 = GeoPlayer("geoPlayer2")

    game.registerPlayer(geoPlayer1)
    game.registerPlayer(geoPlayer2)

    game.go()




