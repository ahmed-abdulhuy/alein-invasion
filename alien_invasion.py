import sys
import pygame
import  game_functions as gf
from settings.Settings import   Setting
from ship import Ship


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_setting)
    while True:
        gf.check_event(ship)
        ship.update(ai_setting.width)
        gf.update_screen(screen, ai_setting, ship)
        pygame.display.flip()


run_game()
