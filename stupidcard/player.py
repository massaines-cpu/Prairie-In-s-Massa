#player

class Player:
    def __init__(self, name : str, strategy):
        self.name = name
        self.hand = []
        self.strategy = strategy
    def __str__(self):
        return self.name + ": " + str([str(carte) for carte in self.hand])
    # def play(self):
    #     return self.hand.pop(-1)
    def play(self):
        return self.strategy(self.hand)