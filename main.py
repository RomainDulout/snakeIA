import pygame

LENGTH_RECT = 40


def main():
    """Init pygame module"""
    pygame.init()

    """Set window display for python"""
    window = pygame.display.set_mode((400, 400))

    """Set pngs to be used"""
    background = pygame.image.load("img/background.jpg").convert()
    snake_corpse = pygame.image.load("img/snake.png").convert_alpha()

    """Create background"""
    window.blit(background, (0, 0))
    pygame.display.flip()  # A reutiliser tout le temps

    """Print snake"""
    snake_position = snake_corpse.get_rect()
    window.blit(snake_corpse, snake_position)

    """Refresh screen"""
    pygame.display.flip()

    """Gestion boucle infinie pour gérer l'évènement"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake_position = snake_position.move(0, LENGTH_RECT)
                elif event.key == pygame.K_UP:
                    snake_position = snake_position.move(0, -LENGTH_RECT)
                elif event.key == pygame.K_LEFT:
                    snake_position = snake_position.move(-LENGTH_RECT, 0)
                elif event.key == pygame.K_RIGHT:
                    snake_position = snake_position.move(LENGTH_RECT, 0)

        window.blit(background, (0, 0))
        window.blit(snake_corpse, snake_position)
        pygame.display.flip()


if __name__ == "__main__":
    main()

