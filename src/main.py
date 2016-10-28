from game import Game
from player_interface import PlayerInterface

class GeoPlayer(PlayerInterface):
    def __init__(self):
        super().__init__()
        print("Creating a Geo player.")

if __name__ == "__main__":
    print("Hanabi simulator started.")

    game = Game()

    # Create and register custom players
    geoPlayer1 = GeoPlayer()
    geoPlayer2 = GeoPlayer()

    game.registerPlayer(geoPlayer1)
    game.registerPlayer(geoPlayer2)

    game.go()




