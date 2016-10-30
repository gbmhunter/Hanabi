class Move:
    def __init__(self):
        # print("New move being created.")

        blah = 2



class GiveClueMove(Move):
    def __init__(self, targetPlayer, numOrColor):
        super().__init__()
        # print("\"GiveClueMove\" being created.")

        self.targetPlayer = targetPlayer
        self.numOrColor = numOrColor

        # This is populated by the Game object
        self.cardUids = None

    def __repr__(self):
        return "{ targetPlayer = %s, numOrColor = %s }" % (repr(self.targetPlayer), repr(self.numOrColor))


class PlayCardMove(Move):
    def __init__(self, cardUid):
        super().__init__()
        # print("\"Play Card\" move being created.")

        self.cardUid = cardUid

    def __repr__(self):
        return "{ cardUid = %s }" % repr(self.cardUid)


class DiscardMove(Move):
    def __init__(self, cardUid):
        super().__init__()
        #print("\"DiscardMove\" being created.")

        self.cardUid = cardUid

    def __repr__(self):
        return "{ cardUid = %s }" % repr(self.cardUid)
