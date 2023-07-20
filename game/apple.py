class Apple:

    def __init__(self, x, y):
        self.apple = [x, y]
        self.nb_apple = 0

    def set_apple(self, x, y):
        self.apple = [x, y]

    def add_nb_apple(self):
        self.nb_apple += 1

    def get_apple(self):
        return self.apple


