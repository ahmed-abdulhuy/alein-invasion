import pygame
import game_functions as gf
from settings.Settings import Setting
from ship import Ship
from pygame.sprite import Group
from game_states import GameStates
from button import Button
from score_board import ScoreBoard


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption('Alien Invasion')

    # Creat a ship Bullets group and aliens fleet
    ship = Ship(screen, ai_setting)
    bullets = Group()
    aliens = Group()

    # Creat game state
    states = GameStates(ai_setting)

    # Creat a button instance
    play_button = Button(ai_setting, screen, 'Play')

    # Creat score board
    sb = ScoreBoard(ai_setting, screen, states)

    # Creat aliens fleet
    gf.creat_fleet(aliens, ship, screen, ai_setting)

    while True:
        gf.check_event(ship, bullets, aliens, screen, ai_setting, states, play_button, sb)

        if states.game_active:
            ship.update(ai_setting.width, ai_setting.height)
            gf.update_bullet(ai_setting, screen, states, sb, ship, bullets, aliens)
            gf.update_aliens(screen, ai_setting, states, sb, aliens, ship, bullets)
        gf.update_screen(screen, ai_setting, states, sb, ship, bullets, aliens, play_button)
        pygame.display.flip()


run_game()
