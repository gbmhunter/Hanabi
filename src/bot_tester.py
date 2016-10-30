from game import Game

class BotTester:

    def __init__(self):

        self.players = None
        self.scores = []
        self.averageScore = 0

    def go(self, players, numIterations):

        for x in range(numIterations):
            self.runOnce(players)

        # Calculate average score
        for score in self.scores:
            self.averageScore += score

        self.averageScore = self.averageScore/len(self.scores)

        print("Average score of " + str(numIterations) + " runs = " + str(self.averageScore))



    def runOnce(self, players):
        game = Game()

        for player in players:
            game.registerPlayer(player)

        # Run game
        game.go()

        self.scores.append(game.getScore())
