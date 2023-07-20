import pygame
from game.environment import Environment
from game.window import Window
from game.mouvement import Mouvement

import time

def main():
    env = Environment()
    window = Window(env.snake.get_head(), env.apple.get_apple())
    mvt = Mouvement()

    while True:
        env.next_move(mvt.get_last_mouvement())
        window.plot_grid(env.get_grid())
        time.sleep(env.turn.get_time())

if __name__ == "__main__":
    main()

