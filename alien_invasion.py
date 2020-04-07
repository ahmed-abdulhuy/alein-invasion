import sys
import pygame
import game_functions as gf
from settings.Settings import Setting
from ship import Ship
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption('Alien Invasion')

    # Creat a ship Bullets group and aliens fleet
    ship = Ship(screen, ai_setting)
    bullets = Group()
    aliens = Group()

    # Creat aliens fleet
    gf.creat_fleet(aliens, ship, screen, ai_setting)
    while True:
        gf.check_event(ship, bullets, screen, ai_setting)
        ship.update(ai_setting.width, ai_setting.height)
        gf.update_bullet(ai_setting, screen, ship, bullets, aliens)
        gf.update_aliens(ai_setting, aliens)
        gf.update_screen(screen, ai_setting, ship, bullets, aliens)
        pygame.display.flip()


run_game()
