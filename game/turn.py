class Turn:
    def __init__(self, time):
        self.time = time

    def reduce_turn(self):
        self.time -= 0.02

    def get_time(self):
        return self.time


