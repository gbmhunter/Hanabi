class Move:
    def __init__(self, player):
        print("New move being created.")
        self.player = player


class GiveClue(Move):
    def __init__(self, player):
        super().__init__(player)
        print("\"Give Clue\" move being created.")


class PlayCard(Move):
    def __init__(self, player, cardNumber):
        super().__init__(player)
        print("\"Play Card\" move being created.")

        self.cardNumber = cardNumber

    def __repr__(self):
        return "{ card = %s }" % repr(self.cardNumber)


class Discard(Move):
    def __init__(self, player, cardNumber):
        super().__init__(player)
        print("\"Discard\" move being created.")

        self.cardNumber = cardNumber
