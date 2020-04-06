import sys
import pygame
from settings.Settings import   Setting
from ship import Ship
from game_functions import check_event


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen)

    while True:
        check_event()
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
