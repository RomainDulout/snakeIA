import pygame

class Mouvement:
    """Permet de gérer les mouvements"""
    mouvement_list = {"left": 0, "up": 1, "right": 2, "down": 3}

    def __init__(self):
        self.last_mouvement = Mouvement.mouvement_list.get("left")

    def get_last_mouvement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.last_mouvement = Mouvement.mouvement_list.get("down")
                elif event.key == pygame.K_UP:
                    self.last_mouvement = Mouvement.mouvement_list.get("up")
                elif event.key == pygame.K_LEFT:
                    self.last_mouvement = Mouvement.mouvement_list.get("left")
                elif event.key == pygame.K_RIGHT:
                    self.last_mouvement = Mouvement.mouvement_list.get("right")
        return self.last_mouvement


