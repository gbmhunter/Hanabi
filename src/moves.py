class Move:
    def __init__(self, player):
        print("New move being created.")
        self.player = player


class GiveClueMove(Move):
    def __init__(self, player, targetPlayer, numOrColor):
        super().__init__(player)
        print("\"GiveClueMove\" being created.")

        self.targetPlayer = targetPlayer
        self.numOrColor = numOrColor


class PlayCard(Move):
    def __init__(self, player, cardUid):
        super().__init__(player)
        print("\"Play Card\" move being created.")

        self.cardUid = cardUid

    def __repr__(self):
        return "{ cardUid = %s }" % repr(self.cardUid)


class Discard(Move):
    def __init__(self, player, cardUid):
        super().__init__(player)
        print("\"Discard\" move being created.")

        self.cardUid = cardUid
