class Snake():
    """ classe snake qui contient les indices de la grille
    concernant la position du serpent"""

    def __init__(self, x, y):
        """Initialise le serpent, dont le corps est stocké dans une liste
            indice 0 : tête du serpent
            indice autres : corps du serpent """
        self.size = 1
        self.body = [[x, y]]

    def add_body(self):
        """Ajoute un element au serpent"""
        self.body.append(self.body[0])
        self.size += 1

    def move_snake(self, x, y):
        """Permet de mouvoir le serpent"""
        self.body.insert(0, [self.get_head()[0] + x, self.get_head()[1] + y])
        self.body.pop()

    def get_body(self):
        """Retourne la liste qui contient le serpent"""
        return self.body

    def get_head(self):
        """Retourne la tête du serpent"""
        return self.body[0]

    def get_size(self):
        """Retourne la taille du serpent"""
        return self.size
