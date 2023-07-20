"""Description de l'environnement"""
import numpy as np
from . import turn as t
from . import snake
from . import apple


class Environment:
    NOTHING = 0
    SNAKE = 1
    APPLE = 2

    def __init__(self, grid_size_x=10, grid_size_y=10):
        """Init the grid at the begining of the game"""
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.grid = np.zeros((self.grid_size_x, self.grid_size_y))
        self.tmp = []

        """Init la durée d'un tour"""
        self.turn = t.Turn(0.5)

        """Init le serpent"""
        self.snake = snake.Snake(4, 4)
        self.set_grid(self.snake.get_head()[0], self.snake.get_head()[1], self.SNAKE)

        """Init la pomme à une place random"""
        self.apple = apple.Apple(np.random.randint(0, 9), np.random.randint(0, 9))
        while not self.is_empty(self.apple.get_apple()[0], self.apple.get_apple()[1]):
            self.apple.set_apple(np.random.randint(0, 9), np.random.randint(0, 9))
        self.set_grid(self.apple.get_apple()[0], self.apple.get_apple()[1], self.APPLE)

    def delete(self, x, y):
        """Permet d'effacer un élément de la grille"""
        self.grid[x, y] = self.NOTHING

    def set_grid(self, x, y, element):
        """Place un élément dans la grille"""
        self.grid[x, y] = element

    def erase_grid(self):
        for x, row in enumerate(self.grid):
            for y, element in enumerate(row):
                self.grid[x, y] = self.NOTHING

    def get_grid(self):
        """Retourne la grille de jeu"""
        return self.grid

    def is_empty(self, x, y):
        """Retourne vrai si la case de la grille demandée est vide"""
        if self.grid[x, y] == self.NOTHING:
            return True
        else:
            return False

    def next_move(self, mouvement):
        """Permet de générer la grille pour le prochain tour"""
        """Check l'ancien mouvement pour éviter l'effet de revenir en arrière"""
        if mouvement == 0:  # gauche
            if self.snake.get_size() > 1:
                if [self.snake.get_head()[0] - 1, self.snake.get_head()[1]] == self.snake.get_body()[1]:
                    self.snake.move_snake(1, 0)
                else:
                    self.snake.move_snake(-1, 0)
            else:
                self.snake.move_snake(-1, 0)
        elif mouvement == 1:  # haut
            if self.snake.get_size() > 1:
                if [self.snake.get_head()[0], self.snake.get_head()[1] - 1] == self.snake.get_body()[1]:
                    self.snake.move_snake(0, 1)
                else:
                    self.snake.move_snake(0, -1)
            else:
                self.snake.move_snake(0, -1)
        elif mouvement == 2:  # droite
            if self.snake.get_size() > 1:
                if [self.snake.get_head()[0] + 1, self.snake.get_head()[1]] == self.snake.get_body()[1]:
                    self.snake.move_snake(-1, 0)
                else:
                    self.snake.move_snake(1, 0)
            else:
                self.snake.move_snake(1, 0)
        elif mouvement == 3:  # bas
            if self.snake.get_size() > 1:
                if [self.snake.get_head()[0], self.snake.get_head()[1] + 1] == self.snake.get_body()[1]:
                    self.snake.move_snake(0, -1)
                else:
                    self.snake.move_snake(0, 1)
            else:
                self.snake.move_snake(0, 1)


        """Vérification si le snake est au bon endroit"""
        self.check_loose(self.snake.get_head())

        """Check si tete serpent sur la meme case que la pomme"""
        if self.apple.get_apple() == self.snake.get_head():
            """Ajoute body"""
            self.snake.add_body()
            """Définit une nouvelle pomme"""
            self.apple.set_apple(np.random.randint(0, 9), np.random.randint(0, 9))
            while not self.is_empty(self.apple.get_apple()[0], self.apple.get_apple()[1]):
                self.apple.set_apple(np.random.randint(0, 9), np.random.randint(0, 9))
            """Accélère le jeu"""
            self.turn.reduce_turn()
            """Redéfinition de la grille"""
            self.erase_grid()
            for i in range(0, self.snake.get_size()):
                self.set_grid(self.snake.get_body()[i][0], self.snake.get_body()[i][1], self.SNAKE)
        elif self.snake.get_body().count(self.snake.get_head()) > 1:
            """Si le serpent touche son body"""
            exit(0)

        """Redéfinition de la grille"""
        self.erase_grid()
        for i in range(0, self.snake.get_size()):
            self.set_grid(self.snake.get_body()[i][0], self.snake.get_body()[i][1], self.SNAKE)
        self.set_grid(self.apple.get_apple()[0], self.apple.get_apple()[1], self.APPLE)


    def check_loose(self, position):
        """Vérifie qu'on est toujours dans l'environnement"""
        if position[0] < 0 or position[1] < 0:
            exit(0)
        elif position[0] > 9 or position[1] > 9:
            exit(0)









