class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def __init__(self, name, style):
        super().__init__(name)
        self.style = style

    def play(self):
        print("The batsman is batting in the {} style.".format(self.style))

class Bowler(Player):
    def __init__(self, name, bowling_type):
        super().__init__(name)
        self.bowling_type = bowling_type

    def play(self):
        print("The bowler is bowling {}.".format(self.bowling_type))
batsman = Batsman("Sachin Tendulkar", "Right-handed batsman")
bowler = Bowler("Glenn McGrath", "Fast bowler")
batsman.play()
bowler.play()
