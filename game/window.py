"""Manage game display """
import pygame


class Window:
    RECT_SIZE = 40
    SNAKE = 1
    APPLE = 2

    def __init__(self, snake_position, apple_position, window_size_x=400, window_size_y=400):
        """Init the game"""
        pygame.init()
        self.window = pygame.display.set_mode((window_size_x, window_size_y))

        """Set pngs to be used"""
        self.background = pygame.image.load("img/background.jpg").convert()
        self.snake = pygame.image.load("img/snake.png").convert_alpha()
        self.apple = pygame.image.load("img/apple.png").convert_alpha()

        """Create background"""
        self.window.blit(self.background, (0, 0))

        """Init apple and snake position"""
        self.snake_position = (self.RECT_SIZE * snake_position[0], self.RECT_SIZE * snake_position[1])
        self.apple_position = (self.RECT_SIZE * apple_position[0], self.RECT_SIZE * apple_position[1])
        self.window.blit(self.snake, self.snake_position)
        self.window.blit(self.apple, self.apple_position)
        pygame.display.flip()

    def plot_grid(self, grid):
        """Methode qui affiche le jeu selon la configuration de la grille"""
        self.window.blit(self.background, (0, 0))
        for index_x, row in enumerate(grid):
            for index_y, element in enumerate(row):
                if element == self.SNAKE:
                    self.window.blit(self.snake, (self.RECT_SIZE * index_x, self.RECT_SIZE * index_y))
                elif element == self.APPLE:
                    self.window.blit(self.apple, (self.RECT_SIZE * index_x, self.RECT_SIZE * index_y))

        pygame.display.flip()



