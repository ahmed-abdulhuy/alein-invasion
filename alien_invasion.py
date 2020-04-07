import sys
import pygame
import game_functions as gf
from settings.Settings import Setting
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_setting)

    # make group to store bullets in
    bullets = Group()

    while True:
        gf.check_event(ship, bullets, screen, ai_setting)
        ship.update(ai_setting.width, ai_setting.height)
        gf.update_bullet(bullets)
        gf.update_screen(screen, ai_setting, ship, bullets)
        pygame.display.flip()


run_game()
